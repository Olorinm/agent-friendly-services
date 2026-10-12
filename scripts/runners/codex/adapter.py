#!/usr/bin/env python3
"""Pipeline start/status/collect/stop for isolated cloud Codex grading."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import shlex
import sys
import tarfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'opencode'))
from config import load, ssh as remote_ssh
from runtime_status import query
from assessment import normalize as normalize_assessment

FILES = ('worker.py', 'normalize.py', 'artifact_capture.py', 'session_usage.py')


def archive(directory):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode='w') as tar:
        for file in Path(directory).rglob('*'):
            if file.is_symlink(): raise ValueError('Input links forbidden')
            if file.is_file(): tar.add(file, arcname=str(file.relative_to(directory)), recursive=False)
    return stream.getvalue()


def sources():
    return {name: (HERE/name if name != 'session_usage.py' else HERE.parent.parent/'session_usage.py').read_bytes()
            for name in FILES}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('operation', choices=['start', 'status', 'collect', 'stop'])
    parser.add_argument('request', type=Path)
    args = parser.parse_args()
    config = load(args.config); request = json.loads(args.request.read_text())
    if request['role'] != 'grading' or request['model'] != 'gpt-6.1-sol' or request['reasoning_effort'] != 'high':
        raise ValueError('Codex adapter accepts only independent GPT-6.1 Sol/high grading')
    if config.get('billing_mode') != 'chatgpt': raise ValueError('Explicit ChatGPT account billing required')
    container = config['containers'][request['runtime']]
    run = (request.get('handle') if args.operation != 'start' else None) or request['run_id']+'-grading'
    if not re.fullmatch(r'[A-Za-z0-9._-]+', run): raise ValueError('Invalid run name')
    remote = config['remote_root']+'/runs/'+run
    private = '/run/afs/'+run
    def ssh(argv, data=None, check=True): return remote_ssh(config, argv, data, check)
    def docker(*argv, data=None, check=True): return ssh(['sudo', '-n', 'docker', *argv], data, check)
    def root(*argv, data=None, check=True): return docker('exec', '-u', '0', container, *argv, data=data, check=check)
    if args.operation == 'start':
        expected = {name: hashlib.sha256(raw).hexdigest() for name, raw in sources().items()}
        probe = 'import hashlib,json,sys;from pathlib import Path;print(json.dumps({n:hashlib.sha256((Path("/run/afs")/n).read_bytes()).hexdigest() for n in sys.argv[1:]}))'
        observed = json.loads(root('python3', '-c', probe, *FILES).stdout)
        if observed != expected: raise ValueError('Idle Codex runtime needs provisioned source update; no run allocated')
        request['runtime_code_preflight'] = {'source_sha256': observed}
        request['runtime_image_id'] = docker('inspect', '--format', '{{.Image}}', container).stdout.decode().strip()
        ssh(['mkdir', '-m', '700', remote])
        ssh(['tar', '-xf', '-', '-C', remote], archive(request['input']))
        root('mkdir', '-p', '/run/afs/inputs/'+run)
        docker('cp', remote+'/.', container+':/run/afs/inputs/'+run)
        ssh(['tee', remote+'.request.json'], json.dumps(request).encode())
        docker('cp', remote+'.request.json', container+':/run/afs/'+run+'.request.json')
        command = 'exec python3 /run/afs/worker.py '+shlex.quote('/run/afs/'+run+'.request.json')+' > /run/afs/'+run+'.worker.log 2>&1'
        docker('exec', '-d', '-u', '0', container, 'sh', '-c', command)
        print(json.dumps({'handle': run}))
    elif args.operation == 'status':
        print(json.dumps(query(lambda: root('cat', private+'/done.json', check=False),
                               lambda: root('pgrep', '-af', '^python3 /run/afs/worker.py /run/afs/'+re.escape(run)+'.request.json$', check=False))))
    elif args.operation == 'collect':
        output = Path(request['output']).resolve(); output.mkdir(parents=True, exist_ok=True)
        raw = root('tar', '-cf', '-', '-C', private+'/output', '.').stdout
        with tarfile.open(fileobj=io.BytesIO(raw)) as tar:
            for member in tar:
                target = (output/member.name).resolve()
                if not target.is_relative_to(output) or not (member.isdir() or member.isfile()): raise ValueError('Unsafe archive member')
                if member.isdir(): target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(tar.extractfile(member).read()); target.chmod(0o600)
        assessment = output/'assessment.json'
        if assessment.is_file():
            (output/'assessment.raw.json').write_bytes(assessment.read_bytes())
            normalized, changes = normalize_assessment(json.loads(assessment.read_text()))
            if changes:
                assessment.write_text(json.dumps(normalized, ensure_ascii=False, indent=2)+'\n')
                (output/'adapter-normalizations.json').write_text(json.dumps(changes)+'\n')
        print(json.dumps({'collected': True}))
    else:
        script = (HERE/'stop.py').read_text()
        pattern = '^python3 /run/afs/worker.py '+re.escape('/run/afs/'+run+'.request.json')+'$'
        result = root('python3', '-c', script, private, pattern, check=False)
        print(json.dumps(json.loads(result.stdout) if result.returncode == 0 else {'stopped': False, 'reason': 'Codex stop could not be confirmed'}))


if __name__ == '__main__': main()
