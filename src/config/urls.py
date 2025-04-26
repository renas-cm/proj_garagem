from django.contrib import admin
from django.urls import path,include 

from rest_framework.routers import DefaultRouter

from core.garagem import views
from core.garagem import models

router = DefaultRouter()
router.register(r'acessorios', views.AcessorioViewSet)
router.register(r'cor', views.CorViewSet)
router.register(r'modelos', views.ModeloViewSet)
router.register(r'veiculos', views.VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
