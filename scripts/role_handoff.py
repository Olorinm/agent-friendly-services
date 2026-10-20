#!/usr/bin/env python3
"""Durable, private cloud design/material jobs using the official Codex adapter.

This producer never evaluates a service or publishes results. Its verified
collected files can be consumed by work_package; model text is not authority
to launch commands, change resources or bypass admission.
"""
import argparse
from datetime import datetime, timezone
from copy import deepcopy
import importlib.util
import json
import re
import shutil
from pathlib import Path
import time

import pipeline as runs
from adapter_usage import read_usage
from session_usage import extract_usage
from task_queue import lock

HERE = Path(__file__).resolve().parent
ROLES = {'task_design': 'task-design.json', 'material_preparation': 'material-preparation.json'}


def tree(path):
    path = Path(path)
    if path.is_symlink() or not path.is_dir():
        raise ValueError('Real packet directory required')
    result = {}
    for file in path.rglob('*'):
        if file.is_symlink() or not (file.is_file() or file.is_dir()):
            raise ValueError('Packet links and special files forbidden')
        if file.is_file(): result[str(file.relative_to(path))] = runs.digest(file)
    return result


def settings_binding(settings):
    if (settings.get('model') != 'gpt-6.1-sol'
            or settings.get('reasoning_effort') not in ('medium', 'high')
            or settings.get('billing_mode') != 'chatgpt'
            or settings.get('harness', {}).get('name') != 'codex'
            or not settings['harness'].get('version')
            or not settings['harness'].get('mode')
            or type(settings.get('seconds')) is not int or settings['seconds'] <= 0
            or not isinstance(settings.get('runtime'), str)):
        raise ValueError('Explicit Sol medium/high account-billed role settings required')
    adapter = HERE / 'runners/codex/adapter.py'
    configs = []
    for operation in ('start', 'status', 'collect', 'stop'):
        argv = settings.get('commands', {}).get(operation, [])
        if (not isinstance(argv, list) or not all(isinstance(arg, str) for arg in argv)
                or str(adapter) not in argv or operation not in argv
                or '{request}' not in argv or '--config' not in argv):
            raise ValueError('Controller-owned official Codex commands required')
        configs.append(Path(argv[argv.index('--config') + 1]))
    if len(set(configs)) != 1 or configs[0].is_symlink() or not configs[0].is_file():
        raise ValueError('One immutable private adapter binding required')
    config = runs.read(configs[0])
    if config.get('billing_mode') != 'chatgpt' or settings['runtime'] not in config['containers']:
        raise ValueError('Role runtime/account differs from adapter')
    sources = {name: runs.digest(HERE / 'runners/codex' / name)
               for name in ('worker.py', 'normalize.py', 'artifact_capture.py')}
    sources['session_usage.py'] = runs.digest(HERE / 'session_usage.py')
    return {'adapter_file': str(configs[0]), 'adapter_sha256': runs.digest(configs[0]),
            'adapter_config': config, 'adapter_source_sha256': runs.digest(adapter), 'runtime_sources': sources}


def prepare(directory, role, input_dir, settings_path):
    if role not in ROLES: raise ValueError('Unsupported preparation role')
    directory = Path(directory).resolve()
    if not re.fullmatch(r'[A-Za-z0-9._-]+', directory.name): raise ValueError('Invalid job ID')
    settings = runs.read(settings_path)
    binding = settings_binding(settings)
    deadline = settings.get('deadline_epoch')
    if type(deadline) not in (int, float) or not time.time() < deadline:
        raise ValueError('Future explicit role deadline required')
    files = tree(input_dir)
    if not all(name in files for name in ('AGENTS.md', 'prompt.txt')):
        raise ValueError('Explicit frozen role and prompt required')
    directory.mkdir(mode=0o700, parents=True, exist_ok=False)
    shutil.copytree(input_dir, directory / 'input')
    request = {'run_id': directory.name, 'role': role, 'fresh_session': True,
               'input': str(directory / 'input'), 'output': str(directory / 'output'),
               **{key: settings[key] for key in ('model', 'reasoning_effort', 'harness',
                                                'seconds', 'runtime', 'deadline_epoch', 'billing_mode')}}
    runs.write(directory / 'manifest.json', {'role': role, 'created_at': runs.now(),
               'input_files': files, 'settings': settings, 'request': request, **binding})
    runs.write(directory / 'state.json', {'phase': 'prepared', 'created_at': runs.now()})
    return directory


def verify(directory):
    manifest = runs.read(directory / 'manifest.json')
    if manifest['role'] not in ROLES or tree(directory / 'input') != manifest['input_files']:
        raise ValueError('Frozen role input changed')
    binding = settings_binding(manifest['settings'])
    if any(binding[key] != manifest[key]
           for key in ('adapter_file', 'adapter_sha256', 'adapter_source_sha256', 'runtime_sources')):
        raise ValueError('Frozen preparation runtime/source changed')
    return manifest


def invoke(directory, manifest, operation, handle=None):
    request = dict(manifest['request'])
    if handle: request['handle'] = handle
    result = runs.invoke(directory, manifest['role'], operation, manifest['settings'], request)
    runs.write(directory / (manifest['role'] + '-' + operation + '-result.json'), result)
    return result


def validate_collection(directory, manifest):
    output = directory / 'output'
    tree(output)
    receipt = runs.read(output / 'receipt.json')
    settings = manifest['settings']; role = manifest['role']
    handle = directory.name + '-' + role
    if (runs.read(directory / (role + '-start.json')) != manifest['request']
            or runs.read(directory / (role + '-start-result.json')).get('handle') != handle
            or runs.read(directory / (role + '-collect.json')) != {**manifest['request'], 'handle': handle}
            or runs.read(directory / (role + '-collect-result.json')).get('collected') is not True):
        raise ValueError('Actual formal role start and collection required')
    if (receipt.get('role') != role or receipt.get('exit_code') != 0
            or receipt.get('timed_out') is not False or receipt.get('input_verified') is not True
            or receipt.get('billing_mode') != 'chatgpt' or not receipt.get('isolation')
            or receipt.get('workspace') != '/workspace/' + handle):
        raise ValueError('No successful verified role receipt')
    for key in ('model', 'reasoning_effort', 'harness', 'runtime'):
        if receipt.get(key) != settings[key]: raise ValueError('Role receipt mismatch: ' + key)
    session = receipt.get('session_id', '')
    if not re.fullmatch(r'[0-9a-fA-F-]{36}', session): raise ValueError('Actual new role session required')
    if receipt.get('runtime_code_preflight', {}).get('source_sha256') != manifest['runtime_sources']:
        raise ValueError('Role runtime source mismatch')
    if not re.fullmatch(r'sha256:[0-9a-f]{64}', receipt.get('runtime_image_id', '')):
        raise ValueError('Actual role image provenance required')
    start, end = (datetime.fromisoformat(receipt[key]) for key in ('started_at', 'ended_at'))
    created = datetime.fromisoformat(manifest['created_at'])
    if (start.tzinfo is None or end.tzinfo is None or start < created
            or not 0 <= (end - start).total_seconds() <= settings['seconds']
            or end.timestamp() > min(time.time() + 5, settings['deadline_epoch'])):
        raise ValueError('Invalid role runtime timestamps')
    events = [json.loads(line) for line in (output / 'events.jsonl').read_text().splitlines() if line.strip()]
    if (not any(row.get('type') == 'thread.started' and row.get('thread_id') == session for row in events)
            or not any(row.get('type') == 'turn.completed' for row in events)
            or any(row.get('type') in ('error', 'turn.failed') for row in events)):
        raise ValueError('Native role turn did not complete; exit zero alone is insufficient')
    raw = output / 'session.raw.jsonl'
    rows = [json.loads(line) for line in raw.read_text().splitlines() if line.strip()]
    if not any(row.get('type') == 'session_meta' and row.get('payload', {}).get('id') == session
               and row['payload'].get('cwd') == receipt['workspace'] for row in rows):
        raise ValueError('Native session does not match receipt')
    if not any(row.get('type') == 'response_item' and row.get('payload', {}).get('role') == 'assistant'
               and row['payload'].get('content') for row in rows):
        raise ValueError('No actual model activity')
    spec = importlib.util.spec_from_file_location('role_observed_input', HERE / 'runners/codex/normalize.py')
    normalizer = importlib.util.module_from_spec(spec); spec.loader.exec_module(normalizer)
    prompt = (directory / 'input/AGENTS.md').read_text().strip() + '\n\n' + (directory / 'input/prompt.txt').read_text()
    if not normalizer.observed_input(raw, prompt, settings['model'], settings['reasoning_effort']):
        raise ValueError('Actual role prompt/model/effort differs from frozen input')
    index = runs.read(output / 'artifact-input-index.json')
    snapshot = index.get('input_snapshot', {})
    if snapshot.get('available') is not True or snapshot.get('root') != '/run/afs/inputs/' + handle:
        raise ValueError('Protected original role input snapshot required')
    for name, sha in manifest['input_files'].items():
        entry = snapshot.get('entries', {}).get(name, {})
        if entry.get('kind') != 'file' or entry.get('sha256') != sha or entry.get('uid') != 0:
            raise ValueError('Role collection original input hash/owner mismatch')
    totals, usage = read_usage(output, settings['model'])
    if usage.get('status') != 'complete' or not any(x['output_tokens'] > 0 for x in usage['requests']):
        raise ValueError('Verified model request usage required')
    final = next(row.get('usage') for row in reversed(events) if row.get('type') == 'turn.completed')
    native = extract_usage(raw, final)
    if (native.get('status') != 'complete' or native.get('totals') != totals
            or native.get('requests') != usage['requests']):
        raise ValueError('Canonical usage differs from actual native model requests or CLI total')
    raw_result = output / 'artifacts' / ROLES[role]
    result_file = output / ROLES[role]
    if not raw_result.is_file() or not result_file.is_file() or runs.digest(raw_result) != runs.digest(result_file):
        raise ValueError('Role result must be the actual captured model artifact')
    result = runs.read(result_file)
    if not isinstance(result, dict) or result.get('schema_version') != 1:
        raise ValueError('Structured role result required')
    proof = {'schema_version': 1, 'role': role, 'verified': True, 'verified_at': runs.now(),
             'session_id': session, 'manifest_sha256': runs.digest(directory / 'manifest.json'),
             'receipt_sha256': runs.digest(output / 'receipt.json'), 'result_sha256': runs.digest(result_file),
             'input_files': manifest['input_files'], 'native_turn_completed': True,
             'source_sha256': {name: runs.digest(output / name) for name in ('events.jsonl', 'session.raw.jsonl', 'usage.json')},
             'account_usage': {'billing_mode': 'chatgpt', 'tokens': totals, 'cost_usd': None,
                               'notice': 'Account usage, unknown dollar amount; not free or DeepSeek API cost'}}
    runs.write(output / 'role-collection-proof.json', proof)
    return proof


def stop(directory, manifest, state):
    # Source/input drift must block allocation and admission, never emergency stop.
    # Use the originally frozen physical target even if the live config changed.
    frozen = deepcopy(manifest)
    config = directory / 'stop-adapter.json'
    runs.write(config, manifest['adapter_config'])
    for argv in frozen['settings']['commands'].values():
        argv[argv.index('--config') + 1] = str(config)
    answer = invoke(directory, frozen, 'stop', state['handle'])
    state['stop_confirmed'] = answer.get('stopped') is True
    try:
        invoke(directory, frozen, 'collect', state['handle'])
        _, observed = read_usage(directory / 'output', manifest['settings']['model'])
        runs.write(directory / 'partial-usage.json', observed)
    except Exception as error:
        state['collection_error'] = type(error).__name__
    state['phase'] = 'stopped' if state['stop_confirmed'] else 'needs_attention'
    runs.write(directory / 'state.json', state)
    return state


def advance(directory, *, halt=False):
    directory = Path(directory).resolve()
    with lock(directory / '.lock', blocking=True):
        state = runs.read(directory / 'state.json')
        manifest = runs.read(directory / 'manifest.json')
        if state['phase'] in ('collected', 'held', 'stopped'): return state
        expired = time.time() >= manifest['settings']['deadline_epoch']
        if (halt or expired) and state.get('handle'):
            try: verify(directory)
            except Exception as error: state['frozen_input_error'] = str(error)
            return stop(directory, manifest, state)
        try:
            manifest = verify(directory)
        except Exception as error:
            if not state.get('handle'): raise
            state['frozen_input_error'] = str(error)
            return stop(directory, manifest, state)
        if state['phase'] == 'prepared':
            if halt or time.time() + manifest['settings']['seconds'] + 20 >= manifest['settings']['deadline_epoch']:
                state.update(phase='held', reason='No full declared role window; no model started')
            elif shutil.disk_usage(directory).free < manifest['settings'].get('storage_floor_bytes', 1024**3):
                state.update(waiting_reason='Low storage; no preparation model allocated')
            else:
                state.pop('waiting_reason', None)
                state.update(phase='starting', handle=directory.name + '-' + manifest['role'], dispatched_at=runs.now())
                runs.write(directory / 'state.json', state)  # Durable before the side effect.
                try:
                    result = invoke(directory, manifest, 'start')
                    if result.get('handle') != state['handle']: raise ValueError('Unexpected role handle')
                    state.update(phase='running', start_confirmed=True)
                except Exception as error:
                    state.update(phase='uncertain_start', error_type=type(error).__name__,
                                 reason='Never resend start; reconcile predicted handle')
        elif halt or expired:
            return stop(directory, manifest, state)
        elif state['phase'] == 'running':
            try:
                status = invoke(directory, manifest, 'status', state['handle'])
                if status.get('status') in ('completed', 'failed'):
                    if invoke(directory, manifest, 'collect', state['handle']).get('collected') is not True:
                        raise ValueError('Role collection was not confirmed')
                    proof = validate_collection(directory, manifest)
                    state.update(phase='collected', collection_proof_sha256=runs.digest(directory / 'output/role-collection-proof.json'),
                                 session_id=proof['session_id'], collected_at=runs.now())
                elif status.get('status') != 'running':
                    raise ValueError('Role status unknown; reconcile before retry')
            except Exception as error:
                state.update(error_type=type(error).__name__, reason=str(error))
                # Only this handle is stopped. Unrelated producer/jobs continue.
                state = stop(directory, manifest, state)
                if state.get('stop_confirmed'): state['phase'] = 'held'
        # starting/uncertain_start/needs_attention never auto-resend a start.
        runs.write(directory / 'state.json', state)
        return state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='action', required=True)
    create = commands.add_parser('prepare'); create.add_argument('--role', choices=ROLES, required=True)
    create.add_argument('--input', type=Path, required=True); create.add_argument('--settings', type=Path, required=True)
    for name in ('advance', 'stop', 'status'): commands.add_parser(name)
    for command in commands.choices.values(): command.add_argument('directory', type=Path)
    args = parser.parse_args()
    if args.action == 'prepare': result = {'directory': str(prepare(args.directory, args.role, args.input, args.settings))}
    elif args.action == 'status': result = runs.read(args.directory / 'state.json')
    else: result = advance(args.directory, halt=args.action == 'stop')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__': main()
