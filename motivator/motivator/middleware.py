from django.core.exceptions import PermissionDenied
from .settings import API_KEY
from django.utils.deprecation import MiddlewareMixin

class CheckTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):
        check_api_key = request.META.get('HTTP_AUTHORIZATION')
        if check_api_key != API_KEY:
            raise PermissionDenied()

        return None
