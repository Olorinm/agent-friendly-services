import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import pipeline
from adapter_usage import read_usage
from service_cost import service_charge

# This is a runner fixture, not a model pretending to perform a service task.
ADAPTER = r'''
import hashlib,json,sys
from pathlib import Path
op=sys.argv[1];q=json.loads(Path(sys.argv[2]).read_text());out=Path(q['output']);out.mkdir(exist_ok=True)
if op=='start':
    p=out/'started';assert not p.exists(),'duplicate dispatch';p.write_text('started')
    assert (Path(q['input'])/'AGENTS.md').is_file()
    if q['role']=='execution':
        assert not (Path(q['input'])/'task.json').exists()
        assert not (Path(q['input'])/'reference.json').exists()
    print(json.dumps({'handle':q['role']+'-handle'}))
elif op=='status':print(json.dumps({'status':'completed'}))
elif op=='stop':print(json.dumps({'stopped':True}))
elif op=='collect':
    def write(name,value): (out/name).write_text(json.dumps(value))
    usage={'input_tokens':10,'cached_input_tokens':4,'cache_write_input_tokens':0,'output_tokens':2}
    write('raw.json',{'usage':usage})
    write('usage.json',{'schema_version':1,'complete':True,'model':q['model'],'sources':[{'path':'raw.json','sha256':hashlib.sha256((out/'raw.json').read_bytes()).hexdigest()}],
                       'totals':usage,'requests':[{'id':'one','usage':usage}]})
    write('receipt.json',{'session_id':q['role']+'-session','workspace':str(out/'workspace'),
          'model':q['model'],'reasoning_effort':q['reasoning_effort'],'harness':q['harness'],'runtime':q['runtime'],
          'input_verified':True,'isolation':'synthetic fixture process; no model or service',
          'started_at':'2026-09-10T00:00:00Z','ended_at':'2026-09-10T00:00:01Z','exit_code':0,'timed_out':False})
    if q['role']=='execution':
        (out/'answer.md').write_text('synthetic answer')
        (out/'events.jsonl').write_text('{}\n')
        write('evidence.json',{'answer':'synthetic answer'})
    else:
        write('assessment.json',{'status':'completed','reason':'Synthetic answer matches frozen requirement','reviewer':'fixture-independent-session',
          'checks':[{'criterion':'answer matches','passed':True,'evidence':'execution/evidence.json'}],
          'evidence':[{'path':'execution/evidence.json'}],'human_interventions':0,
          'service_cost_usd':None,'service_cost':{'kind':'estimated','note':'One metered fixture request',
            'sources':['execution/evidence.json','https://example.com/pricing'],
            'items':[{'quantity':1,'unit':'request','usd_per_unit':0.00000000001}]},
          'model_cost_usd':0,'usage':{'input_tokens':0,'output_tokens':0}})
    print(json.dumps({'collected':True}))
'''


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='afs-pipeline-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.addCleanup(setattr, pipeline, 'ROOT', pipeline.ROOT)
        pipeline.ROOT = self.root
        # Use real renderer and role files, but only fixture catalog/results/prices.
        (self.root / 'scripts').symlink_to(ROOT / 'scripts', target_is_directory=True)
        (self.root / 'node_modules').symlink_to(ROOT / 'node_modules', target_is_directory=True)
        (self.root / 'generated').mkdir()
        (self.root / 'generated/catalog.json').write_text(json.dumps({'services':[{'id':'fixture','catalog':{'routes':[{'id':'api','entry_url':'https://example.com'}]}}]}))
        (self.root / 'tasks.md').write_text('| ID | 用户任务 | 预计输入 | 预计输出 | 完成标准 | 未完成标准 | 版本 |\n| access | Read fixture | fixture input | synthetic answer | answer matches | missing answer | v1 |\n')
        prices = {'source':'https://example.com/prices','revision':'fixture','fetched_at':'2026-09-10','models':{'fixture-model':{'input_cost_per_token':0.000002,'cache_read_input_token_cost':0.0000002,'output_cost_per_token':0.00001}}}
        prices['sha256'] = subprocess.check_output(['node','-e',
            "const c=require('crypto');console.log(c.createHash('sha256').update(JSON.stringify(JSON.parse(process.argv[1]))).digest('hex'))",json.dumps(prices['models'])],text=True).strip()
        (self.root / 'data/pricing').mkdir(parents=True)
        (self.root / 'data/pricing/litellm.json').write_text(json.dumps(prices))
        adapter = self.root / 'adapter.py';adapter.write_text(ADAPTER)
        settings = {'model':'fixture-model','reasoning_effort':'high','harness':{'name':'fixture','version':'1','mode':'noninteractive'},'seconds':60,
                    'commands':{op:[sys.executable,str(adapter),op,'{request}'] for op in ('start','status','collect','stop')}}
        self.config = {'service':'fixture','route':'api','task_file':'tasks.md','task':'access','phase':'access','environment_id':'fixture-route',
                       'environment':'Synthetic test, no network or service access.',
                       'execution':{**settings,'runtime':'fixture-execution'},'grading':{**settings,'runtime':'fixture-grading'}}
        self.config_path = self.root / 'config.json'
        self.config_path.write_text(json.dumps(self.config))
        self.directory = self.root / 'data/experiments/results/run-001'

    def prepare(self):
        return pipeline.prepare(self.config_path, self.directory)

    def finish(self):
        self.prepare()
        for _ in range(4):
            state = pipeline.advance(self.directory)
        self.assertEqual(state['phase'], 'reviewed')

    def test_complete_pipeline_records_only_measured_usage_and_validated_cost(self):
        self.finish()
        charges = pipeline.read(self.directory / 'charges.json')
        self.assertAlmostEqual(charges['model_cost']['amount_usd'], 0.0000328)
        self.assertEqual(charges['service_cost_usd'], 1e-11)
        self.assertEqual(charges['grading_model_cost']['amount_usd'], charges['model_cost']['amount_usd'])
        # npm entry points are already tested against the actual repository separately.
        with patch.object(pipeline.subprocess, 'run') as npm:
            target = pipeline.record(self.directory, generate=True)
            self.assertEqual(npm.call_count, 2)
        value = pipeline.read(target)
        self.assertEqual(value['usage']['input_tokens'], 10)
        self.assertNotIn('model_cost_usd', value)
        self.assertEqual(value['request_usage']['status'], 'complete')
        self.assertEqual(value['service_cost_usd'], 1e-11)
        self.assertEqual(value['pricing_snapshot']['revision'], 'fixture')
        self.assertFalse((target.parent.parent / 'evidence/run-001/execution/raw.json').exists())
        self.assertEqual(pipeline.advance(self.directory)['phase'], 'recorded')

    def test_uncertain_start_is_not_resubmitted(self):
        self.prepare()
        pipeline.write(self.directory / 'state.json', {'phase':'execution_starting'})
        with self.assertRaisesRegex(ValueError, 'reconciliation'):
            pipeline.advance(self.directory)
        self.assertFalse((self.directory / 'execution/started').exists())

    def test_frozen_task_cannot_change_after_prepare(self):
        self.prepare()
        (self.directory / 'frozen/execution/input.md').write_text('changed')
        with self.assertRaisesRegex(ValueError, 'Frozen'):
            pipeline.advance(self.directory)

    def test_business_requires_passed_access_in_same_environment(self):
        self.finish()
        config = {**self.config,'phase':'business','depends_on':str(self.directory),'environment_id':'other'}
        self.config_path.write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError, 'reuse'):
            pipeline.prepare(self.config_path, self.directory.with_name('run-002'))
        config['environment_id'] = self.config['environment_id']
        self.config_path.write_text(json.dumps(config))
        pipeline.prepare(self.config_path, self.directory.with_name('run-002'))

    def test_bad_service_fee_is_rejected_without_recording(self):
        self.prepare()
        for _ in range(3): pipeline.advance(self.directory)
        # Runner collect produces an unsupported zero claim for this test only.
        adapter = self.root / 'adapter.py'
        adapter.write_text(adapter.read_text().replace("'kind':'estimated'", "'kind':'confirmed_free'"))
        with self.assertRaisesRegex(ValueError, 'applicability'):
            pipeline.advance(self.directory)
        self.assertFalse((self.directory / 'charges.json').exists())
        self.assertFalse((self.root / 'data/experiments/evaluations').exists())

    def test_usage_hash_mismatch_and_duplicate_are_not_priced(self):
        self.prepare();pipeline.advance(self.directory);pipeline.advance(self.directory)
        out = self.directory / 'execution'
        data = pipeline.read(out / 'usage.json');data['requests'] *= 2
        pipeline.write(out / 'usage.json',data)
        self.assertIsNone(read_usage(out)[0])
        self.assertEqual(read_usage(out)[1]['status'],'incomplete')
        (out / 'raw.json').write_text('tampered')
        self.assertIn('hash', read_usage(out)[1]['reason'])

    def test_timeout_stops_owned_runtime_and_never_starts_grader(self):
        self.prepare();pipeline.advance(self.directory)
        state = pipeline.read(self.directory / 'state.json')
        state['dispatched_at'] = '2000-01-01T00:00:00+00:00'
        pipeline.write(self.directory / 'state.json',state)
        adapter = self.root / 'adapter.py'
        adapter.write_text(adapter.read_text().replace("elif op=='status':print(json.dumps({'status':'completed'}))",
                                                    "elif op=='status':print(json.dumps({'status':'running'}))"))
        self.assertEqual(pipeline.advance(self.directory)['phase'],'stopped')
        self.assertTrue((self.directory / 'execution-stop.json').exists())
        self.assertFalse((self.directory / 'grading/started').exists())
        with self.assertRaisesRegex(ValueError,'reconciliation'):
            pipeline.advance(self.directory)

    def test_changed_review_cannot_be_recorded(self):
        self.finish()
        assessment = pipeline.read(self.directory / 'grading/assessment.json')
        assessment['service_cost_usd'] = 0
        pipeline.write(self.directory / 'grading/assessment.json',assessment)
        with self.assertRaisesRegex(ValueError,'Reviewed record changed'):
            pipeline.record(self.directory)

    def test_prepare_freezes_prices_for_both_roles(self):
        self.prepare()
        prices = pipeline.read(self.root / 'data/pricing/litellm.json')
        prices['models']['fixture-model']['input_cost_per_token'] = 100
        pipeline.write(self.root / 'data/pricing/litellm.json',prices)
        for _ in range(4): pipeline.advance(self.directory)
        self.assertAlmostEqual(pipeline.read(self.directory / 'charges.json')['model_cost']['amount_usd'],0.0000328)

    def test_cache_write_and_model_ambiguity_are_not_treated_as_zero(self):
        self.prepare();pipeline.advance(self.directory);pipeline.advance(self.directory)
        out = self.directory / 'execution'
        data = pipeline.read(out / 'usage.json')
        del data['requests'][0]['usage']['cache_write_input_tokens']
        pipeline.write(out / 'usage.json',data)
        self.assertIn('cache-write',read_usage(out)[1]['reason'])
        data['requests'][0]['usage']['cache_write_input_tokens'] = 0
        data['requests'][0]['model'] = 'different-model'
        pipeline.write(out / 'usage.json',data)
        self.assertIn('Mixed-model',read_usage(out)[1]['reason'])

    def test_small_and_unsubstantiated_service_charges(self):
        for review in ({'service_cost_usd':0}, {'service_cost_usd':0,'service_cost':'almost free'}):
            with self.assertRaises(ValueError): service_charge(review)
        fee = {'kind':'estimated','sources':['receipt'],'note':'metered',
               'items':[{'quantity':1,'unit':'call','usd_per_unit':1e-11}]}
        self.assertEqual(service_charge({'service_cost':fee})[0],1e-11)
        with self.assertRaises(ValueError): service_charge({'service_cost':fee,'service_cost_usd':0})


if __name__ == '__main__': unittest.main()
