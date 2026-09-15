"""Confirm that the owned model process group, proxy, and worker have stopped."""
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def alive(pid, group=False):
    try:
        (os.killpg if group else os.kill)(pid, 0)
        return True
    except ProcessLookupError:
        return False


def worker_running(pattern):
    result = subprocess.run(['pgrep', '-af', pattern], capture_output=True)
    if result.returncode not in (0, 1):
        raise RuntimeError('Cannot verify worker status')
    return result.returncode == 0


def stop(private, pattern, timeout=8):
    process_file = Path(private) / 'process.json'
    if not process_file.is_file():
        return {'stopped': False, 'reason': 'No process receipt; startup must be reconciled'}
    process = json.loads(process_file.read_text())
    pid, proxy = process['pid'], process['proxy_pid']
    if any(type(p) is not int or p <= 1 for p in (pid, proxy)):
        raise ValueError('Invalid owned process receipt')
    started = time.monotonic()
    sent = set()
    while True:
        worker = worker_running(pattern)
        model, capture = alive(pid, group=True), alive(proxy)
        if not worker and not model and not capture:
            return {'stopped': True}
        elapsed = time.monotonic() - started
        if elapsed >= timeout:
            return {'stopped': False, 'reason': 'Owned processes have not all stopped'}
        # A dead worker cannot attest to old/reused PIDs. Leave uncertain state
        # for reconciliation rather than signal a potentially unrelated process.
        if not worker:
            return {'stopped': False, 'reason': 'Worker absent but recorded child processes remain'}
        sig = signal.SIGTERM if elapsed < 3 else signal.SIGKILL
        if model and sig not in sent:
            try:
                os.killpg(pid, sig)
            except ProcessLookupError:
                pass
            sent.add(sig)
        time.sleep(0.2)


if __name__ == '__main__':
    print(json.dumps(stop(sys.argv[1], sys.argv[2])))
