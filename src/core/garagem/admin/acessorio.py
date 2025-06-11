from django.contrib import admin
from core.garagem.models import Acessorio

@admin.register(Acessorio)
class AcessorioAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)
    
