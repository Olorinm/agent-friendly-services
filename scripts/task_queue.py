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
from pathlib import Path
import subprocess
import time

import pipeline as runs
import comparison_group as groups

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


def init(directory, *, max_concurrency, budget_usd, expires_at, pool):
    if type(max_concurrency) is not int or max_concurrency < 1: raise ValueError('Positive concurrency required')
    if type(budget_usd) not in (int, float) or not math.isfinite(budget_usd) or budget_usd <= 0:
        raise ValueError('Explicit positive model budget required')
    stamp(expires_at)
    if not isinstance(pool, str) or not pool.strip(): raise ValueError('Explicit pool identity required')
    directory = Path(directory).resolve();directory.mkdir(mode=0o700, parents=True, exist_ok=False)
    runs.write(directory/'policy.json', {'max_concurrency': max_concurrency, 'budget_usd': budget_usd,
                                       'expires_at': expires_at, 'pool': pool})
    runs.write(directory/'state.json', {'phase': 'idle', 'jobs': {}, 'ledger': {}, 'created_at': runs.now()})
    (directory/'inbox').mkdir(mode=0o700)
    return directory


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
    return {'task': task, 'route': route, 'files': {str(p): runs.digest(p) for p in files if p.is_file()}}


def adapter_config(settings):
    argv = settings['commands']['start']
    adapter = str((runs.ROOT/'scripts/runners/opencode/adapter.py').resolve())
    if not any(str(Path(arg).resolve()) == adapter for arg in argv if not arg.startswith('-')):
        return None  # Offline fixture adapters are never accepted by ceiling().
    if '--config' not in argv: raise ValueError('OpenCode adapter needs an explicit private config')
    return Path(argv[argv.index('--config')+1]).resolve()


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
        for role in ('execution', 'grading'):
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


def reconcile(state):
    for _, path, _, phase in entries(state):
        for role in ('execution', 'grading'):
            key = str(path)+':'+role
            row = state['ledger'].get(key)
            if not row: continue
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
        if any(d and d['phase'] in DONE and d['phase'] != 'reviewed' for d in deps):
            job.update(phase='blocked', reason='Prerequisite did not pass; no service failure inferred');continue
        if any(not d or d['phase'] != 'reviewed' for d in deps): continue
        if time.time() >= stamp(policy['expires_at']): continue
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


def _advance(directory):
    directory = Path(directory).resolve();policy = runs.read(directory/'policy.json');state = runs.read(directory/'state.json')
    if state['phase'] == 'halted': raise ValueError('Queue halted; reconcile saved state before resuming')
    prepare_jobs(directory, state, policy)
    paths = [p for _, p, _, _ in entries(state)]
    group_paths = [Path(j['handoff']['directory']) for j in state['jobs'].values() if j['prepared'] and j['handoff']['kind'] == 'comparison']
    with groups.locks([*paths, *group_paths]):
        reconcile(state)
        state['dispatch_holds'] = {}
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
                if held(state) + amount > policy['budget_usd']: return hold('Session ceiling exceeds remaining budget after in-flight/unknown reservations')
                state['ledger'][key] = {'ceiling_usd': amount, 'held_usd': amount, 'reserved_at': runs.now()}
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
                                            max_active=policy['max_concurrency']-len(outside), dispatch_guard=guard)
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
                 held_usd=held(state), updated_at=runs.now())
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
    parser.add_argument('action', choices=('init', 'submit', 'release-grading', 'run', 'status'))
    parser.add_argument('directory', type=Path)
    parser.add_argument('--spec', type=Path);parser.add_argument('--max-concurrency', type=int)
    parser.add_argument('--budget-usd', type=float);parser.add_argument('--expires-at');parser.add_argument('--pool')
    parser.add_argument('--job');parser.add_argument('--proofs', type=Path)
    parser.add_argument('--once', action='store_true');args = parser.parse_args()
    if args.action == 'init': print(init(args.directory, max_concurrency=args.max_concurrency, budget_usd=args.budget_usd, expires_at=args.expires_at, pool=args.pool));return
    if args.action == 'submit': print(submit(args.directory, args.spec));return
    if args.action == 'release-grading': print(json.dumps(release_grading(args.directory, args.job, args.proofs)));return
    if args.action == 'status': print(json.dumps(runs.read(args.directory/'state.json')));return
    # All queues for this operator's host use the same pool lock location.
    pool = hashlib.sha256(runs.read(args.directory/'policy.json')['pool'].encode()).hexdigest()
    lock_root = Path.home()/'.cache/agent-friendly-services/pools';lock_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    with lock(args.directory/'.controller.lock'), lock(lock_root/(pool+'.lock')):
        signal.signal(signal.SIGTERM, request_stop)
        signal.signal(signal.SIGINT, request_stop)
        run_loop(args.directory, args.once)


if __name__ == '__main__': main()
