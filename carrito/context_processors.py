from .models import Carrito

def carrito_context(request):
    # Si el usuario no está logueado, devolvemos un diccionario vacío o None
    if not request.user.is_authenticated:
        return {'carrito_global': None}

    # Si está logueado, creamos/obtenemos el carrito
    # Usamos 'carrito_global' para que coincida con tu HTML
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    
    return {
        'carrito_global': carrito
    }