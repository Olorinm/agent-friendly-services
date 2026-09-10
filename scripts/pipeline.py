#!/usr/bin/env python3
"""Prepare, dispatch, collect, grade, and record a frozen run through command adapters.

Adapters implement start/status/collect/stop. No model or service calls are built in.
A pending start is never retried automatically. All orchestration state is private.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time
from adapter_usage import read_usage
from service_cost import service_charge

ROOT = Path(__file__).resolve().parents[1]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parent / filename)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    value.ROOT = ROOT
    return value


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.new')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temp.chmod(0o600)
    temp.replace(path)


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def frozen_files(directory):
    return {str(p.relative_to(directory)): digest(p) for p in directory.rglob('*') if p.is_file()}


def prepare(config_path, directory):
    config = read(config_path)
    directory = Path(directory).resolve()
    if not directory.is_relative_to((ROOT / 'data/experiments/results').resolve()):
        raise ValueError('Run directory must be in data/experiments/results')
    if not re.fullmatch(r'[a-zA-Z0-9._-]+', directory.name):
        raise ValueError('Invalid run directory name')
    for role in ('execution', 'grading'):
        settings = config[role]
        if not all(settings.get(k) for k in ('model', 'reasoning_effort', 'harness', 'runtime')):
            raise ValueError('Each role needs model, reasoning_effort, harness and runtime')
        if not all(settings['harness'].get(k) for k in ('name', 'version', 'mode')):
            raise ValueError('Record harness name, version and mode')
        if type(settings['seconds']) is not int or settings['seconds'] <= 0:
            raise ValueError('Each role needs a positive seconds budget')
        for op in ('start', 'status', 'collect', 'stop'):
            argv = settings['commands'][op]
            if not isinstance(argv, list) or not argv or not all(isinstance(a, str) for a in argv):
                raise ValueError('Adapter commands must be nonempty argv arrays')
            if not any('{request}' in a for a in argv):
                raise ValueError('Commands must consume the frozen request JSON')
    if config['execution']['runtime'] == config['grading']['runtime']:
        raise ValueError('Grading must use a separate runtime')
    if not config.get('environment') or not config.get('environment_id'):
        raise ValueError('Explicit environment description and stable environment_id are required')
    if config['phase'] not in ('access', 'business'):
        raise ValueError('phase must be access or business')
    if config['phase'] == 'business':
        previous = Path(config['depends_on']).resolve()
        prev_config, prev_state = read(previous / 'config.json'), read(previous / 'state.json')
        if prev_state['phase'] not in ('reviewed', 'recorded') or read(previous / 'grading/assessment.json')['status'] != 'completed':
            raise ValueError('Prerequisite must have passed independent grading')
        if (any(prev_config[k] != config[k] for k in ('service', 'route', 'environment_id'))
                or prev_config['execution']['runtime'] != config['execution']['runtime']):
            raise ValueError('Business task must reuse prerequisite service, route and environment')
    parser = module('task_inputs', 'codex-service-trial.py')
    task, _ = parser.select_task((ROOT / config['task_file']).resolve(), config['task'])
    route = parser.select_route(read(ROOT / 'generated/catalog.json'), config['service'], config['route'])
    directory.mkdir(parents=True, exist_ok=False)
    directory.chmod(0o700)
    frozen = directory / 'frozen'
    inputs = frozen / 'execution'
    inputs.mkdir(parents=True)
    context = parser.natural_context(task, route['entry_url'], [], config['execution']['seconds'])
    context['ENVIRONMENT.md'] = config['environment'] + '\n指定入口：' + route['entry_url'] + '\n'
    for name, content in context.items():
        (inputs / name).write_text(content)
    shutil.copyfile(ROOT / 'scripts/roles/execution/AGENTS.md', inputs / 'AGENTS.md')
    (inputs / 'prompt.txt').write_text(parser.natural_prompt(task, route['entry_url'], [], config['execution']['seconds']))
    # Attachments are execution inputs only. Reference answers use a separate source.
    if config.get('attachments'):
        source = Path(config['attachments']).resolve()
        if any(p.is_symlink() for p in source.rglob('*')):
            raise ValueError('Attachments must not contain symlinks')
        shutil.copytree(source, inputs / 'materials')
        with (inputs / 'input.md').open('a') as stream:
            stream.write('\n本题原始附件在 materials/。\n')
    grade = frozen / 'grading'
    grade.mkdir()
    shutil.copyfile(ROOT / 'scripts/roles/grading/AGENTS.md', grade / 'AGENTS.md')
    write(grade / 'task.json', task)
    if config.get('reference'):
        shutil.copyfile(config['reference'], grade / 'reference.json')
    shutil.copyfile(ROOT / 'data/pricing/litellm.json', frozen / 'pricing.json')
    write(directory / 'config.json', config)
    write(directory / 'task.json', task)
    write(directory / 'route.json', route)
    hashes = frozen_files(frozen)
    hashes.update({'../' + name: digest(directory / name) for name in ('config.json', 'task.json', 'route.json')})
    write(directory / 'frozen-hashes.json', hashes)
    write(directory / 'state.json', {'phase': 'prepared', 'created_at': now()})
    return directory


def verify(directory):
    for rel, expected in read(directory / 'frozen-hashes.json').items():
        if digest(directory / 'frozen' / rel) != expected:
            raise ValueError('Frozen inputs changed: ' + rel)


def invoke(directory, role, operation, settings, request):
    request_file = directory / f'{role}-{operation}.json'
    write(request_file, request)
    argv = [arg.replace('{request}', str(request_file)) for arg in settings['commands'][operation]]
    log = directory / f'{role}-{operation}.stderr'
    with log.open('ab') as stderr:
        process = subprocess.Popen(argv, cwd=directory, stdout=subprocess.PIPE, stderr=stderr,
                                   start_new_session=True)
        try:
            stdout, _ = process.communicate(timeout=30)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.communicate()
            raise RuntimeError('Adapter command timed out; inspect state before resubmitting')
    if process.returncode != 0:
        raise RuntimeError(f'{role} {operation} failed; see private stderr log')
    result = json.loads(stdout)
    if not isinstance(result, dict):
        raise ValueError('Adapter must return a JSON object')
    return result


def stage_request(directory, role, settings):
    return {'run_id': directory.name, 'role': role, 'model': settings['model'],
            'reasoning_effort': settings['reasoning_effort'], 'harness': settings['harness'],
            'seconds': settings['seconds'], 'runtime': settings['runtime'],
            'input': str(directory / ('frozen/execution' if role == 'execution' else 'grading-input')),
            'output': str(directory / ('execution' if role == 'execution' else 'grading')),
            'fresh_session': True}


def collect(directory, role, settings, request):
    invoke(directory, role, 'collect', settings, request)
    output = Path(request['output'])
    receipt = read(output / 'receipt.json')
    if not receipt.get('session_id') or not receipt.get('workspace'):
        raise ValueError('Collection needs actual session_id and workspace')
    if not receipt.get('isolation') or receipt.get('input_verified') is not True:
        raise ValueError('Collection must report isolation and verify actual role/task input')
    if type(receipt.get('exit_code')) is not int or type(receipt.get('timed_out')) is not bool:
        raise ValueError('Receipt needs integer exit_code and boolean timed_out')
    for key in ('model', 'reasoning_effort', 'harness', 'runtime'):
        if receipt.get(key) != settings[key]:
            raise ValueError('Runtime receipt differs from configured ' + key)
    for key in ('started_at', 'ended_at'):
        if datetime.fromisoformat(receipt[key]).tzinfo is None:
            raise ValueError('Receipt timestamps need timezone')
    elapsed = (datetime.fromisoformat(receipt['ended_at']) - datetime.fromisoformat(receipt['started_at'])).total_seconds()
    if elapsed < 0:
        raise ValueError('Receipt timestamps are reversed')
    if role == 'grading':
        execution = read(directory / 'execution/receipt.json')
        if receipt['session_id'] == execution['session_id'] or receipt['workspace'] == execution['workspace']:
            raise ValueError('Execution and grading need distinct sessions and workspaces')
    usage, request_usage = read_usage(output, settings['model'])
    measured = {'model': settings['model'], 'usage': usage, 'request_usage': request_usage}
    write(output / 'measured.json', measured)
    cost = subprocess.check_output(['node', '--import', 'tsx', str(ROOT / 'scripts/calculate-cost.ts'),
                                   str(output / 'measured.json'), str(directory / 'frozen/pricing.json')], cwd=ROOT, text=True)
    write(output / 'model-cost.json', json.loads(cost))
    return receipt, elapsed


def finish_execution(directory, config, receipt, elapsed):
    output = directory / 'execution'
    for name in ('answer.md', 'events.jsonl', 'usage.json'):
        if (output / name).is_file():
            shutil.copyfile(output / name, directory / name)
    # Raw source paths remain relative to usage.json. Preserve the entire output
    # privately for grading, and rewrite canonical source references for recording.
    if (directory / 'usage.json').exists():
        usage = read(directory / 'usage.json')
        for source in usage.get('sources', []):
            path = (output / source['path']).resolve()
            if not path.is_relative_to(output.resolve()):
                raise ValueError('Source outside execution output')
            source['path'] = 'execution/' + str(path.relative_to(output))
        write(directory / 'usage.json', usage)
    task, route = read(directory / 'task.json'), read(directory / 'route.json')
    shutil.copyfile(directory / 'frozen/pricing.json', directory / 'pricing.json')
    meta = {'service': config['service'], 'route_id': config['route'], 'entry_url': route['entry_url'],
            'task': task, 'model': receipt['model'], 'reasoning_effort': receipt['reasoning_effort'],
            'harness': receipt['harness'], 'workspace': receipt['workspace'],
            'session_id': receipt['session_id'], 'started_at': receipt['started_at'], 'ended_at': receipt['ended_at'],
            'elapsed_seconds': elapsed, 'seconds_limit': config['execution']['seconds'],
            'exit_code': receipt.get('exit_code'), 'timed_out': receipt.get('timed_out', False),
            'isolation': receipt['isolation'], 'usage_format': 'adapter-v1',
            'usage': read(output / 'measured.json')['usage'],
            'pricing_sha256': digest(directory / 'pricing.json'),
            'prompt_sha256': digest(directory / 'frozen/execution/prompt.txt'),
            'prompt_style': 'natural', 'preparation_note': config.get('preparation_note', ''),
            'environment_id': config['environment_id'], 'phase': config['phase']}
    write(directory / 'run.json', meta)
    grade = directory / 'grading-input'
    if grade.exists():
        raise ValueError('Grading input already exists; inspect partial collection')
    shutil.copytree(directory / 'frozen/grading', grade)
    shutil.copytree(directory / 'frozen/execution', grade / 'frozen-execution')
    shutil.copytree(output, grade / 'execution')
    (grade / 'prompt.txt').write_text('按 AGENTS.md 验收 task.json 的这一次执行。frozen-execution 是冻结输入，execution 是实际记录。'
                                    '不补做用户任务。在输出目录写 assessment.json，采用项目约定字段和费用依据。\n')


def advance(directory):
    directory = Path(directory).resolve()
    verify(directory)
    config, state = read(directory / 'config.json'), read(directory / 'state.json')
    phase = state['phase']
    if phase in ('reviewed', 'recorded'):
        return state
    if phase in ('execution_starting', 'grading_starting', 'stopped'):
        raise ValueError('Dispatch state needs reconciliation; do not automatically resend')
    role = 'execution' if phase in ('prepared', 'execution_running', 'execution_collecting') else 'grading'
    settings = config[role]
    request = stage_request(directory, role, settings)
    if phase in ('prepared', 'execution_collected'):
        state.update(phase=role + '_starting', dispatched_at=now())
        write(directory / 'state.json', state)
        started = invoke(directory, role, 'start', settings, request)
        if not started.get('handle'):
            raise ValueError('Adapter start must return a durable handle')
        state.update(phase=role + '_running', handle=started['handle'])
        write(directory / 'state.json', state)
        return state
    request['handle'] = state['handle']
    status = invoke(directory, role, 'status', settings, request)
    if status.get('status') not in ('running', 'completed', 'failed'):
        raise ValueError('Adapter status must be running, completed or failed')
    age = (datetime.now(timezone.utc) - datetime.fromisoformat(state['dispatched_at'])).total_seconds()
    if status['status'] == 'running':
        if age <= settings['seconds']:
            return state
        # The adapter must terminate the remote session/process tree, not just SSH.
        state.update(phase='stopped', stop_reason='budget exceeded', stopped_role=role)
        write(directory / 'state.json', state)
        invoke(directory, role, 'stop', settings, request)
        invoke(directory, role, 'collect', settings, request)
        return state
    state.update(phase=role + '_collecting')
    write(directory / 'state.json', state)
    receipt, elapsed = collect(directory, role, settings, request)
    if elapsed > settings['seconds'] and not receipt.get('timed_out'):
        raise ValueError('Elapsed runtime exceeds budget without timeout indication')
    if role == 'execution':
        finish_execution(directory, config, receipt, elapsed)
        state.update(phase='execution_collected')
    else:
        if receipt.get('exit_code') != 0 or receipt.get('timed_out'):
            raise ValueError('Grading did not finish successfully')
        assessment = read(directory / 'grading/assessment.json')
        # Reuse the exact recording validator, without publishing anything.
        recorder = module('recorder', 'record-trial.py')
        recorder.record(directory, directory / 'grading/assessment.json', dry_run=True)
        amount, detail = service_charge(assessment)
        write(directory / 'charges.json', {'model_cost': read(directory / 'execution/model-cost.json'),
                                          'service_cost_usd': amount, 'service_cost': detail,
                                          'grading_model_cost': read(directory / 'grading/model-cost.json')})
        state.update(phase='reviewed', record_hashes={name: digest(directory / name) for name in
                     ('run.json', 'charges.json', 'grading/assessment.json', 'pricing.json')})
    write(directory / 'state.json', state)
    return state


def record(directory, generate=False):
    directory = Path(directory).resolve()
    verify(directory)
    state = read(directory / 'state.json')
    if state['phase'] != 'reviewed':
        raise ValueError('Only independently reviewed runs can be recorded')
    for name, expected in state['record_hashes'].items():
        if digest(directory / name) != expected:
            raise ValueError('Reviewed record changed: ' + name)
    recorder = module('recorder', 'record-trial.py')
    target = recorder.record(directory, directory / 'grading/assessment.json')
    write(directory / 'state.json', {**state, 'phase': 'recorded', 'result': str(target)})
    subprocess.run(['npm', 'run', 'validate'], cwd=ROOT, check=True)
    if generate:
        subprocess.run(['npm', 'run', 'generate'], cwd=ROOT, check=True)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    for action in ('prepare', 'advance', 'run', 'status', 'stop', 'record'):
        cmd = sub.add_parser(action)
        cmd.add_argument('directory', type=Path)
        if action == 'prepare':
            cmd.add_argument('--config', required=True, type=Path)
        if action == 'record':
            cmd.add_argument('--generate', action='store_true')
    args = parser.parse_args()
    os.umask(0o077)
    if args.action == 'prepare':
        print(prepare(args.config, args.directory))
    elif args.action in ('status', 'stop'):
        directory = args.directory.resolve()
        state, config = read(directory / 'state.json'), read(directory / 'config.json')
        phase = state['phase']
        if phase.startswith(('execution_', 'grading_')) and phase != 'execution_collected':
            role = phase.split('_')[0]
            request = stage_request(directory, role, config[role])
            if state.get('handle'):
                request['handle'] = state['handle']
            if args.action == 'stop':
                # Persist before touching the external runtime, including uncertain starts.
                write(directory / 'state.json', {**state, 'phase': 'stopped', 'stopped_role': role,
                                                'stop_reason': 'explicit controller stop'})
                print(json.dumps(invoke(directory, role, 'stop', config[role], request)))
            else:
                print(json.dumps({'controller': state, 'runtime': invoke(directory, role, 'status', config[role], request)}))
        else:
            print(json.dumps(state))
    elif args.action == 'record':
        print(record(args.directory, args.generate))
    else:
        # Single controller lock prevents duplicate dispatch. OS releases it on exit.
        import fcntl
        with (args.directory / '.pipeline.lock').open('w') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            while True:
                state = advance(args.directory)
                print(json.dumps(state), flush=True)
                if args.action == 'advance' or state['phase'] in ('reviewed', 'recorded', 'stopped'):
                    break
                time.sleep(2)


if __name__ == '__main__':
    main()
