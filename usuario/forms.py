from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from  .models import Usuario

class RegistroUsuario(UserCreationForm):
    class Meta:
        model= Usuario
        fields= ['username', 'email' ,]

class LoguinForm(AuthenticationForm):
    # Forzamos los widgets para que coincidan con tu estilo y nombres
    username = forms.CharField(
        label="Nombre de usuario o Email", # Para que el usuario sepa qué poner
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'})
    )

    class Meta:
        model = Usuario