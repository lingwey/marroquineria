from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria
from .serializers import CategoriaSerializer
from producto.models import Producto
from django.core.paginator import Paginator
from django.db.models import Q

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset= Categoria.objects.all()
    serializer_class= CategoriaSerializer
    
def catalogo_productos(request):
    productos=Producto.objects.all().select_related('categoria').prefetch_related('imagenes').order_by('id')
    categorias= Categoria.objects.all().order_by('id')
    return render(request, 'catalogo/catalogo.html', {'productos':productos, 'categorias': categorias
    })

