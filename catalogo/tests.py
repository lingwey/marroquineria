from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Categoria

class CategoriaTests(APITestCase):
    def test_crear_categoria_y_generar_slug(self):
        """Verifica que se cree una categoría y el slug sea automático"""
        url = reverse('catalogo:categoria-list') # Ajusta si tu router es diferente
        data = {'nombre': 'Electrónica'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categoria.objects.count(), 1)
        self.assertEqual(Categoria.objects.get().slug, 'electronica')

    def test_listar_categorias(self):
        """Verifica que el GET devuelva las categorías existentes"""
        Categoria.objects.create(nombre="Ropa", slug="ropa")
        url = reverse('catalogo:categoria-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)