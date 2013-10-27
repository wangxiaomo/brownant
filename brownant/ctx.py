from __future__ import absolute_import

import sys

from .globals import _app_ctx_stack


class AppContext(object):

    def __init__(self, app):
        self.app = app
        self._refcnt = 0

    def push(self):
        self._refcnt += 1
        _app_ctx_stack.push(self)

    def pop(self, exc=None):
        self._refcnt -= 1
        if self._refcnt <= 0:
            if exc is None:
                exc = sys.exc_info()[1]
        rv = _app_ctx_stack.pop()
        assert rv is self, 'Popped wrong app context. (%r instead of %r)' \
            % (rv, self)

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.pop(exc_value)


def has_app_context():
    return _app_ctx_stack.top is not None
