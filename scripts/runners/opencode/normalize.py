"""Reconcile Coding Plan wire usage against OpenCode step_finish counters."""
import hashlib
import json
from pathlib import Path

FIELDS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens')

def normalize(root, model):
    root = Path(root)
    result = dict(schema_version=1, complete=False, model=model, sources=[], requests=[])
    totals = dict.fromkeys(FIELDS, 0)
    def source(path):
        result['sources'].append(dict(path=str(path.relative_to(root)), sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    try:
        events = root / 'events.jsonl';source(events)
        for line in events.read_text().splitlines():
            row = json.loads(line)
            if row.get('type') != 'step_finish': continue
            t = row['part']['tokens'];c = t['cache']
            values = (t['input']+c['read']+c['write'], c['read'], c['write'], t['output']+t['reasoning'], t['reasoning'])
            for k, v in zip(FIELDS, values): totals[k] += v
        result['totals'] = totals
        for directory in sorted((root/'wire').iterdir()):
            for path in sorted(directory.iterdir()): source(path)
            meta = json.loads((directory/'meta.json').read_text())
            request = json.loads((directory/'request.json').read_text())
            if meta.get('status') != 200 or meta.get('error'): raise ValueError('Incomplete/failed wire request')
            if request['model'] != model: raise ValueError('Unexpected model')
            chunks = [json.loads(line[5:]) for line in (directory/'response.body').read_text().splitlines() if line.startswith('data:') and line[5:].strip() != '[DONE]']
            usage = [c['usage'] for c in chunks if c.get('usage')]
            if len(usage) != 1: raise ValueError('Expected one final usage event per request')
            u = usage[0]
            # BigModel exposes automatic cache hits, not a separate billable cache-write counter.
            values = (u['prompt_tokens'],u['prompt_tokens_details']['cached_tokens'],0,u['completion_tokens'],u.get('completion_tokens_details',{}).get('reasoning_tokens',0))
            result['requests'].append(dict(id=directory.name, model=model, usage=dict(zip(FIELDS,values))))
        if not result['requests']: raise ValueError('No requests')
        if any(sum(r['usage'][k] for r in result['requests']) != totals[k] for k in FIELDS): raise ValueError('Wire counters differ from OpenCode totals')
        result['complete'] = True
    except (ValueError, KeyError, OSError, TypeError) as e:
        result['reason'] = str(e)
    (root/'usage.json').write_text(json.dumps(result,indent=2)+'\n')
    return result
