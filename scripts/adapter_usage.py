"""Read canonical numeric usage exported by a runner adapter, with source hashes.

The adapter translates its runtime's raw counters; this module validates provenance
and reconciles totals. It does not infer usage from an Agent's prose.
"""
import hashlib
import json
from pathlib import Path
from session_usage import tokens, FIELDS


def read_usage(directory, expected_model=None):
    directory = Path(directory).resolve()
    file = directory / 'usage.json'
    detail = {'status': 'incomplete', 'method': 'runner adapter', 'requests': [],
              'source_sha256': None, 'reason': 'No adapter usage file'}
    try:
        raw = file.read_bytes()
        detail['source_sha256'] = hashlib.sha256(raw).hexdigest()
        data = json.loads(raw)
        if data.get('schema_version') != 1 or type(data.get('complete')) is not bool:
            raise ValueError('Unsupported adapter usage')
        if not isinstance(data.get('model'), str) or not data['model'] or (expected_model and data['model'] != expected_model):
            raise ValueError('Adapter usage model is missing or differs from runtime')
        if not data.get('sources'):
            raise ValueError('Raw usage sources are required')
        for source in data['sources']:
            path = (directory / source['path']).resolve()
            if not path.is_relative_to(directory) or path == file:
                raise ValueError('Raw source must be a separate file inside the record directory')
            if hashlib.sha256(path.read_bytes()).hexdigest() != source['sha256']:
                raise ValueError('Raw usage source hash mismatch')
        seen = set()
        for row in data['requests']:
            identity = row.get('id')
            if not isinstance(identity, str) or not identity or identity in seen:
                raise ValueError('Duplicate or missing request identity')
            if row.get('model', data['model']) != data['model']:
                raise ValueError('Mixed-model requests require separate accounting')
            if 'cache_write_input_tokens' not in row['usage']:
                raise ValueError('Explicit cache-write counters are required')
            seen.add(identity)
            detail['requests'].append(tokens(row['usage']))
        if not seen:
            raise ValueError('No requests captured')
        # These counters are independently reported by captured provider responses.
        # They remain useful when termination loses the runner's final counters.
        # Only expose a lower bound after every source, identity and row validates.
        verified = list(detail['requests'])
        bound = {k: sum(r[k] for r in verified) for k in FIELDS}
        detail.update(requests_verified=True, lower_bound_usage=bound)
        if data['complete'] is not True:
            raise ValueError(data.get('reason') or 'Adapter usage is incomplete')
        if 'cache_write_input_tokens' not in data['totals']:
            raise ValueError('Explicit total cache-write counter is required')
        totals = tokens(data['totals'])
        if any(sum(r[k] for r in detail['requests']) != totals[k] for k in FIELDS):
            raise ValueError('Request counters do not match runtime totals')
        detail.update(status='complete', totals=totals,
                      reason='Adapter request counters reconcile with runtime totals; raw source hashes verified')
        return totals, detail
    except (OSError, ValueError, TypeError, KeyError) as error:
        if not detail.get('requests_verified'):
            detail['requests'] = []
        detail.update(status='incomplete', reason=str(error))
        return None, detail
