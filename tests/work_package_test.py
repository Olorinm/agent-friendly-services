"""Role JSON can select approved facts; it cannot supply runtime authority."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import work_package as packages
import pipeline as runs
import task_queue as queue
import pipeline_test as fixtures
import role_handoff_test as role_fixtures
import role_handoff


class WorkPackageTests(unittest.TestCase):
    setUp = fixtures.PipelineTests.setUp

    def fixture(self):
        for role in ('task_design','material_preparation'):
            runs.write(self.root/role/'receipt.json',{'session_id':role+'-session'})
        self.collection_patch=patch.object(packages,'collection',side_effect=lambda policy,role='material_preparation',result_path=None:self.root/role)
        self.collection_patch.start();self.addCleanup(self.collection_patch.stop)
        material=self.root/'ledger.csv';material.write_text('currency,amount\nEUR,12.5\n')
        self.designer={'schema_version':1,'status':'ready','blockers':[],'package_id':'fixture-package','tasks':[
            {'id':'expenses','version':'v1','description':'Convert reimbursement amounts.', 'inputs':'Read ledger.csv as original expense data.',
             'expected_output':'Converted totals and rate dates.','success':'Totals match source rates.','failure':'Wrong date or arithmetic.',
             'material_ids':['ledger'],'applicable_target_ids':['approved-api']}]}
        config=deepcopy(self.config);config['preflight']=[{'url':'https://example.com','method':'HEAD'}]
        for role in ('execution','grading'):config[role]['max_model_requests']=10
        self.policy={'rounds':[1],'targets':{'approved-api':{'config':config}},'materials':{
            'ledger':{'path':str(material),'sha256':packages.digest(material),'audience':'execution','kind':'raw_data'}}}
        self.design_path=self.root/'task-design.json';runs.write(self.design_path,self.designer)
        self.preparer={'schema_version':1,'status':'ready','blockers':[],'package_id':'fixture-package',
                       'designer_sha256':packages.digest(self.design_path),'materials':[],
                       'assignments':[{'task_id':'expenses','target_id':'approved-api','round':1,'status':'ready','blockers':[]}]}
        self.prep_path=self.root/'material-preparation.json';runs.write(self.prep_path,self.preparer)
        self.policy_path=self.root/'policy.json';runs.write(self.policy_path,self.policy)
        self.output=self.root/'private-package';self.queue=self.root/'queue'
        queue.init(self.queue,max_concurrency=2,budget_usd=10,expires_at='2099-01-01T00:00:00Z',pool='offline-fixture')

    def validate(self):
        return packages.validate(self.designer,self.preparer,self.policy,packages.digest(self.design_path))

    def submit(self):
        return packages.submit_package(self.queue,self.design_path,self.prep_path,self.policy_path,self.output)

    def test_package_compiles_and_submits_exactly_once_without_model_start(self):
        self.fixture();manifest=self.submit();again=self.submit()
        self.assertEqual(manifest,again)
        self.assertEqual(len(list((self.queue/'inbox').iterdir())),1)
        job=manifest['jobs'][0];spec=runs.read(job['spec']);config=runs.read(spec['config'])
        self.assertEqual(config['execution'],self.policy['targets']['approved-api']['config']['execution'])
        self.assertEqual(config['grading'],self.policy['targets']['approved-api']['config']['grading'])
        attached=Path(config['attachments'])
        self.assertEqual([f.name for f in attached.iterdir()],['ledger.csv'])
        self.assertNotIn('Totals match',next(attached.iterdir()).read_text())
        self.assertFalse(Path(spec['directory']).exists())
        self.assertTrue(config['task_file'].startswith('data/experiments/results/work-packages/'))

    def test_task_scope_overshoot_rejects_before_writing_or_submitting(self):
        self.fixture();self.policy['max_tasks']=1
        second=deepcopy(self.designer['tasks'][0]);second['id']='second-expenses'
        self.designer['tasks'].append(second)
        self.preparer['assignments'].append({**self.preparer['assignments'][0],'task_id':second['id']})
        runs.write(self.design_path,self.designer)
        self.preparer['designer_sha256']=packages.digest(self.design_path)
        runs.write(self.prep_path,self.preparer);runs.write(self.policy_path,self.policy)
        with patch.object(packages.queue,'submit') as submit:
            with self.assertRaisesRegex(ValueError,'exceeds controller max_tasks'):self.submit()
            submit.assert_not_called()
        self.assertFalse(self.output.exists())
        self.assertFalse((runs.ROOT/'data/experiments/results/work-packages/fixture-package/tasks.md').exists())
        self.assertEqual(list((self.queue/'inbox').iterdir()),[])

    def test_max_tasks_requires_a_positive_integer(self):
        self.fixture()
        for value in (True,False,0,-1,1.0,'1',None,[],{}):
            with self.subTest(value=value):
                self.policy['max_tasks']=value
                with self.assertRaisesRegex(ValueError,'max_tasks must be a positive integer'):self.validate()

    def test_task_count_at_cap_is_allowed(self):
        self.fixture();self.policy['max_tasks']=1
        self.assertEqual(len(self.validate()['tasks']),1)

    def test_absent_max_tasks_preserves_multiple_task_submission(self):
        self.fixture()
        second=deepcopy(self.designer['tasks'][0]);second['id']='second-expenses'
        self.designer['tasks'].append(second)
        self.preparer['assignments'].append({**self.preparer['assignments'][0],'task_id':second['id']})
        runs.write(self.design_path,self.designer)
        self.preparer['designer_sha256']=packages.digest(self.design_path)
        runs.write(self.prep_path,self.preparer)
        manifest=self.submit()
        self.assertEqual(len(manifest['jobs']),2)
        self.assertEqual(len(list((self.queue/'inbox').iterdir())),2)

    def test_max_tasks_preserves_empty_held_design(self):
        self.fixture();self.policy['max_tasks']=1
        self.designer.update(status='held',blockers=['Design remains blocked'],tasks=[])
        self.preparer.update(status='held',blockers=['Design held'],assignments=[])
        plan=self.validate()
        self.assertTrue(plan['held']);self.assertEqual(plan['tasks'],{})

    def test_tampered_designer_binding_and_compiled_bytes_reject(self):
        self.fixture();self.preparer['designer_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'bind this designer'):self.validate()
        self.preparer['designer_sha256']=packages.digest(self.design_path)
        manifest=self.submit();Path(manifest['jobs'][0]['spec']).write_text('{}')
        with self.assertRaisesRegex(ValueError,'Compiled'):self.submit()

    def test_duplicate_task_or_assignment_and_missing_slot_reject(self):
        self.fixture();self.designer['tasks'].append(deepcopy(self.designer['tasks'][0]))
        with self.assertRaisesRegex(ValueError,'Duplicate task'):self.validate()
        self.designer['tasks'].pop();self.preparer['assignments'].append(deepcopy(self.preparer['assignments'][0]))
        with self.assertRaisesRegex(ValueError,'Duplicate'):self.validate()
        self.preparer['assignments']=[]
        with self.assertRaisesRegex(ValueError,'every declared'):self.validate()

    def test_candidate_and_command_injection_are_rejected(self):
        self.fixture();self.designer['tasks'][0]['applicable_target_ids']=['unapproved']
        with self.assertRaisesRegex(ValueError,'Unsupported candidate'):self.validate()
        self.designer['tasks'][0]['applicable_target_ids']=['approved-api'];self.preparer['assignments'][0]['config']={'commands':'evil'}
        with self.assertRaisesRegex(ValueError,'Unexpected'):self.validate()

    def test_grading_material_cannot_leak_into_execution(self):
        self.fixture();self.policy['materials']['ledger']['audience']='grading'
        with self.assertRaisesRegex(ValueError,'grading-only'):self.validate()

    def test_held_assignment_is_recorded_without_queue_submission(self):
        self.fixture();self.preparer['assignments'][0].update(status='held',blockers=['Required account is unavailable'])
        runs.write(self.prep_path,self.preparer);manifest=self.submit()
        self.assertEqual(manifest['jobs'][0]['status'],'held')
        self.assertEqual(list((self.queue/'inbox').iterdir()),[])

    def test_whole_role_hold_without_a_usable_task_is_retained_without_a_trial(self):
        self.fixture();self.designer.update(status='held',blockers=['No applicable official candidate sources'],tasks=[])
        runs.write(self.design_path,self.designer);self.preparer.update(status='held',blockers=['Design held'],assignments=[],designer_sha256=packages.digest(self.design_path))
        runs.write(self.prep_path,self.preparer);result=self.submit()
        self.assertEqual(result['status'],'held');self.assertEqual(result['jobs'],[])
        self.assertIn('Design held',result['blockers']);self.assertEqual(list((self.queue/'inbox').iterdir()),[])

    def test_missing_held_reason_and_ready_with_blockers_reject(self):
        self.fixture();self.preparer['assignments'][0]['status']='held'
        with self.assertRaisesRegex(ValueError,'Held work'):self.validate()
        self.preparer['assignments'][0].update(status='ready',blockers=['hidden hold'])
        with self.assertRaisesRegex(ValueError,'Held work'):self.validate()

    def test_material_paths_links_and_empty_hash_reject(self):
        self.fixture();path=self.root/'materials';path.mkdir();(path/'data.csv').write_text('currency,amount\nEUR,1\n')
        for name in ('../ledger.csv','/etc/passwd'):
            with self.assertRaisesRegex(ValueError,'inside'):packages.regular_file(path,name)
        (path/'link.csv').symlink_to(self.root/'ledger.csv')
        with self.assertRaisesRegex(ValueError,'links'):packages.regular_file(path,'link.csv')
        self.policy['materials']['ledger']['sha256']=''
        with self.assertRaisesRegex(ValueError,'bytes changed'):self.validate()

    def test_generated_csv_is_registered_from_verified_collection_and_strict_data_schema(self):
        self.fixture();collection=self.root/'collected';(collection/'artifacts/materials').mkdir(parents=True)
        file=collection/'artifacts/materials/ledger.csv';file.write_text('currency,amount\nEUR,42\n')
        self.preparer['materials']=[{'id':'ledger','file':'materials/ledger.csv','sha256':packages.digest(file),'bytes':file.stat().st_size,'synthetic':True,'source':'Synthetic fixture','validation':'Data schema'}]
        self.policy['materials']={};self.policy['generated_materials']={'ledger':{'file':'materials/ledger.csv','format':'csv',
            'columns':{'currency':{'type':'string','pattern':'[A-Z]{3}'},'amount':{'type':'number'}}}}
        with patch.object(packages,'collection',return_value=collection):
            self.assertEqual(self.validate()['materials']['ledger']['audience'],'execution')
            file.write_text('currency,amount,answer\nEUR,42,solution\n');self.preparer['materials'][0]['sha256']=packages.digest(file);self.preparer['materials'][0]['bytes']=file.stat().st_size
            with self.assertRaisesRegex(ValueError,'columns differ'):self.validate()

    def test_ready_generated_data_cannot_contain_a_service_call_or_answer_column(self):
        self.fixture();data=self.root/'generated.json'
        data.write_text(json.dumps([{'currency':'import requests; requests.get("secret")','amount':1}]))
        rule={'format':'json','columns':{'currency':{'type':'string','pattern':'[A-Z]{3}'},'amount':{'type':'number'}}}
        with self.assertRaisesRegex(ValueError,'data schema'):packages.raw_data(data,rule)

    def test_all_template_metadata_is_private_and_references_never_become_attachments(self):
        self.fixture();self.designer.update(role='task_design',demand_sources=['Provided demand brief'])
        self.designer['tasks'][0]['applicability']={'approved-api':'Controller-provided capability brief'}
        self.preparer.update(role='material_preparation',references=[],resource_prerequisites={'account':'controller provided'},frozen_dates={'business':'2026-10-01'})
        runs.write(self.design_path,self.designer);self.preparer['designer_sha256']=packages.digest(self.design_path);runs.write(self.prep_path,self.preparer)
        manifest=self.submit();config=runs.read(runs.read(manifest['jobs'][0]['spec'])['config'])
        reference=runs.read(config['reference'])
        self.assertIn('work_package_preparation',reference)
        self.assertEqual(len(list(Path(config['attachments']).iterdir())),1)

    def test_material_id_does_not_rename_the_declared_original_filename(self):
        self.fixture();self.policy['materials']['expense-ledger']=self.policy['materials'].pop('ledger')
        self.designer['tasks'][0]['material_ids']=['expense-ledger']
        runs.write(self.design_path,self.designer);self.preparer['designer_sha256']=packages.digest(self.design_path)
        runs.write(self.prep_path,self.preparer);runs.write(self.policy_path,self.policy)
        manifest=self.submit();config=runs.read(runs.read(manifest['jobs'][0]['spec'])['config'])
        self.assertEqual([x.name for x in Path(config['attachments']).iterdir()],['ledger.csv'])

    def test_duplicate_material_filename_never_overwrites_another_original(self):
        self.fixture();other=self.root/'other/ledger.csv';other.parent.mkdir();other.write_text('currency,amount\nUSD,3\n')
        self.policy['materials']['second-ledger']={**self.policy['materials']['ledger'],'path':str(other),'sha256':packages.digest(other)}
        self.designer['tasks'][0]['material_ids'].append('second-ledger')
        runs.write(self.design_path,self.designer);self.preparer['designer_sha256']=packages.digest(self.design_path)
        runs.write(self.prep_path,self.preparer);runs.write(self.policy_path,self.policy)
        with self.assertRaisesRegex(ValueError,'Duplicate or unsafe'):self.submit()

    def test_missing_material_may_only_be_explicitly_held(self):
        self.fixture();self.policy['materials']={};self.policy['generated_materials']={'ledger':{'format':'csv'}}
        with self.assertRaisesRegex(ValueError,'lacks its declared'):self.validate()
        self.preparer['assignments'][0].update(status='held',blockers=['No completed raw data artifact'])
        self.assertEqual(self.validate()['assignments'][0]['status'],'held')

    def test_generated_material_cannot_skip_actual_collection_or_hash(self):
        self.fixture();self.policy['materials']={};self.preparer['materials']=[{'id':'ledger','file':'materials/ledger.csv','sha256':''}]
        self.policy['preparer_collection']={'directory':str(self.root),'receipt_sha256':'0'*64,'proof_sha256':'0'*64}
        self.collection_patch.stop()
        with self.assertRaises((OSError,ValueError)):self.validate()

    def test_executor_and_grader_cannot_share_a_runtime(self):
        self.fixture();self.policy['targets']['approved-api']['config']['grading']['runtime']='fixture-execution'
        runs.write(self.policy_path,self.policy)
        with self.assertRaisesRegex(ValueError,'separate'):self.submit()

    def test_one_target_executor_cannot_alias_another_target_grader(self):
        self.fixture();self.policy['targets']['second-api']=deepcopy(self.policy['targets']['approved-api'])
        second=self.policy['targets']['second-api']['config'];second['execution']['runtime']='second-execution'
        second['grading']['runtime']='fixture-execution'
        self.designer['tasks'][0]['applicable_target_ids'].append('second-api')
        self.preparer['assignments'].append({'task_id':'expenses','target_id':'second-api','round':1,'status':'ready','blockers':[]})
        with self.assertRaisesRegex(ValueError,'whole package'):self.validate()

    def test_existing_queue_identity_never_silently_adopts_different_config(self):
        self.fixture();manifest=self.submit();job=manifest['jobs'][0]
        handoff=self.queue/'inbox'/job['id']/'handoff.json';value=runs.read(handoff);value['members'][0]['config']['environment']='changed';runs.write(handoff,value)
        with self.assertRaisesRegex(ValueError,'Existing queued'):self.submit()


class RoleCollectionBindingTests(unittest.TestCase):
    setUp=role_fixtures.RoleHandoffTests.setUp
    prepare=role_fixtures.RoleHandoffTests.prepare
    completed=role_fixtures.RoleHandoffTests.completed

    def binding(self):
        self.prepare();manifest,output=self.completed();role_handoff.validate_collection(self.directory,manifest)
        policy={'designer_collection':{'directory':str(output),'receipt_sha256':packages.digest(output/'receipt.json'),
                                     'proof_sha256':packages.digest(output/'role-collection-proof.json')}}
        return policy,output

    def test_actual_native_collected_designer_binds_json_and_proof(self):
        policy,output=self.binding()
        self.assertEqual(packages.collection(policy,'task_design',output/'task-design.json'),output.resolve())

    def test_receipt_zero_or_agent_ready_cannot_replace_native_completion(self):
        policy,output=self.binding();events=output/'events.jsonl'
        events.write_text(events.read_text().splitlines()[0]+'\n')
        with self.assertRaisesRegex(ValueError,'source bytes changed'):packages.collection(policy,'task_design',output/'task-design.json')

    def test_uncollected_json_or_forged_proof_is_rejected(self):
        policy,output=self.binding();other=self.root/'operator.json';other.write_text('{}')
        with self.assertRaisesRegex(ValueError,'bound collected'):packages.collection(policy,'task_design',other)
        proof=output/'role-collection-proof.json';proof.write_text('{"verified":true}')
        with self.assertRaisesRegex(ValueError,'proof binding changed'):packages.collection(policy,'task_design',output/'task-design.json')


if __name__=='__main__':unittest.main()
