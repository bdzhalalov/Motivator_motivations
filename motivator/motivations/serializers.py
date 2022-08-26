from .models import Motivation
from rest_framework.serializers import ModelSerializer


class MotivationSerializer(ModelSerializer):
    class Meta:

        model = Motivation
        fields = ('id', 'nickname', 'motivation')

class AddMotivationSerializer(ModelSerializer):
    class Meta:

        model = Motivation
        fields = ('nickname', 'motivation')
