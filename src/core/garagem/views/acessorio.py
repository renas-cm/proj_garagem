from rest_framework.viewsets import ModelViewset
from core.garagem.models import Acessorio
from core.garagem.serializers import AcessorioSerializer

class VeiculoViewSet(ModelViewset):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer