from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistroUsuario, LoguinForm
from django.contrib import messages

def registro_usurio(request):
    if request.method == 'POST':
        form= RegistroUsuario(request.POST)
        if form.is_valid():
            usuario= form.save()
            messages.success(request, 'usurio registrado correctamente')
            return redirect('catalogo:catalogo/catalogo.html')
    else:
        form= RegistroUsuario()
    return render(request, 'registro.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoguinForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.get_user()
            login(request, usuario)
            messages.success(request, 'usuario logueado correctamente')
            return redirect('catalogo:catalogo_productos')
        else:
            messages.error(request, 'usuario o contraseña incorrectos')
    else:
        form= LoguinForm()
    return render (request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'usuario deslogueado correctamente')
    return redirect('catalogo:catalogo_productos')
