from django.core.exceptions import PermissionDenied
from .settings import TOKEN, ALLOWED_HOSTS
from django.utils.deprecation import MiddlewareMixin

class CheckTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        hosts = request.META.get('HTTP_HOST')
        host = hosts[:9]
        if auth != TOKEN and host not in ALLOWED_HOSTS:
            raise PermissionDenied()

        return None
