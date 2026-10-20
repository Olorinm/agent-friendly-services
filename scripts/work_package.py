"""Compile role handoffs into the existing queue using controller-owned policy.

Models supply tasks, data and approved IDs, never commands, credentials, runtime
settings or paths. This module submits frozen work; it does not run a model.
"""
import argparse
import csv
from copy import deepcopy
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
from datetime import date

import task_queue as queue
from adapter_usage import read_usage

ID = r'[a-z0-9][a-z0-9-]{0,95}'
SHA = r'[0-9a-f]{64}'
TASK_FIELDS = {'id', 'version', 'description', 'inputs', 'expected_output', 'success', 'failure',
               'material_ids', 'applicable_target_ids'}


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    raw = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    with path.open('x') as stream:
        stream.write(raw)
    path.chmod(0o600)


def identity(value):
    if not isinstance(value, str) or not re.fullmatch(ID, value):
        raise ValueError('Invalid work-package identity')
    return value


def keys(value, allowed, required):
    if not isinstance(value, dict) or set(value) - set(allowed) or set(required) - set(value):
        raise ValueError('Unexpected or missing role handoff fields')


def strings(value, *, nonempty=False):
    if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
        raise ValueError('Expected string list')
    if nonempty and not value:
        raise ValueError('Expected a nonempty string list')
    if len(value) != len(set(value)):
        raise ValueError('Duplicate role handoff entries')
    return value


def status(value):
    if value.get('status') not in ('ready', 'held'):
        raise ValueError('Role handoff must explicitly be ready or held')
    blockers = strings(value.get('blockers'))
    if (value['status'] == 'held') != bool(blockers):
        raise ValueError('Held work needs reasons; ready work cannot conceal blockers')


def regular_file(root, relative):
    if not isinstance(relative, str) or Path(relative).is_absolute() or '..' in Path(relative).parts:
        raise ValueError('Material path must stay inside its collected root')
    root = Path(root).resolve()
    path = root / relative
    if any(p.is_symlink() for p in [path, *path.parents] if p.is_relative_to(root)):
        raise ValueError('Material links are forbidden')
    if not path.is_file() or not path.resolve().is_relative_to(root):
        raise ValueError('Collected material is missing')
    return path


def collection(policy, role='material_preparation', result_path=None):
    """Verify controller binding and actual completed role activity, not model prose."""
    binding = policy['preparer_collection' if role == 'material_preparation' else 'designer_collection']
    root = Path(binding['directory']).resolve()
    receipt_path = regular_file(root, 'receipt.json')
    if not re.fullmatch(SHA, binding.get('receipt_sha256', '')) or digest(receipt_path) != binding['receipt_sha256']:
        raise ValueError('Controller preparer receipt binding changed')
    proof_path = regular_file(root, 'role-collection-proof.json')
    if not re.fullmatch(SHA, binding.get('proof_sha256', '')) or digest(proof_path) != binding['proof_sha256']:
        raise ValueError('Controller role collection proof binding changed')
    proof, receipt = read(proof_path), read(receipt_path)
    if (proof.get('role') != role or proof.get('verified') is not True
            or receipt.get('role') != role or receipt.get('exit_code') != 0
            or receipt.get('timed_out') is not False or receipt.get('input_verified') is not True):
        raise ValueError('Material preparation lacks a verified independent role receipt')
    import role_handoff
    manifest = role_handoff.verify(root.parent)
    name = role_handoff.ROLES[role]
    if (manifest['role'] != role or proof.get('native_turn_completed') is not True
            or proof.get('session_id') != receipt.get('session_id')
            or proof.get('input_files') != manifest['input_files']
            or proof.get('manifest_sha256') != digest(root.parent / 'manifest.json')
            or proof.get('receipt_sha256') != digest(receipt_path)
            or proof.get('result_sha256') != digest(regular_file(root, name))
            or digest(regular_file(root, name)) != digest(regular_file(root / 'artifacts', name))
            or result_path is not None and digest(result_path) != proof['result_sha256']):
        raise ValueError('Role result is not the bound collected model artifact')
    for name, expected in proof.get('source_sha256', {}).items():
        if digest(regular_file(root, name)) != expected:
            raise ValueError('Verified role source bytes changed')
    if set(proof.get('source_sha256', {})) != {'events.jsonl', 'session.raw.jsonl', 'usage.json'}:
        raise ValueError('Role proof lacks native source bindings')
    rows = [json.loads(line) for line in regular_file(root, 'events.jsonl').read_text().splitlines() if line.strip()]
    if (not any(x.get('type') == 'thread.started' and x.get('thread_id') == receipt.get('session_id') for x in rows)
            or not any(x.get('type') == 'turn.completed' for x in rows)
            or any(x.get('type') in ('turn.failed', 'error') for x in rows)):
        raise ValueError('Preparer native turn did not complete')
    _, usage = read_usage(root, receipt.get('model'))
    if not usage.get('requests_verified') or not any(x['output_tokens'] > 0 for x in usage['requests']):
        raise ValueError('Preparer has no verified model request activity')
    import importlib.util
    spec = importlib.util.spec_from_file_location('work_package_observed_input', Path(__file__).parent / 'runners/codex/normalize.py')
    normalizer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(normalizer)
    packet = root.parent / 'input'
    prompt = (packet / 'AGENTS.md').read_text().strip() + '\n\n' + (packet / 'prompt.txt').read_text()
    if not normalizer.observed_input(root / 'session.raw.jsonl', prompt, receipt['model'], receipt['reasoning_effort']):
        raise ValueError('Role actual model/effort/prompt differs from its frozen input')
    from session_usage import extract_usage
    final_usage = next((row.get('usage') for row in reversed(rows) if row.get('type') == 'turn.completed'), None)
    actual = extract_usage(root / 'session.raw.jsonl', final_usage)
    if actual.get('requests') != usage['requests']:
        raise ValueError('Role model requests differ from collected native usage')
    return root


def raw_data(path, rule):
    """Controller-declared record schema excludes arbitrary scripts/instructions."""
    raw = path.read_bytes()
    if len(raw) > rule.get('max_bytes', 1024 * 1024):
        raise ValueError('Generated raw material exceeds its declared size')
    text = raw.decode('utf-8')
    format = rule['format']
    if path.suffix != '.' + format or format not in ('csv', 'json', 'txt'):
        raise ValueError('Only declared raw CSV/JSON/TXT materials are supported')
    if format == 'txt':
        pattern = rule.get('line_pattern')
        if not pattern or any(not re.fullmatch(pattern, line) for line in text.splitlines()):
            raise ValueError('Raw TXT must match a controller-declared data-line schema')
        return
    columns = rule.get('columns')
    if not isinstance(columns, dict) or not columns:
        raise ValueError('Generated records need a controller-declared field schema')
    if format == 'csv':
        reader = csv.DictReader(io.StringIO(text))
        if reader.fieldnames != list(columns):
            raise ValueError('Generated CSV columns differ from declared raw inputs')
        rows = list(reader)
    else:
        rows = json.loads(text)
    if not isinstance(rows, list) or not rows:
        raise ValueError('Generated material must contain raw records')
    if len(rows) > rule.get('max_rows', 10000):
        raise ValueError('Generated material exceeds declared record count')
    for row in rows:
        if not isinstance(row, dict) or set(row) != set(columns):
            raise ValueError('Generated records contain unexpected fields')
        for name, field in columns.items():
            value = row[name]
            kind = field['type']
            if kind in ('number', 'integer'):
                try:
                    number = float(value)
                except (ValueError, TypeError):
                    raise ValueError('Generated numeric material field is invalid')
                if isinstance(value, bool) or not math.isfinite(number) or kind == 'integer' and not number.is_integer():
                    raise ValueError('Generated numeric material field is invalid')
            elif kind == 'date':
                if not isinstance(value, str) or date.fromisoformat(value).isoformat() != value:
                    raise ValueError('Generated material date is invalid')
            elif kind == 'string':
                if not isinstance(value, str) or len(value) > field.get('max_length', 256):
                    raise ValueError('Generated text material field is invalid')
                if not field.get('pattern') or not re.fullmatch(field['pattern'], value):
                    raise ValueError('Generated text must match the declared data schema')
            else:
                raise ValueError('Unsupported raw-data field type')


def register_materials(preparer, policy):
    result = {}
    declarations = preparer.get('materials', [])
    if not isinstance(declarations, list):
        raise ValueError('Preparer materials must be a manifest list')
    collected = collection(policy) if declarations else None
    approved = policy.get('generated_materials', {})
    for row in declarations:
        keys(row, ('id', 'file', 'sha256', 'bytes', 'synthetic', 'source', 'validation'), ('id', 'file', 'sha256'))
        name = identity(row['id'])
        if name in result or name not in approved:
            raise ValueError('Duplicate or unsupported generated material')
        rule = approved[name]
        if row['file'] != rule['file'] or not row['file'].startswith('materials/'):
            raise ValueError('Generated material differs from approved output location')
        path = regular_file(collected / 'artifacts', row['file'])
        if not re.fullmatch(SHA, row['sha256']) or digest(path) != row['sha256']:
            raise ValueError('Generated material hash is absent or changed')
        if 'bytes' in row and row['bytes'] != path.stat().st_size:
            raise ValueError('Generated material byte count differs from collection')
        if row.get('synthetic', True) is not True:
            raise ValueError('Only explicitly synthetic generated data is supported')
        raw_data(path, rule)
        result[name] = {'path': str(path), 'file': row['file'][len('materials/'):],
                        'sha256': row['sha256'], 'audience': 'execution', 'kind': 'raw_data'}
    for name, row in policy.get('materials', {}).items():
        identity(name)
        if name in result or row.get('audience') not in ('execution', 'grading') or row.get('kind') != 'raw_data':
            raise ValueError('Controller material declaration is invalid or duplicated')
        path = Path(row['path'])
        if path.is_symlink() or not path.is_file() or not re.fullmatch(SHA, row.get('sha256', '')) or digest(path) != row['sha256']:
            raise ValueError('Approved material bytes changed')
        result[name] = row
    return result


def validate(designer, preparer, policy, designer_sha256):
    keys(designer, ('schema_version', 'role', 'status', 'blockers', 'package_id', 'tasks', 'material_requirements', 'demand_sources', 'applicability'),
         ('schema_version', 'status', 'blockers', 'package_id', 'tasks'))
    keys(preparer, ('schema_version', 'role', 'status', 'blockers', 'package_id', 'designer_sha256', 'assignments', 'materials', 'references', 'resource_prerequisites', 'frozen_dates'),
         ('schema_version', 'status', 'blockers', 'package_id', 'designer_sha256', 'assignments'))
    if designer['schema_version'] != 1 or preparer['schema_version'] != 1:
        raise ValueError('Unsupported work-package schema')
    if designer.get('role', 'task_design') != 'task_design' or preparer.get('role', 'material_preparation') != 'material_preparation':
        raise ValueError('Role result has the wrong role identity')
    package = identity(designer['package_id'])
    if preparer['package_id'] != package or preparer['designer_sha256'] != designer_sha256:
        raise ValueError('Preparer output does not bind this designer handoff')
    status(designer)
    status(preparer)
    tasks = {}
    targets = policy['targets']
    rounds = policy.get('rounds')
    if (not isinstance(rounds, list) or not rounds or len(rounds) != len(set(rounds))
            or any(type(n) is not int or n < 1 for n in rounds)):
        raise ValueError('Controller must declare distinct positive trial rounds')
    materials = register_materials(preparer, policy)
    requirements = designer.get('material_requirements', [])
    if not isinstance(requirements, list):
        raise ValueError('Material requirements must be a list')
    required_ids = set()
    for item in requirements:
        keys(item, ('id', 'format', 'description', 'synthetic'), ('id', 'format', 'description', 'synthetic'))
        name = identity(item['id'])
        rule = policy.get('generated_materials', {}).get(name)
        if name in required_ids or not rule or item['format'] != rule['format'] or item['synthetic'] is not True:
            raise ValueError('Undeclared or duplicate synthetic material requirement')
        required_ids.add(name)
    if not isinstance(designer['tasks'], list) or (not designer['tasks'] and not any(x['status'] == 'held' for x in (designer, preparer))):
        raise ValueError('Designer must declare tasks')
    for task in designer['tasks']:
        keys(task, TASK_FIELDS | {'demand_sources', 'applicability'}, TASK_FIELDS)
        name = identity(task['id'])
        if name in tasks:
            raise ValueError('Duplicate task identity')
        for field in ('version', 'description', 'inputs', 'expected_output', 'success', 'failure'):
            if not isinstance(task[field], str) or not task[field].strip() or len(task[field]) > 20000:
                raise ValueError('Task metadata must be nonempty bounded text')
        for material in strings(task['material_ids']):
            if (material not in materials and material not in policy.get('generated_materials', {})
                    or material in materials and materials[material]['audience'] != 'execution'):
                raise ValueError('Unsupported or grading-only material cannot enter execution')
        for target in strings(task['applicable_target_ids'], nonempty=True):
            if target not in targets:
                raise ValueError('Unsupported candidate target')
        tasks[name] = task
    declared = set()
    for row in preparer['assignments']:
        keys(row, ('task_id', 'target_id', 'round', 'status', 'blockers'), ('task_id', 'target_id', 'round', 'status', 'blockers'))
        status(row)
        if row['task_id'] not in tasks or row['target_id'] not in tasks[row['task_id']]['applicable_target_ids']:
            raise ValueError('Undeclared or unsupported task/service assignment')
        key = (row['task_id'], row['target_id'], row['round'])
        if type(row['round']) is not int or row['round'] not in policy['rounds'] or key in declared:
            raise ValueError('Duplicate or unsupported trial round')
        if row['status'] == 'ready' and not any(x['status'] == 'held' for x in (designer, preparer)):
            if any(name not in materials for name in tasks[row['task_id']]['material_ids']):
                raise ValueError('Ready assignment lacks its declared original material')
        declared.add(key)
    expected = {(task['id'], target, number) for task in tasks.values()
                for target in task['applicable_target_ids'] for number in policy['rounds']}
    if declared != expected:
        raise ValueError('Preparer must explicitly ready or hold every declared trial slot')
    ready_targets = {row['target_id'] for row in preparer['assignments'] if row['status'] == 'ready'}
    execution = {queue.runtime_identity(targets[name]['config']['execution']) for name in ready_targets}
    grading = {queue.runtime_identity(targets[name]['config']['grading']) for name in ready_targets}
    if execution.intersection(grading):
        raise ValueError('Execution and grading containers must be separate across the whole package')
    return {'package_id': package, 'tasks': tasks, 'materials': materials, 'assignments': preparer['assignments'],
            'held': designer['status'] == 'held' or preparer['status'] == 'held',
            'blockers': designer['blockers'] + preparer['blockers']}


def markdown(tasks):
    fields = ('id', 'description', 'inputs', 'expected_output', 'success', 'failure', 'version')
    escape = lambda value: value.replace('\\', '\\\\').replace('|', r'\|').replace('\r', '').replace('\n', '<br>')
    return ('| ID | 用户任务 | 预计输入 | 预计输出 | 完成标准 | 未完成标准 | 版本 |\n'
            '| --- | --- | --- | --- | --- | --- | --- |\n'
            + ''.join('| ' + ' | '.join(escape(task[key]) for key in fields) + ' |\n' for task in tasks.values()))


def submit_package(queue_dir, designer_path, preparer_path, policy_path, output_dir):
    queue_dir, output = Path(queue_dir).resolve(), Path(output_dir).resolve()
    sources = {name: digest(path) for name, path in [('designer', designer_path), ('preparer', preparer_path), ('policy', policy_path)]}
    designer, preparer, policy = read(designer_path), read(preparer_path), read(policy_path)
    plan = validate(designer, preparer, policy, sources['designer'])
    designed_output = collection(policy, 'task_design', designer_path)
    prepared_output = collection(policy, 'material_preparation', preparer_path)
    if read(designed_output / 'receipt.json')['session_id'] == read(prepared_output / 'receipt.json')['session_id']:
        raise ValueError('Design and preparation need separate fresh role sessions')
    if sources != {name: digest(path) for name, path in [('designer', designer_path), ('preparer', preparer_path), ('policy', policy_path)]}:
        raise ValueError('Role handoff or controller policy changed during validation')
    references = []
    for item in preparer.get('references', []):
        keys(item, ('path', 'sha256', 'bytes', 'source', 'purpose'), ('path', 'sha256', 'bytes', 'source', 'purpose'))
        if not item['path'].startswith('references/'):
            raise ValueError('Independent references must stay outside execution materials')
        source = regular_file(prepared_output / 'artifacts', item['path'])
        if not re.fullmatch(SHA, item['sha256']) or digest(source) != item['sha256'] or source.stat().st_size != item['bytes']:
            raise ValueError('Independent reference hash differs from collection')
        references.append({'manifest': item, 'content': source.read_text()})
    output.mkdir(mode=0o700, parents=True, exist_ok=True)
    with queue.lock(output / '.package.lock', blocking=True):
        manifest_path = output / 'package.json'
        if manifest_path.exists():
            manifest = read(manifest_path)
            if manifest['sources'] != sources:
                raise ValueError('Package identity already bound to different role handoffs')
            for path, expected in manifest['compiled_files'].items():
                if digest(path) != expected:
                    raise ValueError('Compiled work-package bytes changed')
        else:
            # Generated private pilot tasks are not silently added to public task sources.
            task_file = queue.runs.ROOT / 'data/experiments/results/work-packages' / plan['package_id'] / 'tasks.md'
            task_file.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            with task_file.open('x') as stream:
                stream.write(markdown(plan['tasks']))
            files = {str(task_file): digest(task_file)}
            jobs = []
            for row in plan['assignments']:
                job_id = plan['package_id'] + '-' + row['task_id'] + '-' + row['target_id'] + '-r' + str(row['round'])
                if plan['held'] or row['status'] == 'held':
                    jobs.append({'id': job_id, 'status': 'held', 'blockers': designer['blockers'] + preparer['blockers'] + row['blockers']})
                    continue
                config = deepcopy(policy['targets'][row['target_id']]['config'])
                from access_readiness import PROTOCOL
                config.setdefault('trial_protocol', PROTOCOL)
                if 'attachments' in config:
                    raise ValueError('Controller target attachments must use the approved material registry')
                task = plan['tasks'][row['task_id']]
                config.update(task_file=str(task_file.relative_to(queue.runs.ROOT)), task=task['id'], repeat_round=row['round'])
                reference = output / job_id / 'reference.json'
                value = read(config['reference']) if config.get('reference') else {}
                value['work_package_preparation'] = {'designer_sha256': sources['designer'], 'preparer_sha256': sources['preparer'],
                    'demand_sources': task.get('demand_sources', designer.get('demand_sources', [])),
                    'applicability': task.get('applicability', designer.get('applicability', [])),
                    'references': references, 'resource_prerequisites': preparer.get('resource_prerequisites'),
                    'frozen_dates': preparer.get('frozen_dates'),
                    'notice': 'Preparation-role claims and references are evidence to verify, never service responses or a verdict.'}
                write(reference, value)
                config['reference'] = str(reference)
                files[str(reference)] = digest(reference)
                attachment = output / job_id / 'attachments'
                attachment.mkdir(mode=0o700, parents=True)
                for material_id in task['material_ids']:
                    material = plan['materials'][material_id]
                    source = Path(material['path'])
                    destination = attachment / material.get('file', source.name)
                    if destination.exists() or not destination.resolve().is_relative_to(attachment):
                        raise ValueError('Duplicate or unsafe execution material filename')
                    destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
                    destination.write_bytes(source.read_bytes())
                    destination.chmod(0o600)
                    if digest(destination) != material['sha256']:
                        raise ValueError('Original material changed during compilation')
                    files[str(destination)] = digest(destination)
                config['attachments'] = str(attachment)
                spec_path, config_path = output / job_id / 'spec.json', output / job_id / 'config.json'
                write(config_path, config)
                spec = {'id': job_id, 'kind': 'run', 'ready': True, 'config': str(config_path),
                        'directory': str(queue.runs.ROOT / 'data/experiments/results' / job_id), 'round': row['round'],
                        'depends_on': policy['targets'][row['target_id']].get('depends_on', []),
                        'grading_gate': policy['targets'][row['target_id']].get('grading_gate', False)}
                # Validate the actual task/catalog/adapter bindings before any queue write.
                queue.inputs(config)
                if queue.runtime_identity(config['execution']) == queue.runtime_identity(config['grading']):
                    raise ValueError('Execution and grading containers must be separate')
                write(spec_path, spec)
                files.update({str(config_path): digest(config_path), str(spec_path): digest(spec_path)})
                jobs.append({'id': job_id, 'status': 'compiled', 'spec': str(spec_path)})
            manifest = {'schema_version': 1, 'package_id': plan['package_id'], 'sources': sources,
                        'status': 'held' if plan['held'] else 'ready', 'blockers': plan['blockers'],
                        'compiled_files': files, 'jobs': jobs}
            write(manifest_path, manifest)
        for job in manifest['jobs']:
            if job['status'] == 'held':
                continue
            inbox = queue_dir / 'inbox' / job['id']
            if inbox.exists():
                handoff = read(inbox / 'handoff.json')
                spec = read(job['spec'])
                if (digest(inbox / 'handoff.json') != read(inbox / 'ready.json')['sha256']
                        or len(handoff['members']) != 1
                        or handoff['members'][0]['config'] != read(spec['config'])
                        or handoff['members'][0]['directory'] != spec['directory']):
                    raise ValueError('Existing queued identity differs; never duplicate or overwrite it')
            else:
                queue.submit(queue_dir, job['spec'])
        return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--queue', type=Path, required=True)
    parser.add_argument('--designer', type=Path, required=True)
    parser.add_argument('--preparer', type=Path, required=True)
    parser.add_argument('--policy', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = submit_package(args.queue, args.designer, args.preparer, args.policy, args.output)
    print(json.dumps({'package_id': result['package_id'], 'jobs': result['jobs']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
