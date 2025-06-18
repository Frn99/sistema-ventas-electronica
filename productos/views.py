# Contenido completo para productos/views.py

from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Este endpoint de API permite que las categorías sean vistas.
    """
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Este endpoint de API permite que los productos sean vistos.
    """
    queryset = Producto.objects.all().order_by('-fecha_creacion')
    serializer_class = ProductoSerializer