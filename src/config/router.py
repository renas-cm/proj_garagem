from core.garagem import views
from core.usuario.views import UsuarioViewSet
from core.usuario.router import router as usuario_router
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router = DefaultRouter()
router.register(r'acessorios', views.AcessorioViewSet)
router.register(r'cores', views.CorViewSet)
router.register(r'modelos', views.ModeloViewSet)
router.register(r'veiculos', views.VeiculoViewSet)

router.register(r'usuarios', UsuarioViewSet, basename='usuario')
