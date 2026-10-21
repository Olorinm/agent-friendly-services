"""Real native preparation proofs and queue handoffs; adapter I/O is synthetic."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import registered_task_producer as producer
import role_producer_test as native
import pipeline as runs
import role_handoff as roles
import task_queue as queue


class RegisteredProducerTests(unittest.TestCase):
    setUp = native.RoleProducerTests.setUp
    fixture = native.RoleProducerTests.fixture
    mock_model = native.RoleProducerTests.mock_model
    # Reuse only the real native Codex collection/usage fixture, not its designer.
    def fixture_registered(self, count=3, waiting_access=False):
        self.fixture(packages=max(2,count), cap=2)
        producer.libraries(ROOT)
        self.entry_paths=[]
        self.queue_dir=self.queue
        for index, package in enumerate(self.plan['packages'][:count]):
            cfg=deepcopy(self.config);cfg['trial_protocol']='afs-20261013'
            cfg['preflight']=[{'url':'https://example.com','method':'HEAD'}]
            cfg['execution']['max_model_requests']=10
            if waiting_access and index==0:
                cfg.update(phase='business',depends_on=str(self.root/'missing-access'))
            task,_=runs.module('registered_fixture_task','codex-service-trial.py').select_task(self.root/'tasks.md','access')
            item={'id':package['id'],'task_file':'tasks.md','task_id':'access','task_sha256':task['sha256'],
                  'rounds':[1], 'targets':{'approved-api':{'config':cfg}}, 'material_ids':['ledger'],
                  'generated_materials':{'ledger':{'file':'materials/ledger.csv','format':'csv','columns':{
                      'currency':{'type':'string','pattern':'[A-Z]{3}'},'amount':{'type':'number'}}}}}
            # Different explicitly declared environments avoid semantic duplicate slots.
            cfg['environment_id']='registered-'+package['id']
            path=self.root/(package['id']+'.registered.json');runs.write(path,item);self.entry_paths.append(path)
        self.registered_plan={'schema_version':1,'queue':str(self.queue),'deadline_epoch':self.deadline,
            'max_total_concurrency':12,'max_preparation_concurrency':2,
            'preparation_settings':[self.plan['packages'][n]['preparation_settings'] for n in (0,1)],
            'grading_settings':[self.plan['packages'][n]['design_settings'] for n in (0,1)],
            'backlog':[str(p) for p in self.entry_paths]}
        self.registered_plan_path=self.root/'registered-plan.json';runs.write(self.registered_plan_path,self.registered_plan)
        self.registered_dir=self.root/'registered-producer'
        return self.registered_plan

    def complete(self,directory,role,settings,package):
        native.RoleProducerTests.complete(self,directory,role,settings,package)
        if role=='material_preparation':
            p=Path(directory)/'output/material-preparation.json';value=runs.read(p)
            boundary=runs.read(Path(directory)/'input/preparation-boundary.json')
            value['assignments']=[{'task_id':'access','target_id':target,'round':number,'status':'ready','blockers':[]} for target in boundary['targets'] for number in boundary['rounds']]
            if getattr(self,'original_mode',None)=='empty':value['materials']=[]
            if getattr(self,'original_mode',None)=='changed':
                material=Path(directory)/'output/artifacts/materials/ledger.csv';material.write_text('currency,amount\nEUR,99\n');value['materials'][0].update(sha256=runs.digest(material),bytes=material.stat().st_size)
            runs.write(p,value);runs.write(Path(directory)/'output/artifacts/material-preparation.json',value)

    def init_registered(self):return producer.init(self.registered_dir,self.registered_plan_path,ROOT)

    def advance_registered(self,**kwargs):
        with patch.object(roles.runs,'invoke',side_effect=self.mock_model):
            return producer.tick(self.registered_dir,**kwargs)

    def test_registry_native_prep_submits_without_any_designer_and_preserves_original_task(self):
        self.fixture_registered(count=2);self.init_registered()
        self.advance_registered();state=self.advance_registered()
        self.assertTrue(all(x['phase']=='submitted' for x in state['items'].values()))
        self.assertTrue(all(role=='material_preparation' for _,role,_ in self.operations))
        for name in state['items']:
            root=self.registered_dir/'backlog'/name
            projection=runs.read(root/'preparation-input/task-design.json')
            self.assertEqual(projection['source_kind'],'registered_task');self.assertEqual(projection['role'],'registered_task')
            self.assertFalse((root/'design').exists())
            handoff=runs.read(self.queue/'inbox'/(name+'-approved-api-r1')/'handoff.json')
            self.assertEqual(handoff['kind'],'run')
            cfg=handoff['members'][0]['config'];self.assertEqual(cfg['task_file'],'tasks.md');self.assertEqual(cfg['task'],'access')
            self.assertEqual(handoff['members'][0]['inputs']['task']['sha256'],projection['source']['task_sha256'])
        starts=len([x for x in self.operations if x[2]=='start']);self.advance_registered()
        self.assertEqual(starts,len([x for x in self.operations if x[2]=='start']))
        self.assertEqual(len(list((self.queue/'inbox').glob('*/ready.json'))),2)

    def test_collected_package_waiting_access_releases_worker_and_other_targets_submit(self):
        self.fixture_registered(count=3,waiting_access=True);self.init_registered()
        self.advance_registered();state=self.advance_registered()
        self.assertEqual(state['items']['package-1']['phase'],'waiting_access')
        self.assertEqual(state['items']['package-3']['phase'],'preparing')
        self.assertTrue(state['items']['package-1']['worker_released'])
        self.assertEqual(state['items']['package-2']['phase'],'submitted')

    def test_missing_or_unknown_original_free_qualification_cannot_be_repaired_by_ready_prose(self):
        self.fixture_registered(count=2)
        path=self.entry_paths[0];item=runs.read(path)
        item['targets']['approved-api']['config']['resource_authorization']={'service':'fixture','route':'api','service_fee':{'status':'unknown'}}
        runs.write(path,item);self.init_registered();self.advance_registered();state=self.advance_registered()
        self.assertEqual(state['items']['package-1']['phase'],'held')
        self.assertFalse((self.queue/'inbox/package-1-approved-api-r1').exists())
        self.assertEqual(state['items']['package-2']['phase'],'submitted')

    def test_original_hard_hold_stays_binding(self):
        self.fixture_registered(count=2);path=self.entry_paths[0];item=runs.read(path)
        ref=self.root/'held-reference.json';value=runs.read(item['targets']['approved-api']['config']['reference'])
        value['cohort_disclosure']={'held_routes':{'fixture/api':'Missing mandatory original source'}};runs.write(ref,value)
        item['targets']['approved-api']['config']['reference']=str(ref);runs.write(path,item)
        self.init_registered();self.advance_registered();state=self.advance_registered()
        self.assertEqual(state['items']['package-1']['phase'],'held');self.assertIn('assigned route is held',state['items']['package-1']['held_targets'][0]['reason'])

    def test_uncertain_start_stops_before_retry_and_reserves_unconfirmed_worker(self):
        self.fixture_registered(count=3);self.uncertain.add('package-1');self.unconfirmed.add('package-1');self.init_registered()
        state=self.advance_registered();self.assertEqual(state['items']['package-1']['phase'],'attention')
        self.advance_registered();state=self.advance_registered()
        self.assertEqual(len([x for x in self.operations if x==('package-1','material_preparation','start')]),1)
        self.assertTrue(any(x==('package-1','material_preparation','stop') for x in self.operations))
        self.assertEqual(state['items']['package-1']['phase'],'attention')
        self.assertNotEqual(state['items']['package-3'].get('worker'),0)

    def test_drift_halts_owned_handles_and_prevents_new_starts(self):
        self.fixture_registered(count=3);self.running.update(('package-1','package-2'));self.init_registered();self.advance_registered()
        path=self.entry_paths[0];path.write_text(path.read_text()+'\n')
        state=self.advance_registered();self.assertEqual(state['phase'],'stopped')
        self.assertFalse(any(x[0]=='package-3' and x[2]=='start' for x in self.operations))
        self.assertEqual({x[0] for x in self.operations if x[2]=='stop'},{'package-1','package-2'})

    def test_two_worker_envelope_and_physical_separation_are_enforced(self):
        self.fixture_registered(count=2);self.registered_plan['max_total_concurrency']=11;runs.write(self.registered_plan_path,self.registered_plan)
        with self.assertRaisesRegex(ValueError,'envelope'):self.init_registered()
        self.registered_plan['max_total_concurrency']=12;self.registered_plan['grading_settings'][0]=self.registered_plan['preparation_settings'][0];runs.write(self.registered_plan_path,self.registered_plan)
        with self.assertRaisesRegex(ValueError,'Distinct'):self.init_registered()

    def test_low_storage_checked_for_new_role_starts(self):
        self.fixture_registered(count=2);self.init_registered()
        with patch.object(queue,'storage_hold',return_value='low disk'):
            state=self.advance_registered()
        self.assertFalse(self.operations);self.assertTrue(all(x['phase']=='waiting' for x in state['items'].values()))

    def test_backlog_file_append_is_consumed_without_controller_restart(self):
        self.fixture_registered(count=3);inbox=self.root/'intake';inbox.mkdir()
        self.registered_plan['backlog']=[];self.registered_plan['backlog_inbox']=str(inbox);runs.write(self.registered_plan_path,self.registered_plan);self.init_registered()
        self.assertEqual(self.advance_registered()['phase'],'no_ready_work')
        (inbox/'new.json').write_bytes(self.entry_paths[0].read_bytes())
        state=self.advance_registered();self.assertEqual(state['items']['package-1']['phase'],'preparing')

    def test_wrong_task_sha_rejected_before_preparation(self):
        self.fixture_registered(count=2);item=runs.read(self.entry_paths[0]);item['task_sha256']='0'*64;runs.write(self.entry_paths[0],item)
        with self.assertRaisesRegex(ValueError,'task SHA'):self.init_registered()

    def test_unique_native_handles_across_parallel_and_reused_workers(self):
        self.fixture_registered(count=3);self.init_registered();self.advance_registered();self.advance_registered();self.advance_registered()
        names=[]
        for identity in ('package-1','package-2','package-3'):
            job=producer.role_job(self.registered_dir/'backlog'/identity)
            manifest=runs.read(job/'manifest.json');names.append(manifest['request']['run_id'])
            self.assertEqual(manifest['request']['role'],'material_preparation')
        self.assertEqual(len(set(names)),3)
        self.assertNotIn('preparation',names)

    def test_second_producer_directory_cannot_claim_same_queue(self):
        self.fixture_registered(count=2);self.init_registered()
        with self.assertRaisesRegex(ValueError,'another registered'):
            producer.init(self.root/'second-producer',self.registered_plan_path,ROOT)

    def test_existing_frozen_queue_cannot_share_a_preparation_runtime(self):
        self.fixture_registered(count=2);cfg=deepcopy(runs.read(self.entry_paths[0])['targets']['approved-api']['config'])
        cfg['grading']=runs.read(self.registered_plan['preparation_settings'][0]);path=self.root/'existing.json';runs.write(path,cfg)
        spec=self.root/'existing.spec.json';runs.write(spec,{'id':'existing','kind':'run','ready':True,'config':str(path),'directory':str(self.root/'data/experiments/results/existing'),'depends_on':[]})
        queue.submit(self.queue,spec)
        with self.assertRaisesRegex(ValueError,'existing frozen queue owner'):self.init_registered()

    def test_live_policy_drift_blocks_all_new_starts(self):
        self.fixture_registered(count=2);self.init_registered();policy=runs.read(self.queue/'policy.json');policy['max_concurrency']=12;runs.write(self.queue/'policy.json',policy)
        state=self.advance_registered();self.assertEqual(state['phase'],'stopped');self.assertFalse(self.operations)

    def test_state_plan_mirror_drift_cannot_change_deadline_or_worker(self):
        self.fixture_registered(count=2);self.init_registered();state=runs.read(self.registered_dir/'state.json');state['frozen_plan']['deadline_epoch']+=100;runs.write(self.registered_dir/'state.json',state)
        state=self.advance_registered();self.assertEqual(state['phase'],'stopped');self.assertFalse(self.operations)

    def test_halt_preserves_submitted_results_and_confirmed_handles(self):
        self.fixture_registered(count=2);self.init_registered();self.advance_registered();self.advance_registered()
        state=self.advance_registered(halt=True)
        self.assertEqual([x['phase'] for x in state['items'].values()],['submitted','submitted'])

    def original_materials(self,mode):
        self.fixture_registered(count=2);self.original_mode=mode
        material=self.root/'approved-ledger.csv';material.write_text('currency,amount\nEUR,12.5\n')
        for path in self.entry_paths:
            item=runs.read(path);item['generated_materials']={};item['materials']={'ledger':{'path':str(material),'sha256':runs.digest(material),'audience':'execution','kind':'raw_data'}};runs.write(path,item)
        self.init_registered();self.advance_registered();return self.advance_registered()

    def test_original_material_ids_with_empty_native_manifest_reuse_exact_approved_bytes(self):
        state=self.original_materials('empty');self.assertTrue(all(x['phase']=='submitted' for x in state['items'].values()))
        boundary=runs.read(self.registered_dir/'backlog/package-1/preparation-input/preparation-boundary.json')
        self.assertIn('emit materials: []',boundary['materials_output_rule'])

    def test_exact_original_material_echo_is_accepted_without_relabeling_registry(self):
        state=self.original_materials('echo');self.assertTrue(all(x['phase']=='submitted' for x in state['items'].values()))

    def test_changed_original_material_echo_is_rejected(self):
        state=self.original_materials('changed');self.assertTrue(all(x['phase']=='held' for x in state['items'].values()))

    def test_posthoc_ready_target_submits_without_waiting_for_other_access(self):
        self.fixture_registered(count=2,waiting_access=True);path=self.entry_paths[0];item=runs.read(path)
        cfg=deepcopy(item['targets']['approved-api']['config']);cfg['phase']='access';cfg.pop('depends_on',None);cfg['service']='fixture-a';cfg['environment_id']='other-route'
        item['targets']['ready-api']={'config':cfg};runs.write(path,item)
        catalog=runs.read(self.root/'generated/catalog.json');catalog['services'].append({'id':'fixture-a','catalog':{'routes':[{'id':'api','entry_url':'https://example.com'}]}});runs.write(self.root/'generated/catalog.json',catalog)
        self.init_registered();self.advance_registered();state=self.advance_registered()
        self.assertEqual(state['items']['package-1']['phase'],'waiting_access')
        self.assertTrue((self.queue/'inbox/package-1-ready-api-r1/ready.json').exists())
        self.assertEqual(runs.read(self.queue/'inbox/package-1-ready-api-r1/handoff.json')['kind'],'run')
