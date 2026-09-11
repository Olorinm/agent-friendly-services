import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('opencode_normalize',Path(__file__).resolve().parents[1]/'scripts/runners/opencode/normalize.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class UsageTests(unittest.TestCase):
    def test_cache_and_reasoning_are_subsets_and_reconcile(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); wire=root/'wire'/'request1';wire.mkdir(parents=True)
            (root/'events.jsonl').write_text(json.dumps({'type':'step_finish','part':{'tokens':{'input':80,'output':12,'reasoning':8,'cache':{'read':20,'write':0}}}})+'\n')
            (wire/'request.json').write_text(json.dumps({'model':'glm-5.3-flash'}))
            (wire/'meta.json').write_text(json.dumps({'status':200}))
            (wire/'response.body').write_text('data: '+json.dumps({'usage':{'prompt_tokens':100,'prompt_tokens_details':{'cached_tokens':20},'completion_tokens':20,'completion_tokens_details':{'reasoning_tokens':8}}})+'\n\ndata: [DONE]\n')
            result=module.normalize(root,'glm-5.3-flash')
            self.assertTrue(result['complete'])
            self.assertEqual(result['totals']['input_tokens']+result['totals']['output_tokens'],120)
            self.assertEqual(result['totals']['cached_input_tokens'],20)
            self.assertEqual(result['totals']['reasoning_output_tokens'],8)
            (wire/'meta.json').write_text(json.dumps({'status':200,'error':'ConnectionResetError'}))
            self.assertFalse(module.normalize(root,'glm-5.3-flash')['complete'])
            (wire/'meta.json').write_text(json.dumps({'status':200}))
            (root/'events.jsonl').write_text('')
            self.assertFalse(module.normalize(root,'glm-5.3-flash')['complete'])


class AssessmentTests(unittest.TestCase):
    def test_rearranges_existing_billing_facts_without_inference(self):
        spec=importlib.util.spec_from_file_location('opencode_assessment',Path(__file__).resolve().parents[1]/'scripts/runners/opencode/assessment.py')
        assessment=importlib.util.module_from_spec(spec);spec.loader.exec_module(assessment)
        original={'status':'completed','service_cost_usd':0,'service_cost':{'kind':'confirmed_free','sources':['https://example.com/pricing'],'rule':'included calls','observed':'included operation','evidence':'one actual GET'}}
        normalized,changes=assessment.normalize(original)
        self.assertEqual(normalized['service_cost']['applicability'],{k:original['service_cost'][k] for k in ['rule','observed','evidence']})
        self.assertEqual(normalized['service_cost_usd'],original['service_cost_usd'])
        self.assertNotIn('applicability',original['service_cost'])
        self.assertEqual(len(changes),1)
        del original['service_cost']['evidence']
        self.assertEqual(assessment.normalize(original),(original,[]))

class ArtifactTests(unittest.TestCase):
    def test_does_not_follow_executor_symlinks(self):
        import sys
        from unittest.mock import patch
        directory=Path(__file__).resolve().parents[1]/'scripts/runners/opencode'
        sys.path.insert(0,str(directory))
        spec=importlib.util.spec_from_file_location('opencode_worker',directory/'worker.py')
        worker=importlib.util.module_from_spec(spec);spec.loader.exec_module(worker)
        with tempfile.TemporaryDirectory() as d:
            root=Path(d).resolve();workspace=root/'task';workspace.mkdir();private=root/'private';private.mkdir();out=private/'output';out.mkdir()
            (root/'canary').write_text('controller-only secret')
            (workspace/'leak').symlink_to(root/'canary')
            # Exercise the archive parser independently of Linux root/uid setup.
            with patch.object(worker,'Path',side_effect=lambda p: workspace.parent if p=='/workspace' else Path(p)), patch.object(worker,'identity',lambda: None):
                with self.assertRaisesRegex(ValueError,'Unsafe artifact'):
                    worker.collect_artifacts(workspace,private,out)
            self.assertFalse((out/'artifacts/leak').exists())

class ProvisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import sys
        directory = Path(__file__).resolve().parents[1]/'scripts/runners/opencode'
        sys.path.insert(0, str(directory))
        spec = importlib.util.spec_from_file_location('opencode_provision', directory/'provision.py')
        cls.provision = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.provision)

    def settings(self):
        return {'host': 'test-runner', 'remote_root': '/srv/test-runner',
                'containers': {'execution': 'test-executor', 'grading': 'test-grader'},
                'retained_paths': {'execution': ['credentials.json'], 'grading': []}}

    def test_private_config_rejects_alias_injection_and_shared_containers(self):
        with tempfile.TemporaryDirectory() as d:
            config = Path(d)/'config.json'
            for field, value in [('host', '-oProxyCommand=bad'), ('remote_root', '/srv/../'),
                                 ('containers', {'execution': 'shared', 'grading': 'shared'}),
                                 ('retained_paths', {'execution': ['..'], 'grading': []})]:
                settings = self.settings(); settings[field] = value
                config.write_text(json.dumps(settings))
                with self.assertRaises(ValueError):
                    self.provision.load(config)

    def test_refuses_unrelated_containers_before_mutations(self):
        import subprocess
        from unittest.mock import patch
        replies = [subprocess.CompletedProcess([], 0, b'id\n', b''),
                   subprocess.CompletedProcess([], 0, json.dumps([
                       {'Name': '/test-executor', 'Config': {'Labels': {}}, 'State': {'Running': True}}
                   ]).encode(), b'')]
        with patch.object(self.provision, 'ssh', side_effect=replies) as remote:
            with self.assertRaisesRegex(ValueError, 'unrelated'):
                self.provision.run(self.settings(), 'up')
        self.assertEqual(remote.call_count, 2)

    def test_setup_has_no_mounts_ports_or_key_in_arguments(self):
        import io
        import subprocess
        import tarfile
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as d:
            key = Path(d)/'key'; key.write_text('test-private-key')
            settings = self.settings(); settings['key_file'] = str(key)
            def reply(config, args, data=None):
                if args[-2:] == ['ps', '-aq']:
                    out = b''
                elif 'inspect' in args:
                    out = json.dumps([{'Image': 'sha256:test', 'HostConfig': {
                        'Memory': 2147483648, 'NanoCpus': 1000000000, 'PidsLimit': 256}}]).encode()
                elif args[-1] == '--version':
                    out = b'1.18.29\n'
                else:
                    out = b''
                return subprocess.CompletedProcess(args, 0, out, b'')
            with patch.object(self.provision, 'ssh', side_effect=reply) as remote:
                result = self.provision.run(settings, 'up')
            self.assertEqual(result['execution']['opencode_version'], '1.18.29')
            for call in remote.call_args_list:
                args = call.args[1]
                self.assertNotIn('test-private-key', str(args))
                if 'create' in args:
                    self.assertFalse(set(args) & {'-v', '--volume', '--mount', '-p', '--publish', '--privileged'})
                if call.kwargs.get('data'):
                    with tarfile.open(fileobj=io.BytesIO(call.kwargs['data'])) as tar:
                        self.assertEqual(set(tar.getnames()), set(self.provision.WORKER_FILES) | {'bigmodel.key'})
                        self.assertEqual(tar.getmember('bigmodel.key').mode, 0o600)

if __name__=='__main__':unittest.main()
