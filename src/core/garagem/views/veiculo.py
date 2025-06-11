from rest_framework.viewsets import ModelViewSet
from core.garagem.models import Veiculo
from core.garagem.serializers.veiculo import VeiculoSerializer, VeiculoListSerializer, VeiculoDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["modelo", "ano", "preco"]
    ordering_fields = ["modelo", "preco"]
    search_fields = ["modelo",]

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer