from django.contrib.auth import login, logout, authenticate
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
            print("usuario creado")
            return redirect('catalogo:catalogo_productos')
    else:
        form= RegistroUsuario()
    return render(request, 'usuario/registro_usuario.html', {'form':form})

def login_view(request):
    print("--- INICIO DE DEBUG DE LOGIN ---")
    if request.method == 'POST':
        # 1. Ver qué está llegando del HTML
        print(f"POST Data: {request.POST}") 
        
        form = LoguinForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
            print(f"ÉXITO: Usuario {usuario.username} validado.")
            return redirect('catalogo:catalogo_productos')
        else:
            # 2. Ver por qué falló el formulario
            print(f"ERRORES DEL FORMULARIO: {form.errors.as_data()}")
            
            # 3. Prueba manual de fuego
            username_test = request.POST.get('username')
            password_test = request.POST.get('password')
            user_manual = authenticate(username=username_test, password=password_test)
            print(f"AUTENTICACIÓN MANUAL (Username): {user_manual}")
            
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoguinForm()
    
    return render(request, 'usuario/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'usuario deslogueado correctamente')
    return redirect('catalogo:catalogo_productos')
