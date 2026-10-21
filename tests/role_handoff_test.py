"""Cloud preparation starts once and only completed native work becomes input."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import role_handoff as roles
import role_contract


class RoleHandoffTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name); self.directory = self.root / 'designer-one'
        self.input = self.root / 'input'; self.input.mkdir()
        (self.input / 'AGENTS.md').write_text('Independent task designer')
        (self.input / 'prompt.txt').write_text('Design a useful task from this brief.')
        self.adapter = self.root / 'adapter.json'
        roles.runs.write(self.adapter, {'billing_mode': 'chatgpt', 'containers': {'designer': 'design-only'}})
        self.settings = {'model': 'gpt-6.1-sol', 'reasoning_effort': 'medium', 'billing_mode': 'chatgpt',
                         'harness': {'name': 'codex', 'version': '0.162.0', 'mode': 'noninteractive'},
                         'runtime': 'designer', 'seconds': 60, 'deadline_epoch': time.time() + 3600,
                         'commands': {op: ['python3', str(ROOT / 'scripts/runners/codex/adapter.py'),
                                           '--config', str(self.adapter), op, '{request}']
                                      for op in ('start', 'status', 'collect', 'stop')}}
        self.settings_path = self.root / 'settings.json'; roles.runs.write(self.settings_path, self.settings)

    def prepare(self):
        return roles.prepare(self.directory, 'task_design', self.input, self.settings_path)

    def test_output_schema_is_the_consumer_contract_and_part_of_frozen_input(self):
        self.prepare(); manifest = roles.verify(self.directory)
        file = self.directory/'input/output-schema.json'
        self.assertEqual(roles.runs.read(file), role_contract.schema('task_design'))
        self.assertEqual(manifest['input_files']['output-schema.json'], roles.runs.digest(file))
        file.write_text('{}')
        with self.assertRaisesRegex(ValueError, 'input changed'): roles.verify(self.directory)

    def completed(self):
        manifest = roles.verify(self.directory); output = self.directory / 'output'; output.mkdir()
        session = '11111111-2222-3333-4444-555555555555'
        handle = self.directory.name + '-task_design'; workspace = '/workspace/' + handle
        start = datetime.now(timezone.utc)
        receipt = {'session_id': session, 'workspace': workspace, 'role': 'task_design',
                   **{key: self.settings[key] for key in ('model', 'reasoning_effort', 'harness', 'runtime')},
                   'started_at': start.isoformat(), 'ended_at': (start + timedelta(seconds=1)).isoformat(),
                   'exit_code': 0, 'timed_out': False, 'isolation': 'dedicated fixture runtime',
                   'input_verified': True, 'billing_mode': 'chatgpt',
                   'runtime_code_preflight': {'source_sha256': manifest['runtime_sources']},
                   'runtime_image_id': 'sha256:' + 'c' * 64}
        roles.runs.write(output / 'receipt.json', receipt)
        usage = {'input_tokens': 100, 'cached_input_tokens': 20, 'cache_write_input_tokens': 0,
                 'output_tokens': 10, 'reasoning_output_tokens': 0}
        prompt = (self.directory / 'input/AGENTS.md').read_text().strip() + '\n\n' + (self.directory / 'input/prompt.txt').read_text()
        rows = [{'type': 'session_meta', 'payload': {'id': session, 'cwd': workspace}},
                {'type': 'turn_context', 'payload': {'model': 'gpt-6.1-sol', 'effort': 'medium'}},
                {'type': 'response_item', 'payload': {'role': 'user', 'content': [{'text': prompt}]}},
                {'type': 'response_item', 'payload': {'role': 'assistant', 'content': [{'text': 'Task saved.'}]}},
                {'type': 'token_usage_record', 'payload': {'response_id': 'fixture-response', 'usage': usage}}]
        (output / 'session.raw.jsonl').write_text('\n'.join(json.dumps(row) for row in rows) + '\n')
        (output / 'events.jsonl').write_text(json.dumps({'type': 'thread.started', 'thread_id': session}) + '\n'
                                            + json.dumps({'type': 'turn.completed', 'usage': usage}) + '\n')
        roles.runs.write(output / 'usage.json', {'schema_version': 1, 'model': 'gpt-6.1-sol', 'complete': True,
                         'requests': [{'id': 'fixture-response', 'usage': usage}], 'totals': usage,
                         'sources': [{'path': 'session.raw.jsonl', 'sha256': roles.runs.digest(output / 'session.raw.jsonl')}]})
        roles.runs.write(output / 'artifact-input-index.json', {'input_snapshot': {'available': True,
                         'root': '/run/afs/inputs/' + handle,
                         'entries': {name: {'kind': 'file', 'sha256': sha, 'uid': 0}
                                     for name, sha in manifest['input_files'].items()}}})
        result = {'schema_version': 1, 'status': 'ready', 'package_id': 'fixture', 'tasks': []}
        roles.runs.write(output / 'artifacts/task-design.json', result)
        roles.runs.write(output / 'task-design.json', result)
        roles.runs.write(self.directory / 'task_design-start.json', manifest['request'])
        roles.runs.write(self.directory / 'task_design-start-result.json', {'handle': handle})
        roles.runs.write(self.directory / 'task_design-collect.json', {**manifest['request'], 'handle': handle})
        roles.runs.write(self.directory / 'task_design-collect-result.json', {'collected': True})
        return manifest, output

    def test_uncertain_start_is_durable_and_never_repeated(self):
        self.prepare()
        with patch.object(roles, 'invoke', side_effect=RuntimeError('response lost')) as invoke:
            state = roles.advance(self.directory)
            self.assertEqual(state['phase'], 'uncertain_start')
            self.assertEqual(state['handle'], 'designer-one-task_design')
            self.assertEqual(roles.advance(self.directory)['phase'], 'uncertain_start')
            self.assertEqual(invoke.call_count, 1)

    def test_start_intention_exists_before_actual_start(self):
        self.prepare()
        def invoke(directory, manifest, operation, handle=None):
            self.assertEqual(operation, 'start')
            self.assertEqual(roles.runs.read(directory / 'state.json')['phase'], 'starting')
            return {'handle': directory.name + '-task_design'}
        with patch.object(roles, 'invoke', side_effect=invoke):
            self.assertEqual(roles.advance(self.directory)['phase'], 'running')

    def test_completed_role_has_private_verified_account_proof(self):
        self.prepare(); manifest, output = self.completed()
        proof = roles.validate_collection(self.directory, manifest)
        self.assertTrue(proof['verified']); self.assertTrue(proof['native_turn_completed'])
        self.assertEqual(proof['account_usage']['tokens']['output_tokens'], 10)
        self.assertIsNone(proof['account_usage']['cost_usd'])
        self.assertTrue((output / 'role-collection-proof.json').is_file())

    def test_exit_zero_without_native_completion_is_not_accepted(self):
        self.prepare(); manifest, output = self.completed()
        (output / 'events.jsonl').write_text((output / 'events.jsonl').read_text().splitlines()[0] + '\n')
        with self.assertRaisesRegex(ValueError, 'Native role turn'):
            roles.validate_collection(self.directory, manifest)
        self.assertFalse((output / 'role-collection-proof.json').exists())

    def test_canonical_usage_cannot_override_native_requests(self):
        self.prepare(); manifest, output = self.completed()
        file = output / 'usage.json'; usage = roles.runs.read(file)
        usage['requests'][0]['usage']['output_tokens'] = 11
        usage['totals']['output_tokens'] = 11
        roles.runs.write(file, usage)
        with self.assertRaisesRegex(ValueError, 'actual native model requests'):
            roles.validate_collection(self.directory, manifest)

    def test_claimed_model_effort_does_not_override_actual_session(self):
        self.prepare(); manifest, output = self.completed()
        raw = output / 'session.raw.jsonl'; raw.write_text(raw.read_text().replace('"effort": "medium"', '"effort": "high"'))
        with self.assertRaisesRegex(ValueError, 'prompt/model/effort'):
            roles.validate_collection(self.directory, manifest)

    def test_generated_prose_cannot_replace_actual_artifact(self):
        self.prepare(); manifest, output = self.completed()
        roles.runs.write(output / 'task-design.json', {'schema_version': 1, 'status': 'ready', 'fabricated': True})
        with self.assertRaisesRegex(ValueError, 'actual captured model artifact'):
            roles.validate_collection(self.directory, manifest)

    def test_input_or_adapter_mutation_prevents_dispatch(self):
        self.prepare(); (self.directory / 'input/prompt.txt').write_text('Changed task')
        with patch.object(roles, 'invoke') as invoke:
            with self.assertRaisesRegex(ValueError, 'input changed'): roles.advance(self.directory)
            invoke.assert_not_called()
        shutil_input = self.input / 'prompt.txt'
        (self.directory / 'input/prompt.txt').write_bytes(shutil_input.read_bytes())
        roles.runs.write(self.adapter, {'billing_mode': 'chatgpt', 'containers': {'designer': 'different-runtime'}})
        with self.assertRaisesRegex(ValueError, 'runtime/source changed'): roles.verify(self.directory)

    def test_bad_ownership_in_collected_baseline_is_rejected(self):
        self.prepare(); manifest, output = self.completed()
        f = output / 'artifact-input-index.json'; z = roles.runs.read(f)
        z['input_snapshot']['entries']['prompt.txt']['uid'] = 1000; roles.runs.write(f, z)
        with self.assertRaisesRegex(ValueError, 'hash/owner'): roles.validate_collection(self.directory, manifest)

    def test_insufficient_window_holds_without_start(self):
        self.settings['deadline_epoch'] = time.time() + 30; roles.runs.write(self.settings_path, self.settings)
        self.prepare()
        with patch.object(roles, 'invoke') as invoke:
            self.assertEqual(roles.advance(self.directory)['phase'], 'held'); invoke.assert_not_called()

    def test_low_storage_pauses_prepared_role_without_allocation(self):
        self.prepare()
        with patch.object(roles.shutil, 'disk_usage', return_value=type('Disk', (), {'free': 1})()), patch.object(roles, 'invoke') as invoke:
            state = roles.advance(self.directory)
            self.assertEqual(state['phase'], 'prepared')
            self.assertIn('Low storage', state['waiting_reason']); invoke.assert_not_called()

    def test_mutated_adapter_cannot_block_stop_or_redirect_its_target(self):
        self.prepare()
        roles.runs.write(self.directory / 'state.json', {'phase': 'running', 'handle': 'designer-one-task_design'})
        roles.runs.write(self.adapter, {'billing_mode': 'chatgpt', 'containers': {'designer': 'unrelated-target'}})
        (self.directory / 'input/prompt.txt').write_text('Changed while model active')
        seen = []
        def invoke(directory, manifest, op, handle=None):
            seen.append(op)
            argv = manifest['settings']['commands'][op]
            frozen = roles.runs.read(argv[argv.index('--config') + 1])
            self.assertEqual(frozen['containers']['designer'], 'design-only')
            self.assertEqual(handle, 'designer-one-task_design')
            return {'stopped': True} if op == 'stop' else {'collected': True}
        with patch.object(roles, 'invoke', side_effect=invoke):
            state = roles.advance(self.directory, halt=True)
        self.assertEqual(state['phase'], 'stopped'); self.assertTrue(state['stop_confirmed'])
        self.assertIn('frozen_input_error', state); self.assertEqual(seen, ['stop', 'collect'])

    def test_one_failed_status_only_stops_this_handle(self):
        self.prepare(); roles.runs.write(self.directory / 'state.json', {'phase': 'running', 'handle': 'designer-one-task_design'})
        operations = []
        def invoke(directory, manifest, op, handle=None):
            operations.append((op, handle))
            if op == 'status': raise RuntimeError('collector failed')
            return {'stopped': True} if op == 'stop' else {'collected': True}
        with patch.object(roles, 'invoke', side_effect=invoke):
            self.assertEqual(roles.advance(self.directory)['phase'], 'held')
        self.assertEqual(operations, [('status', 'designer-one-task_design'), ('stop', 'designer-one-task_design'),
                                      ('collect', 'designer-one-task_design')])


if __name__ == '__main__': unittest.main()
