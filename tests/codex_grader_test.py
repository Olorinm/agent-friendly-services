import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from adapter_usage import read_usage


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT/relative)
    value = importlib.util.module_from_spec(spec); spec.loader.exec_module(value)
    return value


normalizer = module('codex_grader_normalizer', 'scripts/runners/codex/normalize.py')
configurer = module('codex_grader_configuration', 'scripts/runners/codex/configure-grading.py')


class CodexGraderTests(unittest.TestCase):
    def test_actual_model_effort_and_full_prompt_are_required(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)/'session.raw.jsonl'
            rows = [{'type': 'turn_context', 'payload': {'model': 'gpt-6.1-sol', 'effort': 'high'}},
                    {'type': 'response_item', 'payload': {'role': 'user', 'content': [{'text': 'role\n\nfull frozen prompt'}]}}]
            p.write_text('\n'.join(json.dumps(r) for r in rows))
            self.assertTrue(normalizer.observed_input(p, 'role\n\nfull frozen prompt', 'gpt-6.1-sol', 'high'))
            self.assertFalse(normalizer.observed_input(p, 'different prompt', 'gpt-6.1-sol', 'high'))
            self.assertFalse(normalizer.observed_input(p, 'role', 'gpt-6-sol', 'high'))
            self.assertFalse(normalizer.observed_input(p, 'role', 'gpt-6.1-sol', 'medium'))

    def test_rollout_usage_reconciles_and_source_tampering_is_rejected(self):
        usage = {'input_tokens': 100, 'cached_input_tokens': 60, 'cache_write_input_tokens': 0,
                 'output_tokens': 20, 'reasoning_output_tokens': 5}
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)/'session.raw.jsonl'
            p.write_text(json.dumps({'type': 'token_usage_record', 'payload': {'response_id': 'response-1', 'usage': usage}})+'\n')
            normalizer.normalize(directory, 'gpt-6.1-sol', usage)
            totals, detail = read_usage(directory, 'gpt-6.1-sol')
            self.assertEqual(totals, usage); self.assertEqual(detail['status'], 'complete')
            p.write_text('{}\n')
            totals, detail = read_usage(directory, 'gpt-6.1-sol')
            self.assertIsNone(totals); self.assertFalse(detail.get('requests_verified', False))

    def test_missing_final_usage_remains_unknown(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)/'session.raw.jsonl'
            p.write_text(json.dumps({'type': 'token_usage_record', 'payload': {'response_id': 'response-1',
                'usage': {'input_tokens': 20, 'cached_input_tokens': 0, 'output_tokens': 5}}})+'\n')
            normalizer.normalize(directory, 'gpt-6.1-sol', None)
            totals, detail = read_usage(directory, 'gpt-6.1-sol')
            self.assertIsNone(totals); self.assertEqual(detail['status'], 'incomplete')

    def test_adjusted_session_counters_do_not_claim_a_verified_lower_bound(self):
        with tempfile.TemporaryDirectory() as directory:
            usage = {'input_tokens': 20, 'cached_input_tokens': 0, 'output_tokens': 5}
            p = Path(directory)/'session.raw.jsonl'
            p.write_text(json.dumps({'type': 'event_msg', 'payload': {'type': 'token_count', 'info': {
                'total_token_usage': {**usage, 'input_tokens': 30}, 'last_token_usage': usage}}})+'\n')
            normalizer.normalize(directory, 'gpt-6.1-sol', None)
            totals, detail = read_usage(directory, 'gpt-6.1-sol')
            self.assertIsNone(totals); self.assertFalse(detail.get('requests_verified', False))

    def test_new_configuration_preserves_execution_and_does_not_rewrite_source(self):
        source = {'execution': {'runtime': 'deepseek-exec', 'model': 'deepseek-flash', 'seconds': 600},
                  'grading': {'model': 'deepseek-flash'}, 'trial_protocol': 'old-protocol'}
        result = configurer.configure(source, '/private/codex-adapter.json', 'codex-grade')
        self.assertEqual(result['execution'], source['execution'])
        self.assertEqual(source['grading']['model'], 'deepseek-flash')
        self.assertEqual(result['grading']['model'], 'gpt-6.1-sol')
        self.assertEqual(result['grading']['billing_mode'], 'chatgpt')
        self.assertNotIn('max_model_requests', result['grading'])
        with self.assertRaises(ValueError): configurer.configure(source, '/private/adapter.json', 'deepseek-exec')


if __name__ == '__main__': unittest.main()
