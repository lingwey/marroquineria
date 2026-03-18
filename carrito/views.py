from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from producto.models import Producto
from .models import Carrito, ItemCarrito

@login_required
def agrear_al_carrito (request, producto_id):
    producto= get_object_or_404(Producto, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item, creado= ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        item.cantidad+=1
        item.save()
        messages.info(request, f"se aumento la cantidad de {producto.nombre} en el carrito")
    else:
        messages.info(request, f"prducto {producto.nombre} agregado")
    
    item.save()
    
    return redirect('producto:detalles_producto', pk=producto_id)

@login_required
def eliminar_del_carrito(request, producto_id):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item = carrito.items.filter(producto_id=producto_id).first()
    
    if item:
        if item.cantidad > 1:
            item.cantidad -= 1
            item.save()
            messages.info(request, f"Se quitó una unidad de {item.producto.nombre}")
        else:
            item.delete()
            messages.warning(request, f"Se eliminó {item.producto.nombre} del carrito")
    else:
        messages.error(request, "El producto no se encuentra en el carrito")
        
    return redirect('carrito:ver_carrito')

@login_required
def limpiar_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario= request.user)
    if carrito.items.exists():
        carrito.items.all().delete()
        messages.warning(request, f"carrito vaciado")
    else:
        messages.info(request, f"el carrito esta vacio")
    return redirect('carrito:ver_carrito')

@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario= request.user)
    items = carrito.items.select_related('producto')
    total = carrito.total_precio
    return render(request, 'carrito/ver_carrito.html', {'carrito':carrito, 'items':items, 'total':total})
    