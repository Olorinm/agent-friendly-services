import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import grading_packet

spec = importlib.util.spec_from_file_location('opencode_tool_records', ROOT / 'scripts/runners/opencode/tool_records.py')
records = importlib.util.module_from_spec(spec)
spec.loader.exec_module(records)


class GradingPacketTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.output = self.root / 'execution'
        self.output.mkdir()
        self.grade = self.root / 'grading-input'
        self.grade.mkdir()
        (self.grade / 'task.json').write_text('{"success":"Actual business result"}')
        (self.grade / 'reference.json').write_text('{"independent":"reference"}')

    def log(self, state):
        (self.output / 'events.jsonl').write_text(json.dumps({
            'type': 'tool_use', 'part': {'tool': 'bash', 'callID': 'call-1', 'state': state}}) + '\n')

    def test_full_private_records_preserve_errors_and_mark_preview_truncation(self):
        state = {'status': 'error', 'input': {'command': 'read-only fixture request'},
                 'error': 'Denied: ' + 'x' * 6000}
        self.log(state)
        result = records.extract(self.output)
        self.assertEqual(result['calls'][0]['state'], state)
        index = grading_packet.build(self.root)
        tool = index['tools'][0]
        self.assertTrue(index['tool_capture']['source_sha256_verified'])
        self.assertEqual(tool['status'], 'error')
        self.assertTrue(tool['output']['truncated'])
        full = json.loads((self.grade / tool['path']).read_text())
        self.assertEqual(full['state'], state)
        self.assertEqual(full['source']['line'], 1)
        template = json.loads((self.grade / 'assessment.template.json').read_text())
        self.assertIsNone(template['status'])
        self.assertEqual(template['evidence'], [])
        self.assertIsNone(template['service_cost_usd'])
        self.assertEqual(index['references'][0]['path'], 'reference.json')

    def test_partial_or_missing_capture_is_not_described_as_complete(self):
        (self.output / 'events.jsonl').write_text('{invalid}\n' + json.dumps({'type': 'tool_use'}) + '\n')
        result = records.extract(self.output)
        self.assertFalse(result['complete'])
        index = grading_packet.build(self.root)
        self.assertFalse(index['tool_capture']['complete'])
        self.assertEqual(len(index['tool_capture']['errors']), 2)

    def test_changed_original_log_rejects_normalized_records(self):
        self.log({'status': 'completed', 'input': {}, 'output': 'ok'})
        records.extract(self.output)
        (self.output / 'events.jsonl').write_text('changed')
        with self.assertRaisesRegex(ValueError, 'original source'):
            grading_packet.build(self.root)

    def test_no_adapter_records_falls_back_without_guessing_success(self):
        index = grading_packet.build(self.root)
        self.assertFalse(index['tool_capture']['complete'])
        self.assertIn('original session', index['tool_capture']['reason'])
        self.assertEqual(index['tools'], [])

    def test_grader_relative_evidence_resolves_only_to_exact_captured_files(self):
        output = self.root / 'grading'
        artifacts = output / 'artifacts'
        artifacts.mkdir(parents=True)
        (artifacts / 'reference.json').write_text('{"fixture":"reference"}')
        value = {'status': 'not_completed', 'reason': 'Missing item', 'service_cost_usd': None,
                 'evidence': [{'path': 'reference.json'}, {'path': 'missing.json'}, {'path': '../escape'}]}
        assessment = output / 'assessment.json'
        assessment.write_text(json.dumps(value))
        raw = assessment.read_bytes()
        changes = grading_packet.resolve_evidence_paths(self.root)
        actual = json.loads(assessment.read_text())
        self.assertEqual(len(changes), 1)
        self.assertEqual(actual['evidence'][0]['path'], 'grading/artifacts/reference.json')
        self.assertEqual(actual['evidence'][1:], value['evidence'][1:])
        self.assertEqual(actual['status'], value['status'])
        self.assertEqual(actual['reason'], value['reason'])
        self.assertIsNone(actual['service_cost_usd'])
        self.assertEqual((output / 'assessment.raw.json').read_bytes(), raw)
        self.assertEqual(grading_packet.resolve_evidence_paths(self.root), [])


if __name__ == '__main__':
    unittest.main()
