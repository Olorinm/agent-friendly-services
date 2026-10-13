import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

import pipeline_test as fixtures
import task_queue_test as queue_fixtures
import pipeline as runs
import route_cooldown as cooldown
import task_queue as queue


URL = 'https://api.example.test/v2/search'
HEADER = 'HTTP/2 429\r\nDate: Tue, 13 Oct 2026 08:57:41 GMT\r\nRetry-After: 83752\r\nContent-Type: application/json\r\n\r\n'


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value)); path.chmod(0o600)


def capture(root, command='curl -i -sS ' + URL, output=HEADER, end=1791881861433, tool='bash', error=False):
    state = {'status': 'completed', 'input': {'command': command}, 'output': output, 'time': {'start': end-1000, 'end': end}}
    if error:
        state.update(status='error', error='Command failed with exit code 22', metadata={'output': state.pop('output'), 'exit': 22})
    event = {'type': 'tool_use', 'part': {'tool': tool, 'callID': 'neutral-call', 'state': state}}
    raw = (json.dumps(event) + '\n').encode()
    file = root/'execution/events.jsonl'; file.parent.mkdir(parents=True, exist_ok=True); file.write_bytes(raw)
    locator = {'path': 'events.jsonl', 'sha256': hashlib.sha256(raw).hexdigest(), 'line': 1}
    call = {'tool': tool, 'call_id': 'neutral-call', 'state': state, 'source': locator}
    records = {'schema_version': 1, 'format': 'opencode-json', 'complete': True, 'errors': [], 'source': {k: locator[k] for k in ('path', 'sha256')}, 'calls': [call]}
    write(root/'execution/tool-records.json', records)
    write(root/'execution/receipt.json', {'fixture': 'no network/model'})
    return records, call


class CooldownSources(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve(); self.state = {}
        self.config = {'service': 'neutral', 'route': 'search', 'environment_id': 'neutral-environment', 'execution': {}}
        self.route = {'entry_url': URL}
        self.bound = cooldown.binding(self.config, self.route)
    def refresh(self):
        cooldown.refresh(self.state, [(self.root, self.config, self.route, {'phase': 'execution_collected'})])
    def held(self, when=1791881862):
        return cooldown.hold(self.state, self.bound, when)

    def test_fixed_seconds_deadline_restart_cache_and_expiration(self):
        capture(self.root); self.refresh(); held = self.held(); self.assertIsNotNone(held)
        until = held['until']; self.assertEqual(until, 1791881861.433 + 83752)
        self.state = json.loads(json.dumps(self.state))
        with patch.object(cooldown, 'captured', side_effect=AssertionError('immutable cached source reread')):
            self.refresh(); self.assertEqual(self.held(1791883000)['until'], until)
        self.assertIsNone(self.held(until + 1))

    def test_http_date_and_old_finished_observation_do_not_gain_a_new_deadline(self):
        text = 'HTTP/1.1 429 Too Many Requests\nRetry-After: Tue, 13 Oct 2026 09:00:00 GMT\n\n'
        capture(self.root, output=text); self.refresh()
        until = datetime(2026, 10, 13, 9, tzinfo=timezone.utc).timestamp()
        self.assertEqual(self.held()['until'], until)
        self.assertIsNone(self.held(until + 86400))
        self.refresh(); self.assertIsNone(self.held(until + 86400))

    def test_unknown_credit_message_requires_source_bound_controller_release(self):
        capture(self.root, command='curl -sS ' + URL, output='{"success":false,"reason":"credits","retry_after_seconds":500}')
        self.refresh(); held = self.held(); self.assertIsNone(held['until'])
        identity = held['observation_ids'][0]; item = self.state['route_cooldowns']['observations'][identity]
        with self.assertRaises(ValueError): cooldown.release(self.state, identity, 'wrong-source', 'checked', '2026-10-13T09:00:00Z')
        cooldown.release(self.state, identity, item['source']['sha256'], 'controller checked the missing transport evidence', '2026-10-13T09:00:00Z')
        self.refresh(); self.assertIsNone(self.held())

    def test_429_without_valid_retry_time_is_unknown_not_a_guessed_short_retry(self):
        for retry in ['', 'Retry-After: not-a-date\n', 'Retry-After: -5\n']:
            with self.subTest(retry=retry):
                self.state = {}; capture(self.root, output='HTTP/2 429\n' + retry + '\n'); self.refresh()
                self.assertIsNone(self.held()['until'])

    def test_fail_exit_keeps_captured_header_and_time_but_error_text_is_not_a_response(self):
        capture(self.root, command='curl --fail -i ' + URL, error=True); self.refresh()
        self.assertIsNotNone(self.held())
        records, call = capture(self.root, command='curl --fail -i ' + URL, error=True)
        call['state']['metadata'].pop('output'); call['state']['error'] = HEADER
        raw = (json.dumps({'type': 'tool_use', 'part': {'tool': call['tool'], 'callID': call['call_id'], 'state': call['state']}})+'\n').encode()
        (self.root/'execution/events.jsonl').write_bytes(raw)
        records['source']['sha256'] = hashlib.sha256(raw).hexdigest(); call['source']['sha256'] = records['source']['sha256']
        write(self.root/'execution/tool-records.json', records)
        self.state = {}; self.refresh(); self.assertIsNone(self.held())

    def test_route_credentials_and_grader_resource_locks_do_not_guess_a_shared_bucket(self):
        capture(self.root); self.refresh()
        cfg = copy.deepcopy(self.config); cfg['route'] = 'scrape'
        self.assertIsNone(cooldown.hold(self.state, cooldown.binding(cfg, self.route), 1791881862))
        cfg = copy.deepcopy(self.config); cfg['execution']['credential_scope'] = 'other-authorized-account'
        self.assertIsNone(cooldown.hold(self.state, cooldown.binding(cfg, self.route), 1791881862))
        cfg = copy.deepcopy(self.config); cfg['grading'] = {'resource_locks': ['quota-A']}; cfg['execution']['quota_resource_locks'] = ['quota-A']
        with self.assertRaises(ValueError): cooldown.binding(cfg, self.route)
        with self.assertRaises(ValueError): cooldown.binding(self.config, {'entry_url': None})

    def test_actor_claim_document_model_503_redirect_and_synthesized_header_are_not_transport(self):
        commands = [
            'echo "HTTP/2 429"',
            'curl -i https://docs.example.test/rate-limits',
            'curl -i https://api.model.example.test/v1/chat/completions',
            'curl -L -i ' + URL,
            'curl --config /tmp/options ' + URL,
            'curl -i ' + URL + ' --next https://other.example.test',
            'curl -i ' + URL + '; printf "HTTP/2 429"',
            'curl -i ' + URL + ' && echo fake',
            'curl ' + URL + " --write-out 'HTTP/1.1 429\\nRetry-After: 83752\\n\\n'",
            'curl ' + URL + ' --url-query secret=@/tmp/hidden',
            'curl -i ' + URL + " -H '  Host: other.example.test'",
            'curl -i ' + URL + " --header='  :authority: other.example.test'",
            'curl -i ' + URL + " -H 'X-Test: okay\r\nHost: other.example.test'",
            'curl ' + URL,
        ]
        for i, command in enumerate(commands):
            with self.subTest(command=command):
                root = self.root / str(i); capture(root, command=command)
                state = {}; cooldown.refresh(state, [(root, self.config, self.route, {'phase': 'execution_collected'})])
                self.assertIsNone(cooldown.hold(state, self.bound, 1791881862))
        for output in ['HTTP/2 503\nRetry-After: 83752\n\n', 'HTTP/2 302\nLocation: https://other.example.test\n\nHTTP/2 429\nRetry-After: 83752\n\n']:
            self.assertIsNone(cooldown.signal_from_output(output))
        capture(self.root, tool='read'); self.refresh(); self.assertIsNone(self.held())

    def test_exact_dumped_header_origins_and_manifest_not_spoofed_stdout(self):
        command = 'curl -sS -X POST ' + URL + ' -D /tmp/neutral/headers.txt -o /tmp/neutral/body.json; cat /tmp/neutral/headers.txt /tmp/neutral/body.json'
        def files(status):
            header = self.root/'execution/task-files/tmp/neutral/headers.txt'; header.parent.mkdir(parents=True, exist_ok=True)
            header.write_text('HTTP/2 ' + status + '\nRetry-After: 83752\n\n')
            body = self.root/'execution/task-files/tmp/neutral/body.json'; body.write_text('{"success":false,"reason":"credits"}')
            write(self.root/'execution/task-files-manifest.json', {'schema_version': 1, 'files': [
                {'original_path': '/tmp/neutral/' + p.name, 'path': 'task-files/tmp/neutral/' + p.name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in (header, body)]})
        files('200'); capture(self.root, command=command, output=HEADER); self.refresh(); self.assertIsNone(self.held())
        self.state = {}; files('429'); self.refresh(); held = self.held(); self.assertIsNotNone(held)
        item = next(iter(self.state['route_cooldowns']['observations'].values()))
        self.assertIsNotNone(item['response_file_evidence']['manifest_sha256'])
        with patch.object(cooldown, 'file_signal', side_effect=AssertionError('unchanged response reparsed')): self.refresh()
        self.assertIsNone(cooldown.curl_plan(command + '; printf fake > /tmp/neutral/headers.txt'))
        self.assertIsNone(cooldown.curl_plan(command.replace('/tmp/neutral/headers.txt /tmp/neutral/body.json', '/tmp/other.txt')))
        (self.root/'execution/task-files/tmp/neutral/headers.txt').write_text('changed response\n')
        self.refresh(); self.assertIsNone(self.held()['until'])

    def test_changed_collected_source_is_a_private_reconciliation_hold(self):
        capture(self.root); self.refresh()
        (self.root/'execution/events.jsonl').write_text('changed original event\n')
        self.refresh(); held = self.held(2000000000); self.assertIsNone(held['until'])
        integrity = [i for i in self.state['route_cooldowns']['observations'].values() if i['confidence'] == 'capture_integrity_hold']
        self.assertEqual(len(integrity), 1); self.assertIn('reconcile', integrity[0]['notice'])
        self.state = {}; capture(self.root); self.refresh(); (self.root/'execution/events.jsonl').unlink()
        self.refresh(); self.assertIsNone(self.held(2000000000)['until'])

    def test_reused_dump_paths_cannot_bind_the_end_snapshot_to_an_earlier_call(self):
        command = 'curl -sS ' + URL + ' -D /tmp/neutral/header -o /tmp/neutral/body'
        records, first = capture(self.root, command=command, output='')
        second = copy.deepcopy(first); second['call_id'] = 'neutral-later'; second['state']['time']['end'] += 60000
        events = []
        for call in (first, second): events.append({'type': 'tool_use', 'part': {'tool': call['tool'], 'callID': call['call_id'], 'state': call['state']}})
        raw = ''.join(json.dumps(e) + '\n' for e in events).encode(); (self.root/'execution/events.jsonl').write_bytes(raw)
        source = {'path': 'events.jsonl', 'sha256': hashlib.sha256(raw).hexdigest()}
        for number, call in enumerate((first, second), 1): call['source'] = dict(source, line=number)
        records['source'] = source; records['calls'] = [first, second]; write(self.root/'execution/tool-records.json', records)
        header = self.root/'execution/task-files/tmp/neutral/header'; header.parent.mkdir(parents=True, exist_ok=True); header.write_text(HEADER)
        body = header.with_name('body'); body.write_text('{"success":false,"reason":"credits"}')
        write(self.root/'execution/task-files-manifest.json', {'schema_version': 1, 'files': [
            {'original_path': '/tmp/neutral/' + p.name, 'path': 'task-files/tmp/neutral/' + p.name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in (header, body)]})
        self.refresh(); self.assertIsNone(self.held())
        plan = cooldown.curl_plan(command)
        other = {'state': {'input': {'filePath': '/tmp/neutral/header', 'content': 'overwritten'}}}
        self.assertFalse(cooldown.file_origins_unique(plan, first, [first, other]))

    def test_controller_bridge_binds_actual_complex_shape_manifest_route_time_and_source(self):
        records, call = capture(self.root, command='mkdir -p /tmp/neutral && curl -sS ' + URL + ' -D /tmp/neutral/header; echo status; cat /tmp/neutral/header')
        self.refresh(); self.assertIsNone(self.held())  # Unsupported auto syntax.
        evidence = self.root/'grading-input/review-packet/tools/0001.json'; write(evidence, call)
        proof_sha = hashlib.sha256(evidence.read_bytes()).hexdigest()
        manifest = self.root/'grading-input-hashes.json'; write(manifest, {'review-packet/tools/0001.json': proof_sha})
        source = self.root/'execution/tool-records.json'
        proof = {'schema_version': 1, 'binding_sha256': self.bound['binding_sha256'], 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                 'call_number': 1, 'event_source': call['source'], 'target_url': URL, 'http_status': 429, 'retry_after': 83752,
                 'observed_at': datetime.fromtimestamp(call['state']['time']['end']/1000, timezone.utc).isoformat(),
                 'source_manifest': {'path': 'grading-input-hashes.json', 'sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
                    'evidence_path': 'review-packet/tools/0001.json', 'evidence_file': 'grading-input/review-packet/tools/0001.json', 'evidence_sha256': proof_sha}}
        for name, replacement in [('binding_sha256', 'other-route'), ('source_sha256', 'altered-source'), ('observed_at', '2026-10-15T00:00:00Z')]:
            bad = copy.deepcopy(proof); bad[name] = replacement
            with self.subTest(field=name), self.assertRaises(ValueError): cooldown.import_verified(self.state, self.root, self.config, self.route, bad)
        item = cooldown.import_verified(self.state, self.root, self.config, self.route, proof)
        self.assertEqual(item['confidence'], 'controller_verified_observation'); self.assertIsNotNone(self.held())
        self.assertEqual(cooldown.import_verified(self.state, self.root, self.config, self.route, proof)['until'], item['until'])
        # Before grading starts there is no sealed grading-input manifest yet.
        # The controller's original task-file manifest binds the actual header.
        (self.root/'grading-input-hashes.json').unlink()
        header = self.root/'execution/task-files/tmp/neutral/header'; header.parent.mkdir(parents=True, exist_ok=True); header.write_text(HEADER)
        sha = hashlib.sha256(header.read_bytes()).hexdigest()
        task_manifest = self.root/'execution/task-files-manifest.json'
        write(task_manifest, {'schema_version': 1, 'files': [{'path': 'task-files/tmp/neutral/header', 'original_path': '/tmp/neutral/header', 'sha256': sha}]})
        proof['source_manifest'] = {'path': 'execution/task-files-manifest.json', 'sha256': hashlib.sha256(task_manifest.read_bytes()).hexdigest(),
             'evidence_path': 'task-files/tmp/neutral/header', 'evidence_file': 'execution/task-files/tmp/neutral/header', 'evidence_sha256': sha, 'original_path': '/tmp/neutral/header'}
        self.state = {}; self.assertIsNotNone(cooldown.import_verified(self.state, self.root, self.config, self.route, proof))


class CooldownQueue(unittest.TestCase):
    setUp = fixtures.PipelineTests.setUp
    init = queue_fixtures.QueueTests.init
    submit = queue_fixtures.QueueTests.submit
    advance = queue_fixtures.QueueTests.advance

    def test_credential_scope_is_frozen_in_the_role_handoff_fingerprint(self):
        self.init(); self.config['execution']['credential_scope'] = 'neutral-account-A'
        path = self.submit('freeze-scope')
        proof = runs.read(self.queue/'inbox/freeze-scope/handoff.json')['members'][0]
        self.assertEqual(proof['inputs']['quota_binding']['credential_scope'], 'neutral-account-A')
        changed = copy.deepcopy(proof['config']); changed['execution']['credential_scope'] = 'neutral-account-B'
        self.assertNotEqual(queue.inputs(changed), proof['inputs'])
        self.assertFalse(path.exists())

    def test_private_controller_import_and_release_require_owned_collected_run_and_source(self):
        self.init(); path = self.submit('bridge'); self.advance(); self.advance()
        config = runs.read(path/'config.json'); handoff = runs.read(self.queue/'inbox/bridge/handoff.json')
        bound = cooldown.binding(config, handoff['members'][0]['inputs']['route'])
        records, call = capture(path, command='curl https://example.com; echo headers were checked privately')
        file = path/'grading-input/review-packet/tools/0001.json'; write(file, call)
        evidence_sha = hashlib.sha256(file.read_bytes()).hexdigest()
        manifest = path/'grading-input-hashes.json'; write(manifest, {'review-packet/tools/0001.json': evidence_sha})
        proof = {'schema_version': 1, 'run': str(path), 'binding_sha256': bound['binding_sha256'],
                 'source_sha256': hashlib.sha256((path/'execution/tool-records.json').read_bytes()).hexdigest(),
                 'call_number': 1, 'event_source': call['source'], 'target_url': 'https://example.com', 'http_status': 429,
                 'observed_at': datetime.fromtimestamp(call['state']['time']['end']/1000, timezone.utc).isoformat(),
                 'source_manifest': {'path': 'grading-input-hashes.json', 'sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
                     'evidence_path': 'review-packet/tools/0001.json', 'evidence_file': 'grading-input/review-packet/tools/0001.json', 'evidence_sha256': evidence_sha}}
        private = self.root/'controller-proof.json'; write(private, proof)
        private.chmod(0o644)
        with self.assertRaisesRegex(ValueError, 'private'): queue.controller_cooldown(self.queue, private)
        private.chmod(0o600); identity = queue.controller_cooldown(self.queue, private)
        state = runs.read(self.queue/'state.json'); self.assertIsNone(cooldown.hold(state, bound, time.time())['until'])
        with self.assertRaises(ValueError): queue.controller_cooldown(self.queue, observation_id=identity, source_sha256='wrong', reason='checked')
        queue.controller_cooldown(self.queue, observation_id=identity, source_sha256=proof['source_sha256'], reason='Private controller reconciled access condition')
        self.assertIsNone(cooldown.hold(runs.read(self.queue/'state.json'), bound, time.time()))

    def test_collect_stops_new_same_route_execution_but_existing_grading_proceeds(self):
        self.init(concurrency=2); self.config['execution']['credential_scope'] = 'same-neutral-scope'
        first = self.submit('first'); self.advance()
        # Fixture emits a captured real tool-shaped signal only during collect.
        # It does not perform any HTTP or model request.
        adapter = self.root/'adapter.py'
        injection = '''
        import time
        end=int(time.time()*1000)
        event={'type':'tool_use','part':{'tool':'bash','callID':'neutral','state':{'status':'completed','input':{'command':'curl -i https://example.com'},'output':'HTTP/2 429\\nRetry-After: 83752\\n\\n','time':{'start':end-1000,'end':end}}}}
        raw=(json.dumps(event)+'\\n').encode();(out/'events.jsonl').write_bytes(raw)
        source={'path':'events.jsonl','sha256':hashlib.sha256(raw).hexdigest()}
        write('tool-records.json',{'schema_version':1,'format':'opencode-json','complete':True,'errors':[],'source':source,'calls':[{'tool':'bash','call_id':'neutral','state':event['part']['state'],'source':dict(source,line=1)}]})
'''
        adapter.write_text(adapter.read_text().replace("(out/'events.jsonl').write_text('{}\\n')", "(out/'events.jsonl').write_text('{}\\n')" + injection))
        self.config['execution']['runtime'] = 'second-execution'; self.config['grading']['runtime'] = 'second-grading'
        second = self.submit('second')
        state = self.advance()
        self.assertTrue((first/'execution/receipt.json').exists())
        self.assertFalse((second/'execution/started').exists())
        self.assertEqual(runs.read(second/'state.json')['phase'], 'prepared')
        self.assertIn('cooling down', state['dispatch_holds'][str(second)+':execution'])
        for _ in range(3): state = self.advance()
        self.assertTrue((first/'grading/started').exists())
        self.assertEqual(state['jobs']['first']['phase'], 'reviewed')
        self.assertFalse((second/'execution/started').exists())
        self.assertNotIn(str(second)+':execution', state['ledger'])


if __name__ == '__main__': unittest.main()
