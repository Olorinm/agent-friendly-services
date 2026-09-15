import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import pipeline_test as fixtures
import pipeline
import comparison_group as groups


class ComparisonGroupTests(unittest.TestCase):
    setUp = fixtures.PipelineTests.setUp

    def prepare_group(self, concurrency=2, third_model=None, third_input=None, evidence=False):
        catalog = {'services': [{'id': name, 'catalog': {'routes': [
            {'id': 'api', 'entry_url': 'https://example.com/' + name}]}}
            for name in ('fixture-a', 'fixture-b', 'fixture-c')]}
        pipeline.write(self.root / 'generated/catalog.json', catalog)
        adapter = fixtures.ADAPTER.replace("q['role']+'-session'", "q['run_id']+'-'+q['role']+'-session'")
        adapter = adapter.replace("assert not (Path(q['input'])/'reference.json').exists()",
                                  "assert not (Path(q['input'])/'reference.json').exists()\n        assert not (Path(q['input'])/'peer-results').exists()")
        adapter = adapter.replace("print(json.dumps({'handle':q['role']+'-handle'}))", """
    if q['role']=='grading':
        index=json.loads((Path(q['input'])/'review-packet/index.json').read_text())
        assert index['peer_results']['target_run_id']==q['run_id']
        peers=json.loads((Path(q['input'])/'peer-results/index.json').read_text())
        assert len(peers['members'])==3
        (out/'seen-peers.json').write_text(json.dumps(peers))
    print(json.dumps({'handle':q['role']+'-handle'}))""")
        adapter = adapter.replace(".write_text('synthetic answer')", ".write_text('synthetic answer '+q['run_id'])")
        if evidence:
            adapter = adapter.replace("write('evidence.json',{'answer':'synthetic answer'})", "write('evidence.json',{'answer':'synthetic answer'})\n        (out/'artifacts').mkdir(); write('artifacts/response.json',{'source':'https://example.com/original','value':q['run_id']})")
        (self.root / 'adapter.py').write_text(adapter)
        self.members = []
        for name in ('fixture-a', 'fixture-b', 'fixture-c'):
            cfg = copy.deepcopy(self.config)
            cfg.update(service=name, environment_id=name, phase='business')
            for role in ('execution', 'grading'):
                cfg[role]['runtime'] = name + '-' + role
            if third_model and name == 'fixture-c':
                cfg['execution']['model'] = third_model
            if third_input and name == 'fixture-c':
                (self.root / 'tasks.md').write_text((self.root / 'tasks.md').read_text().replace('fixture input', third_input))
            # A passed prerequisite fixture; real prerequisite enforcement has its own tests.
            prior = self.root / 'data/experiments/results' / (name + '-access')
            pipeline.write(prior / 'config.json', cfg)
            pipeline.write(prior / 'state.json', {'phase': 'reviewed'})
            pipeline.write(prior / 'grading/assessment.json', {'status': 'completed'})
            cfg['depends_on'] = str(prior)
            config_path = self.root / (name + '.json')
            pipeline.write(config_path, cfg)
            directory = prior.with_name(name + '-business')
            pipeline.prepare(config_path, directory)
            self.members.append(directory)
        self.group = self.root / 'data/experiments/results/comparison-round-1'
        self.group_config = self.root / 'group.json'
        pipeline.write(self.group_config, {'round': 1, 'max_concurrency': concurrency,
                                         'members': [{'run': str(p), 'evidence': ['artifacts/response.json'] if evidence else []} for p in self.members]})
        return groups.prepare(self.group_config, self.group)

    def finish_group(self):
        for _ in range(16):
            state = groups.advance(self.group)
            if state['phase'] in ('reviewed', 'needs_attention'):
                return state
        self.fail('Group failed to reach a bounded terminal state')

    def seal_group(self):
        for _ in range(10):
            state = groups.advance(self.group)
            if state['phase'] == 'grading':
                return
        self.fail('Group failed to seal')

    def test_barrier_independent_graders_and_recorded_peer_provenance(self):
        self.prepare_group()
        groups.advance(self.group)
        self.assertEqual([pipeline.read(p / 'state.json')['phase'] for p in self.members],
                         ['execution_running', 'execution_running', 'prepared'])
        groups.advance(self.group)
        self.assertEqual(pipeline.read(self.members[0] / 'state.json')['phase'], 'execution_collected')
        self.assertFalse(any((p / 'grading/started').exists() for p in self.members))
        self.assertEqual(self.finish_group()['phase'], 'reviewed')
        snapshots = [pipeline.frozen_files(p / 'grading-input/peer-results') for p in self.members]
        self.assertTrue(all(s == snapshots[0] for s in snapshots))
        for p in self.members:
            self.assertFalse((p / 'frozen/execution/peer-results').exists())
            peer_index = pipeline.read(p / 'grading/seen-peers.json')
            self.assertNotIn('assessment', json.dumps(peer_index))
            self.assertFalse(list((p / 'grading-input/peer-results').rglob('assessment.json')))
            with patch.object(pipeline.subprocess, 'run'):
                result = pipeline.read(pipeline.record(p))
            context = result['review']['peer_context']
            self.assertEqual(context['round'], 1)
            self.assertEqual(context['run_ids'], [m.name for m in self.members])
            self.assertEqual(context['snapshot_sha256'], pipeline.digest(self.group / 'snapshot-hashes.json'))
            self.assertNotIn(str(self.root), json.dumps(context))

    def test_grouped_run_cannot_bypass_barrier_or_be_regrouped(self):
        self.prepare_group()
        with self.assertRaisesRegex(ValueError, 'Grouped runs'):
            pipeline.advance(self.members[0])
        with self.assertRaisesRegex(ValueError, 'ungrouped'):
            groups.prepare(self.group_config, self.group.with_name('second-group'))
        self.assertFalse((self.members[0] / 'execution/started').exists())

    def test_mismatched_conditions_rejected_before_members_are_bound(self):
        with self.assertRaisesRegex(ValueError, 'must match'):
            self.prepare_group(third_model='different-model')
        self.assertFalse(self.group.exists())
        self.assertFalse(any(groups.binding(p).exists() for p in self.members))

    def test_different_task_inputs_cannot_be_cross_answers(self):
        with self.assertRaisesRegex(ValueError, 'must match'):
            self.prepare_group(third_input='another reporting month')
        self.assertFalse(self.group.exists())

    def test_selected_evidence_is_available_without_raw_sessions(self):
        self.prepare_group(evidence=True); self.seal_group()
        for member in pipeline.read(self.group / 'peer-results/index.json')['members']:
            self.assertEqual(len(member['files']), 2)
            evidence = self.group / 'peer-results' / member['files'][1]['path']
            self.assertEqual(pipeline.read(evidence)['value'], member['run_id'])
        self.assertFalse(list((self.group / 'peer-results').rglob('events.jsonl')))

    def test_cli_group_dispatch_and_stop_use_same_state_and_locks(self):
        self.prepare_group()
        launcher = ('import sys; from pathlib import Path; sys.path.insert(0,sys.argv.pop(1)); '
                    'import pipeline; pipeline.ROOT=Path(sys.argv.pop(1)); pipeline.main()')
        def cli(action):
            output = subprocess.check_output([sys.executable, '-c', launcher, str(fixtures.ROOT / 'scripts'),
                str(self.root), action, str(self.group)], text=True)
            return json.loads(output)
        self.assertEqual(cli('advance-group')['phase'], 'executing')
        status = cli('status-group')
        self.assertEqual(status['members'][self.members[0].name]['phase'], 'execution_running')
        self.assertEqual(cli('stop-group')['phase'], 'stopped')
        self.assertEqual(cli('advance-group')['phase'], 'stopped')
        self.assertFalse((self.members[2] / 'execution/started').exists())

    def test_concurrency_one_never_overlaps_roles(self):
        self.prepare_group(concurrency=1)
        for _ in range(16):
            state = groups.advance(self.group)
            states = [pipeline.read(p / 'state.json') for p in self.members]
            self.assertLessEqual(sum(groups.active(s) for s in states), 1)
            if state['phase'] == 'reviewed':
                break
        self.assertEqual(state['phase'], 'reviewed')

    def test_collected_failure_without_answer_is_reference_status_not_success(self):
        self.prepare_group()
        adapter = self.root / 'adapter.py'
        text = adapter.read_text().replace("'exit_code':0,'timed_out':False", "'exit_code':(1 if q['role']=='execution' and q['run_id']=='fixture-a-business' else 0),'timed_out':False")
        text = text.replace("write('evidence.json',{'answer':'synthetic answer'})", "write('evidence.json',{'answer':'synthetic answer'})\n        if q['run_id']=='fixture-a-business': (out/'answer.md').unlink()")
        text = text.replace("'status':'completed','reason':'Synthetic answer", "'status':('not_completed' if q['run_id']=='fixture-a-business' else 'completed'),'reason':'Synthetic answer")
        text = text.replace("'passed':True", "'passed':q['run_id']!='fixture-a-business'")
        adapter.write_text(text)
        self.assertEqual(self.finish_group()['phase'], 'reviewed')
        peer = pipeline.read(self.group / 'peer-results/index.json')['members'][0]
        self.assertEqual(peer['execution']['exit_code'], 1)
        self.assertEqual(peer['missing_evidence'], ['answer.md'])
        self.assertEqual(peer['files'], [])
        with patch.object(pipeline.subprocess, 'run'):
            result = pipeline.read(pipeline.record(self.members[0]))
        self.assertEqual(result['status'], 'not_completed')
        self.assertIsNone(result['provenance']['answer_sha256'])

    def test_controller_timeout_does_not_hold_successful_peers(self):
        self.prepare_group()
        groups.advance(self.group)
        p = self.members[0]
        state = pipeline.read(p / 'state.json'); state['dispatched_at'] = '2000-01-01T00:00:00Z'
        pipeline.write(p / 'state.json', state)
        adapter = self.root / 'adapter.py'
        adapter.write_text(adapter.read_text().replace("elif op=='status':print(json.dumps({'status':'completed'}))",
            "elif op=='status':print(json.dumps({'status':'running' if q['role']=='execution' and q['run_id']=='fixture-a-business' else 'completed'}))"))
        state = self.finish_group()
        self.assertEqual(state['phase'], 'needs_attention')
        self.assertEqual(pipeline.read(p / 'state.json')['phase'], 'stopped')
        self.assertFalse((p / 'grading/started').exists())
        self.assertTrue(all(pipeline.read(m / 'state.json')['phase'] == 'reviewed' for m in self.members[1:]))
        entry = pipeline.read(self.group / 'peer-results/index.json')['members'][0]
        self.assertEqual(entry['controller_phase'], 'stopped')
        self.assertNotIn('execution', entry)

    def test_uncertain_start_is_stopped_without_resubmission_and_other_runs_finish(self):
        self.prepare_group()
        adapter = self.root / 'adapter.py'
        adapter.write_text(adapter.read_text().replace("p.write_text('started')", "p.write_text('started')\n    if q['role']=='execution' and q['run_id']=='fixture-a-business': raise RuntimeError('lost start response')"))
        state = self.finish_group()
        self.assertEqual(state['phase'], 'needs_attention')
        self.assertTrue(pipeline.read(self.members[0] / 'state.json')['stop_confirmed'])
        self.assertTrue(all(pipeline.read(m / 'state.json')['phase'] == 'reviewed' for m in self.members[1:]))

    def test_unconfirmed_stop_blocks_further_dispatch(self):
        self.prepare_group()
        adapter = self.root / 'adapter.py'
        text = adapter.read_text().replace("p.write_text('started')", "p.write_text('started')\n    raise RuntimeError('lost start response')")
        adapter.write_text(text.replace("{'stopped':True}", "{'stopped':False}"))
        self.assertEqual(groups.advance(self.group)['phase'], 'needs_attention')
        self.assertFalse(any((p / 'execution/started').exists() for p in self.members[1:]))

    def test_peer_snapshot_cannot_change_before_grading(self):
        self.prepare_group(); self.seal_group()
        (self.group / 'peer-results' / self.members[0].name / 'answer.md').write_text('tampered')
        with self.assertRaisesRegex(ValueError, 'snapshot changed'):
            groups.advance(self.group)
        self.assertFalse(any((p / 'grading/started').exists() for p in self.members))

    def test_peer_answer_copies_cannot_be_published_or_replace_target_answer(self):
        self.prepare_group(); self.finish_group()
        target, other = self.members[:2]
        source = target / 'grading-input/peer-results' / other.name / 'answer.md'
        copied = target / 'grading/artifacts/borrowed.md'
        copied.parent.mkdir(parents=True, exist_ok=True); copied.write_bytes(source.read_bytes())
        assessment = target / 'grading/assessment.json'
        review = pipeline.read(assessment); review['evidence'] = [{'path': 'grading/artifacts/borrowed.md'}]
        pipeline.write(assessment, review)
        recorder = pipeline.module('group_recorder', 'record-trial.py')
        with self.assertRaisesRegex(ValueError, 'private peer'):
            recorder.record(target, assessment, dry_run=True)
        (target / 'answer.md').unlink()
        with self.assertRaisesRegex(ValueError, 'missing final answer'):
            recorder.record(target, assessment, dry_run=True)

    def test_changed_grading_input_cannot_be_recorded(self):
        self.prepare_group(); self.finish_group()
        target = self.members[0]
        (target / 'grading-input/peer-results/index.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'Frozen grading input changed'):
            pipeline.record(target)


if __name__ == '__main__':
    unittest.main()
