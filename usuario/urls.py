from django.urls import path
from .views import *

app_name = 'usuario'

urlpatterns = [
    path('registro', registro_usurio, name='registro'),
    path('login', login_view , name='login'),
    path('logout', logout_view, name='logout'),
]
