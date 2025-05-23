from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.garagem.models import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'