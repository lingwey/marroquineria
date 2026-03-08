from .models import Carrito

def carrito_context(request):
    if request.user.is_auteticated:
        carrito, created= Carrito.objects.get_or_create(usuario=request.user)
        return{'carrito':carrito}
    return{'carrito_global':None}