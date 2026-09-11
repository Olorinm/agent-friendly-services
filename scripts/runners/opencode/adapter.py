#!/usr/bin/env python3
"""SSH command adapter for the repository pipeline and pre-provisioned containers.

Private config: {host, remote_root, containers: {runtime_id: container_name}}.
No infrastructure addresses, service credentials, or subscription keys belong here.
"""
import argparse
import io
import json
from pathlib import Path
import re
import shlex
import subprocess
import tarfile
from assessment import normalize as normalize_assessment
from config import load, ssh as remote_ssh

p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True);p.add_argument('operation',choices=['start','status','collect','stop']);p.add_argument('request',type=Path);a=p.parse_args()
c=load(a.config);r=json.loads(a.request.read_text());container=c['containers'][r['runtime']];run=(r.get('handle') if a.operation!='start' else None) or r['run_id']+'-'+r['role']
if not re.fullmatch(r'[A-Za-z0-9._-]+',run) or not re.fullmatch(r'[A-Za-z0-9._-]+',container):raise ValueError('Invalid runtime/run name')
remote=c['remote_root']+'/runs/'+run

def ssh(argv,data=None,check=True):
    return remote_ssh(c,argv,data=data,check=check)
def docker(*args,**kwargs):return ssh(['sudo','-n','docker',*args],**kwargs)
def exec_root(*args,**kwargs):return docker('exec','-u','0',container,*args,**kwargs)
def put(directory):
    buf=io.BytesIO()
    with tarfile.open(fileobj=buf,mode='w') as tar:
        for file in Path(directory).rglob('*'):
            if file.is_symlink():raise ValueError('Input symlinks not allowed')
            if file.is_file():tar.add(file,arcname=str(file.relative_to(directory)),recursive=False)
    return buf.getvalue()

if a.operation=='start':
    r['retained_paths']=c['retained_paths'][r['runtime']]
    if not isinstance(r['retained_paths'],list):raise ValueError('Specify retained_paths for each runtime')
    if r['retained_paths'] is not None and any(not re.fullmatch(r'[A-Za-z0-9._-]+',name) for name in r['retained_paths']):raise ValueError('Retention entries must be top-level names')
    # Exclusive remote directory protects uncertain dispatches from duplicate starts.
    ssh(['mkdir','-m','700',remote])
    ssh(['tar','-xf','-','-C',remote],put(r['input']))
    exec_root('mkdir','-p','/run/afs/inputs/'+run)
    docker('cp',remote+'/.',container+':/run/afs/inputs/'+run)
    payload=json.dumps(r).encode()
    ssh(['tee',remote+'.request.json'],payload)
    docker('cp',remote+'.request.json',container+':/run/afs/'+run+'.request.json')
    script='exec python3 /run/afs/worker.py '+shlex.quote('/run/afs/'+run+'.request.json')+' > /run/afs/'+run+'.worker.log 2>&1'
    docker('exec','-d','-u','0',container,'sh','-c',script)
    print(json.dumps({'handle':run}))
elif a.operation=='status':
    result=exec_root('cat','/run/afs/'+run+'/done.json',check=False)
    if result.returncode==0:print(result.stdout.decode())
    else:
        if result.returncode != 1:raise RuntimeError('Remote status read failed: '+result.stderr.decode())
        process=exec_root('pgrep','-af','^python3 /run/afs/worker.py /run/afs/'+run+'.request.json$',check=False)
        if process.returncode != 0:raise RuntimeError('Worker state unavailable; do not infer completion or redispatch: '+process.stderr.decode())
        print(json.dumps({'status':'running'}))
elif a.operation=='collect':
    out=Path(r['output']);out.mkdir(parents=True,exist_ok=True)
    # Tar comes only from the controller directory, never execute collected files.
    result=exec_root('tar','-cf','-','-C','/run/afs/'+run+'/output','.')
    with tarfile.open(fileobj=io.BytesIO(result.stdout),mode='r:') as tar:
        for item in tar:
            dest=(out/item.name).resolve()
            if not dest.is_relative_to(out.resolve()) or not (item.isdir() or item.isfile()):raise ValueError('Unsafe collection archive')
            if item.isdir():dest.mkdir(parents=True,exist_ok=True)
            else:
                dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(tar.extractfile(item).read());dest.chmod(0o600)
    assessment=out/'assessment.json'
    if r['role']=='grading' and assessment.exists():
        raw=assessment.read_bytes()
        (out/'assessment.raw.json').write_bytes(raw)
        normalized,changes=normalize_assessment(json.loads(raw))
        for item in normalized.get('evidence',[]):
            if (item.get('path')=='execution/artifacts/answer.md'
                    and not (out.parent/'execution/artifacts/answer.md').exists()
                    and (out.parent/'execution/answer.md').is_file()):
                item['path']='execution/answer.md'
                changes.append('Mapped final-answer alias to the captured execution/answer.md; content unchanged')
        if changes:
            assessment.write_text(json.dumps(normalized,ensure_ascii=False,indent=2)+'\n')
            (out/'adapter-normalizations.json').write_text(json.dumps(changes)+'\n')
    print(json.dumps({'collected':True}))
else:
    # Stop only this worker's recorded process group. Container service state persists.
    script="import json,os,signal; p=json.load(open(%r)); os.killpg(p['pid'],signal.SIGTERM)" % ('/run/afs/'+run+'/process.json')
    exec_root('python3','-c',script,check=False)
    print(json.dumps({'stopped':True}))
