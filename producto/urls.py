from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name='producto'
router=DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')

urlpatterns = [
    path('', include(router.urls)),
]
