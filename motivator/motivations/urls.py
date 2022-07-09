from django.urls import path
from .views import MotivationView, list, random_motivation


urlpatterns = [
    path('motivations/create', MotivationView.as_view(), name='motivations'),
    path('motivations/', list, name='main'),
    path('', random_motivation, name='home'),
]
