#!/usr/bin/env python3
"""Stage an externally reviewed run and selected evidence in the local catalog.

This reads measured fields from run.json, never from the reviewer's estimates.
It does not commit, push, or infer a task verdict from the executor's exit code.
See data/experiments/AGENTS.md for the review input and workflow.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def number_or_unknown(value):
    return value is None or (type(value) in (int, float) and 0 <= value < float('inf'))


def service_charge(review):
    """Normalize documented service charges; calculate usage-based estimates."""
    detail = review.get('service_cost')
    amount = review.get('service_cost_usd')
    if detail is None:
        if amount is not None:
            raise ValueError('service_cost sources and basis are required for a known service charge')
        return None, {'kind': 'unknown', 'amount_usd': None, 'sources': [],
                      'note': 'No service billing evidence supplied.'}
    if not isinstance(detail, dict) or detail.get('kind') not in ('reported', 'estimated', 'confirmed_free', 'unknown'):
        raise ValueError('Invalid service_cost kind')
    kind = detail['kind']
    sources = detail.get('sources', [])
    if not isinstance(sources, list) or any(not isinstance(x, str) or not x.strip() for x in sources):
        raise ValueError('service_cost sources must be nonempty source references')
    if not isinstance(detail.get('note'), str) or not detail['note'].strip():
        raise ValueError('service_cost needs a note explaining the billing basis')
    if kind != 'unknown' and not sources:
        raise ValueError('service_cost sources are required')
    if kind == 'estimated':
        items = detail.get('items')
        if not isinstance(items, list) or not items:
            raise ValueError('Estimated service_cost needs usage and unit-price items')
        total = 0
        for item in items:
            if not isinstance(item, dict) or not item.get('unit'):
                raise ValueError('Each service_cost item needs a unit')
            for key in ('quantity', 'usd_per_unit'):
                if item.get(key) is None or not number_or_unknown(item.get(key)):
                    raise ValueError('Service usage and unit prices must be nonnegative numbers')
            total += item['quantity'] * item['usd_per_unit']
        total = round(total, 10)
        if not number_or_unknown(total):
            raise ValueError('Service charge overflow')
        if amount is not None and abs(amount - total) > 1e-9:
            raise ValueError('Service charge does not match usage times price')
        amount = total
    elif kind == 'confirmed_free':
        if amount not in (None, 0):
            raise ValueError('Confirmed free service charge must be zero')
        amount = 0
    elif kind == 'unknown':
        if amount is not None:
            raise ValueError('Unknown service charge cannot contain a known amount')
    elif amount is None:
        raise ValueError('Reported service charge needs an amount')
    return amount, {**detail, 'amount_usd': amount, 'sources': sources}


def public_copy(raw, meta, run_dir, reviewer='', secrets=()):
    """Redact local paths/session identifiers without changing local originals."""
    replacements = {
        str(ROOT): '[REPO]', str(Path.home()): '[HOME]',
        str(run_dir): '[LOCAL_RUN]', str(meta['workspace']): '[WORKSPACE]',
    }
    if meta.get('records'):
        replacements[meta['records']] = '[LOCAL_RUN]'
    sessions = re.findall(r'\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b', reviewer, re.I)
    sessions += [meta[k] for k in ('thread_id', 'session_id') if isinstance(meta.get(k), str)]
    replacements.update({value: '[CODEX_SESSION]' for value in sessions if value})
    replacements.update({value: '[SERVICE_SECRET]' for value in secrets if value})
    def redact_text(value):
        for secret, replacement in sorted(replacements.items(), key=lambda item: -len(item[0])):
            for variant in (secret, json.dumps(secret, ensure_ascii=True)[1:-1],
                            quote(secret, safe='/'), quote(secret, safe='')):
                value = value.replace(variant, replacement)
        return value

    # Preserve JSON syntax and measured numeric fields. Account/resource IDs can
    # be JSON numbers; replacing raw bytes would leave an unquoted placeholder.
    try:
        original = json.loads(raw)
    except UnicodeDecodeError:
        for secret, replacement in sorted(replacements.items(), key=lambda item: -len(item[0])):
            raw = raw.replace(secret.encode(), replacement.encode())
        return raw
    except ValueError:
        return redact_text(raw.decode()).encode()

    def redact_json(value, key=''):
        if isinstance(value, dict):
            return {redact_text(k): redact_json(v, k) for k, v in value.items()}
        if isinstance(value, list):
            return [redact_json(v, key) for v in value]
        if isinstance(value, str):
            return redact_text(value)
        if type(value) is int and key.lower().endswith('id') and str(value) in secrets:
            return '[SERVICE_SECRET]'
        return value

    sanitized = redact_json(original)
    return raw if sanitized == original else (json.dumps(sanitized, ensure_ascii=False, indent=2) + '\n').encode()



def record(run_dir, review_path, route_id=None, task_file=None, task_version=None):
    run_dir, review_path = run_dir.resolve(), review_path.resolve()
    if not run_dir.is_relative_to((ROOT / 'data/experiments/results').resolve()):
        raise ValueError('Run must be under data/experiments/results/')
    meta = json.loads((run_dir / 'run.json').read_text())
    secret_file = run_dir / 'private-secrets.json'
    secrets = json.loads(secret_file.read_text()) if secret_file.exists() else []
    if not isinstance(secrets, list) or any(not isinstance(v, str) or not v for v in secrets):
        raise ValueError('Private secrets must be a list of nonempty strings')
    for workspace in [run_dir / 'workspace', Path(meta['workspace'])]:
        if review_path.is_relative_to(workspace.resolve()):
            raise ValueError('Review must be written outside the measured Agent workspace')
    review = json.loads(review_path.read_text())
    status = review.get('status')
    if status not in ('completed', 'not_completed', 'invalid_run'):
        raise ValueError('Review status must be completed, not_completed, or invalid_run')
    if not isinstance(review.get('reason'), str) or not review['reason'].strip():
        raise ValueError('Review needs an evidence-backed reason')
    if not isinstance(review.get('reviewer'), str) or not review['reviewer'].strip():
        raise ValueError('Identify the external reviewer')
    checks = review.get('checks', [])
    if not isinstance(checks, list) or any(not isinstance(c, dict) or not c.get('criterion')
            or type(c.get('passed')) is not bool or not c.get('evidence') for c in checks):
        raise ValueError('Each check needs criterion, boolean passed, and evidence explanation')
    if status == 'completed' and (not checks or not all(c['passed'] for c in checks)):
        raise ValueError('Completion requires explicit passing checks')
    if status == 'completed' and (meta.get('exit_code') != 0 or meta.get('timed_out')
                                   or not (run_dir / 'answer.md').is_file()):
        raise ValueError('A timed-out/failed run or missing final answer cannot be completed')
    if not meta.get('started_at') or not meta.get('ended_at'):
        raise ValueError('Run is not finished; wait for the runner')
    for k in ('service_cost_usd', 'human_interventions'):
        if k not in review or not number_or_unknown(review[k]):
            raise ValueError(f'{k} must be a measured nonnegative number, or null for unknown')
    if review['human_interventions'] is not None and type(review['human_interventions']) is not int:
        raise ValueError('human_interventions must be an integer or null')

    catalog = json.loads((ROOT / 'generated/catalog.json').read_text())
    service = next((s for s in catalog['services'] if s['id'] == meta['service']), None)
    rid = meta.get('route_id') or route_id
    route = next((r for r in ((service or {}).get('catalog') or {}).get('routes', []) if r['id'] == rid), None)
    if not route or route['entry_url'] != meta['entry_url']:
        raise ValueError('Service, route and entry URL must match the recorded run and catalog')
    if route_id and meta.get('route_id') and route_id != meta['route_id']:
        raise ValueError('Cannot relabel an existing run to a different route')
    task = meta.get('task')
    if not task:
        # Compatibility with the first two pilots: recover frozen content, not
        # today's mutable table. The caller supplies missing provenance only.
        if not task_file:
            raise ValueError('Legacy run needs --task-file (and --task-version if known)')
        cells = [s.strip() for s in meta['task_row'].strip('|').split('|')]
        task = dict(zip(['id', 'description', 'inputs', 'expected_output', 'success', 'failure'], cells[:6]))
        task.update(file=str((ROOT / task_file).resolve().relative_to(ROOT)), version=task_version,
                    sha256=meta['task_sha256'])
    if not (ROOT / task['file']).resolve().is_relative_to(ROOT) or not (ROOT / task['file']).is_file():
        raise ValueError('Task file must exist in the repository')

    service_amount, service_detail = service_charge(review)
    evidence = review.get('evidence', [])
    if not isinstance(evidence, list) or not evidence:
        raise ValueError('Select evidence files, including evidence of any failure/blocker')
    run_id = run_dir.name
    if not re.fullmatch(r'[a-zA-Z0-9._-]+', run_id):
        raise ValueError('Invalid run directory name')
    result_path = ROOT / 'data/experiments/evaluations' / f'{run_id}.json'
    evidence_dir = ROOT / 'data/experiments/evidence' / run_id
    if result_path.exists() or evidence_dir.exists():
        raise ValueError('This run is already recorded; retain history and record a new run')
    files = []
    for item in evidence:
        source = (run_dir / item['path']).resolve()
        if not source.is_relative_to(run_dir) or not source.is_file():
            raise ValueError('Evidence path must be a file inside the run directory')
        if source == (run_dir / 'session.raw.jsonl').resolve():
            raise ValueError('Do not publish the raw session as evidence')
        if source == secret_file.resolve():
            raise ValueError('Do not select the private secret store as evidence')
        raw = source.read_bytes()
        public = public_copy(raw, meta, run_dir, review['reviewer'], secrets)
        if re.search(rb'eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+', public):
            raise ValueError('Evidence contains a JWT-like value; review/redact before recording')
        # The reviewer checks content/credentials; strip host identifiers here too.
        relative = source.relative_to(run_dir)
        dest = evidence_dir / relative
        info = {'path': str(dest.relative_to(ROOT)), 'sha256': hashlib.sha256(public).hexdigest(),
                'note': item.get('note', '')}
        if public != raw:
            info.update(source_sha256=sha(source),
                        redactions=['local paths, Codex session identifiers or explicitly supplied service secrets'])
        files.append((public, dest, info))
    harness = meta.get('harness') or {'name': 'Codex CLI', 'version': meta['cli_version'],
                                    'mode': 'exec --json', 'launcher': 'scripts/codex-service-trial.py'}
    result = {
        'schema_version': 1, 'run_id': run_id, 'service_id': meta['service'], 'route_id': rid,
        'entry_url': meta['entry_url'], 'task': task, 'prompt_sha256': meta['prompt_sha256'],
        'harness': harness, 'model': meta['model'], 'reasoning_effort': meta['reasoning_effort'],
        'started_at': meta['started_at'], 'ended_at': meta['ended_at'],
        'elapsed_seconds': meta['elapsed_seconds'], 'budget_seconds': meta['seconds_limit'],
        'environment': {'host': meta.get('host'), 'isolation': meta['isolation'],
                        'service_credentials': meta.get('service_credentials', 'none'), 'web_search': 'live',
                        'preparation_note': meta.get('preparation_note', 'No service credentials provided.'),
                        'prompt_style': meta.get('prompt_style', 'legacy'),
                        'evidence_collection': meta.get('evidence_collection', 'executor receipts and external review'),
                        'prompt_characters': meta.get('prompt_characters'),
                        'input_delivery': meta.get('input_delivery', 'inline'),
                        'context_files': meta.get('context_files', [])},
        'status': status, 'reason': review['reason'], 'usage': meta.get('usage'),
        'service_cost_usd': service_amount, 'service_cost': service_detail,
        'human_interventions': review['human_interventions'],
        'review': {'method': 'external_agent', 'reviewer': review['reviewer'],
                   'reviewed_at': datetime.now(timezone.utc).isoformat(), 'checks': checks},
        'evidence': [f[2] for f in files],
        'provenance': {'local_run_dir': str(run_dir.relative_to(ROOT)),
                       'run_sha256': sha(run_dir / 'run.json'), 'events_sha256': sha(run_dir / 'events.jsonl'),
                       'answer_sha256': sha(run_dir / 'answer.md'), 'review_sha256': sha(review_path)},
    }
    if "request_usage" in meta:
        # Re-extract from the private raw session; do not trust review-supplied usage.
        from session_usage import extract_usage
        raw_session = run_dir / "session.raw.jsonl"
        result["request_usage"] = extract_usage(raw_session, meta.get("usage")) if raw_session.is_file() else {
            "status": "incomplete", "method": "session", "requests": [],
            "source_sha256": None, "reason": "Session file not found"}
    serialized = json.dumps(result, ensure_ascii=False, indent=2).encode()
    sanitized = public_copy(serialized, meta, run_dir, review['reviewer'], secrets)
    result = json.loads(sanitized)
    if sanitized != serialized or any('redactions' in info for _, _, info in files):
        result['provenance']['privacy_note'] = (
            'Public copies redact local paths, Codex session identifiers and explicitly supplied service secrets. '
            'Evidence sha256 hashes the public copy; source_sha256 and provenance hashes '
            'refer to unchanged local originals. Task results and usage are unchanged.')
    for public, dest, _ in files:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(public)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir', type=Path)
    parser.add_argument('--review', type=Path, required=True)
    parser.add_argument('--route', help='Only needed for a legacy run without a route id')
    parser.add_argument('--task-file', type=Path, help='Only needed for legacy run provenance')
    parser.add_argument('--task-version', help='Only needed for legacy run provenance')
    args = parser.parse_args()
    os.umask(0o077)
    try:
        path = record(args.run_dir, args.review, args.route, args.task_file, args.task_version)
    except (ValueError, KeyError, OSError) as error:
        parser.exit(1, f'Recording failed: {error}\n')
    print(f'Recorded locally: {path.relative_to(ROOT)}. Run npm run validate && npm run generate.')


if __name__ == '__main__':
    main()
