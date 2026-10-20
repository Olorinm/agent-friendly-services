"""The producer freezes inputs, owns bounded roles and submits real queue facts."""
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import pipeline as runs
import pipeline_test as fixtures
import role_handoff as roles
import role_producer as producer
import task_queue as queue


class RoleProducerTests(unittest.TestCase):
    setUp = fixtures.PipelineTests.setUp

    def fixture(self, packages=2, cap=1):
        self.deadline = int(time.time())+3600
        self.queue = self.root/'queue'
        queue.init(self.queue, max_concurrency=2, budget_usd=10,
                   expires_at=datetime.fromtimestamp(self.deadline, timezone.utc).isoformat(), pool='no-model-fixture')
        self.plan = {'schema_version': 1, 'queue': str(self.queue),
                     'deadline_epoch': self.deadline, 'max_preparation_concurrency': cap,
                     'max_total_concurrency': 2+cap, 'packages': []}
        self.settings = {}
        for number in range(packages):
            name = 'package-'+str(number+1); source = self.root/name; source.mkdir()
            packet = source/'design-input'; packet.mkdir()
            (packet/'AGENTS.md').write_text('Frozen task designer; do not solve the task.')
            (packet/'prompt.txt').write_text('Design a simple expense conversion task from a synthetic ledger.')
            (packet/'demand.txt').write_text('Synthetic fixture demand; not service evidence.')
            item = {'id': name, 'design_input': str(packet)}
            for field, role in [('design_settings', 'task_design'), ('preparation_settings', 'material_preparation')]:
                runtime = name+'-'+role
                adapter = source/(role+'-adapter.json')
                runs.write(adapter, {'host': 'fixture-host', 'remote_root': '/fixture/roles',
                                     'billing_mode': 'chatgpt', 'containers': {runtime: runtime+'-container'}})
                settings = {'model': 'gpt-6.1-sol', 'reasoning_effort': 'medium', 'billing_mode': 'chatgpt',
                            'harness': {'name': 'codex', 'version': '0.162.0', 'mode': 'noninteractive'},
                            'runtime': runtime, 'seconds': 60, 'deadline_epoch': self.deadline,
                            'storage_floor_bytes': 1024,
                            'commands': {op: ['python3', str(ROOT/'scripts/runners/codex/adapter.py'),
                                              '--config', str(adapter), op, '{request}']
                                         for op in ('start', 'status', 'collect', 'stop')}}
                path = source/(role+'-settings.json'); runs.write(path, settings)
                item[field] = str(path); self.settings[name, role] = settings
            config = deepcopy(self.config)
            config['preflight'] = [{'url': 'https://example.com', 'method': 'HEAD'}]
            for role in ('execution', 'grading'): config[role]['max_model_requests'] = 10
            policy = {'rounds': [1], 'targets': {'approved-api': {'config': config}}, 'materials': {},
                      'generated_materials': {'ledger': {'file': 'materials/ledger.csv', 'format': 'csv',
                          'columns': {'currency': {'type': 'string', 'pattern': '[A-Z]{3}'}, 'amount': {'type': 'number'}}}}}
            path = source/'policy.json'; runs.write(path, policy); item['policy'] = str(path)
            self.plan['packages'].append(item)
        self.plan_path = self.root/'producer-plan.json'; self.directory = self.root/'producer'
        self.operations = []; self.uncertain = set(); self.unconfirmed = set(); self.running = set()
        self.sessions = {}; self.invocation_settings = []
        return self.plan

    def init(self):
        runs.write(self.plan_path, self.plan)
        return producer.init(self.directory, self.plan_path)

    def update_settings(self, number, key, value):
        path = Path(self.plan['packages'][number][key]); runs.write(path, value)

    def mock_model(self, directory, role, operation, settings, request):
        """Mock only adapter I/O; exercise real role proofs/compiler/queue files."""
        directory = Path(directory); package = directory.parent.name
        self.operations.append((package, role, operation))
        self.invocation_settings.append((package, role, operation, deepcopy(settings)))
        runs.write(directory/(role+'-'+operation+'.json'), request)
        if operation == 'start':
            self.assertEqual(runs.read(directory/'state.json')['phase'], 'starting')
            if package in self.uncertain: raise RuntimeError('start response lost')
            return {'handle': directory.name+'-'+role}
        if operation == 'status': return {'status': 'running' if package in self.running else 'completed'}
        if operation == 'stop': return {'stopped': package not in self.unconfirmed}
        if operation != 'collect': raise AssertionError(operation)
        self.complete(directory, role, settings, package)
        return {'collected': True}

    def complete(self, directory, role, settings, package):
        manifest = roles.verify(directory); output = directory/'output'; output.mkdir(exist_ok=True)
        session = self.sessions.setdefault((package, role), str(uuid.uuid4()))
        handle = directory.name+'-'+role; workspace = '/workspace/'+handle
        started = datetime.now(timezone.utc)
        receipt = {'role': role, 'session_id': session, 'workspace': workspace,
                   **{key: settings[key] for key in ('model', 'reasoning_effort', 'harness', 'runtime')},
                   'started_at': started.isoformat(), 'ended_at': (started+timedelta(milliseconds=1)).isoformat(),
                   'exit_code': 0, 'timed_out': False, 'input_verified': True, 'billing_mode': 'chatgpt',
                   'isolation': 'Synthetic adapter fixture, no model/service calls',
                   'runtime_code_preflight': {'source_sha256': manifest['runtime_sources']},
                   'runtime_image_id': 'sha256:'+'c'*64}
        runs.write(output/'receipt.json', receipt)
        usage = {'input_tokens': 100, 'cached_input_tokens': 20, 'cache_write_input_tokens': 0,
                 'output_tokens': 10, 'reasoning_output_tokens': 0}
        prompt = (directory/'input/AGENTS.md').read_text().strip()+'\n\n'+(directory/'input/prompt.txt').read_text()
        rows = [{'type': 'session_meta', 'payload': {'id': session, 'cwd': workspace}},
                {'type': 'turn_context', 'payload': {'model': settings['model'], 'effort': settings['reasoning_effort']}},
                {'type': 'response_item', 'payload': {'role': 'user', 'content': [{'text': prompt}]}},
                {'type': 'response_item', 'payload': {'role': 'assistant', 'content': [{'text': 'Saved role data.'}]}},
                {'type': 'token_usage_record', 'payload': {'response_id': 'fixture-response', 'usage': usage}}]
        raw = output/'session.raw.jsonl'; raw.write_text('\n'.join(map(json.dumps, rows))+'\n')
        events = [{'type': 'thread.started', 'thread_id': session}, {'type': 'turn.completed', 'usage': usage}]
        (output/'events.jsonl').write_text('\n'.join(map(json.dumps, events))+'\n')
        runs.write(output/'usage.json', {'schema_version': 1, 'model': settings['model'], 'complete': True,
            'requests': [{'id': 'fixture-response', 'usage': usage}], 'totals': usage,
            'sources': [{'path': 'session.raw.jsonl', 'sha256': runs.digest(raw)}]})
        runs.write(output/'artifact-input-index.json', {'input_snapshot': {'available': True,
            'root': '/run/afs/inputs/'+handle, 'entries': {name: {'kind': 'file', 'sha256': sha, 'uid': 0}
                                                        for name, sha in manifest['input_files'].items()}}})
        if role == 'task_design':
            payload = {'schema_version': 1, 'role': role, 'status': 'ready', 'blockers': [], 'package_id': package,
                       'tasks': [{'id': 'expenses', 'version': 'v1', 'description': 'Convert these expense amounts.',
                                  'inputs': 'Read materials/ledger.csv as original synthetic expenses.',
                                  'expected_output': 'Converted amounts and rate dates.', 'success': 'Correct conversion against actual rates.',
                                  'failure': 'Wrong dates or arithmetic.', 'material_ids': ['ledger'],
                                  'applicable_target_ids': ['approved-api']}]}
        else:
            designer = directory/'input/task-design.json'
            material = output/'artifacts/materials/ledger.csv'; material.parent.mkdir(parents=True, exist_ok=True)
            material.write_text('currency,amount\nEUR,12.5\n')
            payload = {'schema_version': 1, 'role': role, 'status': 'ready', 'blockers': [], 'package_id': package,
                       'designer_sha256': runs.digest(designer),
                       'materials': [{'id': 'ledger', 'file': 'materials/ledger.csv', 'sha256': runs.digest(material),
                                      'bytes': material.stat().st_size, 'synthetic': True, 'source': 'Synthetic fixture input',
                                      'validation': 'Parsed CSV with approved columns'}],
                       'assignments': [{'task_id': 'expenses', 'target_id': 'approved-api', 'round': 1,
                                        'status': 'ready', 'blockers': []}]}
        runs.write(output/'artifacts'/roles.ROLES[role], payload)
        runs.write(output/roles.ROLES[role], payload)

    def tick(self, **kwargs):
        with patch.object(roles.runs, 'invoke', side_effect=self.mock_model):
            return producer.tick(self.directory, **kwargs)

    def test_init_requires_one_deadline_and_whole_concurrency_envelope(self):
        self.fixture(cap=2)
        self.plan['max_total_concurrency'] = 3
        with self.assertRaisesRegex(ValueError, 'envelope'): self.init()
        self.assertFalse(self.directory.exists())
        self.plan['max_total_concurrency'] = 4; self.plan['deadline_epoch'] += 1
        with self.assertRaisesRegex(ValueError, 'envelope'): self.init()
        self.assertFalse(self.directory.exists())

    def test_parallel_packages_cannot_share_any_physical_preparation_role(self):
        self.fixture(cap=2)
        first = self.settings['package-1', 'task_design']
        # A different logical runtime/adapter file still resolves to the same
        # host/container, including cross-role sharing between two packages.
        second = self.settings['package-2', 'material_preparation']
        adapter = Path(second['commands']['start'][3])
        config = runs.read(adapter)
        config['containers'][second['runtime']] = first['runtime']+'-container'; runs.write(adapter, config)
        with self.assertRaisesRegex(ValueError, 'share physical'): self.init()

    def test_preparation_cannot_share_executor_or_grader_even_with_cap_one(self):
        self.fixture(packages=1)
        settings = self.settings['package-1', 'task_design']
        # Use the same official adapter-backed physical runtime in target config.
        path = Path(self.plan['packages'][0]['policy']); policy = runs.read(path)
        policy['targets']['approved-api']['config']['grading'] = deepcopy(settings)
        runs.write(path, policy)
        with self.assertRaisesRegex(ValueError, 'share test or grader'): self.init()

    def test_full_design_packet_additions_deletions_and_edits_block_every_dispatch(self):
        self.fixture(packages=1); self.init()
        packet = Path(self.plan['packages'][0]['design_input']); file = packet/'demand.txt'; original = file.read_bytes()
        initial = runs.read(self.directory/'state.json')
        for mutation in ('added', 'deleted', 'modified'):
            with self.subTest(mutation=mutation):
                if mutation == 'added': (packet/'new.txt').write_text('unfrozen material')
                elif mutation == 'deleted': file.unlink()
                else: file.write_text('changed demand')
                with patch.object(roles.runs, 'invoke') as invoke:
                    with self.assertRaises((ValueError, FileNotFoundError)): producer.verify(self.directory, initial)
                    state = producer.tick(self.directory)
                    self.assertEqual(state['phase'], 'stopped')
                    self.assertIn('frozen_source_error', state)
                    invoke.assert_not_called()
                if mutation == 'added': (packet/'new.txt').unlink()
                else: file.write_bytes(original)
                runs.write(self.directory/'state.json', initial)

    def test_source_drift_halts_allocated_handle_and_does_not_start_waiting_package(self):
        self.fixture(packages=2); self.init(); self.running.add('package-1'); self.tick()
        packet = Path(self.plan['packages'][1]['design_input']); (packet/'demand.txt').write_text('changed source')
        self.operations.clear(); state = self.tick()
        self.assertEqual(state['phase'], 'stopped')
        self.assertIn('frozen_source_error', state)
        self.assertIn(('package-1', 'task_design', 'stop'), self.operations)
        self.assertFalse(any(op == 'start' for _, _, op in self.operations))
        self.assertFalse(any(name == 'package-2' for name, _, _ in self.operations))

    def test_changed_plan_cannot_hide_an_active_handle_from_explicit_stop(self):
        self.fixture(packages=2); self.init(); self.running.add('package-1'); self.tick()
        altered = deepcopy(self.plan); altered['packages'] = []
        runs.write(self.directory/'plan.json', altered); self.operations.clear()
        state = self.tick(halt=True)
        self.assertEqual(state['phase'], 'stopped')
        self.assertIn(('package-1', 'task_design', 'stop'), self.operations)
        self.assertFalse(any(op == 'start' for _, _, op in self.operations))

    def test_adapter_drift_stops_original_physical_target_and_never_starts_waiting_package(self):
        self.fixture(packages=2); self.init(); self.running.add('package-1'); self.tick()
        settings = self.settings['package-1', 'task_design']
        path = Path(settings['commands']['start'][3]); before = runs.read(path)
        altered = deepcopy(before); altered['containers'][settings['runtime']] = 'unrelated-container'
        runs.write(path, altered); self.operations.clear(); self.invocation_settings.clear()
        state = self.tick()
        self.assertEqual(state['phase'], 'stopped')
        self.assertFalse(any(op == 'start' for _, _, op in self.operations))
        stop = next(s for package, role, operation, s in self.invocation_settings if operation == 'stop')
        actual_binding = runs.read(stop['commands']['stop'][3])
        self.assertEqual(actual_binding['containers'], before['containers'])
        self.assertNotEqual(actual_binding['containers'], altered['containers'])

    def test_design_to_preparation_to_real_work_package_submission_is_idempotent(self):
        self.fixture(packages=1); self.init()
        for _ in range(6): state = self.tick()
        self.assertEqual(state['phase'], 'finished')
        self.assertEqual(state['packages']['package-1']['phase'], 'submitted')
        self.assertEqual(state['packages']['package-1']['compiled_jobs'], 1)
        inbox = list((self.queue/'inbox').iterdir()); self.assertEqual(len(inbox), 1)
        self.assertEqual(self.operations.count(('package-1', 'task_design', 'start')), 1)
        self.assertEqual(self.operations.count(('package-1', 'material_preparation', 'start')), 1)
        self.assertNotEqual(self.sessions['package-1', 'task_design'], self.sessions['package-1', 'material_preparation'])
        handoff = runs.read(inbox[0]/'handoff.json'); config = handoff['members'][0]['config']
        self.assertEqual([p.name for p in Path(config['attachments']).iterdir()], ['ledger.csv'])
        self.assertEqual((Path(config['attachments'])/'ledger.csv').read_text(), 'currency,amount\nEUR,12.5\n')
        self.assertFalse(Path(handoff['members'][0]['directory']).exists())
        self.assertTrue((self.directory/'package-1/design/output/role-collection-proof.json').is_file())
        self.assertTrue((self.directory/'package-1/preparation/output/role-collection-proof.json').is_file())
        before = list(self.operations)
        for _ in range(3): self.tick()
        self.assertEqual(self.operations, before); self.assertEqual(len(list((self.queue/'inbox').iterdir())), 1)

    def test_ambiguous_start_stops_once_unconfirmed_handle_reserves_its_slot(self):
        self.fixture(packages=2, cap=1); self.init()
        self.uncertain.add('package-1'); self.unconfirmed.add('package-1')
        state = self.tick()
        self.assertEqual(state['packages']['package-1']['phase'], 'attention')
        self.assertEqual(state['packages']['package-2']['phase'], 'waiting')
        self.assertTrue(state['packages']['package-1']['stop_unconfirmed'])
        self.assertEqual(self.operations[:2], [('package-1', 'task_design', 'start'), ('package-1', 'task_design', 'stop')])
        for _ in range(3): self.tick()
        self.assertEqual(self.operations.count(('package-1', 'task_design', 'start')), 1)
        self.assertFalse(any(package == 'package-2' for package, _, _ in self.operations))
        self.assertEqual(list((self.queue/'inbox').iterdir()), [])

    def test_confirmed_stop_releases_failed_package_without_stopping_another(self):
        self.fixture(packages=2, cap=1); self.init(); self.uncertain.add('package-1')
        state = self.tick()
        self.assertEqual(state['packages']['package-1']['phase'], 'held')
        self.assertEqual(state['packages']['package-2']['phase'], 'designing')
        self.assertIn(('package-2', 'task_design', 'start'), self.operations)
        self.assertFalse(any(package == 'package-2' and op == 'stop' for package, _, op in self.operations))

    def test_failed_prepare_never_refunds_another_packages_reserved_slot(self):
        self.fixture(packages=4, cap=2); self.init()
        self.running.update(('package-1', 'package-3', 'package-4'))
        real_prepare = roles.prepare
        def prepare(directory, *args, **kwargs):
            if Path(directory).parent.name == 'package-2':
                raise OSError('fixture input copy failed before this role was allocated')
            return real_prepare(directory, *args, **kwargs)
        with patch.object(roles, 'prepare', side_effect=prepare): state = self.tick()
        self.assertEqual(state['packages']['package-2']['phase'], 'held')
        self.assertEqual(state['packages']['package-4']['phase'], 'waiting')
        started = {name for name, _, op in self.operations if op == 'start'}
        self.assertEqual(started, {'package-1', 'package-3'})

    def test_halt_scans_held_and_attention_handles_instead_of_only_active_rows(self):
        self.fixture(packages=2, cap=2); self.init(); self.running.update(('package-1', 'package-2'))
        self.tick(); state = runs.read(self.directory/'state.json')
        state['packages']['package-1']['phase'] = 'held'; state['packages']['package-2']['phase'] = 'attention'
        runs.write(self.directory/'state.json', state); self.operations.clear()
        result = self.tick(halt=True)
        self.assertEqual(result['phase'], 'stopped')
        self.assertEqual({package for package, _, op in self.operations if op == 'stop'}, {'package-1', 'package-2'})
        self.assertFalse(any(op == 'start' for _, _, op in self.operations))

    def test_explicit_stop_reconciles_even_a_finished_held_summary(self):
        self.fixture(packages=1); self.init(); self.running.add('package-1'); self.tick()
        state = runs.read(self.directory/'state.json'); state['phase'] = 'finished'
        state['packages']['package-1']['phase'] = 'held'; runs.write(self.directory/'state.json', state)
        self.operations.clear(); result = self.tick(halt=True)
        self.assertEqual(result['phase'], 'stopped')
        self.assertEqual([op for _, _, op in self.operations], ['stop', 'collect'])

    def test_storage_is_rechecked_before_preparation_start_after_design_collected(self):
        self.fixture(packages=1); self.init()
        # Outer queue check admits design with ample disk. Space drops between
        # roles; role_handoff must enforce its own floor at preparation start.
        self.tick()
        with patch.object(queue, 'storage_hold', return_value=None), patch.object(roles.shutil, 'disk_usage', return_value=SimpleNamespace(free=0)):
            state = self.tick()
        self.assertEqual(state['packages']['package-1']['phase'], 'preparing')
        prep = self.directory/'package-1/preparation'
        self.assertEqual(runs.read(prep/'state.json')['phase'], 'prepared')
        self.assertIn('Low storage', runs.read(prep/'state.json')['waiting_reason'])
        self.assertNotIn(('package-1', 'material_preparation', 'start'), self.operations)
        self.assertEqual(list((self.queue/'inbox').iterdir()), [])
        self.tick()
        self.assertEqual(self.operations.count(('package-1', 'material_preparation', 'start')), 1)

    def test_design_start_enforces_role_floor_even_after_queue_storage_check_passes(self):
        self.fixture(packages=1); self.init()
        with patch.object(queue, 'storage_hold', return_value=None), patch.object(roles.shutil, 'disk_usage', return_value=SimpleNamespace(free=0)):
            state = self.tick()
        self.assertEqual(state['packages']['package-1']['phase'], 'designing')
        design = self.directory/'package-1/design'
        self.assertEqual(runs.read(design/'state.json')['phase'], 'prepared')
        self.assertIn('Low storage', runs.read(design/'state.json')['waiting_reason'])
        self.assertEqual(self.operations, [])
        self.tick()
        self.assertEqual(self.operations.count(('package-1', 'task_design', 'start')), 1)


if __name__ == '__main__': unittest.main()
