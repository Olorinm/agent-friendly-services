"""Read completion without mistaking the worker's normal exit for lost state."""
import json


def query(read_done, find_worker):
    result = read_done()
    if result.returncode == 0:
        return json.loads(result.stdout)
    if result.returncode != 1:
        raise RuntimeError('Remote status read failed: ' + result.stderr.decode())
    process = find_worker()
    if process.returncode == 0:
        return {'status': 'running'}
    # The worker can publish done.json and exit between the first read and pgrep.
    result = read_done()
    if result.returncode == 0:
        return json.loads(result.stdout)
    raise RuntimeError('Worker state unavailable; do not infer completion or redispatch: '
                       + result.stderr.decode() + process.stderr.decode())
