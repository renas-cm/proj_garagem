from rest_framework.viewsets import ModelViewset
from core.garagem.models import Modelo
from core.garagem.serializers import ModeloSerializer

class VeiculoViewSet(ModelViewset):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer