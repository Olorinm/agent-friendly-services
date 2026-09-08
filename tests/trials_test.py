import importlib.util
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parents[1]


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, REPO / 'scripts' / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


runner = load('runner', 'codex-service-trial.py')
recorder = load('recorder', 'record-trial.py')


class Trials(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='afs-trial-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        runner.ROOT = recorder.ROOT = self.root
        self.task = self.root / 'tasks.md'
        self.task.write_text('| ID | 用户任务 | 预计输入 | 预计输出 | 完成标准 | 未完成标准 | 版本 |\n'
                             '| rows-1 | Read rows | table A | rows | rows match | missing rows | v2 |\n')
        self.catalog = {'services': [{'id': 'database-example', 'catalog': {'routes': [
            {'id': 'http', 'entry_url': 'https://example.com/api'},
            {'id': 'cli', 'entry_url': 'https://example.com/cli'}]}}]}
        (self.root / 'generated').mkdir()
        (self.root / 'generated/catalog.json').write_text(json.dumps(self.catalog))
        self.run = self.root / 'data/experiments/results/trials/run-1'
        self.workspace = self.run / 'workspace'
        self.workspace.mkdir(parents=True)
        (self.workspace / 'response.json').write_text('{"rows": [1]}')
        (self.run / 'answer.md').write_text('rows: [1]')
        task, row = runner.select_task(self.task, 'rows-1')
        self.meta = {'service': 'database-example', 'route_id': 'http', 'entry_url': 'https://example.com/api',
            'task': task, 'task_id': task['id'], 'task_row': row, 'task_sha256': task['sha256'],
            'prompt_sha256': 'a' * 64, 'workspace': str(self.workspace),
            'model': 'fixture-model', 'reasoning_effort': 'high', 'cli_version': 'fixture-harness',
            'started_at': '2026-09-07T01:00:00Z', 'ended_at': '2026-09-07T01:00:02Z',
            'elapsed_seconds': 2, 'seconds_limit': 60, 'exit_code': 0, 'timed_out': False,
            'isolation': 'test fixture', 'usage': {'input_tokens': 17, 'cached_input_tokens': 8, 'output_tokens': 3},
            'agent_cost_usd': None, 'agent_cost_reason': 'unknown in fixture'}
        self.assessment = {'status': 'completed', 'reason': 'Rows match response', 'reviewer': 'external test reviewer',
            'checks': [{'criterion': 'row match', 'passed': True, 'evidence': 'response rows = answer rows'}],
            'evidence': [{'path': 'workspace/response.json'}], 'service_cost_usd': None, 'human_interventions': 0}
        self.review = self.run / 'assessment.json'

    def save(self):
        (self.run / 'run.json').write_text(json.dumps(self.meta))
        self.review.write_text(json.dumps(self.assessment))

    def test_arbitrary_task_and_route_and_ambiguity(self):
        task, _ = runner.select_task(self.task, 'rows-1')
        self.assertEqual(task['description'], 'Read rows')
        self.assertEqual(task['version'], 'v2')
        with self.assertRaisesRegex(ValueError, 'Choose --route'):
            runner.select_route(self.catalog, 'database-example', None)
        self.assertEqual(runner.select_route(self.catalog, 'database-example', 'cli')['entry_url'], 'https://example.com/cli')
        self.task.write_text(self.task.read_text().replace('rows match', 'rows and types match'))
        self.assertNotEqual(task['sha256'], runner.select_task(self.task, 'rows-1')[0]['sha256'])

    def test_natural_inputs_separate_request_material_environment_and_grader(self):
        task, _ = runner.select_task(self.task, 'rows-1')
        task.update(success='SECRET_GRADER_CANARY', failure='FAILURE_CANARY',
                    expected_output='GRADER_OUTPUT_CANARY', resources='Only update the supplied existing table.')
        prompt = runner.natural_prompt(task, 'https://example.com/api', ['API_KEY'], 600)
        context = runner.natural_context(task, 'https://example.com/api', ['API_KEY'], 600)
        manifest = runner.write_context_files(context, self.workspace, self.run)
        self.assertIn('Read rows', prompt)
        self.assertIn('input.md', prompt)
        self.assertNotIn('table A', prompt)
        self.assertNotIn('API_KEY', prompt)
        self.assertEqual(context['input.md'].strip(), 'table A')
        self.assertIn('API_KEY', context['ENVIRONMENT.md'])
        self.assertIn('Only update the supplied existing table.', context['ENVIRONMENT.md'])
        self.assertNotIn('空容器', context['ENVIRONMENT.md'])
        supplied = prompt + ''.join(context.values())
        for hidden in ['SECRET_GRADER_CANARY', 'FAILURE_CANARY', 'GRADER_OUTPUT_CANARY', 'evidence/']:
            self.assertNotIn(hidden, supplied)
        for item in manifest:
            frozen = self.run / 'context-files' / item['path']
            self.assertEqual(frozen.read_bytes(), (self.workspace / item['path']).read_bytes())
            self.assertEqual(item['sha256'], hashlib.sha256(frozen.read_bytes()).hexdigest())
        (self.workspace / 'input.md').write_text('executor modified input')
        self.assertEqual((self.run / 'context-files/input.md').read_text().strip(), 'table A')

    def test_optional_resource_scope_is_frozen_and_not_assumed_for_other_tasks(self):
        old, _ = runner.select_task(self.task, 'rows-1')
        self.assertNotIn('resources', old)
        context = runner.natural_context(old, 'https://example.com/api', [], 600)
        self.assertNotIn('任务表', context['ENVIRONMENT.md'])
        self.task.write_text(self.task.read_text().replace('| 版本 |', '| 版本 | 运行资源 |')
                             .replace('| v2 |', '| v3 | Only the existing table |'))
        current, _ = runner.select_task(self.task, 'rows-1')
        self.assertEqual(current['resources'], 'Only the existing table')
        self.assertNotEqual(old['sha256'], current['sha256'])

    def test_duplicate_task_is_not_silently_selected(self):
        self.task.write_text(self.task.read_text() + self.task.read_text().splitlines()[-1] + '\n')
        with self.assertRaisesRegex(ValueError, 'exactly one'):
            runner.select_task(self.task, 'rows-1')

    def test_metrics_come_from_run_unknown_cost_stays_unknown(self):
        self.assessment.update(usage={'input_tokens': 1}, model='invented', elapsed_seconds=0)
        self.meta.update(prompt_style='natural', evidence_collection='CLI events and external remote read', prompt_characters=123)
        self.meta.update(input_delivery='workspace attachments', context_files=[{'path': 'input.md', 'sha256': 'b' * 64, 'characters': 7}])
        self.save()
        output = recorder.record(self.run, self.review)
        actual = json.loads(output.read_text())
        self.assertEqual(actual['usage']['input_tokens'], 17)
        self.assertEqual(actual['environment']['prompt_style'], 'natural')
        self.assertEqual(actual['environment']['prompt_characters'], 123)
        self.assertEqual(actual['environment']['input_delivery'], 'workspace attachments')
        self.assertEqual(actual['environment']['context_files'], self.meta['context_files'])
        self.assertEqual(actual['model'], 'fixture-model')
        self.assertEqual(actual['elapsed_seconds'], 2)
        self.assertNotIn('agent_cost_usd', actual)
        self.assertNotIn('agent_cost_note', actual)
        self.assertIsNone(actual['service_cost_usd'])
        self.assertTrue((self.root / actual['evidence'][0]['path']).is_file())
        with self.assertRaisesRegex(ValueError, 'already recorded'):
            recorder.record(self.run, self.review)

    def test_numeric_private_ids_remain_valid_json_without_rewriting_usage(self):
        raw = b'{"id": 241383, "workspaceId": 241383, "input_tokens": 241383, "url": "https://example.com/241383"}'
        public = recorder.public_copy(raw, self.meta, self.run, secrets=['241383'])
        value = json.loads(public)
        self.assertEqual(value['id'], '[SERVICE_SECRET]')
        self.assertEqual(value['workspaceId'], '[SERVICE_SECRET]')
        self.assertEqual(value['input_tokens'], 241383)
        self.assertNotIn('241383', value['url'])

    def test_executor_cannot_supply_its_own_review(self):
        self.save()
        target = self.workspace / 'assessment.json'
        target.write_text(json.dumps(self.assessment))
        with self.assertRaisesRegex(ValueError, 'outside'):
            recorder.record(self.run, target)

    def test_public_copies_redact_host_identity_and_keep_originals(self):
        session = '11111111-2222-3333-4444-555555555555'
        self.meta['thread_id'] = session
        self.assessment['reviewer'] = f'external Agent session {session}'
        self.assessment['evidence'] = [{'path': 'run.json'}, {'path': 'workspace/response.json'}]
        self.save()
        original = (self.run / 'run.json').read_bytes()
        response = (self.workspace / 'response.json').read_bytes()
        output = recorder.record(self.run, self.review)
        actual = json.loads(output.read_text())
        public = (self.root / actual['evidence'][0]['path']).read_bytes()
        for private in (str(self.root), str(self.workspace), session):
            self.assertNotIn(private.encode(), public)
            self.assertNotIn(private, output.read_text())
        self.assertIn(b'[WORKSPACE]', public)
        self.assertIn(b'[CODEX_SESSION]', public)
        self.assertEqual((self.run / 'run.json').read_bytes(), original)
        self.assertEqual((self.root / actual['evidence'][1]['path']).read_bytes(), response)
        self.assertEqual(actual['evidence'][0]['sha256'], hashlib.sha256(public).hexdigest())
        self.assertEqual(actual['evidence'][0]['source_sha256'], hashlib.sha256(original).hexdigest())
        self.assertEqual(actual['provenance']['run_sha256'], hashlib.sha256(original).hexdigest())
        self.assertEqual(actual['usage'], self.meta['usage'])

    def test_completion_requires_finished_run_and_passing_review(self):
        for change in [{'exit_code': 1}, {'timed_out': True}]:
            original = dict(self.meta)
            self.meta.update(change)
            self.save()
            with self.assertRaisesRegex(ValueError, 'cannot be completed'):
                recorder.record(self.run, self.review)
            self.meta = original
        self.assessment['checks'][0]['passed'] = False
        self.save()
        with self.assertRaisesRegex(ValueError, 'passing checks'):
            recorder.record(self.run, self.review)

    def test_private_credentials_and_published_redaction(self):
        credential = self.root / 'credential.json'
        credential.write_text(json.dumps({'EXA_API_KEY': 'test-secret-123456'}))
        credential.chmod(0o644)
        with self.assertRaisesRegex(ValueError, 'private'):
            runner.load_credentials(credential)
        credential.chmod(0o600)
        self.assertEqual(runner.load_credentials(credential)['EXA_API_KEY'], 'test-secret-123456')
        (self.run / 'private-secrets.json').write_text(json.dumps(['test-secret-123456']))
        (self.workspace / 'response.json').write_text('{"url":"https://example.com/?key=test-secret-123456","rows":[1]}')
        self.meta['service_credentials'] = 'provided: EXA_API_KEY'
        self.meta['preparation_note'] = 'Free signup outside measured run'
        self.save()
        result = json.loads(recorder.record(self.run, self.review).read_text())
        published = (self.root / result['evidence'][0]['path']).read_text()
        self.assertNotIn('test-secret-123456', published)
        self.assertIn('[SERVICE_SECRET]', published)
        self.assertEqual(result['environment']['service_credentials'], 'provided: EXA_API_KEY')
        self.assertIn('outside', result['environment']['preparation_note'])
        self.assertIn('test-secret-123456', (self.workspace / 'response.json').read_text())

    def test_route_relabel_and_evidence_escape_rejected(self):
        self.save()
        with self.assertRaisesRegex(ValueError, 'relabel'):
            recorder.record(self.run, self.review, route_id='cli')
        outside = self.root / 'outside.txt'
        outside.write_text('outside')
        self.assessment['evidence'] = [{'path': str(outside)}]
        self.save()
        with self.assertRaisesRegex(ValueError, 'inside the run'):
            recorder.record(self.run, self.review)


if __name__ == '__main__':
    unittest.main()
