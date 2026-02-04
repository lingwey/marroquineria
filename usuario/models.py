from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email= models.EmailField(unique=True)
    google_id= models.CharField(max_length=255, unique=True)
    nombre= models.CharField(max_length=255)
    
    is_active=models.BooleanField(default=True)
    fecha_regitro= models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['google_id', 'nombre']
    
    
    def __str__(self):
        return self.email

