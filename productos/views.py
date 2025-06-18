# Contenido completo y actualizado para productos/views.py

from rest_framework import viewsets, permissions
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

# ¡Cambio clave aquí! Usamos ModelViewSet para habilitar todas las operaciones CRUD.
class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Este endpoint de API permite que las categorías sean vistas o editadas.
    """
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer
    # Añadimos la clase de permiso: solo los autenticados pueden escribir.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ¡Y cambio clave aquí también!
class ProductoViewSet(viewsets.ModelViewSet):
    """
    Este endpoint de API permite que los productos sean vistos o editados.
    """
    queryset = Producto.objects.all().order_by('-fecha_creacion')
    serializer_class = ProductoSerializer
    # Añadimos la clase de permiso: solo los autenticados pueden escribir.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]