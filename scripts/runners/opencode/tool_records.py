"""Extract private tool records without interpreting results or executing artifacts."""
import hashlib
import json
from pathlib import Path


def extract(output):
    output = Path(output)
    source = output / 'events.jsonl'
    raw = source.read_bytes()
    source_hash = hashlib.sha256(raw).hexdigest()
    calls, errors = [], []
    for number, line in enumerate(raw.decode().split('\n'), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
            if event.get('type') != 'tool_use':
                continue
            part = event['part']
            state = part['state']
            if not isinstance(state, dict) or not part.get('tool'):
                raise ValueError('Invalid tool event')
            calls.append({'tool': part['tool'], 'call_id': part.get('callID'),
                          'state': state,
                          'source': {'path': 'events.jsonl', 'sha256': source_hash, 'line': number}})
        except (ValueError, KeyError, TypeError, AttributeError):
            errors.append({'line': number, 'reason': 'Unrecognized event; inspect original log'})
    result = {'schema_version': 1, 'format': 'opencode-json', 'complete': not errors,
              'errors': errors, 'calls': calls,
              'source': {'path': 'events.jsonl', 'sha256': source_hash}}
    (output / 'tool-records.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result
