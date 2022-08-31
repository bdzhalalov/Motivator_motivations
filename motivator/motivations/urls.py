from django.urls import path
from .views import MotivationList, RandomMotivation
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'motivations', MotivationList)

urlpatterns = [
    path('motivations/random', RandomMotivation.as_view(), name='home'),
]

urlpatterns += router.urls
