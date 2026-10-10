import concurrent.futures
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts/runners/opencode'))
from request_limits import RequestLimits


class LimitsTest(unittest.TestCase):
    def test_request_closure_warning_is_forwarded_once_without_changing_hard_cap(self):
        warnings=[]
        limits=RequestLimits('deepseek-flash',20,warning_callback=warnings.append)
        for _ in range(16): limits.reserve({'model':'deepseek-flash','messages':[]})
        payload={'model':'deepseek-flash','messages':[{'role':'system','content':'frozen role'},{'role':'user','content':'original task'}]}
        limits.reserve(payload)
        self.assertIn('final budget portion',payload['messages'][0]['content'])
        self.assertEqual(payload['messages'][1]['content'],'original task')
        self.assertEqual(warnings[0]['remaining_requests'],3)
        for _ in range(3): limits.reserve({'model':'deepseek-flash','messages':[]})
        self.assertEqual(len(warnings),1)
        with self.assertRaisesRegex(ValueError,'exhausted'): limits.reserve({'model':'deepseek-flash'})

    def test_time_warning_on_next_request_even_when_request_count_is_low(self):
        limits=RequestLimits('deepseek-flash',100,deadline=100,started_at=0)
        first={'model':'deepseek-flash','messages':[]};limits.reserve(first,now=84)
        self.assertEqual(first['messages'],[])
        last={'model':'deepseek-flash','messages':[]};limits.reserve(last,now=85)
        self.assertIn('final budget portion',last['messages'][0]['content'])
        with self.assertRaisesRegex(ValueError,'deadline'): limits.reserve({'model':'deepseek-flash'},now=100)

    def test_concurrent_attempts_cannot_exceed_reservation(self):
        limits=RequestLimits('deepseek-flash',25)
        def reserve(_):
            try:return limits.reserve({'model':'deepseek-flash'})
            except ValueError:return None
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
            results=list(pool.map(reserve,range(100)))
        self.assertEqual(sorted(x for x in results if x),list(range(1,26)))

    def test_restart_preserves_paid_attempt_count(self):
        limits=RequestLimits('deepseek-flash',25,used=25)
        with self.assertRaisesRegex(ValueError,'exhausted'):
            limits.reserve({'model':'deepseek-flash'})

    def test_model_and_deadline_fail_before_paid_forward(self):
        limits=RequestLimits('deepseek-flash',25,deadline=100)
        with self.assertRaisesRegex(ValueError,'model'):
            limits.reserve({'model':'different'},now=99)
        with self.assertRaisesRegex(ValueError,'deadline'):
            limits.reserve({'model':'deepseek-flash'},now=100)
        self.assertEqual(limits.used,0)

    def test_output_cost_bound_and_default(self):
        limits=RequestLimits('deepseek-flash',25,max_output_tokens=32000)
        for field in ('max_tokens','max_completion_tokens'):
            with self.assertRaisesRegex(ValueError,'Output'):
                limits.reserve({'model':'deepseek-flash',field:32001})
        payload={'model':'deepseek-flash'}
        limits.reserve(payload)
        self.assertEqual(payload['max_tokens'],32000)
        self.assertEqual(limits.used,1)

    def test_multiple_completions_cannot_bypass_reserved_output_cost(self):
        limits=RequestLimits('deepseek-flash',25,max_output_tokens=32000)
        with self.assertRaisesRegex(ValueError,'one completion'):
            limits.reserve({'model':'deepseek-flash','n':2})
        self.assertEqual(limits.used,0)


if __name__=='__main__':unittest.main()
