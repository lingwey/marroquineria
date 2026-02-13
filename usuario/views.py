from django.http import JsonResponse
from django.contrib.auth import login
from google.oauth2 import id_token
from google.auth.transport import requests
from .models import Usuario

GOOGLE_CLIENT_ID = "TU_CLIENT_ID_DE_GOOGLE.apps.googleusercontent.com"

def google_login_view(request):
    # 1. Obtenemos el token que el front-end nos manda
    token = request.POST.get('id_token') 
    
    try:
        # 2. Verificamos con Google si el token es real
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        
        # 3. Buscamos al usuario o lo creamos si es su primera vez
        user, created = Usuario.objects.get_or_create(
            google_id=idinfo['sub'],
            defaults={
                'email': idinfo['email'],
                'nombre': idinfo.get('name', ''),
            }
        )
        
        # 4. Iniciamos la sesión en Django
        login(request, user)
        
        return JsonResponse({"status": "ok", "nuevo_usuario": created})
        
    except ValueError:
        return JsonResponse({"status": "error", "message": "Token inválido"}, status=400)
