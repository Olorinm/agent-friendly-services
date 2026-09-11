#!/usr/bin/env python3
"""Build and provision isolated OpenCode runtimes from external settings.

Never creates cloud resources, purchases capacity, or starts model requests.
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
from config import load, ssh

HERE = Path(__file__).resolve().parent
LABEL = 'org.agent-friendly-services.runner'
WORKER_FILES = ('worker.py', 'normalize.py', 'capture-proxy.py')


def archive(files):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode='w') as tar:
        for name, content in files.items():
            entry = tarfile.TarInfo(name)
            entry.size = len(content)
            entry.mode = 0o600
            tar.addfile(entry, io.BytesIO(content))
    return stream.getvalue()


def run(config, action):
    owner = hashlib.sha256(config['remote_root'].encode()).hexdigest()[:16]
    image = config.get('image', 'afs-opencode:1.18.29')

    def docker(*args, data=None):
        return ssh(config, ['sudo', '-n', 'docker', *args], data=data)

    if action == 'build':
        args = ['build', '-t', image]
        for key, value in config.get('build_args', {}).items():
            if key not in ('OPENCODE_VERSION', 'DEBIAN_MIRROR'):
                raise ValueError('Unsupported build argument: ' + key)
            args += ['--build-arg', key + '=' + str(value)]
        result = docker(*args, '-', data=archive({'Dockerfile': (HERE/'Dockerfile').read_bytes()}))
        sys.stderr.write(result.stdout.decode(errors='replace') + result.stderr.decode(errors='replace'))
        return {'built': image}

    # Inspect once, and never adopt or change unrelated existing containers.
    all_ids = docker('ps', '-aq').stdout.decode().split()
    existing = {}
    if all_ids:
        existing = {x['Name'].lstrip('/'): x for x in json.loads(docker('inspect', *all_ids).stdout)}
    for name in config['containers'].values():
        if name in existing and (existing[name]['Config'].get('Labels') or {}).get(LABEL) != owner:
            raise ValueError('Refusing unrelated container: ' + name)
        if action == 'up' and name in existing and existing[name]['State']['Running']:
            raise ValueError('Container already running; stop the idle batch before provisioning: ' + name)

    key = None
    if action == 'up':
        # Only read an operator-selected file; never accept a literal key argument.
        key_path = Path(config['key_file']).expanduser()
        if not key_path.is_absolute():
            raise ValueError('key_file must be an absolute private path')
        key = key_path.read_bytes().strip()
        if not key:
            raise ValueError('Empty Coding Plan key file')
        ssh(config, ['mkdir', '-p', '-m', '700', config['remote_root'] + '/runs'])
        ssh(config, ['chmod', '700', config['remote_root'], config['remote_root'] + '/runs'])

    result = {}
    for runtime, name in config['containers'].items():
        current = existing.get(name)
        if action == 'stop':
            if current and current['State']['Running']:
                docker('stop', name)
            result[runtime] = 'stopped' if current else 'absent'
            continue
        if not current:
            docker('create', '--name', name, '--label', LABEL + '=' + owner,
                   '--memory', str(config.get('memory', '2g')),
                   '--cpus', str(config.get('cpus', 1)),
                   '--pids-limit', str(config.get('pids_limit', 256)), image)
        docker('start', name)
        docker('exec', '-u', '0', name, 'install', '-d', '-m', '700', '/run/afs')
        files = {f: (HERE/f).read_bytes() for f in WORKER_FILES}
        files['bigmodel.key'] = key
        docker('exec', '-i', '-u', '0', name, 'tar', '-xf', '-', '-C', '/run/afs', data=archive(files))
        version = docker('exec', name, 'opencode', '--version').stdout.decode().strip()
        info = json.loads(docker('inspect', name).stdout)[0]
        result[runtime] = {'container': name, 'image_id': info['Image'], 'opencode_version': version,
                           'memory_bytes': info['HostConfig']['Memory'], 'nano_cpus': info['HostConfig']['NanoCpus'],
                           'pids_limit': info['HostConfig']['PidsLimit']}
    return result


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('action', choices=('build', 'up', 'stop'))
    args = parser.parse_args()
    try:
        result = run(load(args.config), args.action)
    except subprocess.CalledProcessError as error:
        # Command arguments/stdin can contain private paths; print only diagnostics.
        print(error.stderr.decode(errors='replace'), file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
