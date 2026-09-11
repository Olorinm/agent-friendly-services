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

ROOT=Path('/run/afs')
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(): os.setgroups([]);os.setgid(1000);os.setuid(1000)

def collect_artifacts(workspace,private,out):
    if workspace.is_symlink() or workspace.resolve().parent != Path('/workspace'):
        raise ValueError('Workspace moved outside its authorized root')
    # Read executor files as the executor, not as root. Reject links and traversal
    # when unpacking the archive into the controller-only output directory.
    archive=private/'artifacts.tar'
    with archive.open('wb') as stream:
        subprocess.run(['tar','-cf','-','-C',str(workspace),'.'],stdout=stream,preexec_fn=identity,check=True)
    target=out/'artifacts';target.mkdir()
    with tarfile.open(archive) as stream:
        for member in stream:
            dest=(target/member.name).resolve()
            if not dest.is_relative_to(target) or not (member.isdir() or member.isfile()):
                raise ValueError('Unsafe artifact path or link')
            if member.isdir():dest.mkdir(parents=True,exist_ok=True)
            else:
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_bytes(stream.extractfile(member).read())


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
    for parent in (Path('/workspace'),Path('/home/node')):
        for old in parent.iterdir():
            if old.name=='service-tools':continue
            archive=ROOT/'archive'/parent.name;archive.mkdir(parents=True,exist_ok=True)
            shutil.move(str(old),str(archive/(old.name+'-'+str(time.time_ns()))))
    retained=request.get('retained_paths')
    if retained is not None:
        archive=ROOT/'archive'/'service-tools'/run;archive.mkdir(parents=True,exist_ok=True)
        for old in Path('/home/node/service-tools').iterdir():
            if old.name not in retained:shutil.move(str(old),str(archive/old.name))
    shutil.copytree(ROOT/'inputs'/run,workspace);home.mkdir()
    cfg={'$schema':'https://opencode.ai/config.json','model':'zhipuai-coding-plan/'+request['model'],'small_model':'zhipuai-coding-plan/'+request['model'],
         'share':'disabled','autoupdate':False,'agent':{'title':{'disable':True},'summary':{'disable':True}},
         'permission':{'*':'allow','task':'deny','question':'deny'},
         'provider':{'zhipuai-coding-plan':{'options':{'apiKey':'local-capture-proxy','baseURL':'http://127.0.0.1:18181/api/coding/paas/v4'},'models':{request['model']:{'variants':{'high':{'reasoningEffort':'high'}}}}}}}
    (home/'.config/opencode').mkdir(parents=True)
    dump(home/'.config/opencode/opencode.json',cfg)
    for p in (workspace,home):
        subprocess.run(['chown','-R','1000:1000',str(p)],check=True)
    proxy=subprocess.Popen(['python3',str(ROOT/'capture-proxy.py'),'--key',str(ROOT/'bigmodel.key'),'--output',str(out/'wire')],stdout=(private/'proxy.log').open('wb'),stderr=subprocess.STDOUT)
    env={'HOME':str(home),'PATH':'/usr/local/bin:/usr/bin:/bin','LANG':'C.UTF-8','OPENCODE_DISABLE_AUTOUPDATE':'true','OPENCODE_DISABLE_TERMINAL_TITLE':'true','OPENCODE_DISABLE_AUTOCOMPACT':'true'}
    started=now();timed_out=False
    command=['opencode','run','--pure','--format','json','--model','zhipuai-coding-plan/'+request['model'],'--variant',request['reasoning_effort'],'--title',run]
    prompt=(workspace/'prompt.txt').read_bytes()
    with (out/'events.jsonl').open('wb') as events,(out/'stderr.log').open('wb') as err:
        process=subprocess.Popen(command,cwd=workspace,env=env,stdin=subprocess.PIPE,stdout=events,stderr=err,preexec_fn=identity,start_new_session=True)
        dump(private/'process.json',{'pid':process.pid,'proxy_pid':proxy.pid,'started_at':started})
        try: process.communicate(prompt,timeout=request['seconds']-10)
        except subprocess.TimeoutExpired:
            timed_out=True;os.killpg(process.pid,signal.SIGTERM)
            try: process.communicate(timeout=3)
            except subprocess.TimeoutExpired: os.killpg(process.pid,signal.SIGKILL);process.communicate()
    ended=now();time.sleep(0.2);proxy.terminate();proxy.wait(timeout=5)
    rows=[]
    for line in (out/'events.jsonl').read_text().splitlines():
        try: rows.append(json.loads(line))
        except json.JSONDecodeError: pass
    session=next((r['sessionID'] for r in rows if r.get('sessionID')),None)
    (out/'answer.md').write_text('\n'.join(r['part']['text'] for r in rows if r.get('type')=='text'))
    if session:
        with (out/'session.json').open('wb') as f:
            subprocess.run(['opencode','export',session],cwd=workspace,env=env,stdout=f,stderr=(out/'export.stderr').open('wb'),preexec_fn=identity,timeout=20)
    collect_artifacts(workspace,private,out)
    # Preserve state for inspection without exposing it to the next task or copying service keys to grading.
    dump(out/'retained-files.json',[str(p.relative_to('/home/node/service-tools')) for p in Path('/home/node/service-tools').rglob('*') if p.is_file()])
    if (out/'artifacts/assessment.json').is_file():
        if (out/'artifacts/assessment.json').is_symlink():raise ValueError('Assessment must not be a symlink')
        shutil.copyfile(out/'artifacts/assessment.json',out/'assessment.json')
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
    dump(out/'receipt.json',dict(session_id=session,workspace=str(workspace),model=request['model'],reasoning_effort=request['reasoning_effort'],harness=request['harness'],runtime=request['runtime'],started_at=started,ended_at=ended,exit_code=process.returncode,timed_out=timed_out,isolation='Dedicated Docker container; uid 1000 executor; fresh home/session/workspace; controller-only raw model capture; retained service-tools',input_verified=verified))
    normalize(out,request['model'])
    dump(private/'done.json',{'status':'completed' if process.returncode==0 else 'failed'})

if __name__=='__main__':main()
