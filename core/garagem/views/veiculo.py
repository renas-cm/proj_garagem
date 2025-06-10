from rest_framework.viewsets import ModelViewSet
from core.garagem.models import Veiculo
from core.garagem.serializers.veiculo import VeiculoSerializer, VeiculoListSerializer, VeiculoDetailSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer