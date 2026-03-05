from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups= models.ManyToManyField(
        Group,
        related_name='usuarios_set',
        blank=True,
        help_text='Grupos a los que pertenece este usaurio',
        verbose_name='grupos'
    )
    
    user_permissions= models.ManyToManyField(
        Permission,
        related_name='usuarios_user_set',
        blank=True,
        help_text='Permisos especificos para este usuario',
        verbose_name='permisos de usuario'
    )

    def __str__(self):
        return self.username
    
