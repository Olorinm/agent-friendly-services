"""Stop only the recorded Codex process group while its owning worker exists."""
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def stop(private, pattern):
    private = Path(private)
    process = private/'process.json'
    if not process.is_file(): return {'stopped': False, 'reason': 'No durable process receipt; inspect before retry'}
    pid = json.loads(process.read_text())['pid']
    if type(pid) is not int or pid <= 1: raise ValueError('Invalid process identity')
    start = time.monotonic(); sent = set()
    while time.monotonic()-start < 8:
        found = subprocess.run(['pgrep', '-af', pattern], capture_output=True)
        if found.returncode not in (0, 1): raise ValueError('Cannot verify worker')
        try: os.killpg(pid, 0); alive = True
        except ProcessLookupError: alive = False
        if found.returncode == 1 and not alive: return {'stopped': True}
        if found.returncode == 1: return {'stopped': False, 'reason': 'Worker absent but recorded group alive; inspect ownership'}
        sig = signal.SIGTERM if time.monotonic()-start < 3 else signal.SIGKILL
        if alive and sig not in sent:
            try: os.killpg(pid, sig)
            except ProcessLookupError: pass
            sent.add(sig)
        time.sleep(.2)
    return {'stopped': False, 'reason': 'Owned Codex processes remain'}


if __name__ == '__main__': print(json.dumps(stop(sys.argv[1], sys.argv[2])))
