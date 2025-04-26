from rest_framework import serializers
from rest_framework.seriallizers import ModelSerializer
from core.garagem.models import Cor

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = '__all__'
    