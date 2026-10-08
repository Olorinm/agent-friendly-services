#!/usr/bin/env python3
"""Run inside a dedicated container as root; OpenCode itself runs as uid 1000.

Controller-only files and model credentials live in /run/afs (0700). The model
can read only its fresh workspace/home plus retained service-tools. Container
creation and provisioning are the adapter operator's responsibility.
"""
import datetime
import fcntl
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import tarfile
from normalize import normalize
from providers import DEFAULT_PROVIDER, opencode_config, profile

ROOT=Path('/run/afs')
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(): os.setgroups([]);os.setgid(1000);os.setuid(1000)

def archive_session_artifacts(parents, archive_root, service_tools):
    for parent in parents:
        for old in parent.iterdir():
            if old==service_tools:continue
            archive=archive_root/str(parent).lstrip('/');archive.mkdir(parents=True,exist_ok=True)
            shutil.move(str(old),str(archive/(old.name+'-'+str(time.time_ns()))))

def archive_service_artifacts(tools, archive, retained, children):
    if tools.is_symlink() or not tools.is_dir():
        raise ValueError('Service tools must be a real directory')
    # Validate before moving anything. Never traverse a model-created alias.
    for name in children:
        parent=tools/name
        if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
            raise ValueError('Retained child policy requires a real directory')
    archive.mkdir(parents=True,exist_ok=False)
    for old in tools.iterdir():
        if old.name not in retained:
            shutil.move(str(old),str(archive/old.name))
        elif old.name in children:
            for child in old.iterdir():
                if child.name not in children[old.name]:
                    target=archive/old.name;target.mkdir(exist_ok=True)
                    shutil.move(str(child),str(target/child.name))

def collect_artifacts(workspace,private,out):
    if workspace.is_symlink() or workspace.resolve().parent != Path('/workspace'):
        raise ValueError('Workspace moved outside its authorized root')
    # Read executor files as the executor, not as root. Reject links and traversal
    # when unpacking the archive into the controller-only output directory.
    archive=private/'artifacts.tar'
    with archive.open('wb') as stream:
        subprocess.run(['tar','-cf','-','-C',str(workspace),'.'],stdout=stream,preexec_fn=identity,check=True)
    target=out/'artifacts';target.mkdir()
    omitted=[]
    with tarfile.open(archive) as stream:
        for member in stream:
            dest=(target/member.name).resolve()
            if not dest.is_relative_to(target):
                raise ValueError('Unsafe artifact path or link')
            if member.issym() or member.islnk():
                # Never follow executor links, even when they look internal.
                # Preserve the omission so graders can distinguish it from a
                # missing deliverable without losing unrelated regular files.
                omitted.append({'path':member.name,'reason':'Link omitted; target not read'})
                continue
            if not (member.isdir() or member.isfile()):
                raise ValueError('Unsafe artifact type')
            if member.isdir():dest.mkdir(parents=True,exist_ok=True)
            else:
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_bytes(stream.extractfile(member).read())
    dump(out/'artifact-omissions.json',omitted)


def main():
    os.umask(0o077)
    # One service/route container retains state: never let two tasks clear it
    # concurrently, even if multiple controllers dispatch at the same time.
    lock=(ROOT/'worker.lock').open('a')
    fcntl.flock(lock,fcntl.LOCK_EX | fcntl.LOCK_NB)
    request=json.loads(Path(sys.argv[1]).read_text());run=request['run_id']+'-'+request['role']
    private=ROOT/run;private.mkdir(exist_ok=False)
    out=private/'output';out.mkdir()
    workspace=Path('/workspace')/run;home=Path('/home/node')/run
    # Previous task artifacts are archived to controller-only storage. Only
    # service-tools persists as executor-readable state between batch tasks.
    archive_session_artifacts((Path('/workspace'),Path('/home/node'),Path('/tmp'),Path('/var/tmp')),
                              ROOT/'archive',Path('/home/node/service-tools'))
    retained=request.get('retained_paths')
    if retained is not None:
        archive_service_artifacts(Path('/home/node/service-tools'),
            ROOT/'archive'/'service-tools'/run,retained,request.get('retained_children',{}))
    shutil.copytree(ROOT/'inputs'/run,workspace);home.mkdir()
    provider=json.loads((ROOT/'provider.json').read_text())['provider']
    if request.get('provider',DEFAULT_PROVIDER)!=provider:
        raise ValueError('Dispatch provider differs from provisioned runtime')
    route=profile(provider)
    cfg=opencode_config(request,provider)
    (home/'.config/opencode').mkdir(parents=True)
    dump(home/'.config/opencode/opencode.json',cfg)
    for p in (workspace,home):
        subprocess.run(['chown','-R','1000:1000',str(p)],check=True)
    proxy_command=['python3',str(ROOT/'capture-proxy.py'),'--provider',provider,'--model',request['model'],'--key',str(ROOT/'model.key'),'--output',str(out/'wire')]
    if 'max_model_requests' in request:proxy_command += ['--max-requests',str(request['max_model_requests'])]
    if 'deadline_epoch' in request:proxy_command += ['--deadline',str(request['deadline_epoch'])]
    proxy=subprocess.Popen(proxy_command,stdout=(private/'proxy.log').open('wb'),stderr=subprocess.STDOUT)
    env={'HOME':str(home),'PATH':'/usr/local/bin:/usr/bin:/bin','LANG':'C.UTF-8','OPENCODE_DISABLE_AUTOUPDATE':'true','OPENCODE_DISABLE_TERMINAL_TITLE':'true','OPENCODE_DISABLE_AUTOCOMPACT':'true'}
    started=now();timed_out=False
    command=['opencode','run','--pure','--format','json','--model',cfg['model'],'--variant',request['reasoning_effort'],'--title',run]
    prompt=(workspace/'prompt.txt').read_bytes()
    with (out/'events.jsonl').open('wb') as events,(out/'stderr.log').open('wb') as err:
        process=subprocess.Popen(command,cwd=workspace,env=env,stdin=subprocess.PIPE,stdout=events,stderr=err,preexec_fn=identity,start_new_session=True)
        dump(private/'process.json',{'pid':process.pid,'proxy_pid':proxy.pid,'started_at':started})
        timeout=request['seconds']-10
        if 'deadline_epoch' in request:timeout=min(timeout,max(0,request['deadline_epoch']-time.time()-5))
        try: process.communicate(prompt,timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out=True;os.killpg(process.pid,signal.SIGTERM)
            try: process.communicate(timeout=3)
            except subprocess.TimeoutExpired: os.killpg(process.pid,signal.SIGKILL);process.communicate()
    ended=now();time.sleep(0.2);proxy.terminate();proxy.wait(timeout=5)
    rows=[]
    for line in (out/'events.jsonl').read_text().split('\n'):
        try: rows.append(json.loads(line))
        except json.JSONDecodeError: pass
    session=next((r['sessionID'] for r in rows if r.get('sessionID')),None)
    (out/'answer.md').write_text('\n'.join(r['part']['text'] for r in rows if r.get('type')=='text'))
    if session:
        with (out/'session.json').open('wb') as f:
            subprocess.run(['opencode','export',session],cwd=workspace,env=env,stdout=f,stderr=(out/'export.stderr').open('wb'),preexec_fn=identity,timeout=20)
    requests=[json.loads(p.read_text()) for p in (out/'wire').glob('*/request.json')]
    def strings(value):
        if isinstance(value,str):return [value]
        if isinstance(value,list):return [s for v in value for s in strings(v)]
        if isinstance(value,dict):return [s for v in value.values() for s in strings(v)]
        return []
    payload='\n'.join(s for r in requests for s in strings(r.get('messages',[])))
    role=(ROOT/'inputs'/run/'AGENTS.md').read_text().strip()
    # Confirm the actual outbound request contains the role plus frozen prompt.
    verified=bool(requests) and role in payload and all(line in payload for line in prompt.decode().splitlines() if line.strip()) and all(r.get('model')==request['model'] and r.get('reasoning_effort')==request['reasoning_effort'] for r in requests)
    dump(out/'receipt.json',dict(session_id=session,workspace=str(workspace),provider=provider,model_api='https://'+route['host']+route['base_path']+'/chat/completions',model=request['model'],reasoning_effort=request['reasoning_effort'],harness=request['harness'],runtime=request['runtime'],started_at=started,ended_at=ended,exit_code=process.returncode,timed_out=timed_out,isolation='Dedicated Docker container; uid 1000 executor; fresh home/session/workspace; controller-only raw model capture; retained service-tools',input_verified=verified))
    dump(out/'controller-limits.json',{key:request[key] for key in ('max_model_requests','deadline_epoch') if key in request})
    if 'runtime_code_preflight' in request:
        receipt=json.loads((out/'receipt.json').read_text())
        receipt['runtime_code_preflight']=request['runtime_code_preflight']
        dump(out/'receipt.json',receipt)
    normalize(out,request['model'])
    # Persist actual process status and usage before collecting untrusted files.
    # Collection errors must not erase the already observed runtime receipt.
    collect_artifacts(workspace,private,out)
    # Preserve state for inspection without exposing it to the next task or copying service keys to grading.
    dump(out/'retained-files.json',[str(p.relative_to('/home/node/service-tools')) for p in Path('/home/node/service-tools').rglob('*') if p.is_file()])
    if (out/'artifacts/assessment.json').is_file():
        shutil.copyfile(out/'artifacts/assessment.json',out/'assessment.json')
    dump(private/'done.json',{'status':'completed' if process.returncode==0 else 'failed'})

if __name__=='__main__':main()
