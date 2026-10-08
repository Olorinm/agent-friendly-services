"""Check root-injected runner code before allocating or dispatching a new run."""
import hashlib
import json
from pathlib import Path

WORKER_FILES = ('worker.py', 'normalize.py', 'capture-proxy.py', 'providers.py', 'request_limits.py')

# Read only the named support files, never model.key or service credentials.
PROBE = '''import hashlib,json,sys
from pathlib import Path
root=Path(sys.argv[1]); result={}
for name in sys.argv[2:]:
    path=root/name
    result[name]=hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() and not path.is_symlink() else None
print(json.dumps(result))
'''


def manifest(root):
    return {name: hashlib.sha256((Path(root)/name).read_bytes()).hexdigest()
            for name in WORKER_FILES}


def verify(exec_root, expected):
    result = exec_root('python3', '-c', PROBE, '/run/afs', *WORKER_FILES)
    observed = json.loads(result.stdout)
    if observed != expected:
        different = [name for name in WORKER_FILES
                     if not isinstance(observed, dict) or observed.get(name) != expected[name]]
        raise ValueError('Provisioned runner code differs: ' + ', '.join(different)
                         + '. Inspect the idle runtime and run provision.py up before dispatch; '
                         'record changed preparation separately. No run was allocated by this call. '
                         'Do not reprovision an active or uncertain run.')
    return observed
