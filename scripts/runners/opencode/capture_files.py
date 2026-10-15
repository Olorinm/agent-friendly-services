"""Bounded private file capture as executor uid; never execute collected files."""
import hashlib
import io
import json
import os
from pathlib import Path
import stat
import sys
import tarfile

DEFAULT_LIMITS = {'file_bytes': 16*1024*1024, 'total_bytes': 64*1024*1024, 'files': 1024}
# Reserved harness/package cache locations only. Do not exclude similarly named
# task files in /tmp, user-installed dependencies, configuration or session data.
HOME_CACHE_DIRECTORIES = {('.config', 'opencode', 'node_modules'), ('.npm', '_cacache')}
HOME_CACHE_FILES = {('.cache', 'opencode', 'models.json')}


def open_regular(root, parts):
    descriptor = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in parts[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor);descriptor = child
        result = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=descriptor)
        if not stat.S_ISREG(os.fstat(result).st_mode):
            os.close(result);raise ValueError('Not a regular file')
        return result
    finally:
        os.close(descriptor)


def archive(roots, stream, limits=None):
    limits = limits or DEFAULT_LIMITS
    manifest = {'schema_version': 1, 'scope': 'Regular files remaining in the current task temp/home directories, not a full HTTP capture',
                'files': [], 'omitted': [], 'limits': limits,
                'cache_policy': 'Reserved harness caches in the home root are omitted; configuration, installation logs and session data remain in scope.'}
    total = 0
    with tarfile.open(fileobj=stream, mode='w|') as tar:
        for label, value in roots.items():
            root = Path(value)
            if root.is_symlink():
                manifest['omitted'].append({'original_path': str(root), 'reason': 'Root is a link'});continue
            if not root.is_dir():
                manifest['omitted'].append({'original_path':str(root),'reason':'Missing or inaccessible capture root'});continue
            def walk_error(error):
                manifest['omitted'].append({'original_path':str(error.filename),'reason':'Directory cannot be read'})
            for parent, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
                dirs.sort();files.sort()
                for name in list(dirs):
                    path = Path(parent)/name
                    if path.is_symlink():
                        dirs.remove(name);manifest['omitted'].append({'original_path': str(path), 'reason': 'Directory link omitted'})
                    elif label == 'home' and path.relative_to(root).parts in HOME_CACHE_DIRECTORIES:
                        dirs.remove(name);manifest['omitted'].append({'original_path': str(path), 'reason': 'Reserved harness/package cache directory omitted; contents not enumerated'})
                for name in files:
                    path = Path(parent)/name
                    if label == 'home' and path.relative_to(root).parts in HOME_CACHE_FILES:
                        manifest['omitted'].append({'original_path': str(path), 'reason': 'Reserved harness/package cache file omitted'})
                        continue
                    try:
                        fd = open_regular(root, path.relative_to(root).parts)
                        with os.fdopen(fd, 'rb') as source:
                            before = os.fstat(source.fileno())
                            if before.st_nlink != 1: raise ValueError('Hard link omitted')
                            if before.st_size > limits['file_bytes'] or total+before.st_size > limits['total_bytes'] or len(manifest['files']) >= limits['files']:
                                raise ValueError('Capture limit reached; file not truncated')
                            data = source.read(limits['file_bytes']+1)
                            after = os.fstat(source.fileno())
                            if len(data) != before.st_size or (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                                raise ValueError('File changed during capture')
                        target = 'task-files/'+label+'/'+str(path.relative_to(root))
                        info = tarfile.TarInfo(target);info.size=len(data);info.mode=0o600
                        tar.addfile(info, io.BytesIO(data));total += len(data)
                        manifest['files'].append({'original_path': str(path), 'path': target, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
                    except (OSError, ValueError) as error:
                        manifest['omitted'].append({'original_path': str(path), 'reason': str(error)})
        manifest['complete_for_declared_file_scope'] = not manifest['omitted']
        data = (json.dumps(manifest, ensure_ascii=False, indent=2)+'\n').encode()
        info = tarfile.TarInfo('task-files-manifest.json');info.size=len(data);info.mode=0o600
        tar.addfile(info, io.BytesIO(data))
    return manifest


def unpack(source, output):
    output = Path(output)
    with tarfile.open(source) as tar:
        for member in tar:
            dest = output/member.name
            if (not dest.resolve().is_relative_to(output.resolve()) or not member.isfile()
                    or (not member.name.startswith('task-files/') and member.name != 'task-files-manifest.json')):
                raise ValueError('Unsafe private task file archive')
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(tar.extractfile(member).read());dest.chmod(0o600)


if __name__ == '__main__':
    archive(json.loads(sys.argv[1]), sys.stdout.buffer)
