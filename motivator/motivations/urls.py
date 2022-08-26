from django.urls import path
from .views import MotivationView, MotivationList, MotivationListDetails , RandomMotivation


urlpatterns = [
    path('motivations/new', MotivationView.as_view(), name='motivations'),
    path('motivations/', MotivationList.as_view()),
    path('motivations/<int:pk>', MotivationListDetails.as_view()),
    path('motivations/random', RandomMotivation.as_view(), name='home'),
]
