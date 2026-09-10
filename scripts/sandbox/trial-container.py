#!/usr/bin/env python3
"""Manage one service/route container per batch; switch tasks without reinstalling.

The caller stops the old Agent, collects its session, and starts a fresh session.
This helper manages task files, not Agent conversations or remote service state.
"""
import argparse
import io
import json
import re
import shutil
import subprocess
import tarfile
from pathlib import Path

LABEL = 'org.agent-friendly-services.trial'
STATE = '/workspace/.afs-lifecycle.json'


def valid_id(value):
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', value):
        raise ValueError('Run IDs must be lowercase letters, numbers or hyphens (max 64).')
    return value


def task_payload(source):
    source = source.resolve()
    if not source.is_dir() or not (source / 'AGENTS.md').is_file():
        raise ValueError('Input must contain execution AGENTS.md.')
    if any(p.is_symlink() or not (p.is_file() or p.is_dir()) for p in source.rglob('*')):
        raise ValueError('Input must contain only regular files/directories, without symlinks.')
    payload = io.BytesIO()
    with tarfile.open(fileobj=payload, mode='w') as archive:
        for path in source.iterdir():
            archive.add(path, arcname=path.name)
    return payload.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--context', required=True)
    sub = parser.add_subparsers(dest='action', required=True)
    create = sub.add_parser('create')
    create.add_argument('name')
    create.add_argument('--image', default='afs-trial-base:local')
    create.add_argument('--input', type=Path, required=True)
    create.add_argument('--run-id', default='access')
    create.add_argument('--memory', default='1g')
    create.add_argument('--env-file', type=Path)
    advance = sub.add_parser('next-task')
    advance.add_argument('name')
    advance.add_argument('--input', type=Path, required=True)
    advance.add_argument('--run-id', required=True)
    advance.add_argument('--output', type=Path, required=True,
                         help='New private directory for the previous workspace and session archive')
    advance.add_argument('--session-record', type=Path, required=True,
                         help='Collected previous Agent session directory; Agent must already be stopped')
    for action in ('inspect', 'export', 'destroy'):
        command = sub.add_parser(action)
        command.add_argument('name')
        if action == 'export':
            command.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'afs-[a-z0-9][a-z0-9-]{0,55}', args.name):
        parser.error('Use an afs- prefixed lowercase container name (max 60 characters).')
    docker = ['docker', '--context', args.context]

    def run(*command):
        return subprocess.check_output([*docker, *command], text=True)

    def put(payload, directory):
        run('exec', args.name, 'mkdir', '-p', directory)
        subprocess.run([*docker, 'exec', '-i', args.name, 'tar', '--no-same-owner',
                        '-xf', '-', '-C', directory], input=payload, check=True)

    def save_state(state):
        subprocess.run([*docker, 'exec', '-i', args.name, 'python3', '-c',
                        'import sys; from pathlib import Path; '
                        'p=Path(sys.argv[1]); t=p.with_suffix(".new"); '
                        't.write_bytes(sys.stdin.buffer.read()); t.replace(p)', STATE],
                       input=json.dumps(state).encode(), check=True)

    def export(info):
        destination = args.output.resolve()
        destination.mkdir(parents=True, exist_ok=False)
        destination.chmod(0o700)
        (destination / 'container.json').write_text(json.dumps(info, indent=2) + '\n')
        run('cp', args.name + ':/workspace', str(destination / 'workspace'))
        return destination

    if args.action in ('create', 'next-task'):
        valid_id(args.run_id)
        payload = task_payload(args.input)
        workspace = '/workspace/tasks/' + args.run_id
    if args.action == 'create':
        image = json.loads(run('image', 'inspect', args.image))[0]
        if image['Config'].get('User') not in ('node', '1000', '1000:1000'):
            parser.error('Image must use the unprivileged node/1000 user.')
        environment = []
        if args.env_file:
            if not args.env_file.is_file():
                parser.error('Environment file does not exist.')
            environment = ['--env-file', str(args.env_file.resolve())]
        identifier = run('run', '-d', '--name', args.name, '--label', f'{LABEL}=true',
                         '--cap-drop=ALL', '--security-opt=no-new-privileges:true',
                         '--pids-limit=256', '--memory', args.memory, '--cpus=1',
                         *environment, args.image).strip()
        run('exec', args.name, 'mkdir', '-p', '/home/node/service-tools')
        put(payload, workspace)
        save_state({'current': args.run_id, 'runs': [args.run_id]})
    else:
        info = json.loads(run('inspect', args.name))[0]
        if info['Config'].get('Labels', {}).get(LABEL) != 'true':
            raise SystemExit('Refusing a container not created by this helper.')
        identifier = info['Id']
        if args.action == 'inspect':
            print(json.dumps(info, indent=2))
            return
        if args.action == 'export':
            print(export(info))
            return
        if args.action == 'destroy':
            print(run('rm', '-f', args.name).strip())
            return
        state = json.loads(run('exec', args.name, 'cat', STATE))
        previous = valid_id(state['current'])
        if args.run_id in state['runs']:
            parser.error('Run ID already used; preserve history and choose a fresh ID.')
        record = args.session_record.resolve()
        if not record.is_dir() or not any(record.iterdir()):
            parser.error('Collect the previous session before switching tasks.')
        if any(p.is_symlink() for p in record.rglob('*')):
            parser.error('Session archive must not contain symlinks.')
        destination = args.output.resolve()
        if destination == record or record in destination.parents:
            parser.error('Export destination must be outside the session source.')
        destination = export(info)
        shutil.copytree(record, destination / 'session')
        # Stage new inputs before deleting old task files. On export/copy failure,
        # the previous task remains intact. Never remove tool/auth directories.
        put(payload, workspace)
        run('exec', args.name, 'rm', '-rf', '--', '/workspace/tasks/' + previous)
        state.update(current=args.run_id, runs=[*state['runs'], args.run_id])
        save_state(state)
    print(json.dumps({'container': args.name, 'id': identifier,
                      'workspace': workspace, 'run_id': args.run_id, 'context': args.context}))


if __name__ == '__main__':
    main()
