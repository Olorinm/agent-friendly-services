#!/usr/bin/env python3
"""Continuously admit frozen role handoffs, prepare dependencies and reuse pipeline.

One controller owns a runner pool. New jobs can be submitted while it runs; no
discovery, task design, verdict or publication is performed by the scheduler.
The private budget holds worst-case session reservations until reconciled.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
import signal
import shutil
from pathlib import Path
import subprocess
import time

import pipeline as runs
import comparison_group as groups
import route_cooldown as cooldowns

DONE = {'reviewed', 'recorded', 'needs_attention', 'stopped', 'preflight_blocked', 'blocked'}
STOP_REQUESTED = False


def request_stop(signum, frame):
    # Finish the current adapter operation before collecting/stopping its worker.
    # Raising inside start could lose the only durable startup response.
    global STOP_REQUESTED
    STOP_REQUESTED = True


@contextmanager
def lock(path, blocking=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX | (0 if blocking else fcntl.LOCK_NB))
        yield


def stamp(value):
    if not isinstance(value, str): raise ValueError('Explicit deadline required')
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None: raise ValueError('Deadline must include timezone')
    return result.timestamp()


def budget_cap(policy):
    """Null is unbounded only with an explicit policy mode; old caps stay caps."""
    mode = policy.get('budget_mode', 'capped')
    amount = policy.get('budget_usd')
    if mode == 'unbounded':
        if 'budget_usd' not in policy or amount is not None: raise ValueError('Unbounded budget must use budget_usd:null')
        return None
    if mode != 'capped' or type(amount) not in (int, float) or not math.isfinite(amount) or amount <= 0:
        raise ValueError('Explicit positive model budget or explicit unbounded mode required')
    return amount


def init(directory, *, max_concurrency, budget_usd=None, expires_at, pool, no_budget_cap=False,
         storage_floor_bytes=1024**3):
    if type(max_concurrency) is not int or max_concurrency < 1: raise ValueError('Positive concurrency required')
    if type(no_budget_cap) is not bool or no_budget_cap and budget_usd is not None:
        raise ValueError('Choose a model budget or no_budget_cap, not both')
    if type(storage_floor_bytes) is not int or storage_floor_bytes < 0:
        raise ValueError('Storage floor must be a nonnegative integer')
    policy = {'max_concurrency': max_concurrency, 'budget_usd': budget_usd,
              'storage_floor_bytes': storage_floor_bytes,
              'budget_mode': 'unbounded' if no_budget_cap else 'capped', 'expires_at': expires_at, 'pool': pool}
    budget_cap(policy)
    stamp(expires_at)
    if not isinstance(pool, str) or not pool.strip(): raise ValueError('Explicit pool identity required')
    directory = Path(directory).resolve();directory.mkdir(mode=0o700, parents=True, exist_ok=False)
    runs.write(directory/'policy.json', policy)
    runs.write(directory/'state.json', {'phase': 'idle', 'jobs': {}, 'ledger': {}, 'created_at': runs.now()})
    (directory/'inbox').mkdir(mode=0o700)
    return directory


def storage_hold(directory, policy):
    # Old policies keep their saved behavior. Only new preparation/dispatch is
    # paused; active sessions must still be collected or stopped normally.
    floor=policy.get('storage_floor_bytes',0)
    if type(floor) is not int or floor < 0:raise ValueError('Invalid storage floor')
    free=shutil.disk_usage(directory).free
    return f'Controller storage low: {free} free bytes; {floor} required; no service failure inferred' if free < floor else None


def inputs(config):
    parser = runs.module('queue_inputs', 'codex-service-trial.py')
    task, _ = parser.select_task(runs.ROOT/config['task_file'], config['task'])
    route = parser.select_route(runs.read(runs.ROOT/'generated/catalog.json'), config['service'], config['route'])
    files = [runs.ROOT/'data/pricing/litellm.json', runs.ROOT/'scripts/roles/execution/AGENTS.md',
             runs.ROOT/'scripts/roles/grading/AGENTS.md']
    for role in ('execution', 'grading'):
        file = adapter_config(config[role])
        if file: files.append(file)
    if config.get('reference'): files.append(Path(config['reference']).resolve())
    if config.get('grading_secrets_file'):
        source = Path(config['grading_secrets_file'])
        if not source.is_absolute() or source.is_symlink() or not source.is_file():
            raise ValueError('Grading secrets need an absolute private file without symlinks')
        files.append(source)
    if config.get('attachments'):
        files.extend(Path(config['attachments']).resolve().rglob('*'))
    if any(p.is_symlink() for p in files): raise ValueError('Handoff inputs cannot contain symlinks')
    return {'task': task, 'route': route, 'files': {str(p): runs.digest(p) for p in files if p.is_file()},
            'quota_binding': cooldowns.binding(config, route)}


def adapter_config(settings):
    argv = settings['commands']['start']
    adapters = {str((runs.ROOT/'scripts/runners'/name/'adapter.py').resolve()) for name in ('opencode', 'codex')}
    if not any(str(Path(arg).resolve()) in adapters for arg in argv if not arg.startswith('-')):
        return None  # Offline fixture adapters are never accepted by ceiling().
    if '--config' not in argv: raise ValueError('Runner adapter needs an explicit private config')
    return Path(argv[argv.index('--config')+1]).resolve()


def chatgpt_grader(settings):
    if settings.get('billing_mode') != 'chatgpt': return False
    adapter = str((runs.ROOT/'scripts/runners/codex/adapter.py').resolve())
    if (settings.get('model') != 'gpt-6.1-sol' or settings.get('reasoning_effort') != 'high'
            or settings.get('harness', {}).get('name') != 'codex'
            or not any(str(Path(arg).resolve()) == adapter for arg in settings['commands']['start'] if not arg.startswith('-'))):
        raise ValueError('ChatGPT billing requires the independent Codex Sol/high adapter')
    config = runs.read(adapter_config(settings))
    if config.get('billing_mode') != 'chatgpt': raise ValueError('Adapter account billing differs from frozen role')
    return True


def runtime_identity(settings):
    file = adapter_config(settings)
    if not file: return ('declared-fixture', settings['runtime'])
    cfg = runs.read(file)
    return (cfg['host'], cfg['containers'][settings['runtime']])


def submit(directory, spec_path):
    """Task role submits prepared facts; controller marks a handoff ready explicitly."""
    directory = Path(directory).resolve();spec = runs.read(spec_path)
    if spec.get('ready') is not True: raise ValueError('Controller must explicitly mark the role handoff ready')
    identity = spec['id']
    if not isinstance(identity, str) or not identity or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-' for c in identity):
        raise ValueError('Invalid job identity')
    if spec.get('kind') not in ('run', 'comparison'): raise ValueError('Job kind must be run or comparison')
    if type(spec.get('grading_gate', False)) is not bool: raise ValueError('grading_gate must be boolean')
    members = spec.get('members') if spec['kind'] == 'comparison' else [spec]
    if not isinstance(members, list) or not members: raise ValueError('Job needs members')
    if spec['kind'] == 'comparison' and len(members) < 2: raise ValueError('Comparison needs at least two members')
    sealed = []
    for member in members:
        config = runs.read(Path(member['config']).resolve())
        from access_readiness import PROTOCOL
        config.setdefault('trial_protocol', PROTOCOL)
        for role in ('execution', 'grading'):
            if chatgpt_grader(config[role]):
                if role != 'grading': raise ValueError('ChatGPT Codex adapter is grading-only')
                continue
            if type(config[role].get('max_model_requests')) is not int or config[role]['max_model_requests'] < 1:
                raise ValueError('Queued roles need frozen max_model_requests for budget reservations')
        if not config.get('preflight'):
            raise ValueError('Queued runs need an explicit bounded preflight plan')
        path = Path(member['directory']).resolve()
        if path.exists(): raise ValueError('Queue materializes new runs only; never adopt existing or uncertain jobs')
        sealed.append({'directory': str(path), 'config': config, 'inputs': inputs(config),
                       'evidence': member.get('evidence', [])})
    execution = {runtime_identity(m['config']['execution']) for m in sealed}
    grading = {runtime_identity(m['config']['grading']) for m in sealed}
    if execution.intersection(grading): raise ValueError('Execution and grading must use physically separate containers')
    paths = [m['directory'] for m in sealed]
    if len(set(paths)) != len(paths): raise ValueError('Run directories must be unique')
    deps = spec.get('depends_on', [])
    if not isinstance(deps, list) or any(not isinstance(d, str) or d == identity for d in deps): raise ValueError('Invalid dependencies')
    target = directory/'inbox'/identity
    # Atomic directory creation is also a duplicate-submission guard. Failed
    # submissions remain inspectable; never silently replace frozen work.
    target.mkdir(mode=0o700)
    handoff = {'id': identity, 'kind': spec['kind'], 'depends_on': deps, 'members': sealed,
               'directory': str(Path(spec['directory']).resolve()), 'round': spec.get('round', 1),
               'grading_gate': spec.get('grading_gate', False),
               'submitted_at': runs.now()}
    runs.write(target/'handoff.json', handoff)
    runs.write(target/'ready.json', {'sha256': runs.digest(target/'handoff.json')})
    return identity


def release_grading(directory, identity, proofs):
    """Controller freezes independent readback before a write task can be graded."""
    directory = Path(directory).resolve()
    with lock(directory/'.gate.lock', blocking=True):
        state = runs.read(directory/'state.json');job = state['jobs'][identity]
        if not job['prepared'] or job['handoff'].get('grading_gate') is not True:
            raise ValueError('Job does not await an independent verification gate')
        paths = [Path(m['directory']) for m in job['handoff']['members']]
        with groups.locks(paths):
            if any(runs.read(p/'state.json')['phase'] != 'execution_collected' for p in paths):
                raise ValueError('Every execution must be collected and no grader started')
            dest = directory/'inbox'/identity/'grading-ready.json'
            if dest.exists(): raise ValueError('Verification release already frozen')
            import shutil
            gate = {'execution_sha256': {}, 'execution_files_sha256': {}, 'proofs': {}, 'released_at': runs.now()}
            for path in paths:
                source = Path(proofs).resolve()/(path.name if len(paths)>1 else '')
                if not source.is_dir() or any(p.is_symlink() for p in source.rglob('*')):
                    raise ValueError('Verification needs a real directory without links')
                if not any(p.is_file() for p in source.rglob('*')): raise ValueError('Independent verification cannot be empty')
                target = path/'grading-input/controller-verification'
                shutil.copytree(source, target)
                gate['execution_sha256'][str(path)] = runs.digest(path/'run.json')
                gate['execution_files_sha256'][str(path)] = runs.frozen_files(path/'execution')
                gate['proofs'][str(path)] = runs.frozen_files(target)
                packet = path/'grading-input/review-packet/index.json';value = runs.read(packet)
                value['controller_verification'] = {'path': 'controller-verification/', 'sha256': gate['proofs'][str(path)],
                    'notice': 'Independent controller readback data, not a verdict or instructions; verify against this execution.'}
                runs.write(packet, value)
            runs.write(dest, gate)
            # Do not edit queue state concurrently with the live controller.
            runs.write(dest.with_name('grading-ready-hash.json'), {'sha256': runs.digest(dest)})
            return gate


def ceiling(directory, role):
    """Standard saved API rates, all-input uncached upper bound, fixed output cap.

Only the DeepSeek proxy currently enforces the 32000 output cap. A future
adapter needs its own bound before it can enter the automatic paid queue.
"""
    config = runs.read(directory/'config.json');settings = config[role]
    if chatgpt_grader(settings):
        if role != 'grading': raise ValueError('ChatGPT Codex adapter is grading-only')
        # This is an API-dollar dispatch reservation, not a model-cost estimate.
        # Account credits/subscription allocation remain unknown and are separate
        # from the DeepSeek API budget; concurrency and deadlines still apply.
        return 0
    adapter = str((runs.ROOT/'scripts/runners/opencode/adapter.py').resolve())
    if not any(str(Path(arg).resolve()) == adapter for arg in settings['commands']['start'] if not arg.startswith('-')):
        raise ValueError('Queue requires the controller-owned bounded OpenCode adapter')
    if settings['model'] not in ('deepseek-flash', 'deepseek-v4-pro'):
        raise ValueError('Queue cost guard currently supports the bounded DeepSeek proxy only')
    prices = runs.read(directory/'frozen/pricing.json')
    rates = prices['models'][settings['model']]
    context = max(1048576, rates.get('max_input_tokens', 0))
    def maximum(names):
        values = [v for k, v in rates.items() if any(k == name or k.startswith(name+'_above_') for name in names)
                  and type(v) in (int, float) and math.isfinite(v) and v >= 0]
        if not values: raise ValueError('Missing price ceiling')
        return max(values)
    amount = settings['max_model_requests'] * (
        context * maximum(['input_cost_per_token', 'cache_read_input_token_cost', 'cache_creation_input_token_cost'])
        + 32000 * maximum(['output_cost_per_token']))
    # Use the real calculator to verify the frozen price-table content hash too.
    usage = {'input_tokens': 1, 'cached_input_tokens': 0, 'cache_write_input_tokens': 0,
             'output_tokens': 1, 'reasoning_output_tokens': 0}
    runs.write(directory/(role+'-reservation-check.json'), {'model': settings['model'], 'usage': usage})
    value = subprocess.check_output(['node', '--import', 'tsx', str(runs.ROOT/'scripts/calculate-cost.ts'),
                                    str(directory/(role+'-reservation-check.json')), str(directory/'frozen/pricing.json')],
                                   cwd=runs.ROOT, text=True)
    if json.loads(value).get('amount_usd') is None: raise ValueError('Frozen pricing cannot establish a reservation')
    return math.ceil(amount * 1000000000) / 1000000000


def entries(state):
    result = []
    for job in state['jobs'].values():
        if not job.get('prepared'): continue
        for member in job['handoff']['members']:
            path = Path(member['directory'])
            result.append((job, path, runs.read(path/'config.json'), runs.read(path/'state.json')))
    return result


def held(state):
    return sum(row['held_usd'] for row in state['ledger'].values())


def cost_summary(state):
    summary = {'complete_capture_estimate_usd': 0, 'partial_capture_lower_bound_usd': 0,
               'incomplete_captures': 0, 'unresolved_starts': 0, 'preflight_no_model': 0,
               'notice': 'Frozen API rate estimates, not payment. Reservations are not spending; partial bounds are not complete averages.'}
    for key, row in state['ledger'].items():
        if row.get('billing_mode') == 'chatgpt': continue
        name, role = key.rsplit(':', 1);path = Path(name)
        receipt = (path/role/'receipt.json').is_file()
        if role == 'execution' and not receipt and (path/'state.json').is_file() and runs.read(path/'state.json')['phase'] == 'preflight_blocked':
            summary['preflight_no_model'] += 1;continue
        cost = row.get('measured_cost') or {}
        amount = cost.get('amount_usd')
        if type(amount) in (int, float) and math.isfinite(amount) and amount >= 0:
            summary['complete_capture_estimate_usd'] += amount
        else:
            bound = cost.get('lower_bound_usd')
            if type(bound) in (int, float) and math.isfinite(bound) and bound >= 0:
                summary['partial_capture_lower_bound_usd'] += bound
            summary['incomplete_captures' if receipt else 'unresolved_starts'] += 1
    return summary


def reconcile(state):
    for _, path, config, phase in entries(state):
        for role in ('execution', 'grading'):
            key = str(path)+':'+role
            row = state['ledger'].get(key)
            if not row: continue
            if row.get('billing_mode') == 'chatgpt':
                row.update(account_cost_usd=None, account_credits=None)
                if (path/role/'model-cost.json').exists():
                    row['model_api_rate_estimate'] = runs.read(path/role/'model-cost.json')
                continue
            cost_file = path/role/'model-cost.json'
            if cost_file.exists():
                cost = runs.read(cost_file);amount = cost.get('amount_usd')
                row.update(measured_cost=cost)
                if type(amount) in (int, float) and math.isfinite(amount) and amount >= 0:
                    if amount > row['ceiling_usd'] + 1e-9:
                        raise ValueError('Measured cost exceeds reserved ceiling; stop and inspect pricing/bounds')
                    row['held_usd'] = amount
                # Incomplete capture keeps the full reservation, not merely its
                # known lower bound. A possibly paid missing request is not free.
            elif phase['phase'] == 'preflight_blocked' and role == 'execution':
                row['held_usd'] = 0


def prepare_jobs(directory, state, policy):
    for ready in sorted((directory/'inbox').glob('*/ready.json')):
        file = ready.parent/'handoff.json'
        if runs.digest(file) != runs.read(ready)['sha256']: raise ValueError('Submitted handoff changed')
        handoff = runs.read(file);identity = handoff['id']
        if identity not in state['jobs']:
            # No runtime/run may be owned by two jobs, even if both are pending.
            existing = {m['directory'] for j in state['jobs'].values() for m in j['handoff']['members']}
            if existing.intersection(m['directory'] for m in handoff['members']): raise ValueError('Duplicate queued run ownership')
            state['jobs'][identity] = {'handoff': handoff, 'phase': 'waiting', 'prepared': False}
    members = [m for job in state['jobs'].values() for m in job['handoff']['members']]
    execution = {runtime_identity(m['config']['execution']) for m in members}
    grading = {runtime_identity(m['config']['grading']) for m in members}
    if execution.intersection(grading): raise ValueError('Pool cannot reuse an executor container for grading')
    for identity, job in state['jobs'].items():
        if STOP_REQUESTED: break
        if job['prepared'] or job['phase'] in DONE: continue
        handoff = job['handoff'];deps = [state['jobs'].get(key) for key in handoff['depends_on']]
        def dependency_ready(dependency):
            if dependency['phase'] not in DONE:
                return None
            from access_readiness import PROTOCOL, decision
            if all(m['config'].get('trial_protocol') == PROTOCOL for m in handoff['members']):
                try:
                    return all(decision(m['directory'], PROTOCOL)[0] for m in dependency['handoff']['members'])
                except (OSError, ValueError, KeyError):
                    return False  # Hold these children, not unrelated jobs.
            return dependency['phase'] == 'reviewed'
        readiness = [dependency_ready(d) if d else None for d in deps]
        if any(ok is False for ok in readiness):
            job.update(phase='blocked', reason='Prerequisite did not pass; no service failure inferred');continue
        if any(ok is None for ok in readiness): continue
        if time.time() >= stamp(policy['expires_at']) or storage_hold(directory,policy): continue
        # Persist before preparation: a crash leaves a concrete inspection point,
        # never permission to overwrite a partially prepared run.
        job['phase'] = 'preparing';runs.write(directory/'state.json', state)
        try:
            for member in handoff['members']:
                if inputs(member['config']) != member['inputs']: raise ValueError('Task handoff inputs changed before freezing')
                path = Path(member['directory'])
                cfg = ready_config = directory/'inbox'/identity/(path.name+'.config.json')
                runs.write(cfg, member['config'])
                runs.prepare(ready_config, path)
            if handoff['kind'] == 'comparison':
                cfg = directory/'inbox'/identity/'comparison.config.json'
                runs.write(cfg, {'round': handoff['round'], 'max_concurrency': policy['max_concurrency'],
                                 'members': [{'run': m['directory'], 'evidence': m['evidence']} for m in handoff['members']]})
                groups.prepare(cfg, Path(handoff['directory']))
            job.update(prepared=True, phase='running')
        except Exception as error:
            job.update(phase='blocked', reason=str(error))
            # Already created partial directories remain untouched for inspection.


def advance(directory):
    with lock(Path(directory)/'.gate.lock', blocking=True):
        return _advance(directory)


def retry_dependency(directory, identity):
    """Explicitly reconsider a zero-execution dependency hold, never replay a run."""
    from access_readiness import PROTOCOL, decision
    directory=Path(directory).resolve()
    with lock(directory/'.gate.lock', blocking=True):
        state=runs.read(directory/'state.json');job=state['jobs'][identity]
        if (job.get('phase')!='blocked' or job.get('prepared') or job.get('superseded_by')
                or job.get('reason')!='Prerequisite did not pass; no service failure inferred'):
            raise ValueError('Only an unprepared, unsuperseded prerequisite hold can be reconsidered')
        submitted=directory/'inbox'/identity
        if (runs.digest(submitted/'handoff.json')!=runs.read(submitted/'ready.json')['sha256']
                or runs.read(submitted/'handoff.json')!=job['handoff']):
            raise ValueError('Original submitted handoff changed')
        members=job['handoff']['members']
        if any(Path(m['directory']).exists() for m in members):
            raise ValueError('An existing or partially prepared run must not be replayed')
        if not job['handoff']['depends_on'] or any(m['config'].get('trial_protocol')!=PROTOCOL for m in members):
            raise ValueError('Explicit current-protocol access dependencies required')
        verified=[]
        for key in job['handoff']['depends_on']:
            dependency=state['jobs'].get(key)
            if not dependency or dependency['phase'] not in DONE:
                raise ValueError('Access dependency has not finished')
            for member in dependency['handoff']['members']:
                path=Path(member['directory']);ready,reason=decision(path,PROTOCOL)
                if not ready:raise ValueError('Access dependency remains held: '+reason)
                # Preserve which independent admission authorized this retry.
                proof=path/'supplemental-access/active.json'
                verified.append({'run':str(path),'assessment_sha256':runs.digest(path/'grading/assessment.json'),
                                 'supplemental_admission_sha256':runs.digest(proof) if proof.exists() else None})
        job.setdefault('dependency_retries',[]).append({'at':runs.now(),'previous_reason':job['reason'],
                                                       'verified_dependencies':verified})
        job.update(phase='waiting');job.pop('reason',None)
        runs.write(directory/'state.json',state)
        return job


def cooldown_members(state):
    result = []
    for job, path, config, phase in entries(state):
        member = next(m for m in job['handoff']['members'] if Path(m['directory']) == path)
        result.append((path, config, member['inputs']['route'], phase))
    return result


def controller_cooldown(directory, proof_path=None, *, observation_id=None, source_sha256=None, reason=None):
    """Explicit private controller import/release; never read executor answers."""
    directory = Path(directory).resolve()
    with lock(directory/'.gate.lock', blocking=True):
        state = runs.read(directory/'state.json')
        if proof_path is not None:
            file = Path(proof_path)
            if file.is_symlink() or file.stat().st_mode & 0o077:
                raise ValueError('Controller observation must be a private non-symlink file')
            proof = runs.read(file); path = Path(proof['run']).resolve()
            matches = [(cfg, route, phase) for p, cfg, route, phase in cooldown_members(state) if p == path]
            if len(matches) != 1: raise ValueError('Observation run must be a prepared member owned by this queue')
            config, route, phase = matches[0]
            if phase['phase'] in ('prepared', 'execution_starting', 'execution_running', 'execution_collecting'):
                raise ValueError('Controller import requires a collected execution, not a live actor statement')
            runs.verify(path)
            item = cooldowns.import_verified(state, path, config, route, proof)
            result = item['observation_id']
        else:
            cooldowns.release(state, observation_id, source_sha256, reason, runs.now())
            result = observation_id
        runs.write(directory/'state.json', state)
        return result


def _advance(directory):
    directory = Path(directory).resolve();policy = runs.read(directory/'policy.json');state = runs.read(directory/'state.json')
    cap = budget_cap(policy)
    if state['phase'] == 'halted': raise ValueError('Queue halted; reconcile saved state before resuming')
    prepare_jobs(directory, state, policy)
    paths = [p for _, p, _, _ in entries(state)]
    group_paths = [Path(j['handoff']['directory']) for j in state['jobs'].values() if j['prepared'] and j['handoff']['kind'] == 'comparison']
    with groups.locks([*paths, *group_paths]):
        reconcile(state)
        state['dispatch_holds'] = {}
        low_storage=storage_hold(directory,policy)
        if low_storage:state['dispatch_holds']['controller_storage']=low_storage
        def quota_hold(path):
            # Collected sources are cached by immutable file fingerprint. This
            # also sees a member collected earlier in the same group advance.
            cooldowns.refresh(state, cooldown_members(state))
            job, _, cfg, _ = next(item for item in entries(state) if item[1] == path)
            member = next(m for m in job['handoff']['members'] if Path(m['directory']) == path)
            return cooldowns.hold(state, cooldowns.binding(cfg, member['inputs']['route']), time.time())
        def execution_defer(path):
            observation = quota_hold(path)
            if not observation: return None
            seconds = runs.read(path/'config.json')['execution']['seconds']
            if observation['until'] is None or observation['until'] + seconds + 20 >= stamp(policy['expires_at']):
                return observation
            return None
        def active():
            current = entries(state)
            if any(s['phase'] == 'stopped' and s.get('stopped_role') and not s.get('stop_confirmed') for _, _, _, s in current):
                raise ValueError('Unconfirmed stop blocks this runner pool')
            running = [(runtime_identity(cfg[s['phase'].split('_')[0]]), p) for _, p, cfg, s in current if groups.active(s)]
            if len({r for r, _ in running}) != len(running): raise ValueError('Runtime already occupied twice')
            return running
        def guard(path, role, settings):
            deadline = stamp(policy['expires_at'])
            key = str(path)+':'+role
            def hold(reason):
                state['dispatch_holds'][key] = reason
                return False
            if STOP_REQUESTED: return hold('Controller shutdown requested')
            if time.time() + settings['seconds'] + 20 >= deadline: return hold('Insufficient remaining time for the full frozen budget')
            low_storage=storage_hold(directory,policy)
            if low_storage:return hold(low_storage)
            if role == 'execution':
                observation = quota_hold(path)
                if observation:
                    # Persist the private observation before refusing the new
                    # dispatch; grading and collection never consult this gate.
                    runs.write(directory/'state.json', state)
                    return hold(observation['reason'])
            job = next(j for j in state['jobs'].values() if any(Path(m['directory']) == path for m in j['handoff']['members']))
            if role == 'grading' and job['handoff'].get('grading_gate'):
                gate_file = directory/'inbox'/job['handoff']['id']/'grading-ready.json'
                if not gate_file.exists(): return hold('Awaiting independent controller readback and frozen grading release')
                if runs.digest(gate_file) != runs.read(gate_file.with_name('grading-ready-hash.json'))['sha256']:
                    raise ValueError('Verification gate changed')
                gate = runs.read(gate_file)
                if (gate['execution_sha256'][str(path)] != runs.digest(path/'run.json')
                    or gate['execution_files_sha256'][str(path)] != runs.frozen_files(path/'execution')
                    or gate['proofs'][str(path)] != runs.frozen_files(path/'grading-input/controller-verification')):
                    raise ValueError('Released verification does not match this frozen execution/proof')
            file = adapter_config(settings)
            if file:
                member = next(m for job in state['jobs'].values() for m in job['handoff']['members'] if Path(m['directory']) == path)
                if runs.digest(file) != member['inputs']['files'][str(file)]:
                    raise ValueError('Private adapter binding changed after handoff; no dispatch')
            resources = set(settings.get('resource_locks', []))
            for _, other, cfg, status in entries(state):
                if other != path and groups.active(status):
                    active_role = status['phase'].split('_')[0]
                    if runtime_identity(settings) == runtime_identity(cfg[active_role]):
                        return hold('Physical container occupied under another runtime identity')
                    if resources.intersection(cfg[active_role].get('resource_locks', [])):
                        return hold('Shared account/resource occupied')
            if key not in state['ledger']:
                amount = ceiling(path, role)
                if cap is not None and held(state) + amount > cap: return hold('Session ceiling exceeds remaining budget after in-flight/unknown reservations')
                state['ledger'][key] = {'ceiling_usd': amount, 'held_usd': amount, 'reserved_at': runs.now()}
                if chatgpt_grader(settings):
                    state['ledger'][key].update(billing_mode='chatgpt', account_cost_usd=None, account_credits=None,
                        reservation_scope='API dollars only; account usage is not free and remains separately unknown')
                # Durable reservation precedes an irreversible paid dispatch.
                runs.write(directory/'state.json', state)
            return {'deadline_epoch': min(deadline, settings.get('deadline_epoch', deadline))}
        for job in state['jobs'].values():
            if not job['prepared'] or job['phase'] in DONE: continue
            current = active()
            if len(current) > policy['max_concurrency']: raise ValueError('Active sessions exceed queue ceiling')
            own = {Path(m['directory']) for m in job['handoff']['members']}
            outside = [(r, p) for r, p in current if p not in own]
            try:
                if time.time() >= stamp(policy['expires_at']):
                    for path in own: groups.stop_member(path)
                    for path in own:
                        s = runs.read(path/'state.json')
                        if s.get('stopped_role') and s.get('stop_confirmed') and not (path/s['stopped_role']/'model-cost.json').exists():
                            cfg = runs.read(path/'config.json');role = s['stopped_role']
                            request = runs.stage_request(path, role, cfg[role]);request['handle'] = s.get('handle')
                            runs.collect(path, role, cfg[role], request)
                    job['phase'] = 'stopped'
                elif job['handoff']['kind'] == 'comparison':
                    # The guard checks physical identity. Group's existing runtime
                    # check still protects repeated logical IDs inside the group.
                    result = groups.advance(Path(job['handoff']['directory']),
                                            max_active=policy['max_concurrency']-len(outside), dispatch_guard=guard,
                                            execution_defer=execution_defer)
                    job['phase'] = result['phase']
                else:
                    path = next(iter(own));s = runs.read(path/'state.json');cfg = runs.read(path/'config.json')
                    role = 'execution' if s['phase'] == 'prepared' else 'grading'
                    if groups.active(s) or (len(current) < policy['max_concurrency'] and runtime_identity(cfg[role]) not in {r for r, _ in outside}):
                        job['phase'] = runs.advance(path, dispatch_guard=guard)['phase']
                    if job['phase'] in ('reviewed', 'recorded') and runs.read(path/'grading/assessment.json')['status'] != 'completed':
                        job['phase'] = 'needs_attention'
            except Exception as error:
                # A lost startup response never turns into another start.
                job.update(phase='needs_attention', reason=str(error))
                for path in own:
                    try: groups.stop_member(path)
                    except Exception as stop_error: job['stop_error'] = str(stop_error)
            runs.write(directory/'state.json', state)
        active()  # Also catches the final member's uncertain stop.
        reconcile(state)
    state.update(phase='expired' if time.time() >= stamp(policy['expires_at']) else
                 ('running' if any(j['phase'] not in DONE for j in state['jobs'].values()) else 'idle'),
                 held_usd=held(state), api_cost_summary=cost_summary(state), updated_at=runs.now())
    runs.write(directory/'state.json', state)
    return state


def halt(directory, reason):
    """Fatal accounting/ownership uncertainty must not leave paid workers running."""
    state = runs.read(directory/'state.json')
    errors = {}
    current = entries(state)
    with groups.locks([p for _, p, _, _ in current]):
        for job, path, cfg, _ in current:
            try:
                groups.stop_member(path)
                status = runs.read(path/'state.json')
                if status.get('stop_confirmed') and status.get('stopped_role') and not (path/status['stopped_role']/'model-cost.json').exists():
                    role = status['stopped_role'];request = runs.stage_request(path, role, cfg[role])
                    request['handle'] = status.get('handle')
                    runs.collect(path, role, cfg[role], request)
                if job['phase'] not in DONE: job['phase'] = 'needs_attention'
            except Exception as error:
                errors[str(path)] = str(error)
    state.update(phase='halted', halt_reason=reason, stop_errors=errors, updated_at=runs.now())
    try:
        reconcile(state)
    except Exception as error:
        # Preserve the halted state even when the accounting error caused it.
        errors['accounting'] = str(error)
    state['held_usd'] = held(state)
    runs.write(directory/'state.json', state)
    return state


def run_loop(directory, once=False):
    previous = None
    while True:
        if STOP_REQUESTED:
            halt(directory, 'Controller received SIGTERM/SIGINT');return
        try:
            state = advance(directory)
        except Exception as error:
            halt(directory, str(error))
            raise
        compact = {'phase': state['phase'], 'held_usd': state['held_usd'],
                   'jobs': {k: v['phase'] for k, v in state['jobs'].items()},
                   'dispatch_holds': state.get('dispatch_holds', {})}
        if compact != previous: print(json.dumps(compact), flush=True);previous = compact
        if STOP_REQUESTED:
            halt(directory, 'Controller received SIGTERM/SIGINT');return
        if once or state['phase'] == 'expired': return
        time.sleep(2)


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('init', 'submit', 'retry-dependency', 'release-grading', 'observe-cooldown', 'release-cooldown', 'run', 'status'))
    parser.add_argument('directory', type=Path)
    parser.add_argument('--spec', type=Path);parser.add_argument('--max-concurrency', type=int)
    budget = parser.add_mutually_exclusive_group()
    budget.add_argument('--budget-usd', type=float)
    budget.add_argument('--no-budget-cap', action='store_true', help='Explicitly authorize no queue API-dollar cap; deadline and per-run limits still apply')
    parser.add_argument('--expires-at');parser.add_argument('--pool')
    parser.add_argument('--storage-floor-bytes',type=int,default=1024**3)
    parser.add_argument('--job');parser.add_argument('--proofs', type=Path)
    parser.add_argument('--observation', type=Path);parser.add_argument('--observation-id')
    parser.add_argument('--source-sha256');parser.add_argument('--reason')
    parser.add_argument('--once', action='store_true');args = parser.parse_args()
    if args.no_budget_cap and args.action != 'init': parser.error('--no-budget-cap only applies when creating a new queue')
    if args.action == 'init': print(init(args.directory, max_concurrency=args.max_concurrency, budget_usd=args.budget_usd,
        no_budget_cap=args.no_budget_cap, expires_at=args.expires_at, pool=args.pool,
        storage_floor_bytes=args.storage_floor_bytes));return
    if args.action == 'submit': print(submit(args.directory, args.spec));return
    if args.action == 'retry-dependency':
        if not args.job:parser.error('--job is required')
        print(json.dumps(retry_dependency(args.directory,args.job)));return
    if args.action == 'release-grading': print(json.dumps(release_grading(args.directory, args.job, args.proofs)));return
    if args.action == 'observe-cooldown':
        if args.observation is None: parser.error('--observation is required')
        print(controller_cooldown(args.directory, args.observation));return
    if args.action == 'release-cooldown':
        if not all((args.observation_id, args.source_sha256, args.reason)):
            parser.error('--observation-id, --source-sha256 and --reason are required')
        print(controller_cooldown(args.directory, observation_id=args.observation_id,
              source_sha256=args.source_sha256, reason=args.reason));return
    if args.action == 'status': print(json.dumps(runs.read(args.directory/'state.json')));return
    # All queues for this operator's host use the same pool lock location.
    pool = hashlib.sha256(runs.read(args.directory/'policy.json')['pool'].encode()).hexdigest()
    lock_root = Path.home()/'.cache/agent-friendly-services/pools';lock_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    with lock(args.directory/'.controller.lock'), lock(lock_root/(pool+'.lock')):
        signal.signal(signal.SIGTERM, request_stop)
        signal.signal(signal.SIGINT, request_stop)
        run_loop(args.directory, args.once)


if __name__ == '__main__': main()
