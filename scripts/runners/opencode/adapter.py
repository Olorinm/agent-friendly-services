#!/usr/bin/env python3
"""SSH command adapter for the repository pipeline and pre-provisioned containers.

Private config: {host, remote_root, containers: {runtime_id: container_name}}.
No infrastructure addresses, service credentials, or subscription keys belong here.
"""
import argparse
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import re
import shlex
import subprocess
import tarfile
from assessment import normalize as normalize_assessment
from config import load, ssh as remote_ssh
from tool_records import extract as extract_tool_records
from runtime_status import query as query_runtime_status
from providers import DEFAULT_PROVIDER, validate_model
from runtime_code import manifest as code_manifest, verify as verify_runtime_code

p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True);p.add_argument('operation',choices=['preflight','start','status','collect','stop']);p.add_argument('request',type=Path);a=p.parse_args()
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

if a.operation=='preflight':
    from network_preflight import validate
    plan=validate(r['preflight'])
    script=Path(__file__).with_name('network_preflight.py').read_text()
    result=docker('exec','-u','1000',container,'python3','-c',script,json.dumps(plan),check=False)
    print(json.dumps(json.loads(result.stdout) if result.returncode==0 else
                     {'ready':False,'reason':'Container preflight failed or exceeded its 18-second bound; inspect private adapter log'}))
elif a.operation=='start':
    r['provider']=c.get('provider',DEFAULT_PROVIDER)
    validate_model(r['provider'],r['model'])
    observed = verify_runtime_code(exec_root, code_manifest(Path(__file__).parent))
    r['runtime_code_preflight'] = {'source_sha256': observed,
        'verified_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Controller read of root-injected support files before run allocation; not a mid-run immutability guarantee.'}
    if 'max_model_requests' in r and c.get('max_model_requests',r['max_model_requests']) < r['max_model_requests']:
        raise ValueError('Adapter request cap is lower than the frozen role budget; reconcile before allocation')
    if 'deadline_epoch' in c and c['deadline_epoch'] < __import__('time').time()+r['seconds']:
        raise ValueError('Adapter deadline cannot accommodate the frozen role budget; no run allocated')
    r['runtime_image_id']=docker('inspect','--format','{{.Image}}',container).stdout.decode().strip()
    for key in ('max_model_requests','deadline_epoch'):
        if key in c:r[key]=min(r.get(key,c[key]),c[key])
    r['retained_paths']=c['retained_paths'][r['runtime']]
    r['retained_children']=c.get('retained_children',{}).get(r['runtime'],{})
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
    print(json.dumps(query_runtime_status(
        lambda: exec_root('cat','/run/afs/'+run+'/done.json',check=False),
        lambda: exec_root('pgrep','-af','^python3 /run/afs/worker.py /run/afs/'+run+'.request.json$',check=False))))
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
    if (out/'events.jsonl').is_file():
        if not (out/'usage.json').exists():
            from normalize import normalize
            normalize(out,r['model'])
        extract_tool_records(out)
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
    script=Path(__file__).with_name('runtime_stop.py').read_text()
    pattern='^python3 /run/afs/worker.py '+re.escape('/run/afs/'+run+'.request.json')+'$'
    result=exec_root('python3','-c',script,'/run/afs/'+run,pattern,check=False)
    if result.returncode:
        print(json.dumps({'stopped':False,'reason':'Stop verification failed; inspect owned runtime'}))
    else:
        print(json.dumps(json.loads(result.stdout)))
