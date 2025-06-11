from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.garagem.models import Modelo

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'
        