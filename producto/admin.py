from django.contrib import admin
from .models import Producto, ProductoImagenes

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre', 'precio', 'categoria', 'stock', 'descripcion', 'slug')
    
@admin.register(ProductoImagenes)
class ProductoImangenesAdmin(admin.ModelAdmin):
    list_display=('producto', 'imagen', 'alt_text')