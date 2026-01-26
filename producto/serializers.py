from rest_framework import serializers
from .models import Producto, ProductoImagenes
from catalogo.serializers import CategoriaSerializer
from catalogo.models import Categoria


class ProductoImagenesSerializers(serializers.ModelSerializer):
    class Meta:
        models=ProductoImagenes
        fields=['id', 'producto', 'imagen', 'alt_text']

class ProductoSerializer(serializers.ModelSerializer):
    imagenes= ProductoImagenesSerializers(many=True, read_only=True)
    categoria= CategoriaSerializer(read_only=True)
    
    categoria_id= serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        source='categoria',
        write_only=True,
    )
    
    subir_imagenes= serializers.ListField(
        child= serializers.ImageField(max_length=10000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    
    class Meta:
        models=Producto
        fields=['id', 'nombre', 'descripcion', 'precio', 'stock', 'imagenes', 'categoria','categoria_id','slug']
    
    def create (self, validated_data):
        imagenes_data = validated_data.pop('subir_imagenes', [])
        producto= Producto.objects.create(**validated_data)
        for imagen in imagenes_data:
            ProductoImagenes.objects.create(producto=producto, imagen=imagen)
        return producto    