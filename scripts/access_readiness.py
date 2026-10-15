"""Private access admission, distinct from the final user-task verdict."""
import hashlib
import json
from pathlib import Path

PROTOCOL = 'afs-20261013'
FACETS = ('service_call', 'authorization', 'reusable_state', 'isolation')


def validate(value):
    if not isinstance(value, dict):
        raise ValueError('New access protocol requires access_readiness')
    for name in FACETS:
        row = value.get(name)
        if (not isinstance(row, dict) or row.get('status') not in ('ready', 'not_ready', 'unknown')
                or not isinstance(row.get('evidence'), str) or not row['evidence'].strip()):
            raise ValueError('Invalid access_readiness.' + name)
    return value


def decision(directory, protocol):
    directory = Path(directory)
    state = json.loads((directory/'state.json').read_text())
    if state['phase'] not in ('reviewed', 'recorded'):
        return False, 'Access has no validated independent review'
    review_path = directory/'grading/assessment.json'
    review = json.loads(review_path.read_text())
    if protocol != PROTOCOL:
        return review.get('status') == 'completed', 'Legacy prerequisite requires a completed verdict'
    config = json.loads((directory/'config.json').read_text())
    if config.get('phase') != 'access' or config.get('trial_protocol') != PROTOCOL:
        return False, 'A fresh access prerequisite under the same protocol is required'
    expected = state.get('record_hashes', {}).get('grading/assessment.json')
    if expected != hashlib.sha256(review_path.read_bytes()).hexdigest():
        return False, 'Validated access assessment changed or has no review hash'
    if review.get('status') == 'invalid_run':
        # A separate, hash-bound independent review may repair a material gap;
        # it never rewrites the original task verdict or accepts operator prose.
        from supplemental_access_review import decision as supplemental_decision
        return supplemental_decision(directory)
    if review.get('status') not in ('completed', 'not_completed'):
        return False, 'Invalid or unknown access run cannot authorize business tasks'
    readiness = validate(review.get('access_readiness'))
    missing = [name for name in FACETS if readiness[name]['status'] != 'ready']
    if review.get('outcome', {}).get('service_execution') != 'completed':
        missing.append('service_execution')
    return not missing, 'Access ready' if not missing else 'Access not ready: ' + ', '.join(missing)
