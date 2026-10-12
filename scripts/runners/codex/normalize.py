"""Canonical usage and observed-input receipts from a private Codex rollout."""
import hashlib
import json
from pathlib import Path
from session_usage import extract_usage


def observed_input(session, prompt, model, effort):
    texts = []
    contexts = []
    for line in Path(session).read_text().splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        payload = row.get('payload', {})
        if row.get('type') == 'turn_context':
            contexts.append(payload)
        if row.get('type') == 'response_item' and payload.get('role') == 'user':
            texts.extend(c.get('text', '') for c in payload.get('content', []) if isinstance(c, dict))
    return (any(prompt in text for text in texts) and bool(contexts)
            and all(c.get('model') == model and c.get('effort') == effort for c in contexts))


def normalize(output, model, expected):
    output = Path(output)
    session = output/'session.raw.jsonl'
    detail = extract_usage(session, expected) if session.is_file() else {
        'status': 'incomplete', 'requests': [], 'reason': 'Codex rollout missing'}
    # A missing final total can leave useful observed requests. Malformed,
    # conflicting or adjusted counters cannot establish a trustworthy lower bound.
    if detail['status'] != 'complete' and detail.get('reason') not in (
        'CLI final usage missing; observed requests may be incomplete',
        'Per-request sum does not match CLI final usage',
    ):
        detail['requests'] = []
    sources = [{'path': session.name, 'sha256': hashlib.sha256(session.read_bytes()).hexdigest()}] if session.is_file() else []
    value = {'schema_version': 1, 'model': model, 'complete': detail['status'] == 'complete',
             'reason': detail.get('reason'), 'sources': sources,
             'requests': [{'id': f'codex-response-{i+1}', 'usage': usage}
                          for i, usage in enumerate(detail.get('requests', []))]}
    if value['complete']:
        value['totals'] = detail['totals']
    (output/'usage.json').write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    return value
