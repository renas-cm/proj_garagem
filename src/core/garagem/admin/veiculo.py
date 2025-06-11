from django.contrib import admin
from core.garagem.models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'cor', 'ano', 'preco',)
    search_fields = ('modelo', 'cor', 'preco', 'ano',)
    list_filter = ('modelo', 'preco', 'cor',)
    ordering = ('modelo', 'preco', 'ano',)
    list_per_page = 25