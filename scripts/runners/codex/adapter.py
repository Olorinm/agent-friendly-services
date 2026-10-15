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

# Controller-only preparation, before any uid 1000 worker can read the import.
# Materialized input bytes are unchanged; imported owners/modes are not trusted.
PREPARE_INPUT_TREE = r'''
import hashlib,json,os,stat,sys
from pathlib import Path
root=Path('/run/afs'); tree=Path(sys.argv[1])
if os.geteuid()!=0 or tree.parent!=root/'inputs' or tree.name in ('','.','..'):
    raise ValueError('Dedicated controller input tree required')
for parent in (root, tree.parent):
    s=parent.lstat()
    if not stat.S_ISDIR(s.st_mode) or s.st_uid!=0 or s.st_mode & 0o022:
        raise ValueError('Input parent must be protected and root-owned')
if root.stat().st_mode & 0o077:
    raise ValueError('Controller root must be private')
entries=[]; hashes={}
def walk_error(error): raise error
for parent,dirs,files in os.walk(tree,followlinks=False,onerror=walk_error):
    for path in [Path(parent),*[Path(parent)/name for name in files]]:
        s=path.lstat()
        if not (stat.S_ISDIR(s.st_mode) or stat.S_ISREG(s.st_mode)):
            raise ValueError('Input links and special files forbidden')
        if stat.S_ISREG(s.st_mode) and s.st_nlink!=1:
            raise ValueError('Input hard links must be materialized before import')
        entries.append((path,s))
    # os.walk does not descend into directory links; reject them explicitly.
    for name in dirs:
        if not stat.S_ISDIR((Path(parent)/name).lstat().st_mode):
            raise ValueError('Input directory links forbidden')
if not entries or tree.is_symlink():
    raise ValueError('Missing or linked input tree')
def digest(fd):
    h=hashlib.sha256();os.lseek(fd,0,os.SEEK_SET)
    with os.fdopen(os.dup(fd),'rb') as f:
        while chunk:=f.read(1024*1024):h.update(chunk)
    return h.hexdigest()
# Validate the entire tree before changing any ownership or permissions.
for path,s in entries:
    if stat.S_ISREG(s.st_mode):
        fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK)
        try:hashes[str(path.relative_to(tree))]=digest(fd)
        finally:os.close(fd)
for path,s in entries:
    fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK|(os.O_DIRECTORY if stat.S_ISDIR(s.st_mode) else 0))
    try:
        current=os.fstat(fd)
        if (current.st_dev,current.st_ino,current.st_size)!=(s.st_dev,s.st_ino,s.st_size):
            raise ValueError('Input changed during preparation')
        os.fchown(fd,0,0)
        os.fchmod(fd,stat.S_IMODE(s.st_mode)&0o777&~0o022)
        after=os.fstat(fd)
        if after.st_uid!=0 or after.st_gid!=0 or after.st_mode & 0o7022:
            raise ValueError('Input ownership/mode normalization failed')
        if stat.S_ISREG(s.st_mode) and digest(fd)!=hashes[str(path.relative_to(tree))]:
            raise ValueError('Input bytes changed during preparation')
    finally:os.close(fd)
print(json.dumps({'policy':'root-owned-data-input-v1','root':str(tree),'files':len(hashes),
    'content_sha256':hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest(),
    'content_unchanged':True,'uid':0,'gid':0,'group_other_write_and_special_bits_removed':True}))
'''


def archive(directory):
    stream = io.BytesIO()
    root = Path(directory)
    if root.is_symlink() or not root.is_dir(): raise ValueError('Real input directory required')
    # A tar hard-link member can retain the original host uid after Docker cp.
    # Materialize every regular member; never change or unlink the source alias.
    with tarfile.open(fileobj=stream, mode='w', dereference=True) as tar:
        for file in root.rglob('*'):
            if file.is_symlink(): raise ValueError('Input links forbidden')
            if not (file.is_dir() or file.is_file()): raise ValueError('Input special files forbidden')
            if file.is_file(): tar.add(file, arcname=str(file.relative_to(directory)), recursive=False)
    return stream.getvalue()


def prepare_inputs(exec_root, directory):
    return json.loads(exec_root('python3', '-I', '-c', PREPARE_INPUT_TREE, directory).stdout)


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
        request['input_preparation'] = prepare_inputs(root, '/run/afs/inputs/'+run)
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
