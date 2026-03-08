from django.urls import path
from .views import *

app_name= 'carrito'
urlpatterns = [
    path("", ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', agrear_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar/', limpiar_carrito, name='limpiar_carrito'),
]
