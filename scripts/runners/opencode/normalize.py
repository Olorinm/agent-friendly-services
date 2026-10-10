"""Reconcile model wire usage against OpenCode step_finish counters."""
import hashlib
import json
from pathlib import Path

FIELDS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens')

def normalize(root, model):
    root = Path(root)
    result = dict(schema_version=1, complete=False, model=model, sources=[], requests=[])
    totals = dict.fromkeys(FIELDS, 0)
    errors = []
    def source(path):
        result['sources'].append(dict(path=str(path.relative_to(root)), sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    # Read runner totals and wire responses independently. One truncated or failed
    # request must not discard successful, provider-reported requests around it.
    try:
        events = root / 'events.jsonl';source(events)
        for line in events.read_text().split('\n'):
            if not line.strip(): continue
            row = json.loads(line)
            if row.get('type') != 'step_finish': continue
            t = row['part']['tokens'];c = t['cache']
            values = (t['input']+c['read']+c['write'], c['read'], c['write'], t['output']+t['reasoning'], t['reasoning'])
            if any(type(v) is not int or v < 0 for v in values):
                raise ValueError('Invalid runner counters')
            for k, v in zip(FIELDS, values): totals[k] += v
        result['totals'] = totals
    except (ValueError, KeyError, OSError, TypeError) as e:
        errors.append('Runner totals: ' + str(e))
    wire = root / 'wire'
    for directory in sorted(wire.iterdir()) if wire.is_dir() else []:
        try:
            if directory.is_symlink(): raise ValueError('Wire source must not be a link')
            if directory.name in ('guard-events.jsonl', 'budget-warnings.jsonl') and directory.is_file():
                source(directory)
                rows = [json.loads(line) for line in directory.read_text().split('\n') if line.strip()]
                if any(not isinstance(row, dict) or type(row.get('time')) not in (int, float)
                       or (directory.name == 'guard-events.jsonl' and not isinstance(row.get('error'), str)) for row in rows):
                    raise ValueError('Malformed controller event')
                result['local_rejections' if directory.name == 'guard-events.jsonl' else 'budget_warnings'] = rows
                continue
            if not directory.is_dir(): raise ValueError('Unexpected wire entry')
            for path in sorted(directory.iterdir()):
                if path.is_symlink() or not path.is_file(): raise ValueError('Unsafe wire source')
                source(path)
            meta = json.loads((directory/'meta.json').read_text())
            request = json.loads((directory/'request.json').read_text())
            if meta.get('status') != 200: raise ValueError('Incomplete/failed wire request')
            if meta.get('error'):
                # A disconnect after the provider's final usage event does not
                # erase that counter. Keep it as partial, never claim full capture.
                errors.append(directory.name + ': ' + str(meta['error']))
            if request['model'] != model: raise ValueError('Unexpected model')
            body = (directory/'response.body').read_text()
            if request.get('stream') or body.lstrip().startswith('data:'):
                chunks = [json.loads(line[5:]) for line in body.split('\n') if line.startswith('data:') and line[5:].strip() != '[DONE]']
            else:
                chunks = [json.loads(body)]
            usage = [c['usage'] for c in chunks if c.get('usage')]
            if len(usage) != 1: raise ValueError('Expected one final usage event per request')
            u = usage[0]
            values = (u['prompt_tokens'],u['prompt_tokens_details']['cached_tokens'],0,u['completion_tokens'],u.get('completion_tokens_details',{}).get('reasoning_tokens',0))
            if any(type(v) is not int or v < 0 for v in values) or values[1] > values[0] or values[4] > values[3]:
                raise ValueError('Invalid provider counters')
            result['requests'].append(dict(id=directory.name, model=model, usage=dict(zip(FIELDS,values))))
        except (ValueError, KeyError, OSError, TypeError) as e:
            errors.append(directory.name + ': ' + str(e))
    if not result['requests']: errors.append('No requests')
    if any(sum(r['usage'][k] for r in result['requests']) != totals[k] for k in FIELDS):
        errors.append('Wire counters differ from OpenCode totals')
    result['complete'] = not errors
    if errors: result['reason'] = '; '.join(errors)
    (root/'usage.json').write_text(json.dumps(result,indent=2)+'\n')
    return result
