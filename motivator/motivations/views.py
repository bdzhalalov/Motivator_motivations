from .models import Motivation
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import MotivationSerializer
from rest_framework.pagination import PageNumberPagination

class PagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'

@permission_classes((AllowAny,))
class MotivationList(ModelViewSet):
    serializer_class = MotivationSerializer
    queryset = Motivation.objects.filter(is_visible=True)
    pagination_class = PagePagination
        

class RandomMotivation(ListAPIView):
    queryset = Motivation.objects.filter(is_visible=True).order_by('?')[:1]
    serializer_class = MotivationSerializer
