"""The frozen machine contract matches strict consumption, including held work."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import role_contract


class RoleContractTests(unittest.TestCase):
    def prep(self):
        return {'schema_version': 1, 'role': 'material_preparation', 'status': 'held',
            'blockers': ['Official applicability remains unknown'], 'package_id': 'fixture',
            'designer_sha256': 'a'*64, 'assignments': [{'task_id': 'task', 'target_id': 'target', 'round': 1,
                'status': 'held', 'blockers': ['Independent scope evidence missing']}],
            'materials': [{'id': 'raw-data', 'file': 'materials/data.csv', 'sha256': 'b'*64, 'bytes': 10,
                'synthetic': True, 'source': {'method': 'synthetic'},
                'validation': {'csv_parsed': True, 'rows': 1, 'media_review': None}}],
            'resource_prerequisites': {'authorization': 'unknown'}, 'frozen_dates': {'prepared': None}}

    def test_real_structured_validation_and_unknowns_remain_valid(self):
        role_contract.validate('material_preparation', self.prep())

    def test_unsupported_fields_report_the_exact_json_location(self):
        examples = [(['validation'], {}), (['assignments', 0, 'task_version'], 'v1'),
                    (['materials', 0, 'shared_version'], 'shared-v1'),
                    (['materials', 0, 'shared_assignments'], ['task/target/1'])]
        for path, value in examples:
            payload = self.prep(); parent = payload
            for part in path[:-1]: parent = parent[part]
            parent[path[-1]] = value
            expected = '$'+''.join('['+str(p)+']' if isinstance(p, int) else '.'+p for p in path)
            with self.subTest(path=path), self.assertRaises(ValueError) as caught:
                role_contract.validate('material_preparation', payload)
            self.assertIn(expected, str(caught.exception))

    def test_blockers_objects_bool_rounds_and_bool_sizes_are_not_accepted(self):
        for mutate, location in [(lambda p: p.update(blockers=[{'kind': 'materials', 'reason': 'unknown'}]), '$.blockers[0]'),
                (lambda p: p['assignments'][0].update(round=True), '$.assignments[0].round'),
                (lambda p: p['materials'][0].update(bytes=True), '$.materials[0].bytes')]:
            payload = self.prep(); mutate(payload)
            with self.assertRaises(ValueError) as caught: role_contract.validate('material_preparation', payload)
            self.assertIn(location, str(caught.exception))

    def test_emitted_json_schemas_compile_and_agree_with_consumer_on_real_shapes(self):
        design = {'schema_version': 1, 'status': 'held', 'blockers': ['Not ready'], 'package_id': 'fixture', 'tasks': []}
        cases = [('material_preparation', self.prep(), True), ('task_design', design, True)]
        bad = deepcopy(self.prep()); bad['validation'] = {}; cases.append(('material_preparation', bad, False))
        code = '''const Ajv=require('ajv/dist/2020');const fs=require('fs');const rows=JSON.parse(fs.readFileSync(0,'utf8'));const ajv=new Ajv({strict:true});for(const row of rows){const check=ajv.compile(row.schema);if(check(row.value)!==row.expected)throw new Error(JSON.stringify(check.errors));}'''
        value = [{'schema': role_contract.schema(role), 'value': payload, 'expected': expected} for role, payload, expected in cases]
        subprocess.run(['node', '-e', code], input=json.dumps(value), text=True, cwd=ROOT, check=True, capture_output=True)
