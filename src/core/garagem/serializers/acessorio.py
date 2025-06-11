from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.garagem.models import Acessorio 

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = '__all__'