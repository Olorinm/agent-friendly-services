"""Non-secret provenance for explicitly registered credentials, never authentication.

Only bounded NumericDate values and a fixed permission vocabulary are retained.
No subject, issuer, audience, URL, resource name, arbitrary scope, or JWT bytes
are copied. These facts remain private grading material.
"""
import base64
import hashlib
import json
import re


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError('Ambiguous duplicate JSON member')
        value[key] = item
    return value


def decoded_facts(value):
    """Decode a registered JWT; make no signature, validity or usage assertion."""
    if len(value) > 32768:
        return None
    parts = value.split('.')
    if len(parts) != 3 or any(not re.fullmatch(r'[A-Za-z0-9_-]+', p) for p in parts):
        return None
    try:
        def decode(part):
            return json.loads(base64.b64decode(part + '=' * (-len(part) % 4),
                                             altchars=b'-_', validate=True),
                              object_pairs_hook=unique_object)
        header, payload = decode(parts[0]), decode(parts[1])
        if not isinstance(header, dict) or not isinstance(payload, dict):
            return None
    except (ValueError, UnicodeError, RecursionError):
        return None
    dates = {name: payload[name] for name in ('iat', 'exp', 'nbf')
             if type(payload.get(name)) is int and 0 <= payload[name] <= 253402300799}
    permission = {'r': 'read-only', 'rw': 'read-write'}.get(payload.get('a')) if isinstance(payload.get('a'), str) else None
    if not dates and permission is None:
        return None
    result = {'credential_sha256': hashlib.sha256(value.encode()).hexdigest(),
              'decoded_numeric_dates': dates, 'signature_verified': False,
              'validity_verified': False, 'actual_use_verified': False}
    if permission is not None:
        result['unverified_permission_hint'] = {
            'claim': 'a', 'declared_value': payload['a'],
            'turso_format_interpretation': permission,
            'notice': 'Only a hint for the documented Turso credential format; '
                      'vendor format and actual granted permissions require separate evidence.'}
    return result


def document(secrets):
    rows = {row['credential_sha256']: row for value in secrets
            if (row := decoded_facts(value)) is not None}
    if not rows:
        return None
    return {'schema_version': 1,
            'notice': 'Controller-derived private facts from explicitly registered credential bytes. '
                      'The source credential SHA is linked to redacted source files by privacy-redactions.json. '
                      'An absent source link proves registration only, not actual use. '
                      'Payload decoding does not verify a signature, current validity, authorization, '
                      'actual transport, document access, service fee or task completion. '
                      'Do not publish this file or its copies.',
            'credentials': [rows[key] for key in sorted(rows)]}
