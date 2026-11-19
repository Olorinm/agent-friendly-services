"""Project safe admission fields and explicitly selected preparation evidence.

No assessments, answers, commands, credentials or whole runner configurations
are copied. The controller still reviews evidence content and applicability;
hashes establish bytes, not the truth of an assertion.
"""
from copy import deepcopy
import math
from pathlib import Path
import re

import pipeline as runs
import work_package as packages

KINDS = ('official_documentation', 'capability_metadata', 'sealed_baseline', 'resource_observation', 'synthetic_description')


def regular(path):
    path = Path(path)
    if (not path.is_absolute() or any(item.is_symlink() for item in (path, *path.parents))
            or not path.is_file()):
        raise ValueError('Preparation context requires a regular absolute source file')
    return path


def selected(binding, targets):
    """Read only controller-selected facts/files; return their exact hash binding."""
    if binding is None: return None, {}
    packages.keys(binding, ('file', 'sha256'), ('file', 'sha256'))
    path = regular(binding['file'])
    if not re.fullmatch(packages.SHA, binding['sha256']) or runs.digest(path) != binding['sha256']:
        raise ValueError('Preparation context source hash changed')
    value = runs.read(path)
    packages.keys(value, ('schema_version', 'targets', 'evidence'), ('schema_version', 'targets', 'evidence'))
    if type(value['schema_version']) is not int or value['schema_version'] != 1:
        raise ValueError('Unsupported preparation context schema')
    if not isinstance(value['targets'], dict) or not isinstance(value['evidence'], list):
        raise ValueError('Preparation context targets/evidence types are invalid')
    files = {str(path): binding['sha256']}; evidence = {}; output = deepcopy(value)
    for item, exposed in zip(value['evidence'], output['evidence']):
        packages.keys(item, ('id', 'file', 'sha256', 'source', 'purpose', 'kind'), ('id', 'file', 'sha256', 'source', 'purpose', 'kind'))
        identity = packages.identity(item['id'])
        if identity in evidence or item['kind'] not in KINDS or not isinstance(item['purpose'], str) or not item['purpose'].strip():
            raise ValueError('Unsupported or duplicate preparation evidence')
        source = packages.regular_file(path.parent, item['file'])
        if not re.fullmatch(packages.SHA, item['sha256']) or runs.digest(source) != item['sha256']:
            raise ValueError('Selected preparation evidence bytes changed')
        files[str(source)] = item['sha256']; evidence[identity] = source
        # Derived path prevents exposing controller paths or letting a model choose a destination.
        exposed['file'] = 'controller-context/' + identity + source.suffix
    for target_id, facts in value['targets'].items():
        if target_id not in targets: raise ValueError('Preparation context contains an unapproved target')
        packages.keys(facts, ('service', 'route', 'observations'), ('service', 'route', 'observations'))
        config = targets[target_id]['config']
        if facts['service'] != config['service'] or facts['route'] != config['route'] or not isinstance(facts['observations'], list):
            raise ValueError('Preparation context target does not match controller policy')
        for observation in facts['observations']:
            packages.keys(observation, ('topic', 'status', 'statement', 'evidence_ids'), ('topic', 'status', 'statement', 'evidence_ids'))
            if (observation['status'] not in ('confirmed', 'unknown', 'held')
                    or any(not isinstance(observation[key], str) or not observation[key].strip() for key in ('topic', 'statement'))
                    or not set(packages.strings(observation['evidence_ids'], nonempty=True)).issubset(evidence)):
                raise ValueError('Preparation observation needs explicit status and selected evidence')
    return output, files


def fee(value):
    if not isinstance(value, dict): raise ValueError('Fee qualification must be an object')
    return {key: deepcopy(value[key]) for key in ('status', 'scope', 'source_urls', 'amount') if key in value}


def public_limits(settings):
    """Share numeric task prerequisites, never commands, paths or runner secrets."""
    result = {}
    for key in ('seconds', 'max_model_requests', 'deadline_epoch', 'closure_fraction'):
        if key not in settings: continue
        value = settings[key]
        valid = (type(value) in (int, float) and math.isfinite(value) and value > 0
                 and (key != 'closure_fraction' or value < 1)
                 and (key not in ('seconds', 'max_model_requests') or type(value) is int))
        if not valid: raise ValueError('Preparation public runtime limit is invalid: '+key)
        result[key] = value
    return result


def target_facts(config, catalog):
    """Field projection only; unknown qualification is never upgraded to ready."""
    service, route = config['service'], config['route']
    parser = runs.module('preparation_route', 'codex-service-trial.py')
    selected_route = parser.select_route(catalog, service, route)
    result = {'service': service, 'route': route,
              **{key: selected_route[key] for key in ('entry_url', 'docs') if key in selected_route}}
    for role in ('execution', 'grading'):
        limits = public_limits(config.get(role, {}))
        if limits: result[role+'_limits'] = limits
    authorization = config.get('resource_authorization')
    if authorization is not None:
        if not isinstance(authorization, dict) or authorization.get('service') != service or authorization.get('route') != route:
            raise ValueError('Preparation resource authorization must match the assigned target')
        result['resource_authorization'] = {key: deepcopy(authorization[key]) for key in ('service', 'route', 'fee_policy') if key in authorization}
        if 'service_fee' in authorization: result['resource_authorization']['service_fee'] = fee(authorization['service_fee'])
    if config.get('reference'):
        reference = runs.read(regular(config['reference']))
        qualification = reference.get('service_fee_qualification', {}).get(service)
        if qualification is not None and qualification.get('route', route) == route:
            result['service_fee_qualification'] = fee(qualification['service_fee'])
    return result


def populate(inputs, binding, targets):
    context, _ = selected(binding, targets)
    if context is None: return
    source = runs.read(binding['file'])
    for original, exposed in zip(source['evidence'], context['evidence']):
        file = packages.regular_file(Path(binding['file']).parent, original['file'])
        destination = inputs / exposed['file']; destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        destination.write_bytes(file.read_bytes()); destination.chmod(0o600)
        if runs.digest(destination) != original['sha256']: raise ValueError('Preparation evidence changed during copy')
    runs.write(inputs/'controller-context.json', context)
