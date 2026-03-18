from django.contrib import admin
from .models import Carrito, ItemCarrito

class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0  # Para que no aparezcan filas vacías de más
    readonly_fields = ['subtotal_display']

    def subtotal_display(self, obj):
        return f"${obj.subtotal()}"
    subtotal_display.short_description = 'Subtotal'

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    # Columnas que ves en la lista principal
    list_display = ('usuario', 'creado', 'total_items_display', 'total_precio_display')
    
    # Esto agrega la tabla de productos adentro del carrito
    inlines = [ItemCarritoInline]
    
    # Para poder ver los totales en la vista de edición/detalle
    readonly_fields = ('creado', 'actualizado', 'total_items_display', 'total_precio_display')

    def total_items_display(self, obj):
        return obj.total_items()
    total_items_display.short_description = 'Items Totales'

    def total_precio_display(self, obj):
        return f"${obj.total_precio()}"
    total_precio_display.short_description = 'Precio Total'

@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'producto', 'cantidad', 'subtotal_display')
    list_filter = ('carrito__usuario',)

    def subtotal_display(self, obj):
        return f"${obj.subtotal()}"
    subtotal_display.short_description = 'Subtotal'