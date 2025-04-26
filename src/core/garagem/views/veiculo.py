from rest_framework.viewsets import ModelViewSet
from core.garagem.models import Veiculo
from core.garagem.serializers import VeiculoSerializer 

class VeiculoViewSet(ModelViewSet): 
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer