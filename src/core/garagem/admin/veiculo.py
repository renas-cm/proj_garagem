from django.contrib import admin
from core.garagem.models import Veiculo
from core.garagem.models import Compra, ItensCompra

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'cor', 'ano', 'preco',)
    search_fields = ('modelo', 'cor', 'preco', 'ano',)
    list_filter = ('modelo', 'preco', 'cor',)
    ordering = ('modelo', 'preco', 'ano',)
    list_per_page = 25
    
class ItensCompraInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]