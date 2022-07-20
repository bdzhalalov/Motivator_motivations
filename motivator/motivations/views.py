from .models import Motivation
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import MotivationSerializer, AddMotivationSerializer
from django.http import Http404
from rest_framework.response import Response

class MotivationListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5

class MotivationList(ListAPIView):
    serializer_class = MotivationSerializer
    queryset = Motivation.objects.all()
    pagination_class = MotivationListPagination

class MotivationListDetails(ListAPIView):
    serializer_class = MotivationSerializer

    def get_queryset(self):
        try:
            pk = self.kwargs['pk']
            queryset = Motivation.objects.get(id=pk)
            return Motivation.objects.filter(id=queryset.id)
        except Motivation.DoesNotExist:
            raise Http404('Motivation with this "id" does not found...')

        

class RandomMotivation(ListAPIView):
    queryset = Motivation.objects.all().order_by('?')[:1]
    serializer_class = MotivationSerializer


@permission_classes((AllowAny,))
class MotivationView(APIView):

    def post(self, request):
        serializer = AddMotivationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(nickname=request.user)
        return Response('Motivation successfully saved')

    
