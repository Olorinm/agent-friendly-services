"""Check assigned resource boundaries before creating a new frozen run.

Qualification is preparation evidence, not an actual service charge. No prose
is interpreted as a fee rule or hold, and historical frozen runs are untouched.
"""
import hashlib
from urllib.parse import urlsplit


FREE_POLICY = 'confirmed_free_only'
FREE_STATUS = 'documented_free_within_scope'


def sha256(value):
    return hashlib.sha256(value).hexdigest()


def object_value(value, label):
    if not isinstance(value, dict):
        raise ValueError('Preparation admission: ' + label + ' must be an object')
    return value


def source_urls(value):
    return (isinstance(value, list) and bool(value)
            and all(isinstance(url, str) and urlsplit(url).scheme in ('http', 'https')
                    and urlsplit(url).netloc for url in value))


def plan(config, task, reference, reference_bytes, role_bytes, current_protocol):
    """Return private preparation evidence under the frozen free-only role.

    Source URLs and scope must be supplied by preparation; their truth and
    applicability still need that role's review, not a network/prose heuristic.
    """
    mode = config.get('admission_mode', 'enforce')
    if mode not in ('enforce', 'legacy_unchecked'):
        raise ValueError('Preparation admission: unknown admission_mode')
    if mode == 'legacy_unchecked' and config['trial_protocol'] == current_protocol:
        raise ValueError('Preparation admission: legacy_unchecked is unavailable for the current protocol')
    service, route = config['service'], config['route']
    result = {'schema_version': 1, 'service': service, 'route': route,
              'task': {'id': task['id'], 'version': task['version'], 'sha256': task['sha256']},
              'execution_role_sha256': sha256(role_bytes), 'role_fee_policy': FREE_POLICY,
              'reference_sha256': sha256(reference_bytes) if reference_bytes is not None else None,
              'mode': mode, 'fee_evidence': [], 'warnings': []}
    reference = object_value(reference, 'reference') if reference is not None else {}
    disclosure = object_value(reference.get('cohort_disclosure', {}), 'cohort_disclosure')
    held = object_value(disclosure.get('held_routes', {}), 'held_routes')
    exact_key = service + '/' + route
    if exact_key in held:
        # Match the structured key only; descriptive text is not a hold parser.
        raise ValueError('Preparation admission: assigned route is held: ' + exact_key
                         + '; correct preparation evidence before dispatch')

    authorization = object_value(config.get('resource_authorization', {}), 'resource_authorization')
    fee_policy = authorization.get('fee_policy', FREE_POLICY)
    if fee_policy != FREE_POLICY:
        raise ValueError('Preparation admission: the current execution role only permits confirmed-free scope; prepare an authorized new role/input version before changing that boundary')
    if authorization and (authorization.get('service') != service or authorization.get('route') != route):
        raise ValueError('Preparation admission: resource_authorization must match the assigned service and route')
    fees = []
    qualifications = object_value(reference.get('service_fee_qualification', {}), 'service_fee_qualification')
    if service in qualifications:
        qualification = object_value(qualifications[service], 'assigned service_fee_qualification')
        # Legacy qualifications apply to a service. New route-scoped evidence
        # must match explicitly; another route's evidence cannot authorize this one.
        if qualification.get('route', route) == route:
            fees.append(('reference.service_fee_qualification.' + service + '.service_fee',
                         object_value(qualification.get('service_fee'), 'assigned service_fee')))
    if 'service_fee' in authorization:
        fees.append(('config.resource_authorization.service_fee',
                     object_value(authorization['service_fee'], 'resource_authorization service_fee')))

    for source, fee in fees:
        status = fee.get('status')
        result['fee_evidence'].append({'source': source, 'qualification': fee})
        if status == FREE_STATUS:
            scope = fee.get('scope')
            scope_present = (isinstance(scope, str) and bool(scope.strip())) or (
                isinstance(scope, list) and bool(scope) and all(isinstance(s, str) and s.strip() for s in scope))
            if not scope_present or not source_urls(fee.get('source_urls')):
                raise ValueError('Preparation admission: documented free qualification needs official source URLs and applicable scope')
            if fee.get('amount') not in (None, 0):
                raise ValueError('Preparation admission: free qualification contradicts its monetary amount')
        elif status != 'unknown':
            raise ValueError('Preparation admission: assigned fee qualification does not establish free scope: ' + str(status))

    if any(fee.get('status') == 'unknown' for _, fee in fees):
        raise ValueError('Preparation admission: assigned service fee is unknown under the confirmed-free-only execution role')
    elif fees:
        result['status'] = 'documented_free'
    elif mode == 'legacy_unchecked':
        result['status'] = 'unchecked'
        result['warnings'].append('Legacy compatibility only: no matching service/route fee qualification; admission is not confirmed.')
    else:
        raise ValueError('Preparation admission: missing matching service/route fee qualification; hold for preparation review')
    result['effective_fee_policy'] = fee_policy
    return result
