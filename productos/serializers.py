# Contenido completo para productos/serializers.py

from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']


class ProductoSerializer(serializers.ModelSerializer):
    # Para que en la API la categoría se muestre con su nombre y no con su ID,
    # usamos StringRelatedField. Es de solo lectura.
    categoria = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id', 
            'nombre', 
            'descripcion', 
            'precio', 
            'stock', 
            'categoria', # Esto mostrará el nombre de la categoría
            'fecha_creacion'
        ]