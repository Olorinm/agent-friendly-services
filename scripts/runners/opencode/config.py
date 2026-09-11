"""Private connection settings shared by provisioning and dispatch."""
import json
from pathlib import Path, PurePosixPath
import re
import shlex
import subprocess


def load(path):
    path = Path(path).resolve()
    config = json.loads(path.read_text())
    host = config['host']
    if not isinstance(host, str) or not re.fullmatch(r'[A-Za-z0-9_][A-Za-z0-9_.@-]*', host):
        raise ValueError('host must be an SSH alias or user@host; configure ports/keys in SSH config')
    root = config['remote_root']
    if not isinstance(root, str) or not root.startswith('/') or '..' in PurePosixPath(root).parts or root == '/':
        raise ValueError('remote_root must be a dedicated absolute directory')
    config['remote_root'] = root.rstrip('/')
    containers = config['containers']
    if not containers or len(set(containers.values())) != len(containers):
        raise ValueError('Each runtime must have a separate container')
    for runtime, container in containers.items():
        if any(not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', x) for x in (runtime, container)):
            raise ValueError('Invalid runtime or container name')
        retained = config['retained_paths'][runtime]
        if not isinstance(retained, list) or any(
            not isinstance(x, str) or x in ('.', '..') or not re.fullmatch(r'[A-Za-z0-9_.-]+', x)
            for x in retained
        ):
            raise ValueError('retained_paths must list top-level entries per runtime')
    return config


def ssh(config, argv, data=None, check=True):
    return subprocess.run(
        ['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=8', config['host'], shlex.join(argv)],
        input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check,
    )
