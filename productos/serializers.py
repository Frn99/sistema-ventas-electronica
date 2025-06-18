# Contenido completo y actualizado para productos/serializers.py

from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']


class ProductoSerializer(serializers.ModelSerializer):
    # NOTA: Hemos vuelto al comportamiento por defecto para el campo 'categoria'.
    # Esto nos permite asignarle un producto a una categoría usando su ID
    # al momento de crear o actualizar, lo cual es necesario para la escritura.
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'categoria', # Ahora es un campo de escritura/lectura (funciona con el ID)
            'fecha_creacion'
        ]