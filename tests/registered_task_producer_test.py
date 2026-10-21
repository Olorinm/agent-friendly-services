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

    def fixture_execution_pool(self, rounds=(1,2,3), maximum=2):
        self.fixture_registered(count=2)
        path=self.entry_paths[0];item=runs.read(path);item['rounds']=list(rounds)
        target=item['targets']['approved-api'];base=target['config'];base['phase']='business'
        base['service_credentials']={'provided':False,'source':'none; approved anonymous read-only fixture'}
        base['execution'].update(credential_scope='one-real-anonymous-ip-family',quota_endpoints=['https://example.com/'],quota_resource_locks=[],resource_locks=[])
        adapter=self.root/'execution-pool-adapter.json'
        runs.write(adapter,{'host':'fixture-pool-host','containers':{'lane-a':'pool-container-a','lane-b':'pool-container-b'}})
        base['execution']['commands']={op:['python3',str(ROOT/'scripts/runners/opencode/adapter.py'),'--config',str(adapter),op,'{request}'] for op in ('start','status','collect','stop','preflight')}
        catalog=runs.read(self.root/'generated/catalog.json');catalog['services'][0]['catalog']['routes'][0]['auth']={'value':'none'};runs.write(self.root/'generated/catalog.json',catalog)
        lanes=[]
        for name in ('a','b'):
            cfg=deepcopy(base);cfg['execution']['runtime']='lane-'+name;cfg['environment_id']='pool-environment-'+name;access=self.root/('pool-access-'+name);cfg['depends_on']=str(access)
            self.ready_lane_access(access,cfg)
            lanes.append({'id':'lane-'+name,'config':cfg,'depends_on':['pool-access-'+name]})
        target['config']=deepcopy(lanes[0]['config']);target['execution_pool']=lanes
        target['execution_pool_policy']={'mode':'readonly_anonymous','max_active_per_target':maximum}
        runs.write(path,item)
        return path,item,adapter

    def ready_lane_access(self,access,cfg):
        prior=deepcopy(cfg);prior['phase']='access';prior.pop('depends_on',None);runs.write(access/'config.json',prior)
        assessment={'status':'completed','outcome':{'service_execution':'completed'},'access_readiness':{
            name:{'status':'ready','evidence':'Synthetic controller-bound access proof; no model or service query.'} for name in ('service_call','authorization','reusable_state','isolation')}}
        runs.write(access/'grading/assessment.json',assessment)
        runs.write(access/'state.json',{'phase':'reviewed','record_hashes':{'grading/assessment.json':runs.digest(access/'grading/assessment.json')}})

    def pool_handoffs(self):
        return [runs.read(p/'handoff.json') for p in sorted((self.queue/'inbox').glob('package-1-approved-api-r*'))]

    def test_two_idle_lanes_frozen_before_submit_third_round_waits_then_collected_lane_reused(self):
        self.fixture_execution_pool();self.init_registered();self.advance_registered();state=self.advance_registered()
        self.assertEqual(state['items']['package-1']['phase'],'waiting_runtime')
        first=self.pool_handoffs();self.assertEqual(len(first),2)
        self.assertEqual({h['members'][0]['config']['execution']['runtime'] for h in first},{'lane-a','lane-b'})
        self.assertTrue(all(h['kind']=='run' for h in first))
        before={h['id']:deepcopy(h) for h in first}
        completed=Path(first[0]['members'][0]['directory']);runs.write(completed/'state.json',{'phase':'execution_collected'})
        state=self.advance_registered();self.assertEqual(state['items']['package-1']['phase'],'submitted')
        after=self.pool_handoffs();self.assertEqual(len(after),3)
        self.assertEqual({h['id']:h for h in after if h['id'] in before},before)
        for h in after:
            cfg=h['members'][0]['config'];prior=runs.read(Path(cfg['depends_on'])/'config.json')
            self.assertEqual((cfg['environment_id'],cfg['execution']['runtime']),(prior['environment_id'],prior['execution']['runtime']))

    def test_pool_requires_explicit_anonymous_readonly_policy(self):
        path,item,_=self.fixture_execution_pool();item['targets']['approved-api']['execution_pool_policy']['mode']='account_write';runs.write(path,item)
        with self.assertRaisesRegex(ValueError,'readonly_anonymous'):self.init_registered()

    def test_pool_rejects_provided_account_or_unknown_catalog_auth(self):
        path,item,_=self.fixture_execution_pool();item['targets']['approved-api']['config']['service_credentials']['provided']=True;runs.write(path,item)
        with self.assertRaisesRegex(ValueError,'account credentials'):self.init_registered()

    def test_pool_may_not_remove_template_account_or_write_locks(self):
        path,item,_=self.fixture_execution_pool();item['targets']['approved-api']['config']['execution']['resource_locks']=['approved-account-lock'];runs.write(path,item)
        with self.assertRaisesRegex(ValueError,'cannot remove'):self.init_registered()

    def test_pool_lanes_cannot_multiply_family_quota_by_renaming_credential_scope(self):
        path,item,_=self.fixture_execution_pool();item['targets']['approved-api']['execution_pool'][1]['config']['execution']['credential_scope']='invented-second-quota';runs.write(path,item)
        with self.assertRaisesRegex(ValueError,'quota family'):self.init_registered()

    def test_pool_rejects_duplicate_physical_runtime_even_with_new_logical_id(self):
        path,item,adapter=self.fixture_execution_pool();cfg=runs.read(adapter);cfg['containers']['lane-b']='pool-container-a';runs.write(adapter,cfg)
        with self.assertRaisesRegex(ValueError,'distinct physical'):self.init_registered()

    def test_pool_each_lane_needs_its_own_access_prerequisite(self):
        path,item,_=self.fixture_execution_pool();lanes=item['targets']['approved-api']['execution_pool'];lanes[1]['config']['depends_on']=lanes[0]['config']['depends_on'];runs.write(path,item)
        with self.assertRaisesRegex(ValueError,'own access'):self.init_registered()

    def test_ready_access_on_other_lane_is_not_transferred(self):
        path,item,_=self.fixture_execution_pool(rounds=(1,));lane=item['targets']['approved-api']['execution_pool'][0];prior=runs.read(Path(lane['config']['depends_on'])/'config.json');prior['execution']['runtime']='lane-b';runs.write(Path(lane['config']['depends_on'])/'config.json',prior)
        self.init_registered();self.advance_registered();state=self.advance_registered()
        handoff=self.pool_handoffs()[0]
        self.assertEqual(handoff['members'][0]['config']['execution']['runtime'],'lane-b')
        self.assertTrue(any('another execution lane' in x['reason'] for x in state['items']['package-1']['held_targets']))

    def test_pending_access_on_one_lane_does_not_block_other_ready_lane(self):
        path,item,_=self.fixture_execution_pool(rounds=(1,));access=Path(item['targets']['approved-api']['execution_pool'][0]['config']['depends_on']);runs.write(access/'state.json',{'phase':'execution_running'})
        self.init_registered();self.advance_registered();state=self.advance_registered()
        self.assertEqual(self.pool_handoffs()[0]['members'][0]['config']['execution']['runtime'],'lane-b')
        self.assertEqual(state['items']['package-1']['phase'],'submitted')

    def test_max_active_one_defers_second_idle_lane_without_changing_its_quota(self):
        self.fixture_execution_pool(rounds=(1,2),maximum=1);self.init_registered();self.advance_registered();state=self.advance_registered()
        self.assertEqual(len(self.pool_handoffs()),1);self.assertEqual(state['items']['package-1']['phase'],'waiting_runtime')

    def test_shared_cooldown_blocks_all_idle_lanes_and_remains_controller_owned(self):
        path,item,_=self.fixture_execution_pool(rounds=(1,));self.init_registered()
        cfg=item['targets']['approved-api']['config'];binding=queue.inputs(cfg)['quota_binding'];state=runs.read(self.queue/'state.json')
        queue.cooldowns.register(state,{'observation_id':'shared-scope-fixture','scope_id':binding['scope_id'],'binding_sha256':binding['binding_sha256'],'kind':'quota','until':None,'confidence':'captured_transport_signal','source':{'sha256':'a'*64}})
        runs.write(self.queue/'state.json',state)
        self.advance_registered();state=self.advance_registered()
        self.assertFalse(self.pool_handoffs());self.assertEqual(state['items']['package-1']['phase'],'waiting_runtime')
        self.assertIn('shared-scope-fixture',runs.read(self.queue/'state.json')['route_cooldowns']['observations'])

    def test_pool_lane_source_drift_blocks_new_prep_and_leaves_existing_bindings(self):
        _,_,adapter=self.fixture_execution_pool();self.init_registered();cfg=runs.read(adapter);cfg['containers']['lane-a']='unapproved-container';runs.write(adapter,cfg)
        state=self.advance_registered();self.assertEqual(state['phase'],'stopped');self.assertFalse(self.operations)

    def test_pool_rejects_grader_or_preparation_container_as_executor(self):
        path,item,adapter=self.fixture_execution_pool();settings=runs.read(self.registered_plan['preparation_settings'][0]);prep=queue.runtime_identity(settings);cfg=runs.read(adapter);cfg['host']=prep[0];cfg['containers']['lane-b']=prep[1];runs.write(adapter,cfg)
        with self.assertRaisesRegex(ValueError,'share a preparation'):self.init_registered()

    def test_duplicate_pool_slots_cannot_hide_behind_an_unused_template_environment(self):
        _,item,_=self.fixture_execution_pool();other=deepcopy(item);other['id']='package-2'
        other['targets']['approved-api']['config']['environment_id']='unused-template-environment'
        runs.write(self.entry_paths[1],other)
        with self.assertRaisesRegex(ValueError,'Duplicate existing task/route/round'):self.init_registered()

    def test_missing_state_of_attention_owner_does_not_free_its_execution_lane(self):
        self.fixture_execution_pool(rounds=(1,2));self.init_registered();self.advance_registered();self.advance_registered()
        handoff=self.pool_handoffs()[0];state=runs.read(self.queue/'state.json');state['jobs'][handoff['id']]={'handoff':handoff,'phase':'needs_attention','prepared':True};runs.write(self.queue/'state.json',state)
        occupied,_,_=producer.execution_load(self.registered_plan)
        self.assertIn(queue.runtime_identity(handoff['members'][0]['config']['execution']),occupied)

    def test_unconfirmed_execution_stop_keeps_lane_reserved(self):
        self.fixture_execution_pool(rounds=(1,2));self.init_registered();self.advance_registered();self.advance_registered()
        handoff=self.pool_handoffs()[0];path=Path(handoff['members'][0]['directory']);runs.write(path/'state.json',{'phase':'stopped','stop_confirmed':False})
        occupied,_,_=producer.execution_load(self.registered_plan)
        self.assertIn(queue.runtime_identity(handoff['members'][0]['config']['execution']),occupied)
