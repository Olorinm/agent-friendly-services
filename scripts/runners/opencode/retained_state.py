"""Restore an operator-sealed baseline, never a model-mutated configuration."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def seal(tools, baseline):
    tools, baseline = Path(tools), Path(baseline)
    if baseline.exists():
        raise ValueError('Baseline already sealed; use a fresh runtime for different preparation')
    if tools.is_symlink() or not tools.is_dir():
        raise ValueError('Baseline source must be a real directory')
    entries = {}
    for path in sorted(tools.rglob('*')):
        if path.is_symlink() or not (path.is_dir() or path.is_file()):
            raise ValueError('Baseline cannot contain links or special files')
        if path.is_file():
            if path.stat().st_nlink != 1:
                raise ValueError('Baseline cannot contain hard links')
            entries[str(path.relative_to(tools))] = {'sha256': sha(path), 'mode': stat.S_IMODE(path.stat().st_mode) & 0o777}
    baseline.mkdir(mode=0o700)
    shutil.copytree(tools, baseline/'files')
    manifest = baseline/'manifest.json'
    manifest.write_text(json.dumps({'schema_version': 1, 'files': entries}, sort_keys=True)+'\n')
    for path in baseline.rglob('*'):
        path.chmod(0o700 if path.is_dir() else 0o600)
    return sha(manifest)


def verify(baseline, expected=None):
    baseline = Path(baseline)
    manifest = baseline/'manifest.json'
    if (baseline.is_symlink() or manifest.is_symlink() or not manifest.is_file()
            or (baseline/'files').is_symlink() or not (baseline/'files').is_dir()):
        raise ValueError('Missing operator-sealed baseline; provision a fresh runtime')
    digest = sha(manifest)
    if expected and digest != expected:
        raise ValueError('Sealed baseline manifest changed')
    entries = json.loads(manifest.read_text())['files']
    observed = {}
    for path in (baseline/'files').rglob('*'):
        if path.is_symlink() or not (path.is_file() or path.is_dir()):
            raise ValueError('Unsafe baseline file')
        if path.is_file(): observed[str(path.relative_to(baseline/'files'))] = sha(path)
    if observed != {name: value['sha256'] for name, value in entries.items()}:
        raise ValueError('Sealed baseline bytes changed')
    return digest


def restore(tools, baseline, archive, expected=None, owner=None):
    tools, baseline, archive = Path(tools), Path(baseline), Path(archive)
    digest = verify(baseline, expected)
    archive.mkdir(parents=True, exist_ok=False)
    # Move the directory itself, including malicious links, without following it.
    if tools.exists() or tools.is_symlink(): shutil.move(str(tools), str(archive/'previous-state'))
    shutil.copytree(baseline/'files', tools)
    entries = json.loads((baseline/'manifest.json').read_text())['files']
    for path in [tools, *tools.rglob('*')]:
        path.chmod(0o700 if path.is_dir() else entries[str(path.relative_to(tools))]['mode'])
        if owner is not None: os.chown(path, *owner)
    return {'policy': 'sealed-baseline', 'baseline_sha256': digest,
            'baseline_files': {name: value['sha256'] for name, value in entries.items()},
            'notice': 'Only operator-sealed bytes restored. Model-written configuration and answers archived, never inherited.'}


if __name__ == '__main__':
    root = Path('/run/afs')
    if sys.argv[1] == 'seal':
        if list(root.glob('*.request.json')):
            raise ValueError('Cannot seal model-used state; prepare a fresh runtime')
        print(json.dumps({'baseline_sha256': seal('/home/node/service-tools', root/'retained-baseline')}))
    elif sys.argv[1] == 'verify':
        print(json.dumps({'baseline_sha256': verify(root/'retained-baseline')}))
