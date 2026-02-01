from django.shortcuts import render, get_object_or_404

from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets

class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.all()
    serializer_class= ProductoSerializer
    parser_classes= (MultiPartParser, FormParser)

def detalles_producto(request, pk):
    producto= get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/producto_detalles.html', {'producto':producto})
