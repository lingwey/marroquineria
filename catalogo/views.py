from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria
from .serializers import CategoriaSerializer
from producto.models import Producto

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset= Categoria.objects.all()
    serializer_class= CategoriaSerializer
    
def catalogo_productos(request):
    productos=Producto.objects.all().select_related('categoria').prefetch_related('imagenes')
    return render(request, 'catalogo/catalogo.html', {'productos':productos})

