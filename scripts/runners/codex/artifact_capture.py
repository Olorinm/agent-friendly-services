"""Collect new/changed grader files as uid 1000; retain frozen inputs by hash."""
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile

WORKSPACE_ROOT = Path('/workspace')
CONTROLLER_UID = 0


def identity():
    os.setgroups([]); os.setgid(1000); os.setuid(1000)


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    path.chmod(0o600)


def open_regular(root, parts):
    descriptor = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in parts[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor); descriptor = child
        result = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=descriptor)
        if not stat.S_ISREG(os.fstat(result).st_mode):
            os.close(result); raise ValueError('Not a regular file')
        return result
    finally:
        os.close(descriptor)


def trusted_snapshot(private):
    """The grader cannot write this controller-owned original input tree or stdin map."""
    root = private.parent/'inputs'/private.name
    if not root.exists():
        return {'root': str(root), 'available': False, 'entries': {},
                'notice': 'Original input snapshot unavailable; no unchanged files will be omitted.'}
    for path in (private.parent, root.parent, root):
        info = path.lstat()
        if (not stat.S_ISDIR(info.st_mode) or info.st_uid != CONTROLLER_UID
                or info.st_mode & 0o022):
            raise ValueError('Original grading inputs must be controller-owned and not grader-writable')
    entries = {}
    for parent, dirs, files in os.walk(root, followlinks=False):
        for name in sorted(dirs+files):
            path = Path(parent)/name; info = path.lstat()
            if (info.st_uid != CONTROLLER_UID or info.st_mode & 0o022
                    or not (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode))):
                raise ValueError('Unsafe original grading input')
            relative = str(path.relative_to(root))
            entry = {'kind': 'directory' if path.is_dir() else 'file',
                     'mode': stat.S_IMODE(info.st_mode), 'uid': info.st_uid, 'gid': info.st_gid}
            if entry['kind'] == 'file':
                with os.fdopen(open_regular(root, path.relative_to(root).parts), 'rb') as source:
                    before = os.fstat(source.fileno()); digest = hashlib.sha256()
                    while chunk := source.read(1024*1024): digest.update(chunk)
                    after = os.fstat(source.fileno())
                    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                        raise ValueError('Original grading input changed during indexing')
                entry.update(bytes=before.st_size, sha256=digest.hexdigest())
            entries[relative] = entry
    digest = hashlib.sha256(json.dumps(entries, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return {'root': str(root), 'available': True, 'sha256': digest, 'entries': entries,
            'notice': 'Unchanged files remain at these original private input paths; this index is not another copy of their contents.'}


def archive_workspace(workspace, stream, snapshot):
    """Run only as the grader uid; compare content+mode, never names alone."""
    baseline = snapshot['entries']; observed = set(); links = set()
    manifest = {'schema_version': 1, 'scope': 'New or changed grader workspace artifacts; not a full workspace or HTTP capture',
                'input_snapshot': snapshot, 'files': [], 'directories': [], 'omitted': []}
    with tarfile.open(fileobj=stream, mode='w|') as tar:
        def omit(relative, reason, **facts):
            manifest['omitted'].append({'path': relative, 'reason': reason, **facts})

        def walk_error(error):
            omit(str(Path(error.filename).relative_to(workspace)), 'Directory cannot be read')

        for parent, dirs, files in os.walk(workspace, followlinks=False, onerror=walk_error):
            dirs.sort(); files.sort()
            for name in list(dirs):
                path = Path(parent)/name; relative = str(path.relative_to(workspace)); observed.add(relative)
                try:
                    info = path.lstat()
                except OSError as error:
                    dirs.remove(name); omit(relative, str(error)); continue
                if stat.S_ISLNK(info.st_mode):
                    dirs.remove(name); links.add(relative)
                    omit(relative, 'Directory link omitted; target not read', change='replaced_by_link' if relative in baseline else 'new_link')
                    continue
                if not stat.S_ISDIR(info.st_mode):
                    dirs.remove(name); omit(relative, 'Directory changed during capture'); continue
                mode = stat.S_IMODE(info.st_mode); old = baseline.get(relative)
                if old and old['kind'] == 'directory' and old['mode'] == mode:
                    omit(relative, 'Unchanged frozen input directory; original retained', change='unchanged_input', mode=mode)
                else:
                    member = tarfile.TarInfo('artifacts/'+relative); member.type = tarfile.DIRTYPE; member.mode = mode
                    tar.addfile(member)
                    manifest['directories'].append({'path': relative, 'mode': mode, 'change': 'modified_input' if old else 'new'})
            for name in files:
                path = Path(parent)/name; relative = str(path.relative_to(workspace)); observed.add(relative)
                old = baseline.get(relative)
                try:
                    info = path.lstat()
                    if stat.S_ISLNK(info.st_mode):
                        links.add(relative); omit(relative, 'File link omitted; target not read', change='replaced_by_link' if old else 'new_link'); continue
                    with os.fdopen(open_regular(workspace, path.relative_to(workspace).parts), 'rb') as source, tempfile.SpooledTemporaryFile(max_size=8*1024*1024) as saved:
                        before = os.fstat(source.fileno())
                        if before.st_nlink != 1: raise ValueError('Hard link omitted; target not copied')
                        digest = hashlib.sha256(); count = 0
                        while chunk := source.read(1024*1024):
                            saved.write(chunk); digest.update(chunk); count += len(chunk)
                        after = os.fstat(source.fileno()); mode = stat.S_IMODE(before.st_mode)
                        if count != before.st_size or (before.st_size, before.st_mtime_ns, before.st_mode) != (after.st_size, after.st_mtime_ns, after.st_mode):
                            raise ValueError('File changed during capture; not archived')
                        facts = {'bytes': count, 'sha256': digest.hexdigest(), 'mode': mode}
                        if old and old['kind'] == 'file' and all(old[key] == value for key, value in facts.items()):
                            omit(relative, 'Unchanged frozen grading input; original retained', change='unchanged_input', **facts)
                            continue
                        member = tarfile.TarInfo('artifacts/'+relative); member.size = count; member.mode = 0o600
                        saved.seek(0); tar.addfile(member, saved)
                        manifest['files'].append({'path': relative, 'change': 'modified_input' if old else 'new', **facts})
                except (OSError, ValueError) as error:
                    omit(relative, str(error), change='modified_input' if old else 'new')
        for relative in sorted(set(baseline)-observed):
            blocked = any(relative.startswith(link+'/') for link in links)
            omit(relative, 'Frozen input no longer present as a readable workspace entry; original retained',
                 change='unread_under_link' if blocked else 'deleted_input')
        manifest['complete_for_workspace_scope'] = not manifest['omitted']
        data = (json.dumps(manifest, ensure_ascii=False, indent=2)+'\n').encode()
        member = tarfile.TarInfo('artifact-input-index.json'); member.size = len(data); member.mode = 0o600
        tar.addfile(member, io.BytesIO(data))
    return manifest


def collect_artifacts(workspace, private, out):
    if workspace.is_symlink() or workspace.resolve().parent != WORKSPACE_ROOT:
        raise ValueError('Workspace moved outside its authorized root')
    snapshot = trusted_snapshot(private)
    archive = private/'artifacts.tar'
    # Pass only the trusted index over stdin, never a grader-writable baseline.
    # All workspace reads, including link checks, happen as the grader uid.
    code = Path(__file__).read_text()
    with archive.open('wb') as stream:
        archive.chmod(0o600)
        subprocess.run(['python3', '-I', '-c', code, str(workspace)], input=json.dumps(snapshot).encode(),
                       stdout=stream, preexec_fn=identity, check=True)
    if trusted_snapshot(private) != snapshot:
        raise ValueError('Original grading input snapshot changed during collection')
    target = out/'artifacts'; target.mkdir(mode=0o700)
    manifest = None
    with tarfile.open(archive) as stream:
        for member in stream:
            if member.name == 'artifact-input-index.json' and member.isfile():
                raw = stream.extractfile(member).read(); manifest = json.loads(raw)
                (out/'artifact-input-index.json').write_bytes(raw)
                (out/'artifact-input-index.json').chmod(0o600); continue
            if not member.name.startswith('artifacts/') or not (member.isdir() or member.isfile()):
                raise ValueError('Unsafe artifact path or link')
            dest = (out/member.name).resolve()
            if not dest.is_relative_to(target): raise ValueError('Unsafe artifact path')
            if member.isdir(): dest.mkdir(parents=True, exist_ok=True)
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                with dest.open('wb') as file: shutil.copyfileobj(stream.extractfile(member), file)
                dest.chmod(0o600)
    if manifest is None or manifest['input_snapshot'] != snapshot:
        raise ValueError('Missing or inconsistent artifact input snapshot index')
    dump(out/'artifact-omissions.json', manifest['omitted'])


if __name__ == '__main__':
    archive_workspace(Path(sys.argv[1]), sys.stdout.buffer, json.loads(sys.stdin.buffer.read()))
