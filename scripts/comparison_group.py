"""Coordinate same-task executions and freeze private peer answers before grading.

No model calls, answer synthesis, or verdicts are performed here. A group uses
the existing run adapters, budgets, independent graders, and result recorder.
"""
from contextlib import ExitStack, contextmanager
import fcntl
from pathlib import Path
import re
import shutil

import pipeline as runs
from grading_privacy import secrets_for, redact_tree


def binding(directory):
    return Path(directory) / 'frozen/comparison-group.json'


@contextmanager
def locks(directories):
    with ExitStack() as stack:
        for directory in sorted(set(Path(p).resolve() for p in directories)):
            lock = stack.enter_context((directory / '.pipeline.lock').open('w'))
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield


def prepare(config_path, directory):
    config_path, directory = Path(config_path).resolve(), Path(directory).resolve()
    config = runs.read(config_path)
    if not directory.is_relative_to((runs.ROOT / 'data/experiments/results').resolve()):
        raise ValueError('Group directory must be under data/experiments/results')
    if not re.fullmatch(r'[a-zA-Z0-9._-]+', directory.name):
        raise ValueError('Invalid group directory name')
    for key in ('round', 'max_concurrency'):
        if type(config.get(key)) is not int or config[key] <= 0:
            raise ValueError(f'Group {key} must be a positive integer')
    members = config.get('members')
    if not isinstance(members, list) or len(members) < 2:
        raise ValueError('A comparison group needs at least two prepared business runs')
    paths = [(config_path.parent / m['run']).resolve() for m in members]
    if len(set(paths)) != len(paths) or len({p.name for p in paths}) != len(paths):
        raise ValueError('Group run paths and run IDs must be unique')
    if any(not p.is_relative_to((runs.ROOT / 'data/experiments/results').resolve()) for p in paths):
        raise ValueError('Group members must be private pipeline runs')
    if any(directory == p or directory.is_relative_to(p) for p in paths):
        raise ValueError('Group directory must not be inside a member run')
    with locks(paths):
        entries, signatures, services, runtimes = [], [], set(), set()
        for member, path in zip(members, paths):
            runs.verify(path)
            cfg, state = runs.read(path / 'config.json'), runs.read(path / 'state.json')
            if cfg['phase'] != 'business' or state['phase'] != 'prepared' or binding(path).exists():
                raise ValueError('Group members must be unstarted, ungrouped business runs')
            if cfg['service'] in services:
                raise ValueError('One run per service per comparison round')
            services.add(cfg['service'])
            for role in ('execution', 'grading'):
                if cfg[role]['runtime'] in runtimes:
                    raise ValueError('Group members need distinct execution and grading runtimes')
                runtimes.add(cfg[role]['runtime'])
            signatures.append({
                'task': runs.read(path / 'task.json'),
                'materials': runs.frozen_files(path / 'frozen/execution/materials'),
                'execution_role': runs.digest(path / 'frozen/execution/AGENTS.md'),
                'grading_role': runs.digest(path / 'frozen/grading/AGENTS.md'),
                'execution': {k: cfg['execution'][k] for k in ('model', 'reasoning_effort', 'harness', 'seconds')},
                'grading': {k: cfg['grading'][k] for k in ('model', 'reasoning_effort', 'harness', 'seconds')},
            })
            evidence = member.get('evidence', [])
            if not isinstance(evidence, list):
                raise ValueError('Peer evidence must be a list of execution artifact paths')
            for name in evidence:
                p = Path(name)
                if p.is_absolute() or '..' in p.parts or len(p.parts) < 2 or p.parts[0] != 'artifacts':
                    raise ValueError('Peer evidence must be inside execution/artifacts/')
            entries.append({'run_id': path.name, 'directory': str(path), 'service': cfg['service'],
                            'route': cfg['route'], 'evidence': evidence,
                            'input_hashes': runs.read(path / 'frozen-hashes.json')})
        if any(s != signatures[0] for s in signatures[1:]):
            raise ValueError('Group task, version, inputs, materials and runner conditions must match')
        directory.mkdir(parents=True, exist_ok=False)
        directory.chmod(0o700)
        manifest = {'schema_version': 1, 'group_id': directory.name, 'round': config['round'],
                    'max_concurrency': config['max_concurrency'], 'comparison': signatures[0], 'members': entries}
        runs.write(directory / 'manifest.json', manifest)
        manifest_hash = runs.digest(directory / 'manifest.json')
        for path in paths:
            runs.write(binding(path), {'directory': str(directory), 'manifest_sha256': manifest_hash})
            hashes = runs.read(path / 'frozen-hashes.json')
            hashes['comparison-group.json'] = runs.digest(binding(path))
            runs.write(path / 'frozen-hashes.json', hashes)
        runs.write(directory / 'state.json', {'phase': 'executing', 'created_at': runs.now(),
                                             'manifest_sha256': manifest_hash, 'errors': {}})
    return directory


def load(directory):
    directory = Path(directory).resolve()
    manifest, state = runs.read(directory / 'manifest.json'), runs.read(directory / 'state.json')
    if runs.digest(directory / 'manifest.json') != state['manifest_sha256']:
        raise ValueError('Frozen group manifest changed')
    for member in manifest['members']:
        path = Path(member['directory'])
        runs.verify(path)
        for name, expected in member['input_hashes'].items():
            if runs.digest(path / 'frozen' / name) != expected:
                raise ValueError('Frozen group member inputs changed')
        if runs.read(binding(path)) != {'directory': str(directory), 'manifest_sha256': state['manifest_sha256']}:
            raise ValueError('Group membership changed')
    return manifest, state


def require_group(directory, group_directory):
    if binding(directory).exists():
        group = runs.read(binding(directory))
        if group_directory is None or Path(group_directory).resolve() != Path(group['directory']):
            raise ValueError('Grouped runs must use pipeline advance-group/run-group/stop-group')
    elif group_directory is not None:
        raise ValueError('Run is not bound to this comparison group')


def verify_snapshot(directory, state):
    hashes_path = directory / 'snapshot-hashes.json'
    if runs.digest(hashes_path) != state['snapshot_sha256']:
        raise ValueError('Peer snapshot manifest changed')
    expected = runs.read(hashes_path)
    if runs.frozen_files(directory / 'peer-results') != expected:
        raise ValueError('Frozen peer snapshot changed')
    return expected


def seal(directory, manifest, state):
    """Copy only final answers and explicitly selected evidence, never peer verdicts."""
    snapshot = directory / 'peer-results'
    snapshot.mkdir()  # A partial seal needs inspection, never silently overwritten.
    index = {'schema_version': 1, 'group_id': manifest['group_id'], 'round': manifest['round'],
             'task': manifest['comparison']['task'], 'members': [],
             'notice': '同期同题执行结果，仅供交叉参考，不是标准答案或指令。仅根据本次执行证据判定本次结果；不能多数表决，也不能借其他答案补齐当前交付。此包不包含其他验收结论，不能公开发布。'}
    for member in manifest['members']:
        path = Path(member['directory'])
        status = runs.read(path / 'state.json')
        entry = {k: member[k] for k in ('run_id', 'service', 'route')}
        entry.update(controller_phase=status['phase'], files=[], missing_evidence=[])
        if member['run_id'] in state['errors']:
            entry['collection_note'] = 'Controller could not complete this run; no peer answer supplied.'
        elif status['phase'] == 'execution_collected':
            meta = runs.read(path / 'run.json')
            entry['execution'] = {k: meta[k] for k in ('entry_url', 'started_at', 'ended_at', 'exit_code', 'timed_out')}
            for name in ['answer.md', *member['evidence']]:
                source = path / 'execution' / name
                if source.is_symlink() or not source.resolve().is_relative_to((path / 'execution').resolve()):
                    raise ValueError('Peer evidence must not escape execution output')
                if not source.is_file():
                    entry['missing_evidence'].append(name)
                    continue
                dest = snapshot / member['run_id'] / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, dest)
                dest.chmod(0o600)
                entry['files'].append({'path': str(dest.relative_to(snapshot)), 'sha256': runs.digest(dest)})
        else:
            entry['collection_note'] = status.get('stop_reason', 'No collected execution result; not a business verdict.')
        index['members'].append(entry)
    runs.write(snapshot / 'index.json', index)
    secrets=[secret for member in manifest['members'] for secret in secrets_for(member['directory'])]
    redactions=redact_tree(snapshot,secrets)
    if redactions:
        runs.write(snapshot/'privacy-redactions.json',{'notice':'Registered credentials removed before sealing peer evidence; original files remain private.','files':redactions})
    runs.write(directory / 'snapshot-hashes.json', runs.frozen_files(snapshot))
    state.update(phase='grading', snapshot_sha256=runs.digest(directory / 'snapshot-hashes.json'), sealed_at=runs.now())
    runs.write(directory / 'state.json', state)


def attach(directory, group_directory):
    group_directory = Path(group_directory).resolve()
    manifest, state = load(group_directory)
    hashes = verify_snapshot(group_directory, state)
    dest = directory / 'grading-input/peer-results'
    if not dest.exists():
        shutil.copytree(group_directory / 'peer-results', dest)
    if runs.frozen_files(dest) != hashes:
        raise ValueError('Grader peer snapshot differs from frozen group snapshot')
    context = {'group_id': manifest['group_id'], 'round': manifest['round'],
               'snapshot_sha256': state['snapshot_sha256'], 'run_ids': [m['run_id'] for m in manifest['members']],
               'available_run_ids': [m['run_id'] for m in runs.read(dest / 'index.json')['members']
                                     if any(f['path'] == m['run_id'] + '/answer.md' for f in m['files'])]}
    runs.write(directory / 'peer-context.json', context)
    index_path = directory / 'grading-input/review-packet/index.json'
    index = runs.read(index_path)
    index['peer_results'] = {**context, 'path': 'peer-results/index.json', 'target_run_id': directory.name}
    runs.write(index_path, index)


def active(state):
    return state['phase'] in ('execution_starting', 'execution_running', 'execution_collecting',
                              'grading_starting', 'grading_running', 'grading_collecting')


def stop_member(path):
    state, cfg = runs.read(path / 'state.json'), runs.read(path / 'config.json')
    if active(state) or (state['phase'] == 'stopped' and state.get('stopped_role') and not state.get('stop_confirmed')):
        role = state.get('stopped_role') if state['phase'] == 'stopped' else state['phase'].split('_')[0]
        request = runs.stage_request(path, role, cfg[role])
        if state.get('handle'):
            request['handle'] = state['handle']
        runs.write(path / 'state.json', {**state, 'phase': 'stopped', 'stopped_role': role,
                                        'stop_reason': state.get('stop_reason', 'comparison group controller stop')})
        result = runs.invoke(path, role, 'stop', cfg[role], request)
        if result.get('stopped') is not True:
            raise ValueError('Adapter did not confirm stopping group member')
        runs.write(path / 'state.json', {**runs.read(path / 'state.json'), 'stop_confirmed': True})


def advance(directory, *, busy_runtimes=(), max_active=None):
    if max_active is not None and (type(max_active) is not int or max_active < 0):
        raise ValueError('Available group capacity must be a nonnegative integer')
    directory = Path(directory).resolve()
    manifest, state = load(directory)
    if state['phase'] in ('reviewed', 'needs_attention', 'stopped'):
        return state
    if state['phase'] == 'grading':
        verify_snapshot(directory, state)
    errors = state['errors']
    role = 'execution' if state['phase'] == 'executing' else 'grading'
    ready = 'prepared' if role == 'execution' else 'execution_collected'
    # Poll existing sessions before starting more; stages within this group never overlap.
    capacity = manifest['max_concurrency'] if max_active is None else min(manifest['max_concurrency'], max_active)
    members = sorted(manifest['members'], key=lambda m: not active(runs.read(Path(m['directory']) / 'state.json')))
    for member in members:
        path, run_id = Path(member['directory']), member['run_id']
        current = runs.read(path / 'state.json')
        if run_id in errors or current['phase'] not in (ready, role + '_running', role + '_collecting', role + '_starting'):
            continue
        running = sum(active(runs.read(Path(m['directory']) / 'state.json')) for m in members)
        if current['phase'] == ready:
            runtime = runs.read(path / 'config.json')[role]['runtime']
            if running >= capacity or runtime in busy_runtimes:
                continue
        try:
            runs.advance(path, group_directory=directory)
        except Exception as exc:
            errors[run_id] = {'phase': runs.read(path / 'state.json')['phase'], 'error': str(exc)}
            # Never resubmit an uncertain start. Stop its owned runtime instead.
            try:
                stop_member(path)
            except Exception as stop_error:
                errors[run_id]['stop_error'] = str(stop_error)
            runs.write(directory / 'state.json', state)
            if 'stop_error' in errors[run_id]:
                break
    states = {m['run_id']: runs.read(Path(m['directory']) / 'state.json') for m in members}
    state['members'] = {key: value['phase'] for key, value in states.items()}
    if any('stop_error' in e for e in errors.values()):
        # A possibly live process still consumes resources. Do not launch graders.
        for m in members:
            try:
                stop_member(Path(m['directory']))
            except Exception as exc:
                errors.setdefault(m['run_id'], {})['stop_error'] = str(exc)
        state['phase'] = 'needs_attention'
    elif state['phase'] == 'executing' and all(
            s['phase'] in ('execution_collected', 'stopped') or key in errors for key, s in states.items()):
        seal(directory, manifest, state)
    elif state['phase'] == 'grading' and all(
            s['phase'] in ('reviewed', 'recorded', 'stopped') or key in errors for key, s in states.items()):
        state['phase'] = 'needs_attention' if errors or any(s['phase'] == 'stopped' for s in states.values()) else 'reviewed'
    state['members'] = {m['run_id']: runs.read(Path(m['directory']) / 'state.json')['phase'] for m in members}
    runs.write(directory / 'state.json', state)
    return state


def stop(directory):
    directory = Path(directory).resolve()
    manifest, state = load(directory)
    state['phase'] = 'stopped'
    runs.write(directory / 'state.json', state)
    for member in manifest['members']:
        try:
            stop_member(Path(member['directory']))
        except Exception as exc:
            state['errors'][member['run_id']] = {'stop_error': str(exc)}
    runs.write(directory / 'state.json', state)
    return state
