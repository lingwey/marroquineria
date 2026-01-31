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
    query=request.GET.get('q','')
    categoria_id= request.GET.get('categoria', '')
    
    filtro = Producto.objects.filter(Q(nombre__icontains=query)| 
    Q(descripcion__icontains=query))
    
    if query:
        productos=filtro
    
    if categoria_id:
        productos=productos.filter(categoria_id=categoria_id)
    
    paginator = Paginator(productos,6)
    page_number= request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    return render(request, 'catalogo/catalogo.html', {'productos':productos, 'categorias': categorias,
    'query':query, 'page_obj':page_obj, 'categoria_seleccionada': categoria_id
    })

