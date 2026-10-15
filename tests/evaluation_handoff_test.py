"""Regressions for observed admission, answer carryover and response-file loss."""
import hashlib
import importlib.util
import io
import json
import os
import shutil
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import subprocess

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import access_readiness
import pipeline
import task_queue
import task_queue_test as queue_fixtures
import grading_packet
from grading_privacy import protect_grading


def runner_module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts/runners/opencode'/f'{name}.py')
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


retention = runner_module('retained_state')
capture = runner_module('capture_files')


class AdmissionTests(unittest.TestCase):
    setUp = queue_fixtures.QueueTests.setUp
    init = queue_fixtures.QueueTests.init
    submit = queue_fixtures.QueueTests.submit
    advance = queue_fixtures.QueueTests.advance

    def fixture(self, facet='ready'):
        self.config['trial_protocol'] = access_readiness.PROTOCOL
        adapter = self.root/'adapter.py'
        adapter.write_text(adapter.read_text().replace("    print(json.dumps({'collected':True}))", """
    if q['role']=='grading':
        review=json.loads((out/'assessment.json').read_text())
        review['status']='not_completed'
        review['outcome']['user_delivery']='not_completed'
        review['access_readiness']={k:{'status':'ready','evidence':'fixture real adapter response'} for k in ['service_call','authorization','reusable_state','isolation']}
        review['access_readiness']['reusable_state']['status']="""+repr(facet)+"""
        write('assessment.json',review)
    print(json.dumps({'collected':True}))"""))

    def test_new_unversioned_configuration_defaults_to_fixed_protocol(self):
        self.config.pop('trial_protocol')
        pipeline.write(self.config_path,self.config)
        pipeline.prepare(self.config_path,self.directory)
        self.assertEqual(pipeline.read(self.directory/'config.json')['trial_protocol'],access_readiness.PROTOCOL)

    def finish_access(self):
        self.init();path=self.submit('access-first')
        for _ in range(5): state=self.advance()
        self.assertEqual(state['jobs']['access-first']['phase'], 'needs_attention')
        self.assertEqual(pipeline.read(path/'state.json')['phase'], 'reviewed')
        return path

    def test_bad_report_does_not_block_independently_ready_operation(self):
        self.fixture();path=self.finish_access()
        child=self.submit('business-next',['access-first'],business=True)
        self.advance()
        self.assertTrue((child/'execution/started').exists())
        self.assertEqual(pipeline.read(path/'grading/assessment.json')['status'],'not_completed')
        self.assertEqual(pipeline.read(child/'config.json')['trial_protocol'],access_readiness.PROTOCOL)

    def test_unknown_reusable_configuration_holds_business_without_dispatch(self):
        self.fixture('unknown');self.finish_access()
        child=self.submit('business-next',['access-first'],business=True)
        state=self.advance()
        self.assertEqual(state['jobs']['business-next']['phase'],'blocked')
        self.assertFalse(child.exists())

    def test_tampered_review_or_invalid_isolation_never_authorizes_business(self):
        self.fixture();path=self.finish_access()
        review=pipeline.read(path/'grading/assessment.json')
        review['access_readiness']['isolation']['status']='not_ready'
        pipeline.write(path/'grading/assessment.json',review)
        self.assertFalse(access_readiness.decision(path,access_readiness.PROTOCOL)[0])
        state=pipeline.read(path/'state.json')
        state['record_hashes']['grading/assessment.json']=pipeline.digest(path/'grading/assessment.json')
        pipeline.write(path/'state.json',state)
        self.assertFalse(access_readiness.decision(path,access_readiness.PROTOCOL)[0])
        review['status']='invalid_run';review['access_readiness']['isolation']['status']='ready'
        pipeline.write(path/'grading/assessment.json',review)
        state['record_hashes']['grading/assessment.json']=pipeline.digest(path/'grading/assessment.json')
        pipeline.write(path/'state.json',state)
        self.assertFalse(access_readiness.decision(path,access_readiness.PROTOCOL)[0])

    def test_old_protocol_verdict_is_not_reinterpreted(self):
        self.fixture();path=self.finish_access()
        self.assertFalse(access_readiness.decision(path,'afs-20261010')[0])

    def test_explicit_dependency_retry_does_not_dispatch_or_rewrite_handoff(self):
        self.fixture('unknown');access=self.finish_access()
        child=self.submit('held-child',['access-first'],business=True)
        self.advance()
        frozen=(self.queue/'inbox/held-child/handoff.json').read_bytes()
        original=(access/'grading/assessment.json').read_bytes()
        with self.assertRaisesRegex(ValueError,'remains held'):
            task_queue.retry_dependency(self.queue,'held-child')
        # The separate supplemental-admission tests validate the independent
        # review. This fixture isolates queue bookkeeping, not a real verdict.
        with patch.object(access_readiness,'decision',return_value=(True,'fixture independent admission')):
            result=task_queue.retry_dependency(self.queue,'held-child')
        self.assertEqual(result['phase'],'waiting')
        self.assertEqual(len(result['dependency_retries']),1)
        self.assertFalse(child.exists())
        self.assertEqual((self.queue/'inbox/held-child/handoff.json').read_bytes(),frozen)
        self.assertEqual((access/'grading/assessment.json').read_bytes(),original)

    def test_dependency_retry_rejects_supersession_and_partial_preparation(self):
        self.fixture('unknown');self.finish_access()
        child=self.submit('held-child',['access-first'],business=True);self.advance()
        state=pipeline.read(self.queue/'state.json');job=state['jobs']['held-child']
        job['superseded_by']='different-slot';pipeline.write(self.queue/'state.json',state)
        with self.assertRaisesRegex(ValueError,'unsuperseded'):
            task_queue.retry_dependency(self.queue,'held-child')
        job.pop('superseded_by');pipeline.write(self.queue/'state.json',state);child.mkdir()
        with self.assertRaisesRegex(ValueError,'partially prepared'):
            task_queue.retry_dependency(self.queue,'held-child')

    def test_cost_report_separates_undispatched_preflight_from_missing_usage(self):
        root=self.root/'costs';root.mkdir()
        blocked=root/'blocked';blocked.mkdir();pipeline.write(blocked/'state.json',{'phase':'preflight_blocked'})
        partial=root/'partial';(partial/'execution').mkdir(parents=True)
        pipeline.write(partial/'execution/receipt.json',{'fixture':'observed paid execution'})
        state={'ledger':{str(blocked)+':execution':{'held_usd':0},
                         str(partial)+':execution':{'held_usd':100,'measured_cost':{'amount_usd':None,'lower_bound_usd':0.03}},
                         str(root/'grader')+':grading':{'billing_mode':'chatgpt','held_usd':0}}}
        result=task_queue.cost_summary(state)
        self.assertEqual(result['preflight_no_model'],1)
        self.assertEqual(result['incomplete_captures'],1)
        self.assertEqual(result['partial_capture_lower_bound_usd'],0.03)
        self.assertEqual(result['complete_capture_estimate_usd'],0)


class FileBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)

    def test_model_answers_inside_allowed_config_name_are_removed(self):
        tools=self.root/'tools';tools.mkdir()
        (tools/'config.json').write_text('{"endpoint":"https://example.com"}')
        baseline=self.root/'baseline';digest=retention.seal(tools,baseline)
        (tools/'config.json').write_text('{"endpoint":"https://example.com","verified_examples":{"old_answer":123}}')
        (tools/'cached-answer.json').write_text('{"old_answer":123}')
        manifest=retention.restore(tools,baseline,self.root/'archive',digest)
        self.assertEqual(json.loads((tools/'config.json').read_text()),{'endpoint':'https://example.com'})
        self.assertFalse((tools/'cached-answer.json').exists())
        self.assertTrue((self.root/'archive/previous-state/cached-answer.json').exists())
        self.assertEqual(manifest['baseline_sha256'],digest)

    def test_changed_baseline_bytes_are_rejected_before_state_is_removed(self):
        tools=self.root/'tools';tools.mkdir();(tools/'config.json').write_text('{}')
        baseline=self.root/'baseline';digest=retention.seal(tools,baseline)
        (baseline/'files/config.json').write_text('{"answer":1}')
        with self.assertRaisesRegex(ValueError,'bytes changed'):
            retention.restore(tools,baseline,self.root/'archive',digest)
        self.assertTrue((tools/'config.json').exists())

    def test_baseline_links_are_never_sealed(self):
        tools=self.root/'tools';tools.mkdir();(tools/'secret').symlink_to('/etc/passwd')
        with self.assertRaisesRegex(ValueError,'links'):retention.seal(tools,self.root/'baseline')

    def test_temp_raw_response_is_captured_whole_and_indexed(self):
        temp=self.root/'temp';temp.mkdir()
        raw=json.dumps({'rows':[{'value':n} for n in range(1500)]}).encode()
        (temp/'response.json').write_bytes(raw)
        buf=io.BytesIO();manifest=capture.archive({'tmp':str(temp)},buf)
        archive=self.root/'capture.tar';archive.write_bytes(buf.getvalue())
        out=self.root/'output';out.mkdir();capture.unpack(archive,out)
        self.assertEqual((out/'task-files/tmp/response.json').read_bytes(),raw)
        self.assertEqual(manifest['files'][0]['sha256'],hashlib.sha256(raw).hexdigest())
        self.assertTrue(manifest['complete_for_declared_file_scope'])

    def test_temp_links_and_oversize_files_are_disclosed_not_followed_or_truncated(self):
        temp=self.root/'temp';temp.mkdir();(temp/'link').symlink_to('/etc/passwd')
        (temp/'big').write_bytes(b'x'*50);(temp/'small').write_bytes(b'{}')
        buf=io.BytesIO();manifest=capture.archive({'tmp':str(temp)},buf,{'file_bytes':20,'total_bytes':30,'files':2})
        self.assertFalse(manifest['complete_for_declared_file_scope'])
        self.assertEqual(len(manifest['omitted']),2)
        self.assertEqual([r['path'] for r in manifest['files']],['task-files/tmp/small'])

    def test_packet_indexes_full_temp_files_and_redacts_registered_credentials(self):
        temp=self.root/'tmp';temp.mkdir();secret='fixture-service-secret-12345'
        (temp/'response.json').write_text(json.dumps({'token':secret,'rows':[1,2,3]}))
        buf=io.BytesIO();capture.archive({'tmp':str(temp)},buf)
        archive=self.root/'files.tar';archive.write_bytes(buf.getvalue())
        output=self.root/'execution';output.mkdir();capture.unpack(archive,output)
        grade=self.root/'grading-input';grade.mkdir()
        (grade/'task.json').write_text('{"success":"fixture"}')
        pipeline.write(self.root/'config.json',{'phase':'access','trial_protocol':access_readiness.PROTOCOL})
        packet=grading_packet.build(self.root)
        self.assertEqual(packet['task_files'][0]['record_path'],'execution/task-files/tmp/response.json')
        self.assertEqual(set(pipeline.read(grade/'assessment.template.json')['access_readiness']),set(access_readiness.FACETS))
        shutil.copytree(output,grade/'execution')
        (grade/'prompt.txt').write_text('fixture private grading')
        pipeline.write(self.root/'private-secrets.json',[secret])
        protect_grading(self.root)
        self.assertNotIn(secret,(grade/'execution/task-files/tmp/response.json').read_text())
        self.assertIn(secret,(output/'task-files/tmp/response.json').read_text())
        self.assertTrue((grade/'privacy-redactions.json').exists())

    def test_file_capture_timeout_preserves_receipt_and_explicit_gap(self):
        directory=ROOT/'scripts/runners/opencode'
        sys.path.insert(0,str(directory))
        try:worker=runner_module('worker')
        finally:sys.path.remove(str(directory))
        private=self.root/'private';private.mkdir();out=private/'output';out.mkdir()
        (out/'receipt.json').write_text('{"observed":"finished execution"}')
        (self.root/'capture_files.py').write_text((directory/'capture_files.py').read_text())
        with patch.object(worker,'ROOT',self.root),patch.object(worker.subprocess,'run',side_effect=subprocess.TimeoutExpired('fixture',25)) as run:
            worker.collect_task_files(self.root/'home',private,out)
        self.assertEqual(run.call_args.args[0][:3], ['python3', '-I', '-c'])
        self.assertEqual(json.loads((out/'receipt.json').read_text()),{'observed':'finished execution'})
        manifest=json.loads((out/'task-files-manifest.json').read_text())
        self.assertFalse(manifest['complete_for_declared_file_scope'])
        self.assertIn('TimeoutExpired',manifest['omitted'][0]['reason'])


if __name__ == '__main__':unittest.main()
