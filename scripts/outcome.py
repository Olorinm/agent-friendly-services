"""Validate evidence-backed facets without replacing the user-task verdict."""
FACTORS = {'network', 'access', 'model_budget', 'agent_execution', 'test_constraint',
           'materials', 'service_capability', 'unknown'}


def validate(value):
    if not isinstance(value, dict): raise ValueError('New protocol requires an outcome object')
    if value.get('service_execution') not in ('completed', 'not_completed', 'not_observed', 'unknown'):
        raise ValueError('Invalid outcome.service_execution')
    if value.get('user_delivery') not in ('completed', 'not_completed', 'unknown'):
        raise ValueError('Invalid outcome.user_delivery')
    factors = value.get('blocking_factors')
    if not isinstance(factors, list) or any(not isinstance(f, str) or f not in FACTORS for f in factors) or len(set(factors)) != len(factors):
        raise ValueError('Invalid outcome.blocking_factors')
    if not isinstance(value.get('evidence'), str) or not value['evidence'].strip():
        raise ValueError('Outcome facets require concrete evidence')
    return value
