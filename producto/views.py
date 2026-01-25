from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets

class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.all()
    serializer_class= ProductoSerializer
    parser_classes= (MultiPartParser, FormParser)
