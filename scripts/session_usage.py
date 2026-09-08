"""Extract numeric usage only from a local Codex rollout; never export its content/IDs."""
import hashlib
import json
from pathlib import Path
import re
import shutil

FIELDS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens',
          'output_tokens', 'reasoning_output_tokens')


def tokens(value):
    if not isinstance(value, dict):
        raise ValueError('Missing token counters')
    result = {k: value.get(k, 0) for k in FIELDS}
    if any(k not in value for k in ('input_tokens', 'cached_input_tokens', 'output_tokens')):
        raise ValueError('Missing required token counters')
    if any(type(n) is not int or n < 0 for n in result.values()):
        raise ValueError('Invalid token counters')
    if result['cached_input_tokens'] + result['cache_write_input_tokens'] > result['input_tokens']:
        raise ValueError('Cache counters exceed input')
    if result['reasoning_output_tokens'] > result['output_tokens']:
        raise ValueError('Reasoning counters exceed output')
    return result


def extract_usage(path, expected):
    raw = Path(path).read_bytes()
    result = {'status': 'incomplete', 'method': 'session token_count', 'requests': [],
              'source_sha256': hashlib.sha256(raw).hexdigest(), 'reason': ''}
    try:
        exact, fallback, seen = [], [], {}
        previous = dict.fromkeys(FIELDS, 0)
        fallback_error = None
        for line in raw.splitlines():
            event = json.loads(line)
            payload = event.get('payload', {})
            if event.get('type') == 'token_usage_record':
                usage = tokens(payload.get('usage'))
                identity = payload.get('response_id')
                if not isinstance(identity, str) or not identity:
                    raise ValueError('Request usage has no response identity')
                if identity in seen:
                    if seen[identity] != usage:
                        raise ValueError('Conflicting duplicate request usage')
                    continue
                seen[identity] = usage
                exact.append(usage)
            if event.get('type') == 'event_msg' and payload.get('type') == 'token_count' and payload.get('info'):
                info = payload['info']
                total, last = tokens(info.get('total_token_usage')), tokens(info.get('last_token_usage'))
                if total == previous:  # Rate-limit updates can repeat the last usage event.
                    continue
                delta = {k: total[k] - previous[k] for k in FIELDS}
                if delta != last:
                    fallback_error = 'Session counters contain a gap, reset or estimated adjustment'
                fallback.append(last)
                previous = total
        result['requests'] = exact or fallback
        result['method'] = 'session token_usage_record' if exact else 'session token_count'
        if not exact and fallback_error:
            raise ValueError(fallback_error)
        if not result['requests']:
            raise ValueError('No per-request usage recorded')
        total = {k: sum(r[k] for r in result['requests']) for k in FIELDS}
        result['totals'] = total
        if expected is None:
            raise ValueError('CLI final usage missing; observed requests may be incomplete')
        if total != tokens(expected):
            raise ValueError('Per-request sum does not match CLI final usage')
        result.update(status='complete', reason='Per-request counters reconcile with CLI final usage')
    except (ValueError, TypeError, KeyError) as error:
        result['reason'] = str(error) if not isinstance(error, json.JSONDecodeError) else 'Malformed or truncated session JSON'
    return result


def collect_session_usage(auth_root, thread_id, records, expected):
    """Locate only the just-created thread; retain a private copy beside trial logs."""
    missing = {'status': 'incomplete', 'method': 'session', 'requests': [],
               'source_sha256': None, 'reason': 'Session file not found'}
    if not isinstance(thread_id, str) or not re.fullmatch(r'[0-9a-fA-F-]{36}', thread_id):
        return missing
    matches = [p for sub in ('sessions', 'archived_sessions')
               for p in (Path(auth_root) / sub).rglob(f'*{thread_id}.jsonl')]
    if len(matches) != 1:
        return missing
    target = Path(records) / 'session.raw.jsonl'
    # Copy after the CLI exits and its rollout writer has flushed.
    try:
        with target.open('wb') as dest, matches[0].open('rb') as source:
            target.chmod(0o600)
            shutil.copyfileobj(source, dest)
        return extract_usage(target, expected)
    except OSError:
        return {**missing, 'reason': 'Unable to read or preserve the session file'}
