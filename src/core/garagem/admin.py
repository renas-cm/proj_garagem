from django.contrib import admin
from .models import Acessorio, Cor, Modelo, Veiculo

admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Modelo)
admin.site.register(Veiculo)