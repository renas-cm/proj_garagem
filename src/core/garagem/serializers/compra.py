from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from core.garagem.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ["Veiculo", "quantidade"]
        depth = 2
        total = SerializerMethodField()

    def get_total(self, instance):
        return instance.quantidade * instance.veiculo.preco

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)  
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    data = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "data", "itens")
        
    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance
    
class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("veiculo", "quantidade")

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                item["preco_item"] = item["livro"].preco # Coloca o preço do livro no item de compra
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance
    
class CriarEditarCompraSerializer(ModelSerializer):
    itens = ItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")


    

