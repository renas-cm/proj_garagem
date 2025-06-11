from django.contrib import admin
from core.garagem.models import Cor

@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)