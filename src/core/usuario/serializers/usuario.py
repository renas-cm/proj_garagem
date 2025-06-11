from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.usuario.models import Usuario

from ..models import Usuario
from core.uploader.models import Image
from core.uploader.serializers import ImageSerializer

class UsuarioSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Usuario
        fields = "__all__"