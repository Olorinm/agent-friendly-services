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


def public_copy(raw, meta, run_dir, reviewer=''):
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
    for value, replacement in sorted(replacements.items(), key=lambda item: -len(item[0])):
        # Evidence can embed paths in JSON strings or Markdown URL targets.
        for variant in (value, json.dumps(value, ensure_ascii=True)[1:-1],
                        quote(value, safe='/'), quote(value, safe='')):
            raw = raw.replace(variant.encode(), replacement.encode())
    return raw


def record(run_dir, review_path, route_id=None, task_file=None, task_version=None):
    run_dir, review_path = run_dir.resolve(), review_path.resolve()
    if not run_dir.is_relative_to((ROOT / 'data/experiments/results').resolve()):
        raise ValueError('Run must be under data/experiments/results/')
    meta = json.loads((run_dir / 'run.json').read_text())
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
        raw = source.read_bytes()
        if re.search(rb'eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+', raw):
            raise ValueError('Evidence contains a JWT-like value; review/redact before recording')
        # The reviewer checks content/credentials; strip host identifiers here too.
        public = public_copy(raw, meta, run_dir, review['reviewer'])
        relative = source.relative_to(run_dir)
        dest = evidence_dir / relative
        info = {'path': str(dest.relative_to(ROOT)), 'sha256': hashlib.sha256(public).hexdigest(),
                'note': item.get('note', '')}
        if public != raw:
            info.update(source_sha256=sha(source),
                        redactions=['local paths or Codex session identifiers'])
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
                        'service_credentials': 'none', 'web_search': 'live'},
        'status': status, 'reason': review['reason'], 'usage': meta.get('usage'),
        'service_cost_usd': review['service_cost_usd'], 'human_interventions': review['human_interventions'],
        'review': {'method': 'external_agent', 'reviewer': review['reviewer'],
                   'reviewed_at': datetime.now(timezone.utc).isoformat(), 'checks': checks},
        'evidence': [f[2] for f in files],
        'provenance': {'local_run_dir': str(run_dir.relative_to(ROOT)),
                       'run_sha256': sha(run_dir / 'run.json'), 'events_sha256': sha(run_dir / 'events.jsonl'),
                       'answer_sha256': sha(run_dir / 'answer.md'), 'review_sha256': sha(review_path)},
    }
    serialized = json.dumps(result, ensure_ascii=False, indent=2).encode()
    sanitized = public_copy(serialized, meta, run_dir, review['reviewer'])
    result = json.loads(sanitized)
    if sanitized != serialized or any('redactions' in info for _, _, info in files):
        result['provenance']['privacy_note'] = (
            'Public copies redact local paths and Codex session identifiers. '
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
