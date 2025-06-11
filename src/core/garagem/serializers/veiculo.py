from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.uploader.models import Image
from core.uploader.serializers import ImageSerializer
from core.garagem.models import Veiculo

class ImageVeiculoSerializer(ModelSerializer):
    capa_attchment_key = SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attchment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1
        capa = ImageSerializer(required=False)
        
class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'modelo', 'preco']
        
    