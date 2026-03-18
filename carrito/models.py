from django.db import models
from usuario.models import Usuario
from producto.models import Producto

class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='carrito')
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"carrido del usuario {self.usuario.email}"
    
    def total_items(self):
        return sum(item.cantidad for item in self.items.all())
    @property
    def total_precio(self):
        return sum(item.subtotal for item in self.items.all())
    
class ItemCarrito(models.Model):
    carrito=models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad= models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together= ('carrito', 'producto')
    
    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
    @property
    def subtotal(self):
        return self.producto.precio  * self.cantidad
    
    
