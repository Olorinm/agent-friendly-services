#!/usr/bin/env python3
"""Provision graders from selected private ChatGPT auth; never start model calls."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tarfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'opencode'))
from config import load, ssh

LABEL = 'org.agent-friendly-services.codex-grader'


def archive(files):
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode='w') as tar:
        for name, raw in files.items():
            entry = tarfile.TarInfo(name); entry.size = len(raw); entry.mode = 0o600
            tar.addfile(entry, io.BytesIO(raw))
    return output.getvalue()


def run(config, action):
    def docker(*args, data=None): return ssh(config, ['sudo', '-n', 'docker', *args], data)
    image = config.get('image', 'afs-codex-grader:0.162.0')
    owner = hashlib.sha256(config['remote_root'].encode()).hexdigest()[:16]
    if action == 'build':
        result = docker('build', '-t', image, '-', data=archive({'Dockerfile': (HERE/'Dockerfile').read_bytes()}))
        sys.stderr.write(result.stdout.decode(errors='replace')+result.stderr.decode(errors='replace'))
        return {'built': image}
    ids = docker('ps', '-aq').stdout.decode().split()
    existing = {r['Name'].lstrip('/'): r for r in json.loads(docker('inspect', *ids).stdout)} if ids else {}
    for name in config['containers'].values():
        if name in existing and (existing[name]['Config'].get('Labels') or {}).get(LABEL) != owner:
            raise ValueError('Refusing unrelated container')
        if action == 'up' and name in existing and existing[name]['State']['Running']:
            raise ValueError('Stop and reconcile the owned runtime before source/auth refresh')
    if action == 'stop':
        names = [n for n in config['containers'].values() if n in existing and existing[n]['State']['Running']]
        if names: docker('stop', *names)
        return {'stopped': names}
    auth_path = Path(config['auth_file']).expanduser()
    if not auth_path.is_absolute() or auth_path.is_symlink(): raise ValueError('Selected private auth path required')
    raw = auth_path.read_bytes(); auth = json.loads(raw)
    if auth.get('auth_mode') != 'chatgpt' or not auth.get('tokens') or auth.get('OPENAI_API_KEY'):
        raise ValueError('Requires selected ChatGPT login, never API-key fallback')
    ssh(config, ['mkdir', '-p', '-m', '700', config['remote_root']+'/runs'])
    ssh(config, ['chmod', '700', config['remote_root'], config['remote_root']+'/runs'])
    files = {n: (HERE/n).read_bytes() for n in ('worker.py', 'normalize.py', 'artifact_capture.py')}
    files['session_usage.py'] = (HERE.parent.parent/'session_usage.py').read_bytes()
    files['auth.json'] = raw
    result = {}
    for runtime, name in config['containers'].items():
        if name not in existing:
            docker('create', '--name', name, '--label', LABEL+'='+owner, '--memory', str(config.get('memory', '2g')),
                   '--cpus', str(config.get('cpus', 1)), '--pids-limit', str(config.get('pids_limit', 256)), image)
        docker('start', name)
        docker('exec', '-u', '0', name, 'install', '-d', '-m', '700', '/run/afs')
        docker('exec', '-i', '-u', '0', name, 'tar', '-xf', '-', '-C', '/run/afs', data=archive(files))
        version = docker('exec', name, 'codex', '--version').stdout.decode().strip()
        info = json.loads(docker('inspect', name).stdout)[0]
        result[runtime] = {'codex_version': version, 'image_id': info['Image'], 'billing_mode': 'chatgpt',
                           'memory_bytes': info['HostConfig']['Memory'], 'nano_cpus': info['HostConfig']['NanoCpus']}
    return result


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser(); parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('action', choices=['build', 'up', 'stop']); args = parser.parse_args()
    print(json.dumps(run(load(args.config), args.action), ensure_ascii=False, indent=2))


if __name__ == '__main__': main()
