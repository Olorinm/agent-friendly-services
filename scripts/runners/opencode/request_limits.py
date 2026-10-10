"""Controller-owned bounds checked before forwarding a paid model request."""
import threading
import time
import math


class RequestLimits:
    def __init__(self, model=None, max_requests=None, deadline=None, used=0, max_output_tokens=None,
                 started_at=None, closure_fraction=0.85, warning_callback=None, warned=False):
        if max_requests is not None and (type(max_requests) is not int or max_requests <= 0):
            raise ValueError('max_requests must be a positive integer')
        self.model, self.max_requests, self.deadline = model, max_requests, deadline
        self.used = used
        self.max_output_tokens = max_output_tokens
        if not 0 < closure_fraction < 1:
            raise ValueError('closure_fraction must be between zero and one')
        self.started_at = time.time() if started_at is None else started_at
        self.closure_fraction, self.warning_callback, self.warned = closure_fraction, warning_callback, warned
        self.lock = threading.Lock()

    def reserve(self, payload, now=None):
        with self.lock:
            if not isinstance(payload, dict) or (self.model and payload.get('model') != self.model):
                raise ValueError('Request model differs from frozen model')
            if type(payload.get('n', 1)) is not int or payload.get('n', 1) != 1:
                raise ValueError('Only one completion per reserved model request is allowed')
            if self.max_output_tokens is not None:
                for field in ('max_tokens', 'max_completion_tokens'):
                    value=payload.get(field,self.max_output_tokens)
                    if type(value) is not int or not 0 < value <= self.max_output_tokens:
                        raise ValueError('Output token limit exceeds controller bound')
                payload.setdefault('max_tokens',self.max_output_tokens)
            if self.deadline is not None and (time.time() if now is None else now) >= self.deadline:
                raise ValueError('Controller deadline reached')
            if self.max_requests is not None and self.used >= self.max_requests:
                raise ValueError('Model request budget exhausted')
            self.used += 1
            clock = time.time() if now is None else now
            request_close = self.max_requests is not None and self.used >= math.ceil(self.max_requests * self.closure_fraction)
            time_close = self.deadline is not None and clock >= self.started_at + (self.deadline - self.started_at) * self.closure_fraction
            if not self.warned and (request_close or time_close):
                warning = {'time': clock, 'request_sequence': self.used,
                           'remaining_requests': None if self.max_requests is None else self.max_requests - self.used,
                           'remaining_seconds': None if self.deadline is None else max(0, self.deadline - clock)}
                message = ('Controller budget reminder: the run is in its final budget portion. '
                           'Save required deliverables and provide the final response now; avoid optional exploration. '
                           f'Remaining requests after this request: {warning["remaining_requests"]}; '
                           f'remaining seconds at dispatch: {warning["remaining_seconds"]}. '
                           'Report unfinished requirements honestly. This reminder changes no task requirement.')
                messages = payload.setdefault('messages', [])
                if not isinstance(messages, list):
                    self.used -= 1
                    raise ValueError('Request messages must be a list')
                if messages and isinstance(messages[0], dict) and messages[0].get('role') == 'system' and isinstance(messages[0].get('content'), str):
                    messages[0] = {**messages[0], 'content': messages[0]['content'] + '\n\n' + message}
                else:
                    messages.insert(0, {'role': 'system', 'content': message})
                if self.warning_callback: self.warning_callback(warning)
                self.warned = True
            return self.used
