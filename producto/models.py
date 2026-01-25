from django.db import models

class Producto (models.Model):
    nombre= models.CharField(max_length=200)
    descripcion= models.TextField(max_length=1000)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
        
class ProductoImagenes(models.Model):
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/galeria')
    alt_text= models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"imagen de {self.producto.nombre}"