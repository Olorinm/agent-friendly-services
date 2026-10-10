"""Bounded, unauthenticated transport checks inside the execution container.

No signup, mutation, redirects, model calls or response bodies are collected.
A blocked check is an operational hold, never a service capability verdict.
"""
import http.client
import json
import signal
import socket
import ssl
import sys
import time
from urllib.parse import urlsplit


def validate(plan):
    if not isinstance(plan, list) or not 1 <= len(plan) <= 3:
        raise ValueError('Preflight needs one to three read-only targets')
    for target in plan:
        url = urlsplit(target['url'])
        if url.scheme != 'https' or not url.hostname or url.username or url.password or url.fragment:
            raise ValueError('Preflight target must be HTTPS without credentials or fragment')
        if target.get('method', 'GET') not in ('GET', 'HEAD'):
            raise ValueError('Preflight permits GET/HEAD only')
        statuses = target.get('accepted_statuses', [200])
        if not isinstance(statuses, list) or not statuses or any(type(s) is not int or not 100 <= s <= 599 for s in statuses):
            raise ValueError('Preflight accepted_statuses must be explicit HTTP codes')
    return plan


def check(plan, resolve=socket.getaddrinfo, connect=http.client.HTTPSConnection):
    validate(plan)
    rows = []
    for target in plan:
        url = urlsplit(target['url'])
        row = {'url': target['url'], 'method': target.get('method', 'GET'), 'passed': False}
        started = time.monotonic()
        conn = None
        try:
            row['addresses'] = sorted({a[4][0] for a in resolve(url.hostname, url.port or 443, type=socket.SOCK_STREAM)})
            conn = connect(url.hostname, url.port or 443, timeout=5, context=ssl.create_default_context())
            conn.request(row['method'], (url.path or '/') + ('?' + url.query if url.query else ''),
                         headers={'User-Agent': 'agent-friendly-services-preflight/1'})
            response = conn.getresponse()
            row.update(http_status=response.status, passed=response.status in target.get('accepted_statuses', [200]))
            if not row['passed']:
                row['reason'] = 'Unexpected HTTP status; authentication, policy, origin and network cause remain unresolved'
        except (OSError, http.client.HTTPException) as error:
            row['reason'] = type(error).__name__
        finally:
            if conn: conn.close()
            row['seconds'] = round(time.monotonic() - started, 4)
            rows.append(row)
    return {'schema_version': 1, 'ready': all(r['passed'] for r in rows), 'checks': rows,
            'scope': 'Transport/authentication surface only; no service capability or signup verdict'}


if __name__ == '__main__':
    # DNS resolution also needs a process-level bound, not just socket timeouts.
    signal.alarm(18)
    print(json.dumps(check(json.loads(sys.argv[1]))))
