#!/usr/bin/env python3
"""Feed independently designed/materialized work to an existing cloud queue.

Controller-owned plans provide every runtime, service and material boundary.
Agent output selects approved IDs and supplies raw data, never shell commands.
The service queue runs independently, so ordinary jobs need no chat handoff.
"""
import argparse
from copy import deepcopy
import json
from pathlib import Path
import signal
import time

import pipeline as runs
import role_handoff as roles
import task_queue as queue
import work_package

STOP = False
TERMINAL = {'submitted', 'held'}


def request_stop(*unused):
    global STOP
    STOP = True


def init(directory, plan_path):
    plan = runs.read(plan_path)
    if plan.get('schema_version') != 1 or not plan.get('packages'):
        raise ValueError('Explicit producer package plan required')
    cap = plan.get('max_preparation_concurrency')
    if type(cap) is not int or cap < 1: raise ValueError('Positive preparation concurrency required')
    policy = runs.read(Path(plan['queue']) / 'policy.json')
    if (type(plan.get('max_total_concurrency')) is not int
            or cap + policy['max_concurrency'] > plan['max_total_concurrency']
            or queue.stamp(policy['expires_at']) != plan.get('deadline_epoch')):
        raise ValueError('Preparation and queue must fit one explicit concurrency/deadline envelope')
    ids = [item['id'] for item in plan['packages']]
    if len(ids) != len(set(ids)): raise ValueError('Duplicate preparation package identity')
    source_files = {str(roles.HERE / 'roles/material_preparation/AGENTS.md'):
                    runs.digest(roles.HERE / 'roles/material_preparation/AGENTS.md')}
    runtimes = set()
    package_runtimes = []
    input_trees = {}
    for item in plan['packages']:
        work_package.identity(item['id'])
        for key in ('design_settings', 'preparation_settings', 'policy'):
            file = Path(item[key])
            if not file.is_absolute() or file.is_symlink() or not file.is_file():
                raise ValueError('Controller source must be a regular absolute file')
            source_files[str(file)] = runs.digest(file)
        own_runtimes = set()
        for key in ('design_settings', 'preparation_settings'):
            settings = runs.read(item[key]); bound = roles.settings_binding(settings)
            source_files[bound['adapter_file']] = bound['adapter_sha256']
            if settings.get('deadline_epoch') != plan['deadline_epoch']:
                raise ValueError('Preparation role differs from plan deadline')
            runtimes.add(queue.runtime_identity(settings))
            own_runtimes.add(queue.runtime_identity(settings))
        if cap > 1 and any(own_runtimes.intersection(previous) for previous in package_runtimes):
            raise ValueError('Parallel preparation packages cannot share physical runtimes')
        package_runtimes.append(own_runtimes)
        packet = Path(item['design_input'])
        input_trees[str(packet)] = roles.tree(packet)
        for name, sha in input_trees[str(packet)].items(): source_files[str(packet / name)] = sha
    if len(runtimes) < min(cap, len(plan['packages'])):
        raise ValueError('Concurrent preparation needs distinct physical runtimes')
    # Preparation credentials and workspaces must never share an executor or grader.
    for item in plan['packages']:
        for target in runs.read(item['policy'])['targets'].values():
            for role in ('execution', 'grading'):
                settings = target['config'][role]
                config_file = queue.adapter_config(settings)
                if config_file is not None: source_files[str(config_file)] = runs.digest(config_file)
                if queue.runtime_identity(settings) in runtimes:
                    raise ValueError('Preparation must not share test or grader runtimes')
    directory = Path(directory).resolve(); directory.mkdir(mode=0o700, parents=True, exist_ok=False)
    runs.write(directory / 'plan.json', plan)
    runs.write(directory / 'source-hashes.json', source_files)
    runs.write(directory / 'input-trees.json', input_trees)
    runs.write(directory / 'state.json', {'phase': 'prepared', 'created_at': runs.now(),
               'plan_sha256': runs.digest(directory / 'plan.json'),
               'frozen_plan': plan,
               'packages': {identity: {'phase': 'waiting'} for identity in ids}})
    return directory


def verify(directory, state):
    if runs.digest(directory / 'plan.json') != state['plan_sha256']:
        raise ValueError('Frozen producer plan changed')
    for name, sha in runs.read(directory / 'source-hashes.json').items():
        if runs.digest(name) != sha: raise ValueError('Frozen preparation source changed')
    for root, files in runs.read(directory / 'input-trees.json').items():
        if roles.tree(root) != files: raise ValueError('Frozen preparation input membership changed')
    return runs.read(directory / 'plan.json')


def preparation_packet(directory, item, policy):
    design = directory / item['id'] / 'design/output/task-design.json'
    inputs = directory / item['id'] / 'preparation-input'
    # A crash here leaves this preparation visibly partial, never starts a model.
    inputs.mkdir(mode=0o700, parents=True, exist_ok=False)
    (inputs / 'AGENTS.md').write_bytes((roles.HERE / 'roles/material_preparation/AGENTS.md').read_bytes())
    (inputs / 'task-design.json').write_bytes(design.read_bytes())
    allowed = {'package_id': item['id'], 'designer_sha256': runs.digest(design),
               'rounds': policy.get('rounds', [1]), 'generated_materials': policy.get('generated_materials', {}),
               'targets': {key: {'service': row['config']['service'], 'route': row['config']['route']}
                           for key, row in policy['targets'].items()}}
    (inputs / 'preparation-boundary.json').write_text(json.dumps(allowed, ensure_ascii=False, indent=2) + '\n')
    (inputs / 'prompt.txt').write_text(
        'Prepare the original synthetic data required by task-design.json. '
        'Read preparation-boundary.json for the only permitted target IDs, rounds, material files and raw data schemas. '
        'Bind designer_sha256 to the actual bytes. Do not call any candidate service, fetch current exchange rates, '
        'write a solution, change task requirements, or invent readiness. '
        'A draft user ledger may contain deliberately unverified claims as clearly labeled synthetic INPUT, '
        'never a reference answer or an assertion about real service data. '
        'Write material-preparation.json and actual materials files; use held with specific blockers when necessary.\n')
    return inputs


def binding(job):
    output = job / 'output'
    return {'directory': str(output), 'receipt_sha256': runs.digest(output / 'receipt.json'),
            'proof_sha256': runs.digest(output / 'role-collection-proof.json')}


def settle(job, row, reason):
    """An ambiguous handle stays reserved until stop is actually confirmed."""
    result = roles.advance(job, halt=True)
    safe = result['phase'] in ('collected', 'held', 'stopped')
    row.update(phase='held' if safe else 'attention', reason=reason, role_phase=result['phase'])
    if not safe: row['stop_unconfirmed'] = True


def tick(directory, *, halt=False):
    directory = Path(directory).resolve()
    with queue.lock(directory / '.producer.lock', blocking=True):
        state = runs.read(directory / 'state.json')
        plan = state['frozen_plan']
        try: plan = verify(directory, state)
        except Exception as error:
            # A changed input/plan cannot prevent stopping already allocated handles.
            halt = True; state['frozen_source_error'] = str(error)
        halt = halt or time.time() >= plan['deadline_epoch']
        if state['phase'] in ('finished', 'stopped') and not halt: return state
        active = sum(row['phase'] in ('designing', 'preparing', 'attention') for row in state['packages'].values())
        for item in plan['packages']:
            active = sum(row['phase'] in ('designing', 'preparing', 'attention') for row in state['packages'].values())
            row = state['packages'][item['id']]
            root = directory / item['id']; design = root / 'design'; preparation = root / 'preparation'
            try:
                if halt:
                    unconfirmed = False
                    for job in (design, preparation):
                        if (job / 'state.json').exists():
                            result = roles.advance(job, halt=True)
                            unconfirmed |= result['phase'] not in ('collected', 'held', 'stopped')
                    if unconfirmed:
                        row.update(phase='attention', reason='Stop unconfirmed; preserve reservation and reconcile handles')
                    elif row['phase'] not in TERMINAL:
                        row.update(phase='held', reason='Producer stopped; role attempts retained, no service failure inferred')
                    continue
                if row['phase'] in TERMINAL or row['phase'] == 'attention': continue
                if row['phase'] == 'waiting':
                    if active >= plan['max_preparation_concurrency']: continue
                    if queue.storage_hold(Path(plan['queue']), runs.read(Path(plan['queue']) / 'policy.json')):
                        row['waiting_reason'] = 'Low storage; no preparation model allocated'; continue
                    # Save intention first. A partial prepare is attention, never silently replayed.
                    row.update(phase='designing'); runs.write(directory / 'state.json', state)
                    roles.prepare(design, 'task_design', item['design_input'], item['design_settings'])
                    active += 1
                if row['phase'] == 'designing':
                    result = roles.advance(design)
                    if result['phase'] == 'collected':
                        payload = runs.read(design / 'output/task-design.json')
                        if payload.get('package_id') != item['id'] or payload.get('status') != 'ready':
                            row.update(phase='held', reason='Designer did not produce an applicable ready package'); active -= 1; continue
                        inputs = preparation_packet(directory, item, runs.read(item['policy']))
                        row.update(phase='preparing'); runs.write(directory / 'state.json', state)
                        roles.prepare(preparation, 'material_preparation', inputs, item['preparation_settings'])
                    elif result['phase'] in ('held', 'stopped', 'needs_attention', 'uncertain_start', 'starting'):
                        settle(design, row, 'Design role needs inspection')
                        if row['phase'] == 'held': active -= 1
                        continue
                if row['phase'] == 'preparing':
                    result = roles.advance(preparation)
                    if result['phase'] == 'collected':
                        design_proof = runs.read(design / 'output/role-collection-proof.json')
                        prepare_proof = runs.read(preparation / 'output/role-collection-proof.json')
                        if design_proof['session_id'] == prepare_proof['session_id']:
                            raise ValueError('Design and preparation need independent sessions')
                        policy = deepcopy(runs.read(item['policy']))
                        policy['designer_collection'] = binding(design)
                        policy['preparer_collection'] = binding(preparation)
                        compiled_policy = root / 'runtime-policy.json'
                        if compiled_policy.exists():
                            if runs.read(compiled_policy) != policy: raise ValueError('Compiled role binding changed')
                        else: runs.write(compiled_policy, policy)
                        result = work_package.submit_package(plan['queue'], design / 'output/task-design.json',
                                preparation / 'output/material-preparation.json', compiled_policy, root / 'compiled')
                        row.update(phase='submitted', submitted_at=runs.now(),
                                   compiled_jobs=len([x for x in result['jobs'] if x['status'] != 'held']),
                                   held_jobs=len([x for x in result['jobs'] if x['status'] == 'held']))
                        active -= 1
                    elif result['phase'] in ('held', 'stopped', 'needs_attention', 'uncertain_start', 'starting'):
                        settle(preparation, row, 'Preparation role needs inspection')
                        if row['phase'] == 'held': active -= 1
            except Exception as error:
                # Do not turn a partial source/dispatch failure into a second start.
                row.update(phase='held', reason=str(error), error_type=type(error).__name__)
                safe = True
                # This failure owns only these roles; other packages continue.
                for job in (design, preparation):
                    if (job / 'state.json').exists():
                        try:
                            result = roles.advance(job, halt=True)
                            safe &= result['phase'] in ('collected', 'held', 'stopped')
                        except Exception as stop_error:
                            safe = False; row['stop_error'] = type(stop_error).__name__
                if safe: active = max(0, active - 1)
                else: row['phase'] = 'attention'
            runs.write(directory / 'state.json', state)
        state['updated_at'] = runs.now()
        attention = any(x['phase'] == 'attention' for x in state['packages'].values())
        state['phase'] = ('stop_needs_attention' if attention else 'stopped') if halt else (
            'finished' if all(x['phase'] in TERMINAL for x in state['packages'].values()) else 'running')
        runs.write(directory / 'state.json', state)
        return state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('init', 'run', 'stop', 'status'))
    parser.add_argument('directory', type=Path); parser.add_argument('--plan', type=Path)
    parser.add_argument('--once', action='store_true'); args = parser.parse_args()
    if args.action == 'init':
        print(init(args.directory, args.plan)); return
    if args.action == 'status':
        print(json.dumps(runs.read(args.directory / 'state.json'))); return
    signal.signal(signal.SIGTERM, request_stop); signal.signal(signal.SIGINT, request_stop)
    with queue.lock(args.directory / '.controller.lock'):
        while True:
            state = tick(args.directory, halt=STOP or args.action == 'stop')
            print(json.dumps({'phase': state['phase'], 'packages': state['packages']}), flush=True)
            if args.once or state['phase'] in ('finished', 'stopped', 'stop_needs_attention'): return
            time.sleep(3)


if __name__ == '__main__': main()
