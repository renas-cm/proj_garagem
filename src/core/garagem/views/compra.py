from rest_framework.viewsets import  ModelViewSet

from core.garagem.models import Compra 
from core.garagem.serializers import CompraSerializer 

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    
