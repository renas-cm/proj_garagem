from rest_framework.viewsets import ModelViewSet
from core.garagem.models import Cor
from core.garagem.serializers import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer