"""Freeze and accept an explicit, independent supplement to an invalid access run.

This is a private admission record, never a replacement task verdict. As with
the main pipeline, adapter collection is trusted controller evidence; an
operator's declaration of independence is not a model review or a receipt.
Neither this module nor its CLI starts a model.
"""
import argparse
import base64
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import hashlib
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import quote, quote_plus

from access_readiness import FACETS, PROTOCOL, validate

KIND = 'supplemental_access_admission'
HERE = Path(__file__).resolve().parent


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def object_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def write(path, value, *, exclusive=False):
    path = Path(path)
    raw = (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | (os.O_EXCL if exclusive else os.O_TRUNC), 0o600)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(raw)


def tree(directory):
    directory = Path(directory)
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError('Supplement requires a regular directory')
    files = {}
    for path in sorted(directory.rglob('*')):
        if path.is_symlink():
            raise ValueError('Supplement inputs and outputs cannot contain links')
        if path.is_file():
            files[str(path.relative_to(directory))] = digest(path)
    return files


def reject_registered_secrets(directory, secrets):
    """Read-only scan: never redact a hard link to an original frozen packet."""
    variants = set()
    for value in secrets:
        variants.update((value.encode(), json.dumps(value, ensure_ascii=True)[1:-1].encode(),
                         json.dumps(value, ensure_ascii=False)[1:-1].encode(),
                         quote(value, safe='').encode(), quote_plus(value).encode(),
                         base64.b64encode(value.encode()), base64.urlsafe_b64encode(value.encode())))
    if not variants:
        return
    for path in Path(directory).rglob('*'):
        if (any(value in str(path.relative_to(directory)).encode() for value in variants)
                or path.is_file() and any(value in path.read_bytes() for value in variants)):
            raise ValueError('Supplement input contains a registered service secret')


def link_frozen_packet(source, destination):
    """Share host storage; the formal adapter copies bytes into its grader.

    Only reviewed, already frozen controller files are linked. The two files
    changed by this preparation are copied instead; no linked file is written
    or chmodded. Later source modification invalidates both hash bindings.
    """
    destination.mkdir(mode=0o700)
    for path in sorted(source.rglob('*')):
        relative = path.relative_to(source)
        target = destination / relative
        if path.is_dir():
            target.mkdir(mode=0o700)
        elif path.is_file():
            if str(relative) in ('prompt.txt', 'assessment.template.json'):
                shutil.copyfile(path, target)
            else:
                os.link(path, target)


def hard_holds(run):
    """Structured original preparation restrictions cannot be cleared by prose."""
    config = read(run / 'config.json')
    admission = read(run / 'frozen/admission.json')
    holds = []
    if admission.get('status') != 'documented_free' or admission.get('mode') != 'enforce':
        holds.append('Original preparation does not authorize the assigned free-only scope')
    for value in (config, config.get('resource_authorization', {}), read(run / 'grading/assessment.json')):
        if value.get('hard_holds'):
            holds.append('Original explicit hard hold remains')
    reference = run / 'frozen/grading/reference.json'
    if reference.exists():
        value = read(reference)
        routes = value.get('cohort_disclosure', {}).get('held_routes', {})
        if config['service'] + '/' + config['route'] in routes:
            holds.append('Original reference explicitly holds this route')
    return holds


def source_snapshot(run):
    """Bind this target's actual evidence; do not scan unrelated historical runs."""
    run = Path(run).resolve()
    state, config = read(run / 'state.json'), read(run / 'config.json')
    if state.get('phase') not in ('reviewed', 'recorded') or config.get('phase') != 'access' or config.get('trial_protocol') != PROTOCOL:
        raise ValueError('Supplement requires a validated current-protocol access run')
    review = read(run / 'grading/assessment.json')
    if review.get('status') != 'invalid_run':
        raise ValueError('Only an original invalid_run can receive supplemental admission')
    records = state.get('record_hashes', {})
    if not records or records.get('grading/assessment.json') != digest(run / 'grading/assessment.json'):
        raise ValueError('Original validated assessment binding changed')
    for name, expected in records.items():
        path = (run / name).resolve()
        if not path.is_relative_to(run) or path.is_symlink() or digest(path) != expected:
            raise ValueError('Original reviewed evidence changed')
    frozen = read(run / 'frozen-hashes.json')
    for name, expected in frozen.items():
        path = run / 'frozen' / name
        if not path.resolve().is_relative_to(run) or path.is_symlink() or digest(path) != expected:
            raise ValueError('Original frozen evidence changed')
    packet = tree(run / 'grading-input')
    if packet != read(run / 'grading-input-hashes.json'):
        raise ValueError('Original frozen grading packet changed')
    controls = {name: digest(run / name) for name in ('config.json', 'frozen-hashes.json', 'grading-input-hashes.json',
                                                   'execution/receipt.json', 'grading/receipt.json')}
    return {'run_id': run.name, 'record_hashes': records, 'controls': controls,
            'execution_files': tree(run / 'execution'), 'grading_input_files': packet,
            'hard_holds': hard_holds(run)}


def expected_sources():
    codex = HERE / 'runners/codex'
    return {name: digest(codex / name if name != 'session_usage.py' else HERE / name)
            for name in ('worker.py', 'normalize.py', 'artifact_capture.py', 'session_usage.py')}


def review_path(run, directory, identity):
    expected = run / 'supplemental-access/reviews' / identity
    if (not re.fullmatch(r'[A-Za-z0-9._-]+', identity) or Path(directory).resolve() != expected
            or any(path.is_symlink() for path in (expected, *expected.parents) if path.is_relative_to(run))):
        raise ValueError('Supplement review needs its own declared run-local directory')
    return expected


def prepare(run_dir, facts_dir, review_dir, *, review_id, reviewer_settings):
    run = Path(run_dir).resolve()
    destination = review_path(run, review_dir, review_id)
    source = source_snapshot(run)
    if source['hard_holds']:
        raise ValueError('Original hard hold prevents supplemental admission')
    settings = reviewer_settings
    argv = settings.get('commands', {}).get('start', [])
    official = str((HERE / 'runners/codex/adapter.py').resolve())
    if (official not in argv or '--config' not in argv or settings.get('billing_mode') != 'chatgpt'
            or settings.get('model') != 'gpt-6.1-sol' or settings.get('reasoning_effort') != 'high'
            or settings.get('harness', {}).get('name') != 'codex'
            or not all(settings['harness'].get(k) for k in ('version', 'mode'))):
        raise ValueError('Supplement requires the formal independent Codex adapter')
    if type(settings.get('seconds')) is not int or settings['seconds'] <= 0:
        raise ValueError('Supplement reviewer needs a frozen positive seconds budget')
    config = read(run / 'config.json')
    if not settings.get('runtime') or settings['runtime'] == config['execution']['runtime']:
        raise ValueError('Supplement reviewer cannot reuse the executor runtime')
    facts = tree(facts_dir)
    if not facts:
        raise ValueError('Supplement facts cannot be empty')
    from grading_privacy import secrets_for
    secrets = secrets_for(run)
    reject_registered_secrets(run / 'grading-input', secrets)
    reject_registered_secrets(facts_dir, secrets)
    adapter = Path(argv[argv.index('--config') + 1]).resolve()
    if adapter.is_symlink() or not adapter.is_file():
        raise ValueError('Supplement adapter binding is missing')
    reviewer_adapter = read(adapter)
    if (reviewer_adapter.get('billing_mode') != 'chatgpt'
            or not isinstance(reviewer_adapter.get('containers', {}).get(settings['runtime']), str)):
        raise ValueError('Supplement runtime is not in the formal grader pool')
    executor_argv = config['execution'].get('commands', {}).get('start', [])
    if '--config' in executor_argv:
        executor_adapter = read(Path(executor_argv[executor_argv.index('--config') + 1]))
        same_host = (executor_adapter.get('transport', 'ssh'), executor_adapter.get('host')) == (
            reviewer_adapter.get('transport', 'ssh'), reviewer_adapter.get('host'))
        if (same_host and executor_adapter.get('containers', {}).get(config['execution']['runtime'])
                == reviewer_adapter.get('containers', {}).get(settings['runtime'])):
            raise ValueError('Supplement reviewer aliases the physical executor container')
    # A unique directory is durable ownership, never permission to overwrite an attempt.
    destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    destination.mkdir(mode=0o700, exist_ok=False)
    packet = destination / 'input'
    link_frozen_packet(run / 'grading-input', packet)
    supplements = packet / 'supplemental-access'
    supplements.mkdir(mode=0o700, exist_ok=False)
    shutil.copytree(facts_dir, supplements / 'facts')
    shutil.copyfile(run / 'grading/assessment.json', supplements / 'original-assessment.json')
    binding = {'schema_version': 1, 'review_kind': KIND, 'review_id': review_id,
               'original_assessment_sha256': source['record_hashes']['grading/assessment.json'],
               'source_binding_sha256': object_hash(source), 'facts_sha256': object_hash(facts)}
    reviewer = {key: settings[key] for key in ('model', 'reasoning_effort', 'harness')}
    template = {**binding, 'status': 'unknown', 'reviewer': reviewer,
                'service_execution': 'unknown',
                'access_readiness': {name: {'status': 'unknown', 'evidence': ''} for name in FACETS},
                'hard_holds': {'status': 'unknown', 'items': [], 'evidence': ''}}
    write(supplements / 'binding.json', binding)
    write(packet / 'assessment.template.json', template)
    (packet / 'prompt.txt').write_text(
        '本次冻结绑定：' + json.dumps(binding, sort_keys=True, ensure_ascii=False) + '\n'
        '核验 supplemental-access/binding.json、original-assessment.json 及 facts/，再对照原冻结用户要求、ENVIRONMENT.md、reference 和真实执行证据。'
        '这是显式补充材料的独立接入准入核验，不修改旧 assessment 或重做用户任务。不得把总控声明或原四项 ready 当作已解决材料缺口。'
        '逐项核对补充事实来源、原有授权/免费范围/隔离/时限等硬限制；不能证实的限制保持 unknown，仍有阻碍写 blocked 和具体原因。'
        '仅在四项 readiness 全部 ready、service_execution=completed 且 hard_holds.status=clear（有据且 items=[]）时写 status=ready。'
        '其他情况写 not_ready 或 unknown。按 assessment.template.json 输出 assessment.json，绑定字段和 reviewer 模型来源不得改写；实际新会话身份由运行器回执绑定。'
        '原接入用户交付结论保持原样，补充准入不使旧 invalid_run 变为 completed。\n')
    excluded = []
    for receipt in [run / 'execution/receipt.json', run / 'grading/receipt.json', *run.glob('grading-attempt*/receipt.json')]:
        if receipt.is_file():
            excluded.append(read(receipt).get('session_id'))
    reject_registered_secrets(packet, secrets)
    manifest = {'schema_version': 1, 'created_at': datetime.now(timezone.utc).isoformat(),
                'run': str(run), 'binding': binding, 'source': source, 'facts': facts,
                'reviewer_settings': settings, 'adapter_sha256': digest(adapter),
                'runtime_sources': expected_sources(), 'excluded_sessions': excluded,
                'packet_storage': 'Hard links to reviewed frozen host input; independent new prompt, template and facts; adapter copies bytes into isolated grader',
                'input_files': tree(packet)}
    request = {'run_id': review_id, 'role': 'grading', 'fresh_session': True,
               'input': str(packet), 'output': str(destination / 'grading'),
               **{key: settings[key] for key in ('model', 'reasoning_effort', 'harness', 'runtime', 'seconds')},
               **{key: settings[key] for key in ('closure_fraction', 'deadline_epoch', 'billing_mode') if key in settings}}
    manifest['request'] = request
    write(destination / 'grading-request.json', request, exclusive=True)
    write(destination / 'manifest.json', manifest, exclusive=True)
    return manifest


def verify_review(run, destination):
    manifest = read(destination / 'manifest.json')
    binding = manifest['binding']
    review_path(run, destination, binding['review_id'])
    if manifest['run'] != str(run) or manifest['source'] != source_snapshot(run):
        raise ValueError('Original access evidence changed after supplemental freeze')
    if (binding['source_binding_sha256'] != object_hash(manifest['source'])
            or binding['facts_sha256'] != object_hash(manifest['facts'])
            or binding['original_assessment_sha256'] != manifest['source']['record_hashes']['grading/assessment.json']):
        raise ValueError('Supplement source binding is inconsistent')
    if manifest['source']['hard_holds'] or hard_holds(run):
        raise ValueError('Original hard hold remains')
    if tree(destination / 'input') != manifest['input_files']:
        raise ValueError('Frozen supplemental packet changed')
    if tree(destination / 'input/supplemental-access/facts') != manifest['facts']:
        raise ValueError('Frozen supplementary facts changed')
    argv = manifest['reviewer_settings']['commands']['start']
    if digest(Path(argv[argv.index('--config') + 1])) != manifest['adapter_sha256']:
        raise ValueError('Frozen supplemental adapter binding changed')
    return manifest


def validate_collection(run, destination, manifest):
    output = destination / 'grading'
    receipt, assessment = read(output / 'receipt.json'), read(output / 'assessment.json')
    settings, binding = manifest['reviewer_settings'], manifest['binding']
    handle = binding['review_id'] + '-grading'
    if (read(destination / 'grading-start.json') != manifest['request']
            or read(destination / 'grading-start-result.json').get('handle') != handle
            or read(destination / 'grading-collect.json') != {**manifest['request'], 'handle': handle}
            or read(destination / 'grading-collect-result.json').get('collected') is not True):
        raise ValueError('Supplement lacks formal controller start and collect receipts')
    session = receipt.get('session_id')
    if (not isinstance(session, str) or not re.fullmatch(r'[0-9a-fA-F-]{36}', session)
            or session in manifest['excluded_sessions']):
        raise ValueError('Supplement needs a new independent reviewer session')
    for accepted in (run / 'supplemental-access/reviews').glob('*/accepted.json'):
        if accepted.parent != destination and read(accepted).get('session_id') == session:
            raise ValueError('Supplement reviewer session already accepted elsewhere')
    workspace = '/workspace/' + binding['review_id'] + '-grading'
    if (receipt.get('workspace') != workspace or receipt.get('input_verified') is not True
            or receipt.get('exit_code') != 0 or receipt.get('timed_out') is not False
            or receipt.get('billing_mode') != 'chatgpt' or not receipt.get('isolation')):
        raise ValueError('Missing successful independently collected grading receipt')
    for key in ('model', 'reasoning_effort', 'harness', 'runtime'):
        if receipt.get(key) != settings[key]:
            raise ValueError('Supplement reviewer differs from frozen source')
    if receipt.get('runtime_code_preflight', {}).get('source_sha256') != manifest['runtime_sources']:
        raise ValueError('Supplement lacks formal runtime source provenance')
    if not re.fullmatch(r'sha256:[0-9a-f]{64}', receipt.get('runtime_image_id', '')):
        raise ValueError('Supplement lacks runtime image provenance')
    start, end = (datetime.fromisoformat(receipt[key]) for key in ('started_at', 'ended_at'))
    if (start.tzinfo is None or end.tzinfo is None or start < datetime.fromisoformat(manifest['created_at'])
            or end > datetime.now(timezone.utc) + timedelta(seconds=5)
            or not 0 <= (end - start).total_seconds() <= settings['seconds']):
        raise ValueError('Supplement reviewer timestamps are invalid')
    raw = output / 'session.raw.jsonl'
    rows = [json.loads(line) for line in raw.read_text().splitlines() if line.strip()]
    if any(not isinstance(row, dict) or not isinstance(row.get('payload', {}), dict) for row in rows):
        raise ValueError('Malformed collected reviewer session')
    metadata = [row['payload'] for row in rows if row.get('type') == 'session_meta']
    if not any(row.get('id') == session and row.get('cwd') == workspace for row in metadata):
        raise ValueError('Collected reviewer session does not match receipt')
    spec = importlib.util.spec_from_file_location('supplement_observed_input', HERE / 'runners/codex/normalize.py')
    normalizer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(normalizer)
    packet = destination / 'input'
    prompt = (packet / 'AGENTS.md').read_text().strip() + '\n\n' + (packet / 'prompt.txt').read_text()
    if not normalizer.observed_input(raw, prompt, settings['model'], settings['reasoning_effort']):
        raise ValueError('Collected reviewer did not observe the frozen supplemental prompt')
    activity = [row['payload'] for row in rows if row.get('type') == 'response_item'
                and (row['payload'].get('role') == 'assistant'
                     or row['payload'].get('type') == 'function_call')]
    if not any(row.get('content') or row.get('arguments') for row in activity):
        raise ValueError('Collected reviewer has no actual assistant or tool activity')
    usage = read(output / 'usage.json')
    if not any(row.get('path') == raw.name and row.get('sha256') == digest(raw) for row in usage.get('sources', [])):
        raise ValueError('Collected reviewer session source hash is missing')
    artifacts = output / 'artifacts'
    # The official worker collects its actual workspace, and the adapter retains
    # the model-written assessment before its layout-only normalizer runs.
    if (read(output / 'assessment.raw.json') != assessment
            or digest(artifacts / 'assessment.json') != digest(output / 'assessment.raw.json')):
        raise ValueError('Assessment is not the collected model artifact')
    index = read(output / 'artifact-input-index.json')
    snapshot = index.get('input_snapshot', {})
    entries = snapshot.get('entries', {})
    input_files = {name: value for name, value in entries.items() if value.get('kind') == 'file'}
    if (index.get('schema_version') != 1 or snapshot.get('available') is not True
            or snapshot.get('root') != '/run/afs/inputs/' + handle
            or snapshot.get('sha256') != object_hash(entries)
            or set(input_files) != set(manifest['input_files'])
            or any(value.get('uid') != 0 or value.get('mode', 0) & 0o022 for value in entries.values())):
        raise ValueError('Missing formal controller-owned frozen input index')
    omitted = {row['path']: row for row in index.get('omitted', [])}
    changed = {row['path'] for row in index.get('files', []) + index.get('directories', [])}
    for name, expected in manifest['input_files'].items():
        source = input_files[name]
        row = omitted.get(name, {})
        if (source.get('sha256') != expected or source.get('bytes') != (destination / 'input' / name).stat().st_size
                or name in changed or row.get('change') != 'unchanged_input'
                or any(row.get(key) != source.get(key) for key in ('sha256', 'bytes', 'mode'))):
            raise ValueError('Collected frozen reviewer workspace differs from input manifest')
    if any(row.get('change') != 'unchanged_input' and row.get('path') in entries
           for row in index.get('omitted', [])):
        raise ValueError('Frozen reviewer input was deleted, linked or unreadable')
    events = [json.loads(line) for line in (output / 'events.jsonl').read_text().splitlines() if line.strip()]
    if (not any(row.get('type') == 'thread.started' and row.get('thread_id') == session for row in events)
            or not any(row.get('type') == 'turn.completed' for row in events)
            or any(row.get('type') in ('turn.failed', 'error') for row in events)):
        raise ValueError('Collected independent reviewer did not complete its turn')
    from adapter_usage import read_usage
    from session_usage import extract_usage
    final_usage = next((row.get('usage') for row in reversed(events) if row.get('type') == 'turn.completed'), None)
    observed = extract_usage(raw, final_usage)
    _, canonical = read_usage(output, settings['model'])
    if (not canonical.get('requests_verified') or not canonical['requests']
            or observed.get('requests') != canonical['requests']
            or not any(row['output_tokens'] > 0 for row in canonical['requests'])):
        raise ValueError('Supplement needs source-verified actual model request usage')
    if any(assessment.get(key) != value for key, value in binding.items()):
        raise ValueError('Supplement review binding differs from frozen input')
    if assessment.get('reviewer') != {key: settings[key] for key in ('model', 'reasoning_effort', 'harness')}:
        raise ValueError('Supplement reviewer provenance is missing')
    readiness = validate(assessment.get('access_readiness'))
    holds = assessment.get('hard_holds', {})
    if not isinstance(holds, dict):
        raise ValueError('Supplement hard-hold decision must be explicit')
    if (assessment.get('status') != 'ready' or assessment.get('service_execution') != 'completed'
            or any(readiness[name]['status'] != 'ready' for name in FACETS)
            or holds.get('status') != 'clear' or holds.get('items') != []
            or not isinstance(holds.get('evidence'), str) or not holds['evidence'].strip()):
        raise ValueError('Supplement has unresolved readiness or a hard hold')
    return receipt


@contextmanager
def admission_lock(run):
    base = run / 'supplemental-access'
    base.mkdir(mode=0o700, exist_ok=True)
    with (base / '.admission.lock').open('a') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        yield


def accept(run_dir, review_dir, *, replace_active=False):
    run, destination = Path(run_dir).resolve(), Path(review_dir).resolve()
    with admission_lock(run):
        return _accept(run, destination, replace_active)


def _accept(run, destination, replace_active):
    manifest = verify_review(run, destination)
    receipt = validate_collection(run, destination, manifest)
    active = run / 'supplemental-access/active.json'
    if active.exists() and not replace_active:
        raise ValueError('An active supplement already exists; explicit replacement is required')
    accepted = {'schema_version': 1, 'review_id': manifest['binding']['review_id'],
                'manifest_sha256': digest(destination / 'manifest.json'),
                'input_sha256': object_hash(manifest['input_files']),
                'collected_files': tree(destination / 'grading'), 'session_id': receipt['session_id'],
                'controller_files': {name: digest(destination / name) for name in (
                    'grading-start.json', 'grading-start-result.json', 'grading-collect.json', 'grading-collect-result.json')},
                'reviewer': {key: receipt[key] for key in ('workspace', 'model', 'reasoning_effort', 'harness', 'runtime')},
                'accepted_at': datetime.now(timezone.utc).isoformat(),
                'original_verdict_unchanged': True}
    write(destination / 'accepted.json', accepted, exclusive=True)
    pointer = {'review_id': accepted['review_id'], 'accepted_sha256': digest(destination / 'accepted.json')}
    if active.exists():
        pointer['supersedes'] = read(active)
    temporary = active.with_name('active.tmp.json')
    write(temporary, pointer, exclusive=True)
    os.replace(temporary, active)
    return accepted


def decision(run_dir):
    try:
        run = Path(run_dir).resolve()
        pointer = read(run / 'supplemental-access/active.json')
        destination = review_path(run, run / 'supplemental-access/reviews' / pointer['review_id'], pointer['review_id'])
        if digest(destination / 'accepted.json') != pointer['accepted_sha256']:
            raise ValueError('Accepted supplement binding changed')
        accepted = read(destination / 'accepted.json')
        manifest = verify_review(run, destination)
        if (digest(destination / 'manifest.json') != accepted['manifest_sha256']
                or object_hash(manifest['input_files']) != accepted['input_sha256']
                or tree(destination / 'grading') != accepted['collected_files']):
            raise ValueError('Accepted supplemental review changed')
        if any(digest(destination / name) != expected for name, expected in accepted['controller_files'].items()):
            raise ValueError('Accepted supplemental controller receipts changed')
        receipt = validate_collection(run, destination, manifest)
        if receipt['session_id'] != accepted['session_id']:
            raise ValueError('Accepted reviewer session changed')
        return True, 'Access ready through explicit independent supplemental admission; original invalid verdict unchanged'
    except (OSError, ValueError, KeyError, TypeError) as error:
        return False, 'Supplemental access admission unavailable: ' + str(error)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='operation', required=True)
    create = commands.add_parser('prepare')
    create.add_argument('run', type=Path)
    create.add_argument('facts', type=Path)
    create.add_argument('review', type=Path)
    create.add_argument('--review-id', required=True)
    create.add_argument('--reviewer-config', type=Path, required=True)
    collect = commands.add_parser('accept')
    collect.add_argument('run', type=Path)
    collect.add_argument('review', type=Path)
    collect.add_argument('--replace-active', action='store_true')
    status = commands.add_parser('status')
    status.add_argument('run', type=Path)
    args = parser.parse_args()
    if args.operation == 'prepare':
        prepare(args.run, args.facts, args.review, review_id=args.review_id, reviewer_settings=read(args.reviewer_config))
        value = {'review_id': args.review_id, 'input': str(args.review / 'input'),
                 'output': str(args.review / 'grading'), 'manifest_sha256': digest(args.review / 'manifest.json')}
    elif args.operation == 'accept':
        value = accept(args.run, args.review, replace_active=args.replace_active)
        value = {'review_id': value['review_id'], 'session_id': value['session_id'],
                 'original_verdict_unchanged': True, 'admission_ready': True}
    else:
        ready, reason = decision(args.run)
        value = {'ready': ready, 'reason': reason}
    print(json.dumps(value, ensure_ascii=False))


if __name__ == '__main__':
    main()
