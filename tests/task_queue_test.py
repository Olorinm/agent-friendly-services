import copy
from pathlib import Path
import unittest
from unittest.mock import patch

import pipeline_test as fixtures
import pipeline as runs
import task_queue as queue


class QueueTests(unittest.TestCase):
    setUp = fixtures.PipelineTests.setUp

    def init(self, cap=10, concurrency=2):
        self.queue = self.root/'queue'
        queue.init(self.queue, max_concurrency=concurrency, budget_usd=cap,
                   expires_at='2099-01-01T00:00:00Z', pool='fixture-no-network')

    def submit(self, identity, deps=(), business=False, preflight_ready=True, grading_gate=False):
        cfg = copy.deepcopy(self.config)
        cfg['preflight'] = [{'url': 'https://example.com', 'method': 'HEAD'}]
        for role in ('execution', 'grading'):
            cfg[role]['max_model_requests'] = 25
            cfg[role]['commands']['preflight'] = [*cfg[role]['commands']['start']]
            cfg[role]['commands']['preflight'][2] = 'preflight'
        if business:
            cfg.update(phase='business', depends_on=str(self.root/'data/experiments/results'/deps[0]))
        file = self.root/(identity+'.config.json');runs.write(file, cfg)
        adapter = self.root/'adapter.py'
        if "if op=='preflight':" not in adapter.read_text():
            adapter.write_text(adapter.read_text().replace("if op=='start':", "if op=='preflight':print(json.dumps({'ready':"+str(preflight_ready)+"}))\nelif op=='start':"))
        spec = self.root/(identity+'.spec.json')
        path = self.root/'data/experiments/results'/identity
        runs.write(spec, {'id': identity, 'kind': 'run', 'ready': True, 'directory': str(path),
                          'config': str(file), 'depends_on': list(deps), 'grading_gate': grading_gate})
        queue.submit(self.queue, spec)
        return path

    def advance(self):
        with patch.object(queue, 'ceiling', return_value=1):
            return queue.advance(self.queue)

    def test_dynamic_admission_dependencies_and_recoverable_no_duplicate_dispatch(self):
        self.init(concurrency=1)
        first = self.submit('access-first')
        self.assertEqual(self.advance()['jobs']['access-first']['phase'], 'execution_running')
        second = self.submit('business-next', ['access-first'], business=True)
        self.assertEqual(self.advance()['jobs']['business-next']['phase'], 'waiting')
        self.assertFalse(second.exists())
        for _ in range(10): state = self.advance()
        self.assertEqual(state['jobs']['access-first']['phase'], 'reviewed')
        self.assertEqual(state['jobs']['business-next']['phase'], 'reviewed')
        self.assertEqual(state['phase'], 'idle')
        self.assertTrue((first/'execution/started').exists())
        self.assertTrue((second/'grading/started').exists())
        self.assertAlmostEqual(state['held_usd'], 4 * 0.0000328)

    def test_unknown_cost_keeps_reservation_and_blocks_more_spending(self):
        self.init(cap=1.5, concurrency=2)
        path = self.submit('partial')
        adapter = self.root/'adapter.py'
        adapter.write_text(adapter.read_text().replace("'complete':True", "'complete':False"))
        self.advance();state = self.advance()
        for _ in range(3): state = self.advance()
        self.assertEqual(state['held_usd'], 1)
        self.assertFalse((path/'grading/started').exists())
        row = next(iter(state['ledger'].values()))
        self.assertGreater(row['measured_cost']['lower_bound_usd'], 0)
        self.assertIsNone(row['measured_cost']['amount_usd'])

    def test_failed_preflight_has_no_model_dispatch_and_refunds_reservation(self):
        self.init();path = self.submit('unreachable', preflight_ready=False)
        state = self.advance()
        self.assertEqual(state['jobs']['unreachable']['phase'], 'preflight_blocked')
        self.assertEqual(state['held_usd'], 0)
        self.assertFalse((path/'execution/started').exists())
        self.assertFalse((path/'grading').exists())

    def test_handoff_tampering_and_duplicate_submission_are_rejected(self):
        self.init();self.submit('one')
        with self.assertRaises(FileExistsError): queue.submit(self.queue, self.root/'one.spec.json')
        file = self.queue/'inbox/one/handoff.json'
        file.write_text(file.read_text().replace('fixture input', 'changed input'))
        with self.assertRaisesRegex(ValueError, 'handoff changed'): self.advance()

    def test_private_secret_source_is_frozen_by_handoff(self):
        self.init()
        source = self.root / 'secrets.json'
        runs.write(source, ['fixture-private-key-12345'])
        self.config['grading_secrets_file'] = str(source)
        path = self.submit('secret-binding')
        runs.write(source, ['different-private-key-67890'])
        state = self.advance()
        self.assertEqual(state['jobs']['secret-binding']['phase'], 'blocked')
        self.assertIn('inputs changed', state['jobs']['secret-binding']['reason'])
        self.assertFalse(path.exists())

    def test_deadline_stops_collects_and_forbids_another_paid_dispatch(self):
        self.init();path = self.submit('deadline')
        self.advance()
        policy = runs.read(self.queue/'policy.json');policy['expires_at'] = '2000-01-01T00:00:00Z'
        runs.write(self.queue/'policy.json', policy)
        state = self.advance()
        self.assertEqual(state['phase'], 'expired')
        self.assertTrue(runs.read(path/'state.json')['stop_confirmed'])
        self.assertTrue((path/'execution/model-cost.json').exists())
        self.assertFalse((path/'grading/started').exists())

    def test_same_runtime_exclusion_applies_to_unrelated_jobs(self):
        self.init(concurrency=2);first = self.submit('first');second = self.submit('second')
        self.advance()
        self.assertTrue((first/'execution/started').exists())
        self.assertFalse((second/'execution/started').exists())

    def test_shared_account_lock_serializes_distinct_runtimes(self):
        self.init(concurrency=2)
        self.config['execution']['resource_locks'] = ['synthetic-shared-account']
        first = self.submit('first')
        self.config['execution']['runtime'] = 'different-execution'
        self.config['grading']['runtime'] = 'different-grading'
        second = self.submit('second')
        self.advance()
        self.assertTrue((first/'execution/started').exists())
        self.assertFalse((second/'execution/started').exists())

    def test_halt_stops_paid_workers_and_cannot_auto_resume(self):
        self.init();path=self.submit('owned')
        self.advance()
        state=queue.halt(self.queue,'synthetic accounting uncertainty')
        self.assertEqual(state['phase'],'halted')
        self.assertTrue(runs.read(path/'state.json')['stop_confirmed'])
        self.assertTrue((path/'execution/model-cost.json').exists())
        with self.assertRaisesRegex(ValueError,'halted'):self.advance()

    def test_shutdown_during_poll_stops_collects_without_next_dispatch(self):
        self.init();path=self.submit('owned');self.advance()
        with patch.object(queue, 'advance') as step, patch.object(queue, 'STOP_REQUESTED', False):
            def poll(directory):
                queue.request_stop(15, None)
                return runs.read(directory/'state.json')
            step.side_effect=poll
            queue.run_loop(self.queue)
        step.assert_called_once()
        state=runs.read(self.queue/'state.json')
        self.assertEqual(state['phase'], 'halted')
        self.assertTrue(runs.read(path/'state.json')['stop_confirmed'])
        self.assertTrue((path/'execution/model-cost.json').exists())
        self.assertFalse((path/'grading/started').exists())
        self.assertAlmostEqual(state['held_usd'], 0.0000328)

    def test_shutdown_flag_forbids_paid_start(self):
        self.init();path=self.submit('pending')
        with patch.object(queue, 'STOP_REQUESTED', True): self.advance()
        self.assertFalse(path.exists())

    def test_independent_readback_gate_blocks_grading_until_frozen_release(self):
        self.init();path=self.submit('write-task',grading_gate=True)
        self.advance();self.advance();state=self.advance()
        self.assertFalse((path/'grading/started').exists())
        self.assertIn('readback',next(iter(state['dispatch_holds'].values())))
        proofs=self.root/'independent-proof';proofs.mkdir()
        runs.write(proofs/'readback.json',{'fixture':'controller readback; no service call'})
        queue.release_grading(self.queue,'write-task',proofs)
        self.advance();state=self.advance()
        self.assertEqual(state['jobs']['write-task']['phase'],'reviewed')
        self.assertTrue((path/'grading-input/controller-verification/readback.json').exists())

    def test_changed_readback_proof_never_starts_grader(self):
        self.init();path=self.submit('write-task',grading_gate=True)
        self.advance();self.advance()
        proofs=self.root/'independent-proof';proofs.mkdir()
        runs.write(proofs/'readback.json',{'fixture':'independent controller'})
        queue.release_grading(self.queue,'write-task',proofs)
        (path/'grading-input/controller-verification/readback.json').write_text('tampered')
        state=self.advance()
        self.assertEqual(state['jobs']['write-task']['phase'],'needs_attention')
        self.assertFalse((path/'grading/started').exists())

    def test_physical_identity_recognizes_aliases_in_separate_adapter_configs(self):
        adapter=str(self.root/'scripts/runners/opencode/adapter.py')
        settings=[]
        for name in ('logical-a','logical-b'):
            file=self.root/(name+'.adapter.json')
            runs.write(file,{'host':'same-ssh-host','containers':{name:'same-container'}})
            settings.append({'runtime':name,'commands':{'start':['python3',adapter,'--config',str(file),'start','{request}']}})
        self.assertEqual(queue.runtime_identity(settings[0]),queue.runtime_identity(settings[1]))

    def test_real_saved_price_ceiling_and_hash_check_without_a_model_call(self):
        path=self.root/'reservation-only';path.mkdir()
        cfg=copy.deepcopy(self.config)
        cfg['execution'].update(model='deepseek-flash',max_model_requests=40)
        cfg['execution']['commands']['start']=['python3',str(self.root/'scripts/runners/opencode/adapter.py'),'--config','/unused/private.json','start','{request}']
        runs.write(path/'config.json',cfg)
        prices=runs.read(fixtures.ROOT/'data/pricing/litellm.json')
        runs.write(path/'frozen/pricing.json',prices)
        self.assertAlmostEqual(queue.ceiling(path,'execution'),14.118912)
        prices['models']['deepseek-flash']['input_cost_per_token']=0
        runs.write(path/'frozen/pricing.json',prices)
        with self.assertRaisesRegex(ValueError,'Frozen pricing'):queue.ceiling(path,'execution')


if __name__ == '__main__': unittest.main()
