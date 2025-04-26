from rest_framework.viewsets import ModelViewSet
from core.garagem.models import Acessorio
from core.garagem.serializers import AcessorioSerializer

class AcessorioViewSet(ModelViewSet): 
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer