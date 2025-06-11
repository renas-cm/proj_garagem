from django.contrib import admin

from .models import Document, Image

admin.site.register(Image)
admin.site.register(Document)
