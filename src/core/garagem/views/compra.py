from rest_framework.viewsets import  ModelViewSet

from core.garagem.models import Compra 
from core.garagem.serializers import CompraSerializer, CriarEditarCompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer  
    filterset_fields = ["usuario", "status", "data"]
    ordering_fields = ["usuario", "status", "data"]
    
    def get_queryset(self):
        usuario = self.request.user
        
        if usuario.tipo == Usuario.Tipos.GERENTE:
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
            
    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
