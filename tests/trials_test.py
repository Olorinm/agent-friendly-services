import importlib.util
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))
from session_usage import extract_usage, collect_session_usage


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


    def session_fixture(self, exact=True):
        a = {'input_tokens': 10, 'cached_input_tokens': 4, 'output_tokens': 2}
        b = {'input_tokens': 7, 'cached_input_tokens': 4, 'output_tokens': 1}
        events = [{'type': 'session_meta', 'payload': {'private_content': 'PRIVATE_CANARY'}}]
        for i, (usage, total) in enumerate([(a, a), (b, self.meta['usage'])]):
            event = ({'type': 'token_usage_record', 'payload': {'response_id': str(i), 'usage': usage}}
                     if exact else {'type': 'event_msg', 'payload': {'type': 'token_count',
                         'info': {'last_token_usage': usage, 'total_token_usage': total}}})
            events.extend([event, event])
        raw = self.run / 'session.raw.jsonl'
        raw.write_text('\n'.join(json.dumps(e) for e in events)+'\n')
        return raw

    def test_session_usage_deduplicates_and_exports_only_numeric_counters(self):
        for exact in [True, False]:
            detail = extract_usage(self.session_fixture(exact), self.meta['usage'])
            self.assertEqual(detail['status'], 'complete')
            self.assertEqual(len(detail['requests']), 2)
            self.assertNotIn('PRIVATE_CANARY', json.dumps(detail))
            self.assertNotIn('response_id', json.dumps(detail))

    def test_partial_mismatched_and_truncated_sessions_stay_incomplete(self):
        raw = self.session_fixture()
        self.assertEqual(extract_usage(raw, None)['status'], 'incomplete')
        self.assertEqual(extract_usage(raw, dict(self.meta['usage'], input_tokens=18))['status'], 'incomplete')
        raw.write_text(raw.read_text()+'{"private":"SECRET')
        detail = extract_usage(raw, self.meta['usage'])
        self.assertEqual(detail['status'], 'incomplete')
        self.assertNotIn('SECRET', json.dumps(detail))

    def test_counter_gaps_do_not_become_request_usage(self):
        raw = self.session_fixture(False)
        raw.write_text(raw.read_text().replace('"input_tokens": 17', '"input_tokens": 18'))
        self.assertEqual(extract_usage(raw, self.meta['usage'])['status'], 'incomplete')

    def test_recorder_reextracts_usage_and_rejects_raw_session_publication(self):
        self.session_fixture()
        self.meta['request_usage'] = {'requests': [{'input_tokens': 99999}]}
        self.save()
        result_path = recorder.record(self.run, self.review)
        detail = json.loads(result_path.read_text())['request_usage']
        self.assertEqual(detail['status'], 'complete')
        self.assertEqual(len(detail['requests']), 2)
        self.assertNotIn('PRIVATE_CANARY', result_path.read_text())

    def test_raw_session_cannot_be_selected_as_evidence(self):
        self.session_fixture()
        self.assessment['evidence'] = [{'path': 'session.raw.jsonl'}]
        self.save()
        with self.assertRaisesRegex(ValueError, 'raw session'):
            recorder.record(self.run, self.review)

    def test_runner_persists_and_collects_session_after_process_exit(self):
        # A fake CLI exercises the actual launcher/subprocess/collector without API calls.
        auth = self.root / 'codex-home'
        auth.mkdir()
        cli = self.root / 'codex'
        cli.write_text('#!' + sys.executable + '\n' + r"""
import json,os,sys
from pathlib import Path
if '--version' in sys.argv:
    print('codex-cli fixture');sys.exit(0)
assert '--ephemeral' not in sys.argv
sys.stdin.read()
sid = '11111111-2222-3333-4444-555555555555'
usage = {'input_tokens':17,'cached_input_tokens':8,'output_tokens':3}
p = Path(os.environ['CODEX_HOME'])/'sessions'/'2026'/'09'/'08'/('rollout-'+sid+'.jsonl')
p.parent.mkdir(parents=True)
p.write_text(json.dumps({'type':'token_usage_record','payload':{'response_id':'one','usage':usage}})+'\n')
print(json.dumps({'type':'thread.started','thread_id':sid}))
print(json.dumps({'type':'turn.completed','usage':usage}))
""")
        cli.chmod(0o700)
        workspace = self.root / 'new-workspace'
        workspace.mkdir()
        with patch.dict('os.environ', {'CODEX_HOME': str(auth)}), patch.object(sys, 'argv',
                ['runner', 'database-example', '--route', 'http', '--task-file', 'tasks.md',
                 '--task', 'rows-1', '--model', 'fixture', '--seconds', '10']), \
                patch.object(runner.shutil, 'which', return_value=str(cli)), \
                patch.object(runner.tempfile, 'mkdtemp', return_value=str(workspace)):
            self.assertEqual(runner.main(), 0)
        recorded = list((self.root/'data/experiments/results/trials').glob('codex-*/run.json'))
        self.assertEqual(len(recorded), 1)
        meta = json.loads(recorded[0].read_text())
        self.assertEqual(meta['request_usage']['status'], 'complete')
        self.assertEqual(len(meta['request_usage']['requests']), 1)
        self.assertEqual((recorded[0].parent/'session.raw.jsonl').stat().st_mode & 0o777, 0o600)

    def test_arbitrary_task_and_route_and_ambiguity(self):
        task, _ = runner.select_task(self.task, 'rows-1')
        self.assertEqual(task['description'], 'Read rows')
        self.assertEqual(task['version'], 'v2')
        with self.assertRaisesRegex(ValueError, 'Choose --route'):
            runner.select_route(self.catalog, 'database-example', None)
        self.assertEqual(runner.select_route(self.catalog, 'database-example', 'cli')['entry_url'], 'https://example.com/cli')
        self.task.write_text(self.task.read_text().replace('rows match', 'rows and types match'))
        self.assertNotEqual(task['sha256'], runner.select_task(self.task, 'rows-1')[0]['sha256'])

    def test_browser_connection_stays_private_and_rejects_remote_hosts(self):
        connection = self.root / 'browser.json'
        connection.write_text(json.dumps({'cdp_url': 'ws://127.0.0.1:4567/devtools/browser/private-id'}))
        connection.chmod(0o600)
        browser = runner.load_browser(connection)
        task, _ = runner.select_task(self.task, 'rows-1')
        context = runner.natural_context(task, 'https://example.com', [], 600, browser)
        self.assertIn('.private/browser.json', context['ENVIRONMENT.md'])
        self.assertNotIn('private-id', ''.join(context.values()))
        for url in ['ws://example.com:4567/devtools/browser/id', 'file:///tmp/browser', 'http://127.0.0.1']:
            connection.write_text(json.dumps({'cdp_url': url}))
            with self.assertRaises(ValueError):
                runner.load_browser(connection)
        connection.chmod(0o644)
        with self.assertRaisesRegex(ValueError, 'private'):
            runner.load_browser(connection)

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

    def test_service_charge_requires_evidence_and_estimates_from_usage(self):
        with self.assertRaisesRegex(ValueError, 'sources'):
            recorder.service_charge({'service_cost_usd': 0})
        detail = {'kind': 'estimated', 'sources': ['https://example.com/prices', 'receipt.json'],
                  'note': 'Ten billed requests at the documented rate',
                  'items': [{'quantity': 10, 'unit': 'request', 'usd_per_unit': 0.002}]}
        amount, basis = recorder.service_charge({'service_cost_usd': None, 'service_cost': detail})
        self.assertEqual(amount, 0.02)
        self.assertEqual(basis['amount_usd'], 0.02)
        with self.assertRaisesRegex(ValueError, 'does not match'):
            recorder.service_charge({'service_cost_usd': 0.01, 'service_cost': detail})
        detail.update(kind='confirmed_free', note='Verified free allowance for this run',
                      applicability={'rule': 'Free tier allowance', 'observed': 'Account has remaining quota', 'evidence': 'usage.json'})
        self.assertEqual(recorder.service_charge({'service_cost_usd': None, 'service_cost': detail})[0], 0)
        self.assessment.update(service_cost_usd=None, service_cost=detail)
        self.save()
        output = json.loads(recorder.record(self.run, self.review).read_text())
        self.assertEqual(output['service_cost_usd'], 0)
        self.assertEqual(output['service_cost']['sources'], detail['sources'])

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

    def test_copied_raw_adapter_log_cannot_be_published_as_evidence(self):
        self.meta['usage_format'] = 'adapter-v1'
        raw = self.run / 'raw-events.jsonl'
        raw.write_text('PRIVATE MODEL INPUT')
        (self.run / 'copy.md').write_bytes(raw.read_bytes())
        (self.run / 'usage.json').write_text(json.dumps({'sources': [{'path': raw.name}]}))
        self.assessment['evidence'] = [{'path': 'copy.md'}]
        self.save()
        with self.assertRaisesRegex(ValueError, 'private adapter'):
            recorder.record(self.run, self.review, dry_run=True)

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
