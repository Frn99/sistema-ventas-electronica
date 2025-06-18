# Contenido completo para productos/admin.py

from django.contrib import admin
from .models import Categoria, Producto

# Clase para mejorar la visualización de Categoria en el admin
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

# Clase para mejorar la visualización de Producto en el admin
class ProductoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de productos
    list_display = ('id', 'nombre', 'categoria', 'precio', 'stock', 'fecha_creacion')

    # Filtros que aparecerán a la derecha para buscar productos
    list_filter = ('categoria', 'fecha_creacion')

    # Campos por los que se puede buscar directamente
    search_fields = ('nombre', 'descripcion', 'categoria__nombre')

    # Orden por defecto de los productos (los más nuevos primero)
    ordering = ('-fecha_creacion',)

# Registrar los modelos con sus clases de personalización
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)