#!/usr/bin/env python3
"""Docker integration check: reuse, archive, cleanup, and failed switch protection.

Creates and removes only its own test container. No service or model calls.
"""
import argparse
import json
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--context', required=True)
p.add_argument('--image', default='afs-trial-base:local')
a = p.parse_args()
name = 'afs-lifecycle-check-' + uuid.uuid4().hex[:10]
docker = ['docker', '--context', a.context]
helper = [sys.executable, str(Path(__file__).with_name('trial-container.py')), '--context', a.context]


def call(*args):
    return subprocess.check_output(args, text=True)


with tempfile.TemporaryDirectory(prefix='afs-lifecycle-check-') as tmp:
    root = Path(tmp)
    source = root / 'input'
    source.mkdir()
    (source / 'AGENTS.md').write_text('Synthetic lifecycle fixture; no agent executes this.\n')
    record = root / 'record'
    record.mkdir()
    (record / 'session.json').write_text('{"synthetic":true}\n')
    created = False
    try:
        first = json.loads(call(*helper, 'create', name, '--image', a.image, '--input', str(source)))
        created = True
        call(*docker, 'exec', name, 'python3', '-c',
             'from pathlib import Path; '
             'Path("/home/node/service-tools/installed").write_text("version-1"); '
             'Path("/home/node/auth-fixture").write_text("synthetic-auth"); '
             'Path("/workspace/tasks/access/answer.txt").write_text("old-answer")')
        second = json.loads(call(*helper, 'next-task', name, '--run-id', 'business-001',
                                 '--input', str(source), '--session-record', str(record),
                                 '--output', str(root / 'archive')))
        assert first['id'] == second['id']
        assert first['workspace'] != second['workspace']
        assert (root / 'archive/workspace/tasks/access/answer.txt').read_text() == 'old-answer'
        assert (root / 'archive/session/session.json').is_file()
        call(*docker, 'exec', name, 'python3', '-c',
             'from pathlib import Path; '
             'assert not Path("/workspace/tasks/access").exists(); '
             'assert Path("/workspace/tasks/business-001/AGENTS.md").exists(); '
             'assert Path("/home/node/service-tools/installed").read_text()=="version-1"; '
             'assert Path("/home/node/auth-fixture").read_text()=="synthetic-auth"')
        # An existing export destination must fail before touching current files.
        failure = subprocess.run([*helper, 'next-task', name, '--run-id', 'business-002',
                                  '--input', str(source), '--session-record', str(record),
                                  '--output', str(root / 'archive')], capture_output=True)
        assert failure.returncode != 0
        call(*docker, 'exec', name, 'test', '-f', second['workspace'] + '/AGENTS.md')
        duplicate = subprocess.run([*helper, 'next-task', name, '--run-id', 'access',
                                    '--input', str(source), '--session-record', str(record),
                                    '--output', str(root / 'unused')], capture_output=True)
        assert duplicate.returncode != 0 and not (root / 'unused').exists()
        info = json.loads(call(*helper, 'inspect', name))
        assert not info['Mounts'] and info['Config']['User'] == 'node'
        print('PASS: same container, preserved install/auth, fresh task files, archive, failure protection, no mounts')
    finally:
        if created:
            call(*helper, 'destroy', name)
