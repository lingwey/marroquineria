from django.urls import path, include
from .views import CategoriaViewSet
from rest_framework.routers import DefaultRouter

app_name= 'catalogo'
router=DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')

urlpatterns = [
    path('', include(router.urls))
]
