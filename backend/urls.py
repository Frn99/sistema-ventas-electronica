# Contenido completo para backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from productos import views

# El router proporciona una forma fácil de determinar automáticamente la configuración de la URL.
router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet, basename='productos')

# Conecta nuestra API usando el enrutamiento automático de URL.
# Además, incluimos las URL de inicio de sesión para la API navegable.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]