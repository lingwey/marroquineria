from django.urls import path, include
from .views import CategoriaViewSet, catalogo_productos
from rest_framework.routers import DefaultRouter

app_name= 'catalogo'
router=DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')

urlpatterns = [
    path('productos-catalogo/', catalogo_productos, name='catalogo_productos'),
    path('', include(router.urls)),
]
