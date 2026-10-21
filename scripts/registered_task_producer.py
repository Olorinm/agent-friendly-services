#!/usr/bin/env python3
"""Prepare approved registry tasks continuously; preserve their original task hashes.

The material role is native Codex, never a fabricated designer. Base libraries and
active runner source remain in --base-source-root; this controller has its own hash.
"""
import argparse
from copy import deepcopy
import importlib
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time

B = None
STOP = False
TERMINAL = {'submitted', 'held'}


def libraries(base):
    global B
    base = Path(base).resolve(); sys.path.insert(0, str(base/'scripts'))
    names = ('pipeline', 'task_queue', 'role_handoff', 'work_package', 'role_contract', 'preparation_context', 'admission', 'route_cooldown')
    loaded = {name: importlib.import_module(name) for name in names}
    if any(Path(module.__file__).resolve().parent != base/'scripts' for module in loaded.values()):
        raise ValueError('Mixed base libraries; use a fresh process with the explicit base source root')
    B = type('Base', (), loaded | {'root': base})
    return B


def role_job(root):
    root = Path(root)
    return root/('prep-'+hashlib.sha256(str(root.resolve()).encode()).hexdigest()[:12]+'-'+root.name)


def write(path, value):
    path = Path(path); path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    raw = json.dumps(value, ensure_ascii=False, indent=2)+'\n'
    if path.exists():
        if path.read_text() != raw: raise ValueError('Immutable producer output changed: '+str(path))
    else:
        with path.open('x') as stream: stream.write(raw)
        path.chmod(0o600)


def source(path, hashes):
    path = B.preparation_context.regular(path); hashes[str(path)] = B.pipeline.digest(path)
    return path


def current_task(item):
    relative = Path(item['task_file'])
    if relative.is_absolute() or '..' in relative.parts: raise ValueError('Registered task path must stay in the base registry')
    path = B.pipeline.ROOT/relative
    if not path.resolve().is_relative_to(B.pipeline.ROOT.resolve()) or path.is_symlink(): raise ValueError('Registered task source escapes the base registry')
    task, _ = B.pipeline.module('registered_task_parser', 'codex-service-trial.py').select_task(path, item['task_id'])
    if task['sha256'] != item['task_sha256']: raise ValueError('Registered task SHA changed')
    return task


def bind_settings(path, deadline, hashes, preparation=False):
    settings = B.pipeline.read(source(path, hashes))
    if settings.get('deadline_epoch') != deadline: raise ValueError('Role must share the absolute deadline')
    if preparation:
        if settings.get('reasoning_effort') != 'medium': raise ValueError('Preparation requires Sol medium')
        binding = B.role_handoff.settings_binding(settings)
        hashes[binding['adapter_file']] = binding['adapter_sha256']
    else:
        if not B.task_queue.chatgpt_grader(settings): raise ValueError('Approved independent Codex grading pool required')
        adapter = B.task_queue.adapter_config(settings); hashes[str(adapter)] = B.pipeline.digest(adapter)
    return settings


def envelope(plan):
    q = B.task_queue; r = B.pipeline; queue_dir = Path(plan['queue']); policy = r.read(queue_dir/'policy.json')
    if (policy['max_concurrency'] > 10 or policy['max_concurrency']+2 > 12
            or q.stamp(policy['expires_at']) != plan['deadline_epoch']):
        raise ValueError('Live queue no longer fits the two-worker concurrency/deadline envelope')
    owner_path = queue_dir/'.registered-producer-owner.json'
    if owner_path.exists() and r.read(owner_path).get('directory') != plan.get('producer_directory'):
        raise ValueError('Queue already belongs to another registered preparation producer')
    prep = {q.runtime_identity(r.read(path)) for path in plan['preparation_settings']}
    handoffs = [r.read(path) for path in (queue_dir/'inbox').glob('*/handoff.json')]
    handoffs.extend(job['handoff'] for job in r.read(queue_dir/'state.json').get('jobs', {}).values())
    for handoff in handoffs:
        for member in handoff['members']:
            if any(q.runtime_identity(member['config'][role]) in prep for role in ('execution', 'grading')):
                raise ValueError('Preparation physical runtime overlaps an existing frozen queue owner')
    return policy


def advance_role(job, plan, halt=False):
    # Only prepared can allocate a model; collection/stopping must remain possible
    # even when a changed policy blocks every new allocation.
    state = B.pipeline.read(job/'state.json')
    if not halt and state['phase'] == 'prepared':
        with B.task_queue.lock(Path(plan['queue'])/'.gate.lock', blocking=True):
            envelope(plan)
            return B.role_handoff.advance(job)
    return B.role_handoff.advance(job, halt=halt)


def init(directory, plan_path, base_source_root):
    libraries(base_source_root); r = B.pipeline; q = B.task_queue
    plan = r.read(plan_path); plan['producer_directory'] = str(Path(directory).resolve()); policy = r.read(Path(plan['queue'])/'policy.json')
    if (plan.get('schema_version') != 1 or plan.get('max_preparation_concurrency') != 2
            or len(plan.get('preparation_settings', [])) != 2 or plan.get('max_total_concurrency') != 12
            or policy['max_concurrency'] > 10 or policy['max_concurrency']+2 > 12
            or q.stamp(policy['expires_at']) != plan.get('deadline_epoch')):
        raise ValueError('Two preparation workers and queue must fit one12session/deadline envelope')
    with q.lock(Path(plan['queue'])/'.gate.lock', blocking=True): envelope(plan)
    hashes = {}; workers = [bind_settings(p, plan['deadline_epoch'], hashes, True) for p in plan['preparation_settings']]
    graders = [bind_settings(p, plan['deadline_epoch'], hashes) for p in plan.get('grading_settings', [])]
    physical = [q.runtime_identity(s) for s in workers+graders]
    if not graders or len(set(physical)) != len(physical): raise ValueError('Distinct preparation/grading physical runtimes required')
    for relative in ('scripts/pipeline.py', 'scripts/task_queue.py', 'scripts/role_handoff.py', 'scripts/work_package.py',
                     'scripts/role_contract.py', 'scripts/preparation_context.py', 'scripts/admission.py',
                     'scripts/access_readiness.py', 'scripts/route_cooldown.py', 'scripts/codex-service-trial.py', 'scripts/roles/material_preparation/AGENTS.md',
                     'generated/catalog.json', 'data/pricing/litellm.json'):
        source(B.root/relative, hashes)
    directory = Path(directory).resolve()
    with q.lock(Path(plan['queue'])/'.gate.lock', blocking=True):
        envelope(plan)
        owner = Path(plan['queue'])/'.registered-producer-owner.json'
        write(owner, {'directory': str(directory), 'deadline_epoch': plan['deadline_epoch']})
        hashes[str(owner)] = r.digest(owner)
    directory.mkdir(mode=0o700, parents=True, exist_ok=False)
    plan = deepcopy(plan); plan['base_source_root'] = str(B.root)
    write(directory/'plan.json', plan); write(directory/'source-hashes.json', hashes)
    write(directory/'controller-source.json', {'producer': str(Path(__file__).resolve()),
          'producer_sha256': r.digest(Path(__file__)), 'base_source_root': str(B.root), 'base_source_sha256': hashes})
    r.write(directory/'state.json', {'phase': 'no_ready_work', 'frozen_plan': plan, 'plan_sha256': r.digest(directory/'plan.json'),
                                    'items': {}, 'halted': False})
    for path in plan.get('backlog', []): enqueue(directory, path)
    return directory


def target_lanes(target):
    """Return only controller-approved configurations; model output never selects lanes."""
    pool = target.get('execution_pool')
    if pool is None:
        return [{'id': 'default', 'config': target['config'], 'depends_on': target.get('depends_on', [])}]
    if not isinstance(pool, list) or not pool:
        raise ValueError('Execution pool must contain approved lane objects')
    return pool


def validate_pool(target):
    if 'execution_pool' not in target:
        return
    p = B.work_package; q = B.task_queue; base = target['config']
    policy = target.get('execution_pool_policy', {})
    p.keys(policy, ('mode', 'max_active_per_target'), ('mode', 'max_active_per_target'))
    if (policy['mode'] != 'readonly_anonymous' or type(policy['max_active_per_target']) is not int
            or not 1 <= policy['max_active_per_target'] <= 2):
        raise ValueError('Execution pools require explicit readonly_anonymous scope and a maximum of one or two active lanes')
    route = B.pipeline.module('pool_route', 'codex-service-trial.py').select_route(
        B.pipeline.read(B.pipeline.ROOT/'generated/catalog.json'), base['service'], base['route'])
    if route.get('auth', {}).get('value') != 'none' or base.get('service_credentials', {}).get('provided') is not False:
        raise ValueError('Execution pools cannot use account credentials or undocumented anonymous access')
    scope = base['execution'].get('credential_scope')
    if not isinstance(scope, str) or not scope.strip():
        raise ValueError('Anonymous pool requires one explicit shared quota credential_scope')
    expected = q.cooldowns.binding(base, route)
    seen_ids = set(); seen_runtime = set(); seen_access = set()
    fixed = ('model', 'reasoning_effort', 'harness', 'seconds', 'max_model_requests', 'closure_fraction', 'deadline_epoch')
    for lane in target_lanes(target):
        p.keys(lane, ('id', 'config', 'depends_on'), ('id', 'config', 'depends_on'))
        name = p.identity(lane['id']); cfg = lane['config']; execution = cfg['execution']
        if name in seen_ids: raise ValueError('Duplicate execution lane ID')
        seen_ids.add(name)
        if (cfg.get('phase') != 'business' or cfg.get('service_credentials', {}).get('provided') is not False
                or any(cfg.get(key) != base.get(key) for key in ('service', 'route', 'task_file', 'task', 'trial_protocol', 'resource_authorization', 'preflight'))
                or any(execution.get(key) != base['execution'].get(key) for key in fixed)):
            raise ValueError('Pool lane must preserve the approved task, anonymous scope and model/tool budgets')
        if not set(base['execution'].get('resource_locks', [])).issubset(execution.get('resource_locks', [])):
            raise ValueError('Execution pool cannot remove approved account/write/resource locks')
        if q.cooldowns.binding(cfg, route) != expected:
            raise ValueError('All pool lanes must share the exact service/route quota family and endpoints')
        physical = q.runtime_identity(execution)
        if physical in seen_runtime or cfg.get('depends_on') in seen_access:
            raise ValueError('Every pool lane needs a distinct physical runtime and its own access prerequisite')
        seen_runtime.add(physical); seen_access.add(cfg.get('depends_on'))
        if (not isinstance(cfg.get('environment_id'), str) or not cfg['environment_id'].strip()
                or not isinstance(cfg.get('depends_on'), str) or not Path(cfg['depends_on']).is_absolute()
                or not isinstance(lane['depends_on'], list) or not lane['depends_on']
                or any(not isinstance(value, str) or not value for value in lane['depends_on'])):
            raise ValueError('Each pool lane needs its own frozen environment/access dependency')
        if bool(cfg.get('reference')) != bool(base.get('reference')) or (cfg.get('reference') and B.pipeline.digest(cfg['reference']) != B.pipeline.digest(base['reference'])):
            raise ValueError('Pool lanes cannot change the original independent reference or its hard holds')


def execution_load(plan):
    """Pending starts reserve a lane too; collected execution releases it before grading."""
    q = B.task_queue; r = B.pipeline; directory = Path(plan['queue']); state = r.read(directory/'state.json')
    handoffs = {r.read(path)['id']: r.read(path) for path in (directory/'inbox').glob('*/handoff.json')}
    handoffs.update({key: job['handoff'] for key, job in state.get('jobs', {}).items()})
    occupied = set(); families = {}; locks = set()
    for identity, handoff in handoffs.items():
        for member in handoff['members']:
            path = Path(member['directory']); observed = r.read(path/'state.json') if (path/'state.json').exists() else {}
            phase = observed.get('phase')
            if (phase in ('execution_collected', 'reviewed', 'recorded', 'preflight_blocked')
                    or isinstance(phase, str) and phase.startswith('grading_')
                    or phase == 'stopped' and observed.get('stop_confirmed') is True):
                continue
            owner = state.get('jobs', {}).get(identity, {})
            if (not observed and owner.get('phase') in ('blocked', 'preflight_blocked')
                    and owner.get('prepared') is False):
                continue  # Preparation never dispatched this member.
            # A missing run state or unconfirmed stop is uncertainty, not an idle
            # container, even when the queue labels the owner needs_attention.
            cfg = member['config']; physical = q.runtime_identity(cfg['execution']); occupied.add(physical)
            locks.update(cfg['execution'].get('resource_locks', []))
            family = q.inputs(cfg)['quota_binding']['scope_id']; families[family] = families.get(family, 0)+1
    return occupied, families, locks


def lane_access(lane):
    """Never transfer one lane's access result to another runtime/environment."""
    cfg = lane['config']; r = B.pipeline; q = B.task_queue
    if cfg['phase'] != 'business': return 'ready', None
    from access_readiness import PROTOCOL, decision
    access = Path(cfg['depends_on']); phase = r.read(access/'state.json')['phase'] if (access/'state.json').exists() else 'waiting'
    if phase not in q.DONE | {'recorded'}: return 'pending', 'Access still pending'
    ok, reason = decision(access, PROTOCOL)
    if not ok: return 'held', reason
    prior = r.read(access/'config.json')
    if (any(prior.get(key) != cfg.get(key) for key in ('service', 'route', 'environment_id'))
            or prior['execution']['runtime'] != cfg['execution']['runtime']
            or q.runtime_identity(prior['execution']) != q.runtime_identity(cfg['execution'])):
        return 'held', 'Access prerequisite belongs to another execution lane/environment'
    return 'ready', None


def choose_lane(target, candidates, plan):
    occupied, families, locks = execution_load(plan)
    if 'execution_pool' not in target: return candidates[0] if candidates else None
    maximum = target['execution_pool_policy']['max_active_per_target']
    for lane in candidates:
        cfg = lane['config']; binding = B.task_queue.inputs(cfg)['quota_binding']
        cooldown = B.task_queue.cooldowns.hold(B.pipeline.read(Path(plan['queue'])/'state.json'), binding, time.time())
        if (cooldown is None and B.task_queue.runtime_identity(cfg['execution']) not in occupied
                and families.get(binding['scope_id'], 0) < maximum
                and not locks.intersection(cfg['execution'].get('resource_locks', []))):
            return lane
    return None


def enqueue(directory, item_path):
    directory = Path(directory); r = B.pipeline; p = B.work_package
    with B.task_queue.lock(directory/'.lock', blocking=True):
        state = r.read(directory/'state.json'); plan = state['frozen_plan']; hashes = {}
        item = r.read(source(item_path, hashes)); identity = p.identity(item['id']); task = current_task(item)
        rounds = item.get('rounds')
        if (not isinstance(rounds, list) or not rounds or any(type(n) is not int or n < 1 for n in rounds)
                or len(rounds) != len(set(rounds)) or not item.get('targets')): raise ValueError('Explicit targets and distinct positive rounds required')
        if identity in state['items']: raise ValueError('Backlog identity already exists')
        hashes[str(B.pipeline.ROOT/item['task_file'])] = r.digest(B.pipeline.ROOT/item['task_file'])
        worker_physical = {B.task_queue.runtime_identity(r.read(x)) for x in plan['preparation_settings']}
        grader_physical = {B.task_queue.runtime_identity(r.read(x)) for x in plan['grading_settings']}
        if item.get('peer_policy', 'posthoc_audit') not in ('posthoc_audit', 'comparison_barrier'): raise ValueError('Unsupported peer policy')
        for name in list(item.get('materials', {}))+list(item.get('generated_materials', {}))+item.get('material_ids', []): p.identity(name)
        if any(name not in item.get('materials', {}) and name not in item.get('generated_materials', {}) for name in item.get('material_ids', [])): raise ValueError('Unapproved original material ID')
        for target_id, target in item['targets'].items():
            p.identity(target_id); validate_pool(target)
            if 'execution_pool' in target and item.get('peer_policy', 'posthoc_audit') != 'posthoc_audit':
                raise ValueError('Execution pools require posthoc_audit independent grading')
            from access_readiness import PROTOCOL
            for cfg in [target['config']]+[lane['config'] for lane in target_lanes(target)]:
                if cfg.get('trial_protocol') != PROTOCOL: raise ValueError('Registered producer requires the current access-readiness protocol')
                if (cfg.get('task_file'), cfg.get('task')) != (item['task_file'], item['task_id']):
                    raise ValueError('Controller config must preserve the original registered task')
                if B.task_queue.runtime_identity(cfg['execution']) in worker_physical | grader_physical:
                    raise ValueError('Executor cannot share a preparation or grader container')
                for role in ('execution', 'grading'):
                    adapter = B.task_queue.adapter_config(cfg[role])
                    if adapter is not None: source(adapter, hashes)
                if cfg.get('reference'): source(cfg['reference'], hashes)
                if cfg.get('attachments'): raise ValueError('Use approved original material registry instead of config attachments')
        for material in item.get('materials', {}).values():
            path = source(material['path'], hashes)
            if r.digest(path) != material['sha256'] or material.get('audience') not in ('execution', 'grading') or material.get('kind') != 'raw_data':
                raise ValueError('Approved raw material binding changed')
        _, extra = B.preparation_context.selected(item.get('preparation_context'), item['targets']); hashes.update(extra)
        for other in state['items']:
            prior = r.read(directory/'backlog'/other/'item.json')
            if (prior['task_sha256'] == item['task_sha256'] and set(prior['rounds']).intersection(rounds)
                    and {(lane['config']['service'], lane['config']['route'], lane['config'].get('environment_id'))
                         for target in prior['targets'].values() for lane in target_lanes(target)}
                    .intersection((lane['config']['service'], lane['config']['route'], lane['config'].get('environment_id'))
                                  for target in item['targets'].values() for lane in target_lanes(target))):
                raise ValueError('Duplicate existing task/route/round/condition in backlog')
        root = directory/'backlog'/identity
        write(root/'item.json', item); write(root/'sources.json', hashes)
        write(root/'task.json', task)
        state['items'][identity] = {'phase': 'waiting', 'item_sha256': r.digest(root/'item.json')}
        r.write(directory/'state.json', state)
    return identity


def verify(directory, state):
    r = B.pipeline
    if r.digest(directory/'plan.json') != state['plan_sha256'] or state['frozen_plan'] != r.read(directory/'plan.json'): raise ValueError('Producer plan or frozen state mirror changed')
    own = r.read(directory/'controller-source.json')
    if r.digest(Path(__file__)) != own['producer_sha256']: raise ValueError('Registered producer source changed')
    for name, sha in r.read(directory/'source-hashes.json').items():
        if r.digest(name) != sha: raise ValueError('Base/controller runtime source changed')
    for identity, row in state['items'].items():
        root = directory/'backlog'/identity
        if r.digest(root/'item.json') != row['item_sha256']: raise ValueError('Backlog item changed')
        for name, sha in r.read(root/'sources.json').items():
            if r.digest(name) != sha: raise ValueError('Registered preparation source changed')
        current_task(r.read(root/'item.json'))
    return state['frozen_plan']


def packet(root, item):
    r = B.pipeline; task = current_task(item); inputs = root/'preparation-input'; inputs.mkdir(mode=0o700)
    (inputs/'AGENTS.md').write_bytes((B.role_handoff.HERE/'roles/material_preparation/AGENTS.md').read_bytes())
    projection = {'schema_version': 1, 'source_kind': 'registered_task', 'role': 'registered_task', 'package_id': item['id'],
        'source': {'task_file': item['task_file'], 'task_id': task['id'], 'task_sha256': task['sha256']},
        'tasks': [{**task, 'material_ids': item.get('material_ids', []), 'applicable_target_ids': list(item['targets'])}],
        'notice': 'Controller projection of an existing registry row, not a task-design Agent output or proof. All task fields/resources remain unchanged.'}
    write(inputs/'task-design.json', projection)
    boundary = {'package_id': item['id'], 'designer_sha256': r.digest(inputs/'task-design.json'), 'source_kind': 'registered_task',
        'rounds': item['rounds'], 'generated_materials': item.get('generated_materials', {}),
        'original_material_ids': list(item.get('materials', {})), 'materials_output_rule': 'materials[] lists only generated_materials outputs. If only approved original IDs are used, emit materials: []; controller attaches exact registered original bytes. Original IDs may be echoed only with exact approved file bytes/SHA/size; this cannot replace the registry.', 'peer_policy': item.get('peer_policy', 'posthoc_audit'),
        'targets': {key: B.preparation_context.target_facts(value['config'], r.read(r.ROOT/'generated/catalog.json')) for key, value in item['targets'].items()}}
    write(inputs/'preparation-boundary.json', boundary)
    for name, material in item.get('materials', {}).items():
        if material['audience'] == 'execution':
            destination = inputs/'original-materials'/name/Path(material['path']).name
            destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True); destination.write_bytes(Path(material['path']).read_bytes())
    B.preparation_context.populate(inputs, item.get('preparation_context'), item['targets'])
    (inputs/'prompt.txt').write_text('Prepare only the assigned existing registry task. task-design.json is explicitly a registered_task controller projection, NOT a native designer session; bind designer_sha256 to its exact bytes. Do not change the task or resources. Read output-schema.json and preparation-boundary.json. Write the native material-preparation.json contract and every approved target/round assignment; If using only approved original-material IDs, emit materials: [] exactly; controller reattaches exact bytes. materials[] is for generated_materials only; never regenerate, rename or revise approved originals. Generate only explicitly approved original synthetic CSV/JSON/TXT; no answers, call scripts, prior assessments or service business queries. Independent references stay under references/ and never become execution inputs. Preserve real unknowns/held conditions. An original reference hard hold cannot be removed by prose. No accounts, credentials, payments or resource changes.\n')
    return inputs


def prepared(root, item):
    r = B.pipeline; w = B.work_package; output = role_job(root)/'output'
    binding = {'directory': str(output), 'receipt_sha256': r.digest(output/'receipt.json'), 'proof_sha256': r.digest(output/'role-collection-proof.json')}
    w.collection({'preparer_collection': binding}, result_path=output/'material-preparation.json')
    payload = r.read(output/'material-preparation.json'); B.role_contract.validate('material_preparation', payload); w.status(payload)
    if payload.get('role') != 'material_preparation' or payload['package_id'] != item['id'] or payload['designer_sha256'] != r.digest(root/'preparation-input/task-design.json'):
        raise ValueError('Native preparer did not bind registered-task projection')
    expected = {(item['task_id'], target, n) for target in item['targets'] for n in item['rounds']}; seen = set()
    for row in payload['assignments']:
        w.status(row); key = (row['task_id'], row['target_id'], row['round'])
        if key not in expected or key in seen: raise ValueError('Unexpected or duplicate assignment')
        seen.add(key)
    if seen != expected: raise ValueError('Preparer omitted declared assignments')
    protected = set(B.role_handoff.private_input_sources(r.read(role_job(root)/'manifest.json')).values())
    protected.update(r.digest(output/name) for name in ('material-preparation.json', 'receipt.json', 'role-collection-proof.json', 'artifact-input-index.json'))
    materials = deepcopy(item.get('materials', {})); material_declarations = set()
    for row in payload.get('materials', []):
        name = row['id']; rule = item.get('generated_materials', {}).get(name)
        if name in material_declarations: raise ValueError('Duplicate material declaration')
        material_declarations.add(name)
        if name in item.get('materials', {}):
            approved = materials[name]; original = Path(approved['path']); copied = w.regular_file(output/'artifacts', row['file'])
            if (approved['audience'] != 'execution' or approved.get('synthetic') is False
                    or row['sha256'] != approved['sha256'] or r.digest(original) != row['sha256'] or r.digest(copied) != row['sha256']
                    or row.get('bytes', copied.stat().st_size) != original.stat().st_size):
                raise ValueError('Original material echo differs from approved bytes/audience')
            # Preserve controller origin metadata; a model echo never relabels or replaces it.
            continue
        if not rule or name in materials or row['file'] != rule['file']: raise ValueError('Unsupported generated material')
        path = w.regular_file(output/'artifacts', row['file'])
        if r.digest(path) != row['sha256'] or row['sha256'] in protected or row.get('bytes', path.stat().st_size) != path.stat().st_size or row.get('synthetic', True) is not True:
            raise ValueError('Generated data hash/size/privacy/synthetic declaration invalid')
        w.raw_data(path, rule); materials[name] = {'path': str(path), 'sha256': row['sha256'], 'file': row['file'][10:], 'audience': 'execution', 'kind': 'raw_data'}
    for name in item.get('material_ids', []):
        if name not in materials or materials[name]['audience'] != 'execution': raise ValueError('Original execution material missing or grading-only')
    references = []
    for row in payload.get('references', []):
        if not row['path'].startswith('references/'): raise ValueError('Reference must stay grading-only')
        path = w.regular_file(output/'artifacts', row['path'])
        if r.digest(path) != row['sha256'] or path.stat().st_size != row['bytes']: raise ValueError('Reference bytes changed')
        references.append({'manifest': row, 'content': path.read_text()})
    return payload, materials, references, binding


def grade_load(plan):
    q = B.task_queue; r = B.pipeline; counts = {}; active = set(); queue_dir = Path(plan['queue'])
    for ready in (queue_dir/'inbox').glob('*/ready.json'):
        file = ready.parent/'handoff.json'
        if r.digest(file) != r.read(ready)['sha256']: raise ValueError('Queue handoff changed')
        for member in r.read(file)['members']:
            path = Path(member['directory']); phase = r.read(path/'state.json')['phase'] if (path/'state.json').exists() else 'waiting'
            physical = q.runtime_identity(member['config']['grading'])
            if phase not in q.DONE: counts[physical] = counts.get(physical, 0)+1
            if phase.startswith('grading_') and phase != 'grading_collected': active.add(physical)
    return counts, active


def ensure_submit(plan, spec):
    q = B.task_queue; r = B.pipeline; queue_dir = Path(plan['queue']); value = r.read(spec); existing = queue_dir/'inbox'/value['id']
    if not existing.exists(): return q.submit(queue_dir, spec)
    ready = r.read(existing/'ready.json'); handoff = r.read(existing/'handoff.json')
    members = value['members'] if value['kind'] == 'comparison' else [value]
    expected = [{'directory': str(Path(m['directory']).resolve()), 'config': r.read(m['config']), 'inputs': q.inputs(r.read(m['config'])), 'evidence': m.get('evidence', [])} for m in members]
    if (r.digest(existing/'handoff.json') != ready['sha256'] or handoff['members'] != expected
            or handoff['kind'] != value['kind'] or handoff['round'] != value['round'] or handoff['depends_on'] != value['depends_on']):
        raise ValueError('Existing submitted identity differs; do not replay')
    return value['id']


def submit_ready(directory, identity, row, plan):
    r = B.pipeline; q = B.task_queue; root = directory/'backlog'/identity; item = r.read(root/'item.json'); payload, materials, references, proof = prepared(root, item)
    if payload['status'] == 'held': row.update(phase='held', reason=payload['blockers']); return
    with q.lock(Path(plan['queue'])/'.gate.lock', blocking=True):
        if time.time() >= plan['deadline_epoch'] or q.storage_hold(Path(plan['queue']), r.read(Path(plan['queue'])/'policy.json')): return
        from access_readiness import PROTOCOL, decision
        ready_targets = {}; pending = []; held = []
        for key, target in item['targets'].items():
            cfg = target['config']; reference_bytes = Path(cfg['reference']).read_bytes() if cfg.get('reference') else None
            try:
                original_reference = r.read(cfg['reference']) if reference_bytes else {}
                if original_reference.get('mandatory_reference_missing') is True or original_reference.get('status') == 'mandatory_reference_missing':
                    raise ValueError('Original mandatory reference missing; preparation prose cannot waive this hold')
                B.admission.plan(cfg, current_task(item), original_reference if reference_bytes else None, reference_bytes, (r.ROOT/'scripts/roles/execution/AGENTS.md').read_bytes(), PROTOCOL)
            except ValueError as error: held.append({'target': key, 'reason': str(error)}); continue
            eligible = []
            for lane in target_lanes(target):
                status, reason = lane_access(lane)
                if status == 'ready': eligible.append(lane)
                elif status == 'pending': pending.append({'target': key, 'lane': lane['id'], 'reason': reason})
                else: held.append({'target': key, 'lane': lane['id'], 'reason': reason})
            if eligible: ready_targets[key] = eligible
        barrier = item.get('peer_policy', 'posthoc_audit') == 'comparison_barrier'
        row.update(waiting_targets=pending, held_targets=held, peer_policy=item.get('peer_policy', 'posthoc_audit'))
        if barrier and pending: row['phase'] = 'waiting_access'; return
        counts, active = grade_load(plan); graders = [r.read(p) for p in plan['grading_settings']]
        submitted = row.setdefault('submitted_specs', []); deferred = []
        for number in item['rounds']:
            assignments = {a['target_id']: a for a in payload['assignments'] if a['round'] == number}
            chosen = [(key, item['targets'][key]) for key in ready_targets if assignments[key]['status'] == 'ready']
            held.extend({'target': key, 'round': number, 'reason': assignments[key]['blockers']} for key in ready_targets if assignments[key]['status'] != 'ready')
            batches = [chosen] if barrier and chosen else [[value] for value in chosen]
            for batch in batches:
                dispatch_id = identity+'-r'+str(number) if barrier else identity+'-'+batch[0][0]+'-r'+str(number)
                record = root/'compiled'/(dispatch_id+'.dispatch.json')
                if record.exists():
                    compilation = r.read(record)
                    for path, sha in compilation['files'].items():
                        if r.digest(path) != sha: raise ValueError('Frozen dispatch bytes changed')
                    if not (Path(plan['queue'])/'inbox'/dispatch_id).exists():
                        # Recovery after compile-before-submit must recheck the
                        # SAME frozen lane; it is not a reservation in the queue
                        # yet. Already submitted jobs bypass this self-check.
                        frozen_busy = False
                        for selected in compilation.get('execution_lanes', []):
                            approved = item['targets'][selected['target']]
                            if 'execution_pool' not in approved: continue
                            lane = next(value for value in target_lanes(approved) if value['id'] == selected['lane_id'])
                            if choose_lane(approved, [lane], plan) is None:
                                deferred.append({'target': selected['target'], 'round': number, 'reason': 'Previously frozen execution lane is not idle or shared cap/cooldown prevents submission'})
                                frozen_busy = True
                        if frozen_busy: continue
                else:
                    selected = []
                    for key, target in batch:
                        lane = choose_lane(target, ready_targets[key], plan)
                        if lane is None:
                            deferred.append({'target': key, 'round': number, 'reason': 'No idle approved execution lane, target cap reached or shared cooldown active'})
                            continue
                        selected.append((key, lane))
                    if len(selected) != len(batch): continue
                    members = []; deps = []; used = set(); files = {}; lane_bindings = []
                    for key, target in selected:
                        lane_bindings.append({'target': key, 'lane_id': target['id'], 'environment_id': target['config']['environment_id'],
                                              'execution_runtime': target['config']['execution']['runtime'], 'access_run': target['config'].get('depends_on')})
                        options = [g for g in graders if q.runtime_identity(g) not in used]
                        if not options: raise ValueError('Grading pool smaller than selected comparison')
                        grader = min(options, key=lambda g: (q.runtime_identity(g) in active, counts.get(q.runtime_identity(g), 0), g['runtime']))
                        physical = q.runtime_identity(grader); used.add(physical); counts[physical] = counts.get(physical, 0)+1
                        cfg = deepcopy(target['config']); cfg['grading'] = deepcopy(grader); job = identity+'-'+key+'-r'+str(number); dest = root/'compiled'/job
                        ref = r.read(cfg['reference']) if cfg.get('reference') else {}
                        ref['registered_task_preparation'] = {'source_kind': 'registered_task', 'original_task_sha256': item['task_sha256'], 'native_preparer_collection': proof, 'references': deepcopy(references),
                            'resource_prerequisites': payload.get('resource_prerequisites'), 'frozen_dates': payload.get('frozen_dates'), 'notice': 'Independent preparation evidence, never a verdict or a waiver of original reference holds.'}
                        for name, material in materials.items():
                            if material['audience'] == 'grading': ref['registered_task_preparation']['references'].append({'material_id': name, 'sha256': material['sha256'], 'content': Path(material['path']).read_text()})
                        write(dest/'reference.json', ref); cfg['reference'] = str(dest/'reference.json'); files[cfg['reference']] = r.digest(cfg['reference'])
                        if item.get('material_ids'):
                            attachment = dest/'attachments'; attachment.mkdir(mode=0o700, parents=True)
                            for name in item['material_ids']:
                                material = materials[name]; src = Path(material['path']); filename = material.get('file', src.name); output = attachment/filename
                                if Path(filename).is_absolute() or '..' in Path(filename).parts or output.exists(): raise ValueError('Unsafe or duplicate original material filename')
                                output.parent.mkdir(mode=0o700, parents=True, exist_ok=True); output.write_bytes(src.read_bytes()); output.chmod(0o600)
                                if r.digest(output) != material['sha256']: raise ValueError('Original material changed')
                                files[str(output)] = r.digest(output)
                            cfg['attachments'] = str(attachment)
                        if q.inputs(cfg)['task']['sha256'] != item['task_sha256']: raise ValueError('Compiled registry task hash changed')
                        config = dest/'config.json'; write(config, cfg); files[str(config)] = r.digest(config)
                        members.append({'directory': str(r.ROOT/'data/experiments/results'/job), 'config': str(config)}); deps.extend(target.get('depends_on', []))
                    spec = {'id': dispatch_id, 'kind': 'comparison' if len(members)>1 else 'run', 'ready': True, 'round': number, 'depends_on': sorted(set(deps)), 'grading_gate': False}
                    if len(members)>1: spec.update(directory=str(r.ROOT/'data/experiments/results'/dispatch_id), members=members)
                    else: spec.update(members[0])
                    file = root/'compiled'/(dispatch_id+'.spec.json'); write(file, spec); files[str(file)] = r.digest(file)
                    compilation = {'spec': str(file), 'files': files, 'batch': {'task_sha256': item['task_sha256'], 'round': number, 'peer_policy': item.get('peer_policy', 'posthoc_audit'), 'targets': [key for key, _ in batch]}, 'execution_lanes': lane_bindings, 'source_kind': 'registered_task'}
                    write(record, compilation)
                ensure_submit(plan, Path(compilation['spec']))
                if compilation['spec'] not in submitted: submitted.append(compilation['spec'])
        if not barrier:
            # Access still pending on an unused optional lane does not keep a fully
            # submitted target alive; every remaining slot keeps its original ID.
            unfinished = {key for key in item['targets'] if any(
                str(root/'compiled'/(identity+'-'+key+'-r'+str(number)+'.spec.json')) not in submitted
                for number in item['rounds'])}
            pending = [value for value in pending if value['target'] in unfinished]
        row.update(phase='waiting_runtime' if deferred else 'waiting_access' if pending else 'submitted' if submitted else 'held',
                   submitted_jobs=len(submitted), waiting_targets=pending, waiting_execution=deferred, held_targets=held)


def settle(job, row, reason):
    try:
        result = B.role_handoff.advance(job, halt=True)
        safe = result['phase'] in ('collected', 'held', 'stopped')
        row.update(phase='held' if safe else 'attention', reason=reason, role_phase=result['phase'])
        if not safe: row['stop_unconfirmed'] = True
    except Exception as error: row.update(phase='attention', reason=reason, stop_error=str(error), stop_unconfirmed=True)


def poll_inbox(directory):
    state = B.pipeline.read(directory/'state.json'); inbox = state['frozen_plan'].get('backlog_inbox')
    if state.get('halted') or not inbox: return
    for file in sorted(Path(inbox).glob('*.json')):
        try:
            item = B.pipeline.read(B.preparation_context.regular(file))
            if item['id'] not in B.pipeline.read(directory/'state.json')['items']: enqueue(directory, file)
        except Exception as error:
            (directory/'intake-errors').mkdir(mode=0o700, exist_ok=True)
            # Invalid input is visible and never becomes a role allocation.
            B.pipeline.write(directory/'intake-errors'/file.name, {'source': str(file), 'error': str(error)})


def tick(directory, halt=False):
    directory = Path(directory); r = B.pipeline; q = B.task_queue; roles = B.role_handoff
    if not halt: poll_inbox(directory)
    with q.lock(directory/'.lock', blocking=True):
        state = r.read(directory/'state.json'); plan = state['frozen_plan']
        try:
            verify(directory, state)
            with q.lock(Path(plan['queue'])/'.gate.lock', blocking=True): envelope(plan)
        except Exception as error: halt = True; state['source_error'] = str(error)
        halt = halt or state.get('halted', False) or time.time() >= plan['deadline_epoch']
        if halt: state['halted'] = True
        for identity, row in state['items'].items():
            root = directory/'backlog'/identity; job = role_job(root)
            if halt:
                if row['phase'] in TERMINAL and (not (job/'state.json').exists() or r.read(job/'state.json')['phase'] in ('collected', 'held', 'stopped')): continue
                if (job/'state.json').exists() and r.read(job/'state.json').get('handle'): settle(job, row, 'Producer halted; preserve original records')
                elif row['phase'] not in TERMINAL: row.update(phase='held', reason='Producer halted before dispatch')
                continue
            if row['phase'] not in ('preparing', 'attention'): continue
            try:
                result = advance_role(job, plan, halt=row['phase']=='attention')
                if result['phase'] == 'collected':
                    prepared(root, r.read(root/'item.json')); row.update(phase='ready_to_submit', worker_released=True)
                elif result['phase'] in ('uncertain_start', 'starting', 'needs_attention'):
                    settle(job, row, 'Uncertain start/status; never resend start')
                elif result['phase'] in ('held', 'stopped'): row.update(phase='held', reason=result.get('reason'))
            except Exception as error: settle(job, row, str(error))
            r.write(directory/'state.json', state)
        if not halt:
            for identity, row in state['items'].items():
                if row['phase'] in ('ready_to_submit', 'waiting_access', 'waiting_runtime'):
                    try: submit_ready(directory, identity, row, plan)
                    except Exception as error: row.update(phase='held', reason=str(error), preparation_collected=True)
                    r.write(directory/'state.json', state)
            for identity, row in state['items'].items():
                if row['phase'] != 'waiting': continue
                busy = {x.get('worker') for x in state['items'].values() if x['phase'] in ('preparing', 'attention')}
                free = [n for n in range(2) if n not in busy]
                if not free or q.storage_hold(Path(plan['queue']), r.read(Path(plan['queue'])/'policy.json')): continue
                worker = free[0]; settings = r.read(plan['preparation_settings'][worker])
                if time.time()+settings['seconds']+20 >= plan['deadline_epoch']: row.update(phase='held', reason='No complete preparation role window'); continue
                root = directory/'backlog'/identity; row.update(phase='preparing', worker=worker); r.write(directory/'state.json', state)
                try:
                    inputs = packet(root, r.read(root/'item.json')); roles.prepare(role_job(root), 'material_preparation', inputs, plan['preparation_settings'][worker])
                    result = advance_role(role_job(root), plan)
                    if result['phase'] in ('uncertain_start', 'starting', 'needs_attention'): settle(role_job(root), row, 'Uncertain preparation start')
                    elif result['phase'] in ('held', 'stopped'): row.update(phase='held', reason=result.get('reason'))
                except Exception as error:
                    if (role_job(root)/'state.json').exists(): settle(role_job(root), row, str(error))
                    else: row.update(phase='held', reason=str(error))
                r.write(directory/'state.json', state)
        phases = [x['phase'] for x in state['items'].values()]
        state['phase'] = ('stop_needs_attention' if 'attention' in phases else 'stopped') if halt else (
            'running' if any(p in ('waiting', 'preparing', 'ready_to_submit', 'attention') for p in phases) else 'no_ready_work')
        state['reserved_preparation_slots'] = sum(x['phase'] in ('preparing', 'attention') for x in state['items'].values())
        state['updated_at'] = r.now(); r.write(directory/'state.json', state)
        return state


def main():
    os.umask(0o077); parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('init', 'enqueue', 'run', 'status', 'halt')); parser.add_argument('directory', type=Path)
    parser.add_argument('--plan', type=Path); parser.add_argument('--entry', type=Path); parser.add_argument('--base-source-root', type=Path); parser.add_argument('--once', action='store_true'); args = parser.parse_args()
    if args.action == 'init':
        if not args.plan or not args.base_source_root: parser.error('init requires --plan and --base-source-root')
        print(init(args.directory, args.plan, args.base_source_root)); return
    plan = json.loads((args.directory/'plan.json').read_text()); base = args.base_source_root or Path(plan['base_source_root'])
    if str(Path(base).resolve()) != plan['base_source_root']: parser.error('Base source root differs from initialized producer')
    libraries(base)
    if args.action == 'status': print(json.dumps(B.pipeline.read(args.directory/'state.json'))); return
    if args.action == 'enqueue': print(enqueue(args.directory, args.entry)); return
    def request_stop(*unused):
        global STOP
        STOP = True
    signal.signal(signal.SIGTERM, request_stop); signal.signal(signal.SIGINT, request_stop)
    with B.task_queue.lock(args.directory/'.controller.lock'):
        while True:
            state = tick(args.directory, halt=STOP or args.action=='halt'); print(json.dumps(state), flush=True)
            if args.once or state['phase'] in ('stopped', 'stop_needs_attention'): return
            time.sleep(3)


if __name__ == '__main__': main()
