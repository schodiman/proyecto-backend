from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'perfiles', views.PerfilUsuarioViewSet)
router.register(r'publicaciones', views.PublicacionViewSet)
router.register(r'historiales', views.HistorialEstadoViewSet)
router.register(r'interacciones', views.InteraccionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),   
]    