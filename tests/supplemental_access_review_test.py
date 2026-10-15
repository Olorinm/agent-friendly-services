"""Material-gap admission needs a new collected review, never a regraded task."""
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
import importlib.util
import io
from pathlib import Path
import shutil
import sys
import stat
import tarfile
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import access_readiness
import supplemental_access_review as supplement

spec = importlib.util.spec_from_file_location('supplement_fixture_artifact_capture', ROOT / 'scripts/runners/codex/artifact_capture.py')
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)


class SupplementalAccessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.run = self.base / 'fixture-access'
        for name in ['execution', 'grading', 'grading-input', 'frozen/grading', 'frozen/execution']:
            (self.run / name).mkdir(parents=True)
        self.put(self.run / 'config.json', {'phase': 'access', 'trial_protocol': access_readiness.PROTOCOL,
                                           'service': 'fixture', 'route': 'sdk', 'execution': {'runtime': 'executor'}})
        self.put(self.run / 'grading/assessment.json', {'status': 'invalid_run', 'outcome': {'failure_cause': 'materials'}})
        self.put(self.run / 'execution/receipt.json', {'session_id': 'executor-session'})
        self.put(self.run / 'grading/receipt.json', {'session_id': '11111111-1111-1111-1111-111111111111'})
        self.put(self.run / 'execution/result.json', {'rows': [1]})
        self.put(self.run / 'frozen/admission.json', {'mode': 'enforce', 'status': 'documented_free'})
        self.put(self.run / 'frozen/grading/reference.json', {})
        (self.run / 'frozen/execution/ENVIRONMENT.md').write_text('Only the assigned fixture resource; no hard hold.')
        (self.run / 'grading-input/AGENTS.md').write_text('Independent fixture reviewer role')
        (self.run / 'grading-input/prompt.txt').write_text('Original grading prompt')
        self.put(self.run / 'grading-input/original-evidence.json', {'observed': 1})
        self.put(self.run / 'grading-input-hashes.json', supplement.tree(self.run / 'grading-input'))
        self.put(self.run / 'frozen-hashes.json', supplement.tree(self.run / 'frozen'))
        self.put(self.run / 'state.json', {'phase': 'reviewed', 'record_hashes': {
            'grading/assessment.json': supplement.digest(self.run / 'grading/assessment.json')}})
        self.facts = self.base / 'facts'
        self.facts.mkdir()
        self.put(self.facts / 'claims.json', {'exp': 123456, 'configuration_sha256': 'a' * 64})
        self.adapter = self.base / 'grading-adapter.json'
        self.put(self.adapter, {'billing_mode': 'chatgpt', 'containers': {'grader': 'physical-grader'}})
        self.settings = {'model': 'gpt-6.1-sol', 'reasoning_effort': 'high',
                         'harness': {'name': 'codex', 'version': '0.162.0', 'mode': 'noninteractive'},
                         'runtime': 'grader', 'seconds': 60, 'billing_mode': 'chatgpt',
                         'commands': {'start': ['python3', str(ROOT / 'scripts/runners/codex/adapter.py'),
                                               '--config', str(self.adapter), 'start', '{request}']}}
        self.review_id = 'fixture-access-supplement-01'
        self.review = self.path(self.review_id)

    def put(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) + '\n')

    def path(self, identity):
        return self.run / 'supplemental-access/reviews' / identity

    def prepare(self, identity=None):
        identity = identity or self.review_id
        return supplement.prepare(self.run, self.facts, self.path(identity), review_id=identity,
                                  reviewer_settings=self.settings)

    def collect(self, directory=None, *, session='22222222-2222-2222-2222-222222222222'):
        directory = directory or self.review
        manifest = supplement.read(directory / 'manifest.json')
        settings = manifest['reviewer_settings']
        output = directory / 'grading'
        output.mkdir()
        workspace = '/workspace/' + manifest['binding']['review_id'] + '-grading'
        assessment = supplement.read(directory / 'input/assessment.template.json')
        assessment.update(status='ready', service_execution='completed',
                          access_readiness={name: {'status': 'ready', 'evidence': 'Bound actual fixture response and supplemental source'}
                                            for name in access_readiness.FACETS},
                          hard_holds={'status': 'clear', 'items': [], 'evidence': 'Frozen ENV/reference authorization checked'})
        self.put(output / 'assessment.json', assessment)
        self.put(output / 'assessment.raw.json', assessment)
        model_workspace = self.base / 'model-workspaces' / manifest['binding']['review_id']
        model_workspace.parent.mkdir(exist_ok=True)
        shutil.copytree(directory / 'input', model_workspace, dirs_exist_ok=True)
        self.put(model_workspace / 'assessment.json', assessment)
        entries = {}
        for path in (directory / 'input').rglob('*'):
            entry = {'kind': 'directory' if path.is_dir() else 'file', 'mode': stat.S_IMODE(path.stat().st_mode), 'uid': 0, 'gid': 0}
            if path.is_file():
                entry.update(bytes=path.stat().st_size, sha256=supplement.digest(path))
            entries[str(path.relative_to(directory / 'input'))] = entry
        snapshot = {'root': '/run/afs/inputs/' + manifest['binding']['review_id'] + '-grading', 'available': True,
                    'sha256': supplement.object_hash(entries), 'entries': entries}
        archive = io.BytesIO()
        collector.archive_workspace(model_workspace, archive, snapshot)
        archive.seek(0)
        with tarfile.open(fileobj=archive) as stream:
            stream.extractall(output, filter='data')
        start = datetime.now(timezone.utc)
        self.put(output / 'receipt.json', {
            'session_id': session, 'workspace': workspace, 'model': settings['model'],
            'reasoning_effort': settings['reasoning_effort'], 'harness': settings['harness'],
            'runtime': settings['runtime'], 'started_at': start.isoformat(),
            'ended_at': (start + timedelta(seconds=1)).isoformat(), 'exit_code': 0, 'timed_out': False,
            'isolation': 'Fixture official isolated collector', 'input_verified': True, 'billing_mode': 'chatgpt',
            'runtime_code_preflight': {'source_sha256': manifest['runtime_sources']},
            'runtime_image_id': 'sha256:' + 'c' * 64})
        prompt = (directory / 'input/AGENTS.md').read_text().strip() + '\n\n' + (directory / 'input/prompt.txt').read_text()
        rows = [{'type': 'session_meta', 'payload': {'id': session, 'cwd': workspace}},
                {'type': 'turn_context', 'payload': {'model': settings['model'], 'effort': settings['reasoning_effort']}},
                {'type': 'response_item', 'payload': {'role': 'user', 'content': [{'text': prompt}]}},
                {'type': 'response_item', 'payload': {'role': 'assistant', 'content': [{'text': 'Fixture review inspected the bound evidence and wrote assessment.json.'}]}}]
        usage = {'input_tokens': 100, 'cached_input_tokens': 20, 'cache_write_input_tokens': 0,
                 'output_tokens': 10, 'reasoning_output_tokens': 0}
        rows.append({'type': 'token_usage_record', 'payload': {'response_id': 'fixture-response', 'usage': usage}})
        (output / 'session.raw.jsonl').write_text('\n'.join(json.dumps(row) for row in rows) + '\n')
        (output / 'events.jsonl').write_text(json.dumps({'type': 'thread.started', 'thread_id': session}) + '\n'
                                            + json.dumps({'type': 'turn.completed', 'usage': usage}) + '\n')
        self.put(output / 'usage.json', {'schema_version': 1, 'model': settings['model'], 'complete': True,
                                        'requests': [{'id': 'codex-response-1', 'usage': usage}], 'totals': usage,
                                        'sources': [{'path': 'session.raw.jsonl',
                                                     'sha256': supplement.digest(output / 'session.raw.jsonl')}]})
        request = manifest['request']
        self.put(directory / 'grading-start.json', request)
        self.put(directory / 'grading-start-result.json', {'handle': manifest['binding']['review_id'] + '-grading'})
        self.put(directory / 'grading-collect.json', {**request, 'handle': manifest['binding']['review_id'] + '-grading'})
        self.put(directory / 'grading-collect-result.json', {'collected': True})
        return assessment

    def rewrite_assessment(self, assessment):
        for name in ['assessment.json', 'assessment.raw.json', 'artifacts/assessment.json']:
            self.put(self.review / 'grading' / name, assessment)

    def test_valid_supplement_admits_without_rewriting_original_verdict_or_state(self):
        original_review = (self.run / 'grading/assessment.json').read_bytes()
        original_state = (self.run / 'state.json').read_bytes()
        self.assertFalse(access_readiness.decision(self.run, access_readiness.PROTOCOL)[0])
        self.prepare()
        self.collect()
        supplement.accept(self.run, self.review)
        self.assertTrue(access_readiness.decision(self.run, access_readiness.PROTOCOL)[0])
        self.assertEqual((self.run / 'grading/assessment.json').read_bytes(), original_review)
        self.assertEqual((self.run / 'state.json').read_bytes(), original_state)

    def test_frozen_packet_storage_is_shared_but_new_prompt_never_changes_original(self):
        old_prompt = (self.run / 'grading-input/prompt.txt').read_bytes()
        self.prepare()
        self.assertEqual((self.run / 'grading-input/prompt.txt').read_bytes(), old_prompt)
        self.assertEqual((self.run / 'grading-input/original-evidence.json').stat().st_ino,
                         (self.review / 'input/original-evidence.json').stat().st_ino)
        self.assertNotEqual((self.run / 'grading-input/prompt.txt').stat().st_ino,
                            (self.review / 'input/prompt.txt').stat().st_ino)

    def test_registered_secret_in_supplement_is_held_without_mutating_original(self):
        self.put(self.run / 'private-secrets.json', ['fixture-secret-token'])
        self.put(self.facts / 'claims.json', {'unsafe': 'fixture-secret-token'})
        original = (self.run / 'grading-input/prompt.txt').read_bytes()
        with self.assertRaisesRegex(ValueError, 'registered service secret'):
            self.prepare()
        self.assertEqual((self.run / 'grading-input/prompt.txt').read_bytes(), original)

    def test_operator_assertion_or_ready_facets_without_collected_review_cannot_admit(self):
        self.prepare()
        self.put(self.review / 'grading/assessment.json', {'independent': True, 'status': 'ready'})
        with self.assertRaises(OSError):
            supplement.accept(self.run, self.review)
        self.assertFalse(supplement.decision(self.run)[0])

    def test_changed_old_execution_evidence_and_original_assessment_are_rejected(self):
        for name in ['execution/result.json', 'grading/assessment.json']:
            with self.subTest(name=name):
                self.prepare()
                self.collect()
                original = (self.run / name).read_bytes()
                (self.run / name).write_text('{"changed":true}')
                with self.assertRaises(ValueError):
                    supplement.accept(self.run, self.review)
                (self.run / name).write_bytes(original)
                shutil.rmtree(self.review)

    def test_changed_frozen_supplement_packet_is_rejected(self):
        self.prepare()
        self.collect()
        self.put(self.review / 'input/supplemental-access/facts/claims.json', {'exp': 999})
        with self.assertRaisesRegex(ValueError, 'packet changed'):
            supplement.accept(self.run, self.review)

    def test_original_route_hold_cannot_be_cleared_by_operator_or_new_review(self):
        self.put(self.run / 'frozen/grading/reference.json', {'cohort_disclosure': {'held_routes': {'fixture/sdk': 'Unresolved free scope'}}})
        self.put(self.run / 'frozen-hashes.json', supplement.tree(self.run / 'frozen'))
        with self.assertRaisesRegex(ValueError, 'hard hold'):
            self.prepare()

    def test_supplement_hard_hold_or_unknown_decision_still_blocks(self):
        self.prepare()
        assessment = self.collect()
        for updates in [{'status': 'unknown'}, {'hard_holds': {'status': 'blocked', 'items': ['Expired authorization'], 'evidence': 'Actual source'}},
                        {'hard_holds': False}, {'service_execution': 'unknown'}]:
            with self.subTest(updates=updates):
                value = {**assessment, **updates}
                self.rewrite_assessment(value)
                with self.assertRaises((ValueError, AttributeError)):
                    supplement.accept(self.run, self.review)

    def test_duplicate_or_executor_reviewer_session_is_rejected(self):
        self.prepare()
        self.collect(session='11111111-1111-1111-1111-111111111111')
        with self.assertRaisesRegex(ValueError, 'new independent'):
            supplement.accept(self.run, self.review)
        shutil.rmtree(self.review / 'grading')
        self.collect()
        supplement.accept(self.run, self.review)
        second = 'fixture-access-supplement-02'
        self.prepare(second)
        self.collect(self.path(second))
        with self.assertRaisesRegex(ValueError, 'session already accepted'):
            supplement.accept(self.run, self.path(second), replace_active=True)

    def test_forged_receipt_wrong_runtime_sources_or_missing_native_rollout_is_rejected(self):
        self.prepare()
        self.collect()
        receipt = supplement.read(self.review / 'grading/receipt.json')
        receipt['runtime_code_preflight']['source_sha256']['worker.py'] = 'd' * 64
        self.put(self.review / 'grading/receipt.json', receipt)
        with self.assertRaisesRegex(ValueError, 'runtime source provenance'):
            supplement.accept(self.run, self.review)

    def test_metadata_only_rollout_and_operator_ready_are_not_an_independent_review(self):
        self.prepare()
        self.collect()
        raw = self.review / 'grading/session.raw.jsonl'
        rows = [json.loads(line) for line in raw.read_text().splitlines()]
        rows = [row for row in rows if row.get('type') != 'token_usage_record'
                and row.get('payload', {}).get('role') != 'assistant']
        raw.write_text('\n'.join(json.dumps(row) for row in rows) + '\n')
        self.put(self.review / 'grading/usage.json', {'sources': [{'path': raw.name, 'sha256': supplement.digest(raw)}]})
        with self.assertRaisesRegex(ValueError, 'no actual assistant'):
            supplement.accept(self.run, self.review)

    def test_missing_real_requests_or_controller_collect_receipt_is_rejected(self):
        self.prepare()
        self.collect()
        usage = self.review / 'grading/usage.json'
        saved = usage.read_bytes()
        value = supplement.read(usage)
        value['requests'] = []
        self.put(usage, value)
        with self.assertRaisesRegex(ValueError, 'actual model request usage'):
            supplement.accept(self.run, self.review)
        usage.write_bytes(saved)
        self.put(self.review / 'grading-collect-result.json', {'independent': True})
        with self.assertRaisesRegex(ValueError, 'formal controller'):
            supplement.accept(self.run, self.review)

    def test_collected_model_artifact_and_workspace_must_match_frozen_manifest(self):
        self.prepare()
        self.collect()
        path = self.review / 'grading/artifact-input-index.json'
        index = supplement.read(path)
        next(row for row in index['omitted'] if row['path'] == 'original-evidence.json')['change'] = 'deleted_input'
        self.put(path, index)
        with self.assertRaisesRegex(ValueError, 'workspace differs'):
            supplement.accept(self.run, self.review)

    def test_real_delta_collector_keeps_unchanged_input_only_in_trusted_index(self):
        self.prepare()
        self.collect()
        self.assertFalse((self.review / 'grading/artifacts/original-evidence.json').exists())
        index = supplement.read(self.review / 'grading/artifact-input-index.json')
        self.assertEqual(next(row for row in index['omitted'] if row['path'] == 'original-evidence.json')['change'], 'unchanged_input')
        supplement.accept(self.run, self.review)
        self.assertTrue(supplement.decision(self.run)[0])

    def test_single_active_pointer_requires_explicit_replacement_and_old_attempt_is_retained(self):
        self.prepare()
        self.collect()
        supplement.accept(self.run, self.review)
        original_accepted = (self.review / 'accepted.json').read_bytes()
        second = 'fixture-access-supplement-02'
        self.prepare(second)
        self.collect(self.path(second), session='33333333-3333-3333-3333-333333333333')
        with self.assertRaisesRegex(ValueError, 'explicit replacement'):
            supplement.accept(self.run, self.path(second))
        supplement.accept(self.run, self.path(second), replace_active=True)
        self.assertEqual((self.review / 'accepted.json').read_bytes(), original_accepted)
        self.assertTrue(supplement.decision(self.run)[0])

    def test_changed_evidence_or_accepted_record_after_activation_invalidates_admission(self):
        self.prepare()
        self.collect()
        supplement.accept(self.run, self.review)
        (self.run / 'execution/result.json').write_text('{}')
        self.assertFalse(supplement.decision(self.run)[0])


if __name__ == '__main__':
    unittest.main()
