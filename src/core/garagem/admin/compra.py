...
from garagem.models import Compra

@admin.register(Compra)
class Compra(admin.ModelAdmin):
    list_display = ("usuario", "status")
    ordering = ("-id",)
    list_per_page = 25