import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('opencode_normalize',Path(__file__).resolve().parents[1]/'scripts/runners/opencode/normalize.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class UsageTests(unittest.TestCase):
    def test_budget_rejection_sidecar_preserves_reconciled_forwarded_usage(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); wire = root/'wire/request1'; wire.mkdir(parents=True)
            (root/'events.jsonl').write_text(json.dumps({'type':'step_finish','part':{'tokens':{'input':80,'output':12,'reasoning':8,'cache':{'read':20,'write':0}}}})+'\n')
            (wire/'request.json').write_text(json.dumps({'model':'deepseek-flash'}))
            (wire/'meta.json').write_text(json.dumps({'status':200}))
            usage = {'usage':{'prompt_tokens':100,'prompt_tokens_details':{'cached_tokens':20},'completion_tokens':20,'completion_tokens_details':{'reasoning_tokens':8}}}
            (wire/'response.body').write_text('data: '+json.dumps(usage)+'\n\ndata: [DONE]\n')
            guard = root/'wire/guard-events.jsonl'
            guard.write_text(json.dumps({'time':123.5,'error':'Model request budget exhausted'})+'\n')
            result = module.normalize(root,'deepseek-flash')
            self.assertTrue(result['complete'])
            self.assertEqual(len(result['requests']),1)
            self.assertEqual(result['totals']['input_tokens'],100)
            self.assertEqual(len(result['local_rejections']),1)
            self.assertIn('wire/guard-events.jsonl',[s['path'] for s in result['sources']])
            (wire/'meta.json').write_text(json.dumps({'status':200,'error':'ConnectionResetError'}))
            self.assertFalse(module.normalize(root,'deepseek-flash')['complete'])
            (wire/'meta.json').write_text(json.dumps({'status':200}))
            guard.write_text('{"time":123.5}\n')
            self.assertFalse(module.normalize(root,'deepseek-flash')['complete'])

    def test_unicode_separators_inside_events_and_sse_do_not_break_usage_capture(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);wire=root/'wire/request1';wire.mkdir(parents=True)
            tool={'type':'tool_use','part':{'state':{'output':'binary-looking\u0085\u2028\u2029text'}}}
            finish={'type':'step_finish','part':{'tokens':{'input':80,'output':12,'reasoning':8,'cache':{'read':20,'write':0}}}}
            (root/'events.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in [tool,finish])+'\n')
            (wire/'request.json').write_text(json.dumps({'model':'deepseek-flash'}))
            (wire/'meta.json').write_text(json.dumps({'status':200}))
            chunk={'choices':[{'delta':{'content':'text\u0085\u2028\u2029'}}]}
            usage={'usage':{'prompt_tokens':100,'prompt_tokens_details':{'cached_tokens':20},'completion_tokens':20,'completion_tokens_details':{'reasoning_tokens':8}}}
            (wire/'response.body').write_text('data: '+json.dumps(chunk,ensure_ascii=False)+'\n\ndata: '+json.dumps(usage)+'\n\ndata: [DONE]\n')
            result=module.normalize(root,'deepseek-flash')
            self.assertTrue(result['complete'])
            self.assertEqual(result['totals']['output_tokens'],20)

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


class ProviderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        directory=Path(__file__).resolve().parents[1]/'scripts/runners/opencode'
        spec=importlib.util.spec_from_file_location('opencode_providers',directory/'providers.py')
        cls.providers=importlib.util.module_from_spec(spec);spec.loader.exec_module(cls.providers)

    def test_deepseek_uses_its_own_route_and_keeps_credentials_out_of_agent_config(self):
        cfg=self.providers.opencode_config({'model':'deepseek-flash','reasoning_effort':'high'},'deepseek')
        self.assertEqual(cfg['model'],'afs-deepseek/deepseek-flash')
        provider=cfg['provider']['afs-deepseek']
        self.assertEqual(provider['options'],{'apiKey':'local-capture-proxy','baseURL':'http://127.0.0.1:18181/v1'})
        self.assertEqual(provider['models']['deepseek-flash']['interleaved'],{'field':'reasoning_content'})
        self.assertEqual(provider['models']['deepseek-flash']['variants']['high'],{'reasoningEffort':'high'})
        self.assertEqual(cfg['permission']['task'],'deny')
        self.assertEqual(self.providers.profile('deepseek')['host'],'api.deepseek.com')

    def test_legacy_route_remains_explicit_and_cross_provider_models_are_rejected(self):
        name=self.providers.DEFAULT_PROVIDER
        cfg=self.providers.opencode_config({'model':'glm-5.3-flash','reasoning_effort':'high'},name)
        self.assertEqual(cfg['model'],'zhipuai-coding-plan/glm-5.3-flash')
        self.assertEqual(cfg['provider'][name]['options']['baseURL'],'http://127.0.0.1:18181/api/coding/paas/v4')
        for provider,model in [('deepseek','glm-5.3-flash'),(name,'deepseek-flash')]:
            with self.assertRaisesRegex(ValueError,'does not match'):
                self.providers.validate_model(provider,model)
        with self.assertRaisesRegex(ValueError,'Unsupported'):
            self.providers.profile('https://untrusted.example')


class AssessmentTests(unittest.TestCase):
    def test_typed_source_references_preserve_all_values_and_reject_ambiguity(self):
        spec=importlib.util.spec_from_file_location('opencode_assessment',Path(__file__).resolve().parents[1]/'scripts/runners/opencode/assessment.py')
        assessment=importlib.util.module_from_spec(spec);spec.loader.exec_module(assessment)
        source={'type':'api_response','ref':'evidence/plan.txt','note':'actual free-plan fields'}
        original={'status':'completed','service_cost_usd':None,'service_cost':{'kind':'unknown','sources':[source]}}
        normalized,changes=assessment.normalize(original)
        self.assertEqual(normalized['service_cost']['sources'],['[api_response] evidence/plan.txt — actual free-plan fields'])
        self.assertIsNone(normalized['service_cost_usd'])
        self.assertEqual(normalized['service_cost']['kind'],'unknown')
        self.assertEqual(original['service_cost']['sources'],[source])
        self.assertEqual(len(changes),1)
        self.assertEqual(assessment.normalize(normalized),(normalized,[]))
        for invalid in ({**source,'url':'https://conflicting.example'}, {**source,'extra':'unrecognized fact'},
                        {**source,'ref':''}, {**source,'type':None}):
            original['service_cost']['sources']=[invalid]
            self.assertEqual(assessment.normalize(original),(original,[]))

    def test_source_objects_preserve_url_and_note_without_promoting_unknown(self):
        spec=importlib.util.spec_from_file_location('opencode_assessment',Path(__file__).resolve().parents[1]/'scripts/runners/opencode/assessment.py')
        assessment=importlib.util.module_from_spec(spec);spec.loader.exec_module(assessment)
        original={'status':'completed','service_cost_usd':None,'service_cost':{'kind':'unknown','sources':[{'url':'https://example.com/rule','note':'existing observation'},'other source']}}
        normalized,changes=assessment.normalize(original)
        self.assertEqual(normalized['service_cost']['sources'],['https://example.com/rule — existing observation','other source'])
        self.assertEqual(normalized['service_cost']['kind'],'unknown')
        self.assertNotIn('note',normalized['service_cost'])
        self.assertIsInstance(original['service_cost']['sources'][0],dict)
        self.assertEqual(len(changes),1)
        self.assertEqual(assessment.normalize(normalized),(normalized,[]))

    def test_billing_evidence_list_is_joined_without_adding_facts(self):
        spec=importlib.util.spec_from_file_location('opencode_assessment',Path(__file__).resolve().parents[1]/'scripts/runners/opencode/assessment.py')
        assessment=importlib.util.module_from_spec(spec);spec.loader.exec_module(assessment)
        original={'status':'completed','service_cost_usd':0,'service_cost':{'kind':'confirmed_free','note':'existing basis',
            'applicability':{'rule':'free reads','observed':'keyless GET','evidence':['first source','second source']}}}
        normalized,changes=assessment.normalize(original)
        self.assertEqual(normalized['service_cost']['applicability']['evidence'],'first source\nsecond source')
        self.assertEqual(original['service_cost']['applicability']['evidence'],['first source','second source'])
        self.assertEqual(normalized['status'],original['status']);self.assertEqual(normalized['service_cost_usd'],0)
        self.assertEqual(len(changes),1)
        self.assertEqual(assessment.normalize(normalized),(normalized,[]))
        for invalid in ([],[''],['source',None],{'source':'somewhere'}):
            original['service_cost']['applicability']['evidence']=invalid
            self.assertEqual(assessment.normalize(original),(original,[]))

    def test_rearranges_existing_billing_facts_without_inference(self):
        spec=importlib.util.spec_from_file_location('opencode_assessment',Path(__file__).resolve().parents[1]/'scripts/runners/opencode/assessment.py')
        assessment=importlib.util.module_from_spec(spec);spec.loader.exec_module(assessment)
        original={'status':'completed','service_cost_usd':0,'service_cost':{'kind':'confirmed_free','sources':['https://example.com/pricing'],'rule':'included calls','observed':'included operation','evidence':'one actual GET'}}
        normalized,changes=assessment.normalize(original)
        self.assertEqual(normalized['service_cost']['applicability'],{k:original['service_cost'][k] for k in ['rule','observed','evidence']})
        self.assertEqual(normalized['service_cost_usd'],original['service_cost_usd'])
        self.assertNotIn('applicability',original['service_cost'])
        self.assertEqual(normalized['service_cost']['note'],original['service_cost']['rule'])
        self.assertEqual(len(changes),2)
        del original['service_cost']['evidence']
        self.assertEqual(assessment.normalize(original),(original,[]))

    def test_string_applicability_preserves_facts_and_does_not_resolve_conflicts(self):
        spec=importlib.util.spec_from_file_location('opencode_assessment',Path(__file__).resolve().parents[1]/'scripts/runners/opencode/assessment.py')
        assessment=importlib.util.module_from_spec(spec);spec.loader.exec_module(assessment)
        original={'status':'not_completed','service_cost_usd':None,'service_cost':{
            'kind':'confirmed_free','sources':['https://example.com/pricing'],
            'rule':'keyless reads are free','applicability':'actual keyless GET', 'evidence':'captured response'}}
        normalized,changes=assessment.normalize(original)
        self.assertEqual(normalized['status'],original['status'])
        self.assertIsNone(normalized['service_cost_usd'])
        self.assertEqual(normalized['service_cost']['applicability'],{
            'rule':'keyless reads are free','observed':'actual keyless GET','evidence':'captured response'})
        self.assertEqual(normalized['service_cost']['note'],'keyless reads are free')
        self.assertEqual(original['service_cost']['applicability'],'actual keyless GET')
        self.assertEqual(len(changes),3)
        self.assertEqual(assessment.normalize(normalized),(normalized,[]))
        original['service_cost']['observed']='conflicting observation'
        self.assertEqual(assessment.normalize(original),(original,[]))
        del original['service_cost']['observed']
        del original['service_cost']['evidence']
        self.assertEqual(assessment.normalize(original),(original,[]))

class RuntimeStatusTests(unittest.TestCase):
    def test_worker_exit_race_rechecks_completion_without_redispatch(self):
        import subprocess
        from unittest.mock import Mock
        spec = importlib.util.spec_from_file_location('opencode_status', Path(__file__).resolve().parents[1]/'scripts/runners/opencode/runtime_status.py')
        status = importlib.util.module_from_spec(spec); spec.loader.exec_module(status)
        missing = subprocess.CompletedProcess([], 1, b'', b'')
        done = subprocess.CompletedProcess([], 0, b'{"status":"completed"}', b'')
        read_done = Mock(side_effect=[missing, done])
        self.assertEqual(status.query(read_done, lambda: missing), {'status': 'completed'})
        self.assertEqual(read_done.call_count, 2)
        with self.assertRaisesRegex(RuntimeError, 'unavailable'):
            status.query(lambda: missing, lambda: missing)

class RuntimeCodeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = Path(__file__).resolve().parents[1]/'scripts/runners/opencode'
        spec = importlib.util.spec_from_file_location('opencode_runtime_code', cls.directory/'runtime_code.py')
        cls.code = importlib.util.module_from_spec(spec); spec.loader.exec_module(cls.code)

    def test_real_probe_rejects_stale_missing_and_symlinked_code_without_reading_credentials(self):
        import subprocess
        import sys
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name in self.code.WORKER_FILES:
                (root/name).write_bytes((self.directory/name).read_bytes())
            expected = self.code.manifest(root)
            # An unreadable/unrelated credential must not be included in the probe.
            (root/'model.key').mkdir()
            def execute(*args):
                return subprocess.run([sys.executable, *args[1:3], str(root), *args[4:]],
                                      capture_output=True, check=True)
            self.assertEqual(self.code.verify(execute, expected), expected)
            normalizer = root/'normalize.py'; original = normalizer.read_bytes()
            normalizer.write_text('old sidecar parser')
            with self.assertRaisesRegex(ValueError, 'normalize.py'):
                self.code.verify(execute, expected)
            normalizer.unlink()
            with self.assertRaisesRegex(ValueError, 'normalize.py'):
                self.code.verify(execute, expected)
            replacement = root/'outside.py'; replacement.write_bytes(original)
            normalizer.symlink_to(replacement)
            with self.assertRaisesRegex(ValueError, 'normalize.py'):
                self.code.verify(execute, expected)

    def test_adapter_rejects_stale_runtime_before_allocating_or_starting_a_run(self):
        import runpy
        import subprocess
        import sys
        import types
        from unittest.mock import patch
        calls = []
        observed = self.code.manifest(self.directory)
        observed['normalize.py'] = '0'*64
        def ssh(config, argv, **kwargs):
            calls.append(argv)
            return subprocess.CompletedProcess(argv, 0, json.dumps(observed).encode(), b'')
        cfg = {'host':'unused', 'remote_root':'/private/test', 'provider':'deepseek',
               'containers':{'runtime':'owned-container'}}
        stub = types.SimpleNamespace(load=lambda path: cfg, ssh=ssh)
        with tempfile.TemporaryDirectory() as d:
            request = Path(d)/'request.json'
            request.write_text(json.dumps({'runtime':'runtime', 'run_id':'new-run',
                                           'role':'execution', 'model':'deepseek-flash'}))
            argv = ['adapter.py', '--config', '/unused/private-config.json', 'start', str(request)]
            with patch.object(sys, 'path', [str(self.directory), *sys.path]), \
                 patch.object(sys, 'argv', argv), patch.dict(sys.modules, {'config':stub}):
                with self.assertRaisesRegex(ValueError, 'No run was allocated'):
                    runpy.run_path(str(self.directory/'adapter.py'), run_name='__main__')
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][:7], ['sudo','-n','docker','exec','-u','0','owned-container'])
        self.assertEqual(calls[0][7:9], ['python3','-c'])


class ArtifactTests(unittest.TestCase):
    def test_fresh_session_archives_shared_temporary_files_without_following_links(self):
        import sys
        directory=Path(__file__).resolve().parents[1]/'scripts/runners/opencode'
        sys.path.insert(0,str(directory))
        spec=importlib.util.spec_from_file_location('opencode_worker',directory/'worker.py')
        worker=importlib.util.module_from_spec(spec);spec.loader.exec_module(worker)
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);parents=[root/p for p in ('workspace','home/node','tmp','var/tmp')]
            for parent in parents:
                parent.mkdir(parents=True);(parent/'old-answer').write_text('prior task')
            service_tools=parents[1]/'service-tools';service_tools.mkdir()
            (parents[0]/'service-tools').write_text('not the persistent directory')
            secret=root/'secret';secret.write_text('outside')
            (parents[2]/'alias').symlink_to(secret)
            worker.archive_session_artifacts(parents,root/'archive',service_tools)
            self.assertTrue(service_tools.is_dir())
            self.assertEqual(list(parents[1].iterdir()),[service_tools])
            self.assertTrue(all(not list(p.iterdir()) for p in (parents[0],parents[2],parents[3])))
            self.assertEqual(secret.read_text(),'outside')
            self.assertEqual(len(list((root/'archive').rglob('old-answer-*'))),4)

    def test_nested_retention_archives_task_material_and_rejects_parent_alias(self):
        import sys
        directory=Path(__file__).resolve().parents[1]/'scripts/runners/opencode'
        sys.path.insert(0,str(directory))
        spec=importlib.util.spec_from_file_location('opencode_worker',directory/'worker.py')
        worker=importlib.util.module_from_spec(spec);spec.loader.exec_module(worker)
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);tools=root/'tools';installed=tools/'installed';installed.mkdir(parents=True)
            (installed/'node_modules').mkdir();(installed/'extract.mjs').write_text('generic parser')
            (installed/'prior.pdf').write_text('prior task');(tools/'answer.md').write_text('prior answer')
            (installed/'alias').symlink_to(root/'outside')
            policy={'installed':['node_modules','extract.mjs']}
            worker.archive_service_artifacts(tools,root/'archive',['installed'],policy)
            self.assertEqual({p.name for p in installed.iterdir()},{'node_modules','extract.mjs'})
            self.assertEqual((root/'archive/installed/prior.pdf').read_text(),'prior task')
            self.assertTrue((root/'archive/installed/alias').is_symlink())
            self.assertEqual((root/'archive/answer.md').read_text(),'prior answer')
            installed.rename(root/'outside');installed.symlink_to(root/'outside')
            with self.assertRaisesRegex(ValueError,'real directory'):
                worker.archive_service_artifacts(tools,root/'archive2',['installed'],policy)
            self.assertFalse((root/'archive2').exists())

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
            (workspace/'answer.md').write_text('real deliverable')
            (workspace/'alias.md').symlink_to('answer.md')
            # Exercise the archive parser independently of Linux root/uid setup.
            with patch.object(worker,'Path',side_effect=lambda p: workspace.parent if p=='/workspace' else Path(p)), patch.object(worker,'identity',lambda: None):
                worker.collect_artifacts(workspace,private,out)
            self.assertFalse((out/'artifacts/leak').exists())
            self.assertFalse((out/'artifacts/alias.md').exists())
            self.assertEqual((out/'artifacts/answer.md').read_text(),'real deliverable')
            omitted=json.loads((out/'artifact-omissions.json').read_text())
            self.assertEqual({r['path'].removeprefix('./') for r in omitted},{'leak','alias.md'})
            self.assertNotIn('controller-only secret',json.dumps(omitted))

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
                                 ('retained_paths', {'execution': ['..'], 'grading': []}),
                                 ('retained_children', {'unknown': {}}),
                                 ('retained_children', {'execution': {'unknown': []}}),
                                 ('retained_children', {'execution': {'credentials.json': ['..']}}),
                                 ('provider', 'untrusted-host'), ('model', 'deepseek-flash')]:
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
            settings['provider']='deepseek';settings['model']='deepseek-flash'
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
                        self.assertEqual(set(tar.getnames()), set(self.provision.WORKER_FILES) | {'model.key','provider.json'})
                        self.assertEqual(tar.getmember('model.key').mode, 0o600)
                        self.assertEqual(json.load(tar.extractfile('provider.json')),{'provider':'deepseek'})

if __name__=='__main__':unittest.main()
