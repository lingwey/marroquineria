from django.urls import path
from .views import google_login_view

app_name = 'usuario'

urlpatterns = [
    path('login', google_login_view, name='login'),
]
