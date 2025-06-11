from rest_framework import parsers

from ..models import Document
from ..serializers import DocumentUploadSerializer
from .create import CreateViewSet

class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all() #  pylint: disable=no-member
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

