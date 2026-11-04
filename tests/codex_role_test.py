"""Explicit Codex roles/effort retain fresh inputs and truthful receipts."""
from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT/relative)
    value = importlib.util.module_from_spec(spec); spec.loader.exec_module(value)
    return value


adapter = module('roles_codex_adapter', 'scripts/runners/codex/adapter.py')
normalizer = module('roles_codex_normalize', 'scripts/runners/codex/normalize.py')
capture = module('roles_codex_capture', 'scripts/runners/codex/artifact_capture.py')
with patch.dict(sys.modules, {'normalize': normalizer, 'artifact_capture': capture}):
    worker = module('roles_codex_worker', 'scripts/runners/codex/worker.py')


class CodexRoleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()

    def request(self, role='grading', effort='high'):
        return {'role': role, 'model': 'gpt-6.1-sol', 'reasoning_effort': effort,
                'run_id': 'fixture', 'runtime': 'codex', 'seconds': 90,
                'harness': {'name': 'codex', 'version': '0.162.0'}}

    def test_only_explicit_supported_roles_model_and_efforts_are_accepted(self):
        for role in ('task_design', 'material_preparation', 'grading'):
            for effort in ('medium', 'high'):
                request = self.request(role, effort)
                adapter.validate_request(request)
                self.assertEqual(worker.validate_request(request), 'fixture-'+role)
        for key, value in [('role', 'execution'), ('role', 'unknown'),
                           ('role', None), ('model', 'gpt-6-sol'),
                           ('reasoning_effort', 'low'), ('reasoning_effort', 'xhigh'),
                           ('reasoning_effort', None)]:
            with self.subTest(key=key, value=value):
                request = self.request(); request[key] = value
                with self.assertRaises(ValueError): adapter.validate_request(request)
                with self.assertRaises(ValueError): worker.validate_request(request)

    def test_command_uses_actual_frozen_effort_and_retains_context_isolation(self):
        for role in ('task_design', 'material_preparation', 'grading'):
            for effort in ('medium', 'high'):
                command = worker.codex_command(self.request(role, effort), Path('/workspace/fixture-'+role))
                options = dict(command[i+1].split('=', 1) for i, value in enumerate(command) if value == '-c')
                self.assertEqual(json.loads(options['model_reasoning_effort']), effort)
                for name in ('features.apps', 'features.memories', 'features.plugins',
                             'features.hooks', 'skills.include_instructions', 'agents.enabled'):
                    self.assertFalse(json.loads(options[name]))
                self.assertIn('--ignore-user-config', command); self.assertIn('--ignore-rules', command)
                self.assertEqual(command[-1], '-')

    def test_observed_medium_requires_matching_actual_context_for_every_turn(self):
        session = self.root/'session.jsonl'
        rows = [{'type': 'turn_context', 'payload': {'model': 'gpt-6.1-sol', 'effort': 'medium'}},
                {'type': 'response_item', 'payload': {'role': 'user', 'content': [{'text': 'frozen role\n\nfrozen input'}]}}]
        session.write_text('\n'.join(map(json.dumps, rows)))
        self.assertTrue(normalizer.observed_input(session, 'frozen role\n\nfrozen input', 'gpt-6.1-sol', 'medium'))
        self.assertFalse(normalizer.observed_input(session, 'frozen role\n\nfrozen input', 'gpt-6.1-sol', 'high'))
        rows.append({'type': 'turn_context', 'payload': {'model': 'gpt-6.1-sol', 'effort': 'high'}})
        session.write_text('\n'.join(map(json.dumps, rows)))
        self.assertFalse(normalizer.observed_input(session, 'frozen role\n\nfrozen input', 'gpt-6.1-sol', 'medium'))

    def test_adapter_routes_status_to_actual_role_handle(self):
        for role in ('task_design', 'material_preparation', 'grading'):
            request = self.request(role, 'medium'); path = self.root/(role+'.json')
            path.write_text(json.dumps(request)); calls = []
            def remote(config, argv, data=None, check=True):
                calls.append(argv)
                return SimpleNamespace(stdout=b'{"status":"completed"}', returncode=0)
            with patch.object(adapter, 'load', return_value={'billing_mode': 'chatgpt', 'containers': {'codex': 'fixture'}, 'remote_root': '/controller'}), patch.object(adapter, 'remote_ssh', side_effect=remote), patch.object(sys, 'argv', ['adapter', '--config', 'config.json', 'status', str(path)]), redirect_stdout(io.StringIO()):
                adapter.main()
            self.assertIn('/run/afs/fixture-'+role+'/done.json', calls[0])

    def run_worker(self, role, effort):
        base = self.root/(role+'-'+effort); base.mkdir()
        controller = base/'controller'; controller.mkdir()
        workspace_root = base/'workspace'; workspace_root.mkdir()
        home_root = base/'home'; home_root.mkdir()
        temp_root = base/'temp'; temp_root.mkdir()
        for parent in (workspace_root, home_root, temp_root):
            (parent/'old-answer.txt').write_text('previous role secret must be archived')
        run = 'fixture-'+role
        frozen = controller/'inputs'/run; frozen.mkdir(parents=True)
        (frozen/'AGENTS.md').write_text('frozen '+role+' role')
        (frozen/'prompt.txt').write_text('frozen input')
        (controller/'auth.json').write_text(json.dumps({'auth_mode': 'chatgpt', 'tokens': {'fixture': 'synthetic-no-real-auth'}}))
        request = self.request(role, effort); path = base/'request.json'; path.write_text(json.dumps(request))
        commands = []; output = controller/run/'output'; expected_prompt = 'frozen '+role+' role\n\nfrozen input'
        class Process:
            pid = 12345; returncode = 0
            def communicate(self, prompt, timeout):
                self_prompt = prompt.decode(); self_test.assertEqual(self_prompt, expected_prompt)
                workspace = workspace_root/run
                self_test.assertFalse((workspace/'old-answer.txt').exists())
                self_test.assertFalse((home_root/'old-answer.txt').exists())
                self_test.assertFalse((temp_root/'old-answer.txt').exists())
                (workspace/'codex-final.md').write_text('role result')
                (workspace/worker.ROLE_OUTPUTS[role]).write_text(json.dumps({'schema_version': 1, 'status': 'ready'}))
                (workspace/'assessment.json').write_text(json.dumps({'status': 'completed'}))
                (output/'events.jsonl').write_text(json.dumps({'type': 'thread.started', 'thread_id': '00000000-0000-0000-0000-000000000001'})+'\n'+json.dumps({'type': 'turn.completed', 'usage': {'input_tokens': 10, 'output_tokens': 2}})+'\n')
        self_test = self
        def popen(command, **kwargs):
            commands.append(command)
            self.assertIs(kwargs['preexec_fn'], worker.identity)
            self.assertEqual(kwargs['env']['HOME'], str(home_root/run))
            self.assertEqual(kwargs['env']['CODEX_HOME'], str(home_root/run/'.codex'))
            return Process()
        def rollout(auth_root, session, out):
            rows = [{'type': 'turn_context', 'payload': {'model': request['model'], 'effort': effort}},
                    {'type': 'response_item', 'payload': {'role': 'user', 'content': [{'text': expected_prompt}]}}]
            (out/'session.raw.jsonl').write_text('\n'.join(map(json.dumps, rows)))
        def collect(workspace, private, out): shutil.copytree(workspace, out/'artifacts')
        previous_umask = os.umask(0o077)
        try:
            with patch.object(worker, 'ROOT', controller), patch.object(worker, 'WORKSPACE_ROOT', workspace_root), patch.object(worker, 'HOME_ROOT', home_root), patch.object(worker, 'TEMP_ROOTS', (temp_root,)), patch.object(worker.subprocess, 'run', return_value=SimpleNamespace(returncode=0)), patch.object(worker.subprocess, 'check_output', return_value='codex-cli 0.162.0'), patch.object(worker.subprocess, 'Popen', side_effect=popen), patch.object(worker, 'capture_rollout', side_effect=rollout), patch.object(worker, 'normalize'), patch.object(worker, 'collect_artifacts', side_effect=collect), patch.object(sys, 'argv', ['worker.py', str(path)]):
                worker.main()
        finally: os.umask(previous_umask)
        receipt = json.loads((output/'receipt.json').read_text())
        self.assertEqual(receipt['role'], role); self.assertEqual(receipt['reasoning_effort'], effort)
        self.assertTrue(receipt['input_verified']); self.assertIn(role, receipt['isolation'])
        self.assertEqual(receipt['workspace'], str(workspace_root/run))
        self.assertTrue((output/worker.ROLE_OUTPUTS[role]).is_file())
        if role != 'grading': self.assertFalse((output/'assessment.json').exists())
        self.assertEqual((output/'answer.md').read_text(), 'role result')
        self.assertEqual((frozen/'prompt.txt').read_text(), 'frozen input')
        self.assertIn('model_reasoning_effort='+json.dumps(effort), commands[0])

    def test_worker_receipts_artifacts_and_fresh_sessions_for_all_roles(self):
        for role in ('task_design', 'material_preparation', 'grading'):
            with self.subTest(role=role): self.run_worker(role, 'medium')
        self.run_worker('grading', 'high')


if __name__ == '__main__': unittest.main()
