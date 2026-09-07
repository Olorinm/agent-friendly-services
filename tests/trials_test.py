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

    def test_duplicate_task_is_not_silently_selected(self):
        self.task.write_text(self.task.read_text() + self.task.read_text().splitlines()[-1] + '\n')
        with self.assertRaisesRegex(ValueError, 'exactly one'):
            runner.select_task(self.task, 'rows-1')

    def test_metrics_come_from_run_unknown_cost_stays_unknown(self):
        self.assessment.update(usage={'input_tokens': 1}, model='invented', elapsed_seconds=0)
        self.save()
        output = recorder.record(self.run, self.review)
        actual = json.loads(output.read_text())
        self.assertEqual(actual['usage']['input_tokens'], 17)
        self.assertEqual(actual['model'], 'fixture-model')
        self.assertEqual(actual['elapsed_seconds'], 2)
        self.assertNotIn('agent_cost_usd', actual)
        self.assertNotIn('agent_cost_note', actual)
        self.assertIsNone(actual['service_cost_usd'])
        self.assertTrue((self.root / actual['evidence'][0]['path']).is_file())
        with self.assertRaisesRegex(ValueError, 'already recorded'):
            recorder.record(self.run, self.review)

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
