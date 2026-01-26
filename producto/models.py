from django.db import models
from django.utils.text import slugify

class Producto (models.Model):
    nombre= models.CharField(max_length=200)
    descripcion= models.TextField(max_length=1000)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=True)
    slug= models.SlugField(unique=True, blank=True)
    
    categoria=models.ForeignKey('catalogo.Categoria', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='productos')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base= slugify(self.nombre)
            slug= slug_base
            contador = 1
            while Producto.objects.filter(slug=slug).exists():
                slug= f"{slug_base}-{contador}"
                contador +=1
            self.slug=slug
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
        
class ProductoImagenes(models.Model):
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/galeria')
    alt_text= models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"imagen de {self.producto.nombre}"