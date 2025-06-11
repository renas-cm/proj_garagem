from rest_framework.viewsets import ModelViewSet

from ..models import Usuario
from core.usuario.serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
