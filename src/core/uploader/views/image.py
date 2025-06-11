from core.uploader.models import Image
from core.uploader.serializers import ImageUploadSerializer
from core.uploader.views.create import CreateViewSet
from rest_framework import parsers


class ImageUploadViewSet(CreateViewSet):
    queryset = Image.objects.all() #  pylint: disable=no-member
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
