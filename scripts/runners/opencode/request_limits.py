"""Controller-owned bounds checked before forwarding a paid model request."""
import threading
import time


class RequestLimits:
    def __init__(self, model=None, max_requests=None, deadline=None, used=0, max_output_tokens=None):
        if max_requests is not None and (type(max_requests) is not int or max_requests <= 0):
            raise ValueError('max_requests must be a positive integer')
        self.model, self.max_requests, self.deadline = model, max_requests, deadline
        self.used = used
        self.max_output_tokens = max_output_tokens
        self.lock = threading.Lock()

    def reserve(self, payload, now=None):
        with self.lock:
            if not isinstance(payload, dict) or (self.model and payload.get('model') != self.model):
                raise ValueError('Request model differs from frozen model')
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
            return self.used
