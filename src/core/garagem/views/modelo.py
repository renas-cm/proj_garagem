from rest_framework.viewsets import ModelViewSet
from core.garagem.models import Modelo
from core.garagem.serializers import ModeloSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer