from rest_framwork.viewsets import ModelViewset
from core.garagem.models import Veiculo
from core.garagem.serializers import VeiculoSerializer

class VeiculoViewSet(ModelViewset):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer