class HtmxCsrfMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.headers.get('HX-Request') and not request.headers.get('X-CSRFToken'):
            from django.middleware.csrf import get_token
            request.META['CSRF_COOKIE'] = get_token(request)
        return self.get_response(request)