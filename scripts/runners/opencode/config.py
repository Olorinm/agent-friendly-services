"""Private connection settings shared by provisioning and dispatch."""
import json
import math
from pathlib import Path, PurePosixPath
import re
import shlex
import subprocess
from providers import DEFAULT_PROVIDER, profile, validate_model


def load(path):
    path = Path(path).resolve()
    config = json.loads(path.read_text())
    profile(config.get('provider', DEFAULT_PROVIDER))
    if 'model' in config:
        validate_model(config.get('provider', DEFAULT_PROVIDER), config['model'])
    if 'max_model_requests' in config and (type(config['max_model_requests']) is not int or config['max_model_requests'] <= 0):
        raise ValueError('max_model_requests must be a positive integer')
    if 'deadline_epoch' in config and (type(config['deadline_epoch']) not in (int,float) or not math.isfinite(config['deadline_epoch']) or config['deadline_epoch'] <= 0):
        raise ValueError('deadline_epoch must be a finite positive Unix timestamp')
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
    children = config.get('retained_children', {})
    if not isinstance(children, dict) or set(children) - set(containers):
        raise ValueError('retained_children must name configured runtimes')
    for runtime, container in containers.items():
        if any(not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', x) for x in (runtime, container)):
            raise ValueError('Invalid runtime or container name')
        retained = config['retained_paths'][runtime]
        if not isinstance(retained, list) or any(
            not isinstance(x, str) or x in ('.', '..') or not re.fullmatch(r'[A-Za-z0-9_.-]+', x)
            for x in retained
        ):
            raise ValueError('retained_paths must list top-level entries per runtime')
        nested = children.get(runtime, {})
        if not isinstance(nested, dict) or set(nested) - set(retained):
            raise ValueError('retained_children must name retained top-level directories')
        for names in nested.values():
            if not isinstance(names, list) or any(
                not isinstance(x, str) or x in ('.', '..') or not re.fullmatch(r'[A-Za-z0-9_.-]+', x)
                for x in names
            ):
                raise ValueError('retained_children must list direct child names')
    return config


def ssh(config, argv, data=None, check=True):
    return subprocess.run(
        ['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=8', config['host'], shlex.join(argv)],
        input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check,
    )
