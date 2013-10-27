from werkzeug.local import LocalStack, LocalProxy


def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError('working outside of application context')
    return top.app


_app_ctx_stack = LocalStack()
current_app = LocalProxy(_find_app)
