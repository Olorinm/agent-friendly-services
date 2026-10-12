"""Collect grader artifacts as uid 1000; never follow links into credentials."""
import json
import os
from pathlib import Path
import subprocess
import tarfile

def identity():
    os.setgroups([]); os.setgid(1000); os.setuid(1000)

def dump(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n")

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
