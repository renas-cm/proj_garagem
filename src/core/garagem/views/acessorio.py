from rest_framework.viewsets import ModelViewSet
from core.garagem.models import Acessorio
from core.garagem.serializers import AcessorioSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AcessorioViewSet(ModelViewSet): 
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer