"""One local contract for the two producer outputs and their frozen JSON schema.

Only the small schema vocabulary emitted here is interpreted. This is not a
loader for model-supplied schemas; dispatch/admission semantics stay in the
existing work-package consumer.
"""
from copy import deepcopy
import json
import math
import re

ID = r'^[a-z0-9][a-z0-9-]{0,95}$'
SHA = r'^[0-9a-f]{64}$'


def schema(role):
    text = {'type': 'string', 'minLength': 1, 'pattern': r'\S'}
    identity = {'type': 'string', 'pattern': ID}
    digest = {'type': 'string', 'pattern': SHA}
    strings = {'type': 'array', 'items': text, 'uniqueItems': True}
    metadata = {'description': 'Private descriptive JSON only; cannot supply dispatch authority.'}

    def obj(properties, required):
        return {'type': 'object', 'properties': properties, 'required': list(required), 'additionalProperties': False}

    common = {'schema_version': {'type': 'integer', 'const': 1},
              'role': {'type': 'string', 'const': role},
              'status': {'type': 'string', 'enum': ['ready', 'held']},
              'blockers': strings, 'package_id': identity}
    if role == 'task_design':
        task = {key: {**text, 'maxLength': 20000} for key in
                ('version', 'description', 'inputs', 'expected_output', 'success', 'failure')}
        task.update(id=identity, material_ids=strings,
                    applicable_target_ids={**strings, 'minItems': 1}, demand_sources=metadata, applicability=metadata)
        required = ('id', 'version', 'description', 'inputs', 'expected_output', 'success', 'failure',
                    'material_ids', 'applicable_target_ids')
        common.update(tasks={'type': 'array', 'items': obj(task, required)},
                      material_requirements={'type': 'array', 'items': obj({
                          'id': identity, 'format': {'type': 'string', 'enum': ['csv', 'json', 'txt']},
                          'description': text, 'synthetic': {'type': 'boolean', 'const': True}},
                          ('id', 'format', 'description', 'synthetic'))},
                      demand_sources=metadata, applicability=metadata)
        required = ('schema_version', 'status', 'blockers', 'package_id', 'tasks')
    elif role == 'material_preparation':
        common.update(designer_sha256=digest,
            assignments={'type': 'array', 'items': obj({
                'task_id': identity, 'target_id': text, 'round': {'type': 'integer', 'minimum': 1},
                'status': common['status'], 'blockers': strings},
                ('task_id', 'target_id', 'round', 'status', 'blockers'))},
            materials={'type': 'array', 'items': obj({
                'id': identity, 'file': {**text, 'pattern': r'^materials/.+\.(csv|json|txt)$'},
                'sha256': digest, 'bytes': {'type': 'integer', 'minimum': 0},
                'synthetic': {'type': 'boolean', 'const': True}, 'source': metadata, 'validation': metadata},
                ('id', 'file', 'sha256'))},
            references={'type': 'array', 'items': obj({
                'path': {**text, 'pattern': r'^references/.+'}, 'sha256': digest,
                'bytes': {'type': 'integer', 'minimum': 0}, 'source': metadata, 'purpose': metadata},
                ('path', 'sha256', 'bytes', 'source', 'purpose'))},
            resource_prerequisites=metadata, frozen_dates=metadata)
        required = ('schema_version', 'status', 'blockers', 'package_id', 'designer_sha256', 'assignments')
    else:
        raise ValueError('Unsupported producer output role')
    return {'$schema': 'https://json-schema.org/draft/2020-12/schema',
            'title': role + ' output v1', **deepcopy(obj(common, required))}


def validate(role, value):
    """Check the exact emitted contract, reporting the offending JSON location."""
    def visit(rule, item, path):
        def fail(message): raise ValueError(path + ': ' + message)
        kind = rule.get('type')
        matches = {'object': isinstance(item, dict), 'array': isinstance(item, list),
                   'string': isinstance(item, str), 'integer': type(item) is int,
                   'boolean': type(item) is bool}
        if kind and not matches[kind]: fail('Expected ' + kind)
        if 'const' in rule and (type(item) is not type(rule['const']) or item != rule['const']): fail('Unsupported value')
        if 'enum' in rule and item not in rule['enum']: fail('Unsupported value')
        if kind == 'object':
            extra = set(item) - set(rule['properties'])
            if extra: raise ValueError(path+'.'+sorted(extra)[0]+': Unexpected role handoff field')
            missing = set(rule['required']) - set(item)
            if missing: raise ValueError(path+'.'+sorted(missing)[0]+': Missing role handoff field')
            for key, child in item.items(): visit(rule['properties'][key], child, path+'.'+key)
        elif kind == 'array':
            if len(item) < rule.get('minItems', 0): fail('Expected a nonempty list')
            if rule.get('uniqueItems') and len(item) != len({json.dumps(x, sort_keys=True) for x in item}): fail('Duplicate role handoff entries')
            for i, child in enumerate(item): visit(rule['items'], child, path+'['+str(i)+']')
        elif kind == 'string':
            if len(item) < rule.get('minLength', 0) or len(item) > rule.get('maxLength', float('inf')): fail('Invalid text length')
            if 'pattern' in rule and not re.search(rule['pattern'], item): fail('Invalid text format')
        elif kind == 'integer' and item < rule.get('minimum', item): fail('Integer below minimum')
        elif not kind:
            # Descriptive metadata may be any real JSON value, including objects.
            def finite(child):
                if isinstance(child, float) and not math.isfinite(child): fail('Non-finite JSON number')
                if isinstance(child, dict):
                    for value in child.values(): finite(value)
                elif isinstance(child, list):
                    for value in child: finite(value)
            finite(item)
            try: json.dumps(item, allow_nan=False)
            except (TypeError, ValueError): fail('Descriptive metadata must be JSON')
    visit(schema(role), value, '$')
