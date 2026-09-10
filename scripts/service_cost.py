"""Shared service charge validation; facts remain the independent reviewer's responsibility."""
import json
import math
import sys
from pathlib import Path

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
    if not number_or_unknown(amount):
        raise ValueError('Invalid service amount')
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
        if not number_or_unknown(total):
            raise ValueError('Service charge overflow')
        if amount is not None and not math.isclose(amount, total, rel_tol=1e-12, abs_tol=0):
            raise ValueError('Service charge does not match usage times price')
        amount = total
    elif kind == 'confirmed_free':
        applicability = detail.get('applicability')
        if not isinstance(applicability, dict) or any(
                not isinstance(applicability.get(k), str) or not applicability[k].strip()
                for k in ('rule', 'observed', 'evidence')):
            raise ValueError('Confirmed free needs applicability: rule, observed, evidence')
        if amount not in (None, 0):
            raise ValueError('Confirmed free service charge must be zero')
        amount = 0
    elif kind == 'unknown':
        if amount is not None:
            raise ValueError('Unknown service charge cannot contain a known amount')
    elif amount is None:
        raise ValueError('Reported service charge needs an amount')
    return amount, {**detail, 'amount_usd': amount, 'sources': sources}



if __name__ == '__main__':
    try:
        amount, detail = service_charge(json.loads(Path(sys.argv[1]).read_text()))
        print(json.dumps({'service_cost_usd': amount, 'service_cost': detail}, ensure_ascii=False))
    except (ValueError, TypeError, KeyError, OSError) as error:
        raise SystemExit(f'Service cost rejected: {error}')
