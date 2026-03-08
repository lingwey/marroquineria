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
            login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('catalogo:catalogo_productos')
    else:
        form= RegistroUsuario()
    return render(request, 'usuario/registro_usuario.html', {'form':form})

def login_view(request):
    if request.method == 'POST': 
        
        form = LoguinForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('catalogo:catalogo_productos')
        else:
           messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoguinForm()
    
    return render(request, 'usuario/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'usuario deslogueado correctamente')
    return redirect('catalogo:catalogo_productos')
