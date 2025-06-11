from django.contrib import admin
from core.garagem.models import Modelo

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'categoria')
    search_fields = ('nome', 'marca', 'categoria')
    list_filter = ('marca', 'categoria')
    ordering = ('nome', 'marca')