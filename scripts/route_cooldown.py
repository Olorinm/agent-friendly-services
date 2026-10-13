"""Private, conservative dispatch holds from captured execution tool signals.

Tool output is not an independent network tap. Automatic observations only
pause new executions for review; they are never service facts or grades. The
controller can import a verified observation for unsupported command shapes.
"""
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
import json
import math
from pathlib import Path
import shlex
from urllib.parse import urlsplit, urlunsplit


def digest(value):
    return hashlib.sha256(value).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def epoch(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('Observation time needs a timezone')
    return parsed.timestamp()


def endpoint(value):
    url = urlsplit(value)
    if url.scheme != 'https' or not url.hostname or url.username or url.password or url.fragment:
        raise ValueError('Quota endpoint needs HTTPS without credentials or fragment')
    # Query values can contain credentials. Keep only the declared HTTP origin
    # and exact path; no hostname substring/prefix or whole-output guessing.
    port = url.port
    host = url.hostname.lower()
    if ':' in host: host = '[' + host + ']'
    authority = host + (':' + str(port) if port and port != 443 else '')
    return urlunsplit(('https', authority, url.path or '/', '', ''))


def binding(config, route):
    settings = config['execution']
    credential = settings.get('credential_scope')
    locks = settings.get('quota_resource_locks', [])
    if not isinstance(locks, list) or any(not isinstance(v, str) or not v for v in locks):
        raise ValueError('quota_resource_locks must be explicit execution lock IDs')
    if not set(locks).issubset(settings.get('resource_locks', [])):
        raise ValueError('Quota scope cannot borrow a grader or undeclared resource lock')
    if credential is not None and (not isinstance(credential, str) or not credential.strip()):
        raise ValueError('credential_scope must be a declared nonempty identifier, never a secret')
    if credential is None:
        credential = ('execution-quota-locks:' + digest(canonical(sorted(set(locks))))) if locks else 'environment:' + config['environment_id']
    urls = settings.get('quota_endpoints', [route.get('entry_url')])
    if not isinstance(urls, list) or not urls or any(not isinstance(v, str) or not v for v in urls):
        raise ValueError('quota_endpoints must declare service HTTP endpoints')
    urls = sorted(set(endpoint(v) for v in urls))
    scope = {'service': config['service'], 'route': config['route'], 'credential_scope': credential}
    return {**scope, 'scope_id': digest(canonical(scope)), 'endpoints': urls,
            'binding_sha256': digest(canonical({**scope, 'endpoints': urls}))}


def registry(state):
    return state.setdefault('route_cooldowns', {'observations': {}, 'releases': {}, 'scans': {}})


def safe_file(base, relative):
    raw = Path(relative)
    if raw.is_absolute() or '..' in raw.parts:
        raise ValueError('Evidence must be relative to this private run')
    result = base / raw
    if any(p.is_symlink() for p in [result, *result.parents] if p != base.parent):
        raise ValueError('Quota evidence cannot follow symlinks')
    if not result.resolve().is_relative_to(base.resolve()):
        raise ValueError('Quota evidence outside this run')
    return result


def captured(run, expected_sha256=None, *, raw=None, selected=None):
    """Bind a normalized call back to the actual captured event, not actor files."""
    run = Path(run)
    path = safe_file(run, 'execution/tool-records.json')
    raw = path.read_bytes() if raw is None else raw
    if expected_sha256 and digest(raw) != expected_sha256:
        raise ValueError('Captured tool source changed')
    value = json.loads(raw)
    if value.get('schema_version') != 1 or value.get('format') != 'opencode-json' or value.get('complete') is not True:
        raise ValueError('Complete controller-captured OpenCode tool records required')
    source = value['source']
    if source.get('path') != 'events.jsonl':
        raise ValueError('Quota observation needs original execution events')
    selected = value['calls'] if selected is None else selected
    wanted = {c['source']['line'] for c in selected}
    lines = {}; total = 0; checksum = hashlib.sha256()
    with safe_file(run, 'execution/events.jsonl').open('rb') as stream:
        for total, line in enumerate(stream, 1):
            checksum.update(line)
            if total in wanted: lines[total] = line.decode('utf-8')
    if checksum.hexdigest() != source['sha256']:
        raise ValueError('Tool source does not match captured events')
    for call in selected:
        locator = call['source']; number = locator['line']
        if type(number) is not int or not 1 <= number <= total or locator.get('sha256') != source['sha256'] or locator.get('path') != source['path']:
            raise ValueError('Invalid captured event locator')
        event = json.loads(lines[number])
        part = event.get('part', {})
        if event.get('type') != 'tool_use' or part.get('tool') != call['tool'] or part.get('state') != call['state'] or part.get('callID') != call.get('call_id'):
            raise ValueError('Normalized tool call does not match original event')
    return value, digest(raw)


def curl_plan(command):
    """A literal curl, optionally followed only by cat of its output files."""
    if not isinstance(command, str) or any(c in command for c in ('$', '`', '\n', '\r')):
        return None
    try:
        parser = shlex.shlex(command, posix=True, punctuation_chars=';&|<>()')
        parser.whitespace_split = True
        words = list(parser)
    except ValueError:
        return None
    if not words or words[0] not in ('curl', '/usr/bin/curl', '/usr/local/bin/curl'):
        return None
    segments = [[]]
    for word in words:
        if word == ';': segments.append([])
        elif word and all(c in ';&|<>()' for c in word): return None
        else: segments[-1].append(word)
    if not segments[-1]: segments.pop()
    argv = segments[0]; urls = []; header_file = None; body_file = None; headers = False
    flags = {'--include', '--silent', '--show-error', '--fail', '--fail-with-body', '--compressed', '--http1.1', '--http2', '--head'}
    values = {'-X', '--request', '-H', '--header', '-A', '--user-agent', '-d', '--data', '--data-raw', '--data-binary', '--json', '-m', '--max-time', '--connect-timeout', '-D', '--dump-header', '-o', '--output', '--url'}
    index = 1
    while index < len(argv):
        word = argv[index]
        if word.startswith(('http://', 'https://')): urls.append(word)
        elif word in flags: headers = headers or word in ('--include', '--head')
        elif word.startswith('-') and not word.startswith('--') and len(word) > 1 and all(c in 'sSfIi' for c in word[1:]):
            headers = headers or 'i' in word or 'I' in word
        else:
            name, equal, value = word.partition('=')
            if name not in values: return None
            if not equal:
                index += 1
                if index >= len(argv): return None
                value = argv[index]
            if name in ('-H', '--header'):
                header = value.strip().lower()
                if header.startswith(('@', 'host:', ':authority:')) or '\r' in value or '\n' in value: return None
            if name in ('-D', '--dump-header'): header_file = value; headers = value == '-'
            if name in ('-o', '--output'): body_file = value
            if name == '--url': urls.append(value)
        index += 1
    if len(urls) != 1:
        return None
    try: url = endpoint(urls[0])
    except (ValueError, TypeError): return None
    if len(segments) > 1:
        if not header_file or header_file == '-' or not body_file: return None
        allowed = {header_file, body_file}; seen = set()
        for segment in segments[1:]:
            if not segment or segment[0] != 'cat' or not segment[1:] or any(v not in allowed for v in segment[1:]): return None
            seen.update(segment[1:])
        if header_file not in seen: return None
    return {'url': url, 'stdout_headers': headers, 'header_file': header_file, 'body_file': body_file}


def curl_target(command):
    plan = curl_plan(command)
    return plan['url'] if plan else None


def file_origins_unique(plan, call, calls):
    """End-of-run snapshots cannot stand in for earlier overwritten versions."""
    names = [plan['header_file'], plan['body_file']]
    def strings(value):
        if isinstance(value, str): yield value
        elif isinstance(value, list):
            for child in value: yield from strings(child)
        elif isinstance(value, dict):
            for child in value.values(): yield from strings(child)
    for other in calls:
        if other is call: continue
        inputs = list(strings(other.get('state', {}).get('input', {})))
        # Even another apparent read makes path provenance ambiguous here. This
        # intentionally narrow detector does not interpret arbitrary write code.
        if any(name in value or Path(name).name in value for name in names for value in inputs): return False
    return True


def file_signal(run, plan, call, calls):
    """Only the exact curl output origins, as archived by the controller."""
    if not plan['header_file'] or plan['header_file'] == '-': return None
    if not plan['body_file']: return None
    names = [plan['header_file'], plan['body_file']]
    if any(not Path(n).is_absolute() or '..' in Path(n).parts for n in names): return None
    if not file_origins_unique(plan, call, calls): return None
    manifest_path = safe_file(run, 'execution/task-files-manifest.json')
    manifest_raw = manifest_path.read_bytes(); manifest = json.loads(manifest_raw)
    evidence = []
    for origin in names:
        matches = [f for f in manifest['files'] if f.get('original_path') == origin]
        if len(matches) != 1: return None
        entry = matches[0]
        if not entry['path'].startswith('task-files/'): return None
        data = safe_file(run, 'execution/' + entry['path']).read_bytes()
        if digest(data) != entry['sha256']: raise ValueError('Captured curl response file differs from controller manifest')
        evidence.append((entry, data))
    result = signal_from_output(evidence[0][1].decode('utf-8'))
    if result:
        result['response_file_evidence'] = {'manifest_path': 'execution/task-files-manifest.json', 'manifest_sha256': digest(manifest_raw),
             'files': [{'original_path': e['original_path'], 'path': 'execution/' + e['path'], 'sha256': e['sha256']} for e, _ in evidence]}
    return result


def retry_deadline(retry_after, observed_at):
    if retry_after is None: return None
    if type(retry_after) is int and retry_after >= 0 or isinstance(retry_after, str) and retry_after.strip().isdigit():
        try: until = observed_at + int(retry_after)
        except (OverflowError, ValueError): return None
        return until if math.isfinite(until) else None
    if isinstance(retry_after, str):
        try:
            date = parsedate_to_datetime(retry_after)
            if date.tzinfo is None: return None
            return date.timestamp()
        except (ValueError, TypeError, OverflowError): pass
    return None


def signal_from_output(output):
    if not isinstance(output, str): return None
    # A response header must begin stdout, not appear in an HTML/document/body
    # example. Redirects are not followed by curl_target; never use later blocks.
    text = output.replace('\r\n', '\n').strip()
    if text.startswith('HTTP/'):
        header, _, _body = text.partition('\n\n')
        first, *lines = header.splitlines()
        fields = first.split()
        if len(fields) < 2 or fields[0] not in ('HTTP/1.0', 'HTTP/1.1', 'HTTP/2', 'HTTP/3') or fields[1] != '429': return None
        if any(line.startswith('HTTP/') for line in _body.splitlines()): return None
        headers = {}
        for line in lines:
            if ':' not in line: return None
            name, value = line.split(':', 1)
            name = name.lower().strip()
            if name in headers: return {'http_status': 429, 'retry_after': None}
            headers[name] = value.strip()
        return {'http_status': 429, 'retry_after': headers.get('retry-after')}
    try: body = json.loads(text)
    except ValueError: return None
    if isinstance(body, dict) and body.get('success') is False and body.get('reason') in ('credits', 'quota', 'quota_exceeded', 'rate_limit_exceeded'):
        # Without an independently structured response, a JSON message is only
        # an unknown operational hold. Do not invent an HTTP code or deadline.
        return {'http_status': None, 'quota_reason': body['reason'], 'retry_after': None}
    return None


def observation(bound, run, call, tool_sha, signal, *, verified=False, observed_at=None, manifest=None):
    end = call['state'].get('time', {}).get('end')
    if type(end) not in (int, float) or not math.isfinite(end):
        raise ValueError('Fixed actual tool observation time required')
    fixed = end / 1000
    if observed_at is not None and abs(epoch(observed_at) - fixed) > 0.001:
        raise ValueError('Observation time must match the actual captured tool end')
    identity = digest(canonical([bound['scope_id'], call['source'], digest(canonical(call))]))
    return {'observation_id': identity, 'scope_id': bound['scope_id'], 'binding_sha256': bound['binding_sha256'],
            'service': bound['service'], 'route': bound['route'], 'credential_scope': bound['credential_scope'],
            'run': str(run), 'observed_at': datetime.fromtimestamp(fixed, timezone.utc).isoformat(),
            'observed_epoch': fixed, 'until': retry_deadline(signal.get('retry_after'), fixed),
            'http_status': signal.get('http_status'), 'quota_reason': signal.get('quota_reason'),
            'confidence': 'controller_verified_observation' if verified else 'operational_observation_awaiting_verification',
            'source': {'path': 'execution/tool-records.json', 'sha256': tool_sha, 'event': call['source'], 'call_sha256': digest(canonical(call))},
            'source_manifest': manifest,
            'response_file_evidence': signal.get('response_file_evidence'),
            'notice': 'Dispatch hold only; not an independent network fact, service failure, assessment or result.'}


def register(state, item):
    rows = registry(state)['observations']
    old = rows.get(item['observation_id'])
    if old:
        if old['confidence'] == 'controller_verified_observation' or item['confidence'] != 'controller_verified_observation':
            return old  # Re-reading the same evidence cannot roll its deadline.
    rows[item['observation_id']] = item
    return item


def integrity_hold(state, bound, run, expected_sha, actual_sha, reason):
    identity = digest(canonical(['capture-integrity', str(run), expected_sha, actual_sha]))
    return register(state, {'observation_id': identity, 'scope_id': bound['scope_id'], 'binding_sha256': bound['binding_sha256'],
        'service': bound['service'], 'route': bound['route'], 'credential_scope': bound['credential_scope'],
        'run': str(run), 'observed_at': datetime.now(timezone.utc).isoformat(), 'until': None,
        'confidence': 'capture_integrity_hold', 'source': {'path': 'execution/tool-records.json', 'sha256': actual_sha or expected_sha},
        'notice': reason + '; controller reconciliation required, not a service verdict'})


def refresh(state, members):
    """Only inspect collected executions; keep live collection/grading untouched."""
    store = registry(state)
    for run, config, route, phase in members:
        run = Path(run)
        if phase['phase'] in ('prepared', 'execution_starting', 'execution_running', 'execution_collecting'):
            continue
        path = run / 'execution/tool-records.json'
        source = run / 'execution/events.jsonl'
        cache = store['scans'].get(str(run))
        if not path.is_file() or not source.is_file() or not (run / 'execution/receipt.json').is_file():
            if cache: integrity_hold(state, binding(config, route), run, cache['tool_sha256'], None, 'Previously captured quota source is missing')
            continue
        fingerprint = [[p.stat().st_mtime_ns, p.stat().st_size] for p in (path, source)]
        extra_fingerprint = None
        if cache:
            try:
                extra_fingerprint = {name: [safe_file(run, name).stat().st_mtime_ns, safe_file(run, name).stat().st_size]
                                     for name in cache.get('extra_sha256', {})}
            except (OSError, ValueError): extra_fingerprint = None
        if cache and cache['files'] == fingerprint and cache.get('extra_files', {}) == extra_fingerprint: continue
        try:
            bound = binding(config, route)
            raw = safe_file(run, 'execution/tool-records.json').read_bytes()
            records = json.loads(raw); tool_sha = digest(raw)
            if cache:
                # Changed mtime alone (idempotent re-collection) is not a new
                # observation. Changed bytes need explicit reconciliation.
                checksum = hashlib.sha256()
                with safe_file(run, 'execution/events.jsonl').open('rb') as stream:
                    for chunk in iter(lambda: stream.read(1048576), b''): checksum.update(chunk)
                if tool_sha != cache['tool_sha256'] or checksum.hexdigest() != cache['source_sha256']:
                    raise ValueError('Previously collected quota source changed; reconcile private capture')
                if any(digest(safe_file(run, name).read_bytes()) != expected for name, expected in cache.get('extra_sha256', {}).items()):
                    raise ValueError('Previously captured quota response/manifest changed; reconcile private capture')
            candidates = []
            for call in records['calls']:
                status = call['state']
                if call['tool'] != 'bash' or status.get('status') not in ('completed', 'error'): continue
                plan = curl_plan(status.get('input', {}).get('command'))
                if plan is None or plan['url'] not in bound['endpoints']: continue
                if plan['header_file'] and plan['header_file'] != '-':
                    found = file_signal(run, plan, call, records['calls'])
                else:
                    output = status.get('output')
                    if not isinstance(output, str): output = status.get('metadata', {}).get('output')
                    if isinstance(output, str) and output.lstrip().startswith('HTTP/') and not plan['stdout_headers']: continue
                    found = signal_from_output(output)
                if found: candidates.append((call, found))
            if candidates:
                captured(run, raw=raw, selected=[c for c, _ in candidates])
                for call, found in candidates: register(state, observation(bound, run, call, tool_sha, found))
            extra = {}
            for _, found in candidates:
                evidence = found.get('response_file_evidence')
                if evidence:
                    extra[evidence['manifest_path']] = evidence['manifest_sha256']
                    extra.update({f['path']: f['sha256'] for f in evidence['files']})
            store['scans'][str(run)] = {'files': fingerprint, 'tool_sha256': tool_sha, 'source_sha256': records['source']['sha256'],
                'extra_sha256': extra, 'extra_files': {name: [safe_file(run, name).stat().st_mtime_ns, safe_file(run, name).stat().st_size] for name in extra}}
        except (OSError, ValueError, KeyError, TypeError, IndexError) as error:
            if cache:
                bound = binding(config, route)
                checksum = digest(path.read_bytes())
                integrity_hold(state, bound, run, cache['tool_sha256'], checksum, str(error))
            # Unsupported initial captures do not manufacture a service signal.


def hold(state, bound, now):
    store = registry(state); rows = []
    for identity, item in store['observations'].items():
        if item['scope_id'] != bound['scope_id']: continue
        release = store['releases'].get(identity)
        if release and release['source_sha256'] == item['source']['sha256']: continue
        if item['until'] is None or item['until'] > now: rows.append(item)
    if not rows: return None
    unknown = any(r['until'] is None for r in rows)
    changed_capture = any(r['confidence'] == 'capture_integrity_hold' for r in rows)
    return {'reason': 'Collected service evidence changed; private controller reconciliation required' if changed_capture else
                     ('Service quota operational hold awaiting controller verification' if unknown else 'Service route cooling down after captured quota observation'),
            'observation_ids': sorted(r['observation_id'] for r in rows),
            'until': None if unknown else max(r['until'] for r in rows),
            'source_sha256': sorted(set(r['source']['sha256'] for r in rows)),
            'service_failure_inferred': False}


def import_verified(state, run, config, route, proof):
    bound = binding(config, route)
    if proof.get('schema_version') != 1 or proof.get('binding_sha256') != bound['binding_sha256']:
        raise ValueError('Controller observation does not match the frozen route/credential binding')
    if type(proof.get('call_number')) is not int or proof['call_number'] < 1:
        raise ValueError('Controller observation needs an actual call number')
    records, tool_sha = captured(run, proof['source_sha256'])
    if proof['call_number'] > len(records['calls']):
        raise ValueError('Controller observation call number is outside captured records')
    call = records['calls'][proof['call_number'] - 1]
    if proof.get('event_source') != call['source']:
        raise ValueError('Controller observation needs the exact original event locator')
    if endpoint(proof['target_url']) not in bound['endpoints']:
        raise ValueError('Controller observation target does not match declared service endpoint')
    if call['state'].get('status') not in ('completed', 'error') or call['tool'] not in ('bash', 'webfetch'):
        raise ValueError('Controller observation needs an ended actual service-tool call')
    if proof.get('http_status') != 429 and proof.get('quota_reason') not in ('credits', 'quota', 'quota_exceeded', 'rate_limit_exceeded'):
        raise ValueError('Only actual quota observations can create a hold')
    manifest = proof['source_manifest']
    if manifest.get('path') not in ('grading-input-hashes.json', 'execution/task-files-manifest.json'):
        raise ValueError('Controller observation needs an original grading or task-file capture manifest')
    raw = safe_file(Path(run), manifest['path']).read_bytes()
    if digest(raw) != manifest['sha256']:
        raise ValueError('Controller source manifest changed')
    sealed = json.loads(raw)
    source_path = manifest['evidence_path']
    evidence = safe_file(Path(run), manifest['evidence_file']).read_bytes()
    expected = None
    if manifest['path'] == 'grading-input-hashes.json':
        expected = sealed.get(source_path) if isinstance(sealed, dict) else None
    elif isinstance(sealed, dict) and sealed.get('schema_version') == 1:
        matched = [row for row in sealed.get('files', []) if row.get('path') == source_path and row.get('original_path') == manifest.get('original_path')]
        if len(matched) == 1 and manifest['evidence_file'] == 'execution/' + source_path:
            expected = matched[0]['sha256']
    if expected != digest(evidence) or digest(evidence) != manifest['evidence_sha256']:
        raise ValueError('Controller observation evidence is not bound by its original manifest')
    # The private proof names a source the controller has actually examined.
    # It does not authorize an actor-generated result/answer to become evidence.
    if not manifest['evidence_file'].startswith(('grading-input/review-packet/tools/', 'execution/task-files/')):
        raise ValueError('Controller observation needs captured tool/response evidence, never an actor answer')
    if manifest['evidence_file'].startswith('grading-input/review-packet/tools/') and json.loads(evidence) != call:
        raise ValueError('Controller proof tool evidence must be the observed original call')
    return register(state, observation(bound, run, call, tool_sha,
                    {k: proof.get(k) for k in ('http_status', 'quota_reason', 'retry_after')},
                    verified=True, observed_at=proof['observed_at'], manifest=manifest))


def release(state, identity, source_sha256, reason, released_at):
    item = registry(state)['observations'][identity]
    if item['source']['sha256'] != source_sha256 or not isinstance(reason, str) or not reason.strip():
        raise ValueError('Controller release requires observation ID, exact source SHA and a reason')
    registry(state)['releases'][identity] = {'source_sha256': source_sha256, 'reason': reason,
                                            'released_at': released_at, 'authority': 'explicit_private_controller_action'}
