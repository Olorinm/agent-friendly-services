#!/usr/bin/env python3
"""Isolated Codex roles; never loads executor credentials or repository context."""
import datetime
import fcntl
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time
from normalize import normalize, observed_input
from artifact_capture import collect_artifacts

ROOT = Path('/run/afs')
WORKSPACE_ROOT = Path('/workspace')
HOME_ROOT = Path('/home/node')
TEMP_ROOTS = (Path('/tmp'), Path('/var/tmp'))
ROLE_OUTPUTS = {'task_design': 'task-design.json',
                'material_preparation': 'material-preparation.json',
                'grading': 'assessment.json'}
EFFORTS = ('medium', 'high')


def validate_request(request):
    if (request.get('role') not in tuple(ROLE_OUTPUTS) or request.get('model') != 'gpt-6.1-sol'
            or request.get('reasoning_effort') not in EFFORTS):
        raise ValueError('Codex requires an explicit design/preparation/grading role and GPT-6.1 Sol medium/high')
    run = request['run_id']+'-'+request['role']
    if not re.fullmatch(r'[A-Za-z0-9._-]+', run): raise ValueError('Invalid run name')
    return run


def codex_command(request, workspace):
    validate_request(request)
    overrides = {'model_reasoning_effort': request['reasoning_effort'], 'approval_policy': 'never', 'project_doc_max_bytes': 0,
                 'skills.include_instructions': False, 'skills.bundled.enabled': False, 'agents.enabled': False,
                 'features.plugins': False, 'features.apps': False, 'features.memories': False,
                 'features.skill_search': False, 'features.shell_snapshot': False, 'features.hooks': False,
                 'features.plugin_hooks': False, 'features.recommended_plugins': False,
                 'allow_login_shell': False, 'web_search': 'disabled'}
    command = ['codex', 'exec', '--ignore-user-config', '--ignore-rules', '--skip-git-repo-check',
               '--strict-config', '--sandbox', 'danger-full-access', '--model', request['model'],
               '--cd', str(workspace), '--color', 'never', '--json', '-o', str(workspace/'codex-final.md')]
    for key, value in overrides.items(): command += ['-c', key+'='+json.dumps(value)]
    return command+['-']


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def identity():
    os.setgroups([]); os.setgid(1000); os.setuid(1000)


def capture_rollout(auth_root, session, output):
    # Read model-controlled home files with the model's privileges. A symlink
    # cannot cause the root controller to copy its own private credentials.
    if not isinstance(session, str) or not re.fullmatch(r'[0-9a-fA-F-]{36}', session):
        return
    script = '''from pathlib import Path
import sys
root = Path(sys.argv[1]); session = sys.argv[2]
matches = [p for sub in ('sessions', 'archived_sessions')
           for p in (root/sub).rglob('*'+session+'.jsonl')]
if len(matches) != 1: sys.exit(1)
sys.stdout.buffer.write(matches[0].read_bytes())
'''
    result = subprocess.run(['python3', '-c', script, str(auth_root), session],
                            capture_output=True, preexec_fn=identity)
    if result.returncode == 0:
        (output/'session.raw.jsonl').write_bytes(result.stdout)


def main():
    os.umask(0o077)
    lock = (ROOT/'worker.lock').open('a')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    request = json.loads(Path(sys.argv[1]).read_text())
    run = validate_request(request)
    private = ROOT/run; private.mkdir(exist_ok=False)
    output = private/'output'; output.mkdir()
    workspace = WORKSPACE_ROOT/run
    home = HOME_ROOT/run
    archive = ROOT/'archive'/run; archive.mkdir(parents=True)
    for parent in (WORKSPACE_ROOT, HOME_ROOT, *TEMP_ROOTS):
        for old in parent.iterdir():
            dest = archive/str(parent).lstrip('/'); dest.mkdir(parents=True, exist_ok=True)
            shutil.move(str(old), str(dest/old.name))
    shutil.copytree(ROOT/'inputs'/run, workspace)
    home.mkdir(); auth_root = home/'.codex'; auth_root.mkdir()
    auth = json.loads((ROOT/'auth.json').read_text())
    if auth.get('auth_mode') != 'chatgpt' or not auth.get('tokens') or auth.get('OPENAI_API_KEY'):
        raise ValueError('Codex roles require the selected ChatGPT login; no API-key fallback')
    dump(auth_root/'auth.json', auth)
    for path in (workspace, home):
        subprocess.run(['chown', '-R', '1000:1000', str(path)], check=True)
    role_instructions = (workspace/'AGENTS.md').read_text().strip()
    prompt = role_instructions+'\n\n'+(workspace/'prompt.txt').read_text()
    expected_version = 'codex-cli '+request['harness']['version']
    actual_version = subprocess.check_output(['codex', '--version'], text=True).strip()
    if actual_version != expected_version or request['harness']['name'] != 'codex':
        raise ValueError('Actual Codex CLI version differs from frozen harness')
    command = codex_command(request, workspace)
    environment = {'HOME': str(home), 'CODEX_HOME': str(auth_root), 'PATH': '/usr/local/bin:/usr/bin:/bin',
                   'LANG': 'C.UTF-8'}
    started = now(); timed_out = False
    timeout = max(1, request['seconds']-5)
    if request.get('deadline_epoch'): timeout = min(timeout, max(1, request['deadline_epoch']-time.time()-5))
    with (output/'events.jsonl').open('wb') as events, (output/'stderr.log').open('wb') as errors:
        process = subprocess.Popen(command, cwd=workspace, env=environment, stdin=subprocess.PIPE,
                                   stdout=events, stderr=errors, preexec_fn=identity, start_new_session=True)
        dump(private/'process.json', {'pid': process.pid, 'started_at': started})
        try: process.communicate(prompt.encode(), timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try: process.communicate(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL); process.communicate()
    ended = now(); rows = []
    for line in (output/'events.jsonl').read_text().splitlines():
        try: rows.append(json.loads(line))
        except json.JSONDecodeError: pass
    session = next((r.get('thread_id') for r in rows if r.get('type') == 'thread.started'), None)
    expected = next((r.get('usage') for r in reversed(rows) if r.get('type') == 'turn.completed'), None)
    capture_rollout(auth_root, session, output)
    normalize(output, request['model'], expected)
    source = output/'session.raw.jsonl'
    verified = source.is_file() and observed_input(source, prompt, request['model'], request['reasoning_effort'])
    dump(output/'receipt.json', {'role': request['role'], 'session_id': session, 'workspace': str(workspace), 'model': request['model'],
         'reasoning_effort': request['reasoning_effort'], 'harness': request['harness'], 'runtime': request['runtime'],
         'started_at': started, 'ended_at': ended, 'exit_code': process.returncode, 'timed_out': timed_out,
         'isolation': 'Dedicated Docker '+request['role']+' session; uid 1000; fresh home/session/workspace; no executor credentials; only frozen role input',
         'input_verified': verified, 'runtime_code_preflight': request.get('runtime_code_preflight'),
         'runtime_image_id': request.get('runtime_image_id'), 'billing_mode': 'chatgpt',
         'billing_note': 'ChatGPT account usage; actual credits and allocated subscription cost unknown, not zero'})
    dump(output/'controller-limits.json', {'seconds': request['seconds'],
         'deadline_epoch': request.get('deadline_epoch'), 'billing_mode': 'chatgpt',
         'max_model_requests_enforced': False})
    collect_artifacts(workspace, private, output)
    final = output/'artifacts/codex-final.md'
    (output/'answer.md').write_bytes(final.read_bytes() if final.is_file() else b'')
    role_output = ROLE_OUTPUTS[request['role']]
    result = output/'artifacts'/role_output
    if result.is_file(): shutil.copyfile(result, output/role_output)
    dump(private/'done.json', {'status': 'completed' if process.returncode == 0 else 'failed'})
    lock.close()


if __name__ == '__main__': main()
