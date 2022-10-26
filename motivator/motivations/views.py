import hashlib
from rest_framework.response import Response
from rest_framework_condition import etag
from .models import Motivation
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import MotivationSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
from rest_framework import status

class PagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'

def set_cache_key(request):
    etag = hashlib.sha256(bytes(int(request.GET.get('page')))).hexdigest()
    cache.set('etag'+str(request.GET.get('page')), etag)
    return etag
    

@permission_classes((AllowAny,))
class MotivationList(ModelViewSet):
    serializer_class = MotivationSerializer
    queryset = Motivation.objects.filter(is_visible=True)
    pagination_class = PagePagination

    

    @etag(set_cache_key)
    def list(self, request, *args, **kwargs):

        if cache.get('etag' + str(request.GET.get('page'))) == request.META.get('HTTP_IF_NONE_MATCH'):
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        else:
            queryset = self.filter_queryset(self.get_queryset())
            
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            
            return Response(serializer.data)
  

class RandomMotivation(ListAPIView):
    queryset = Motivation.objects.filter(is_visible=True).order_by('?')[:1]
    serializer_class = MotivationSerializer
