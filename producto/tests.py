from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Producto
from catalogo.models import Categoria
import io
from PIL import Image

def generate_photo_file():
    """Genera una imagen falsa para pruebas"""
    file = io.BytesIO()
    image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return SimpleUploadedFile(file.name, file.read(), content_type='image/png')

class ProductoTests(APITestCase):
    def setUp(self):
        # Necesitamos una categoría para asignar a los productos
        self.categoria = Categoria.objects.create(nombre="Comida", slug="comida")

    def test_crear_producto_con_imagenes_y_slug_unico(self):
        """Prueba creación, nesting de imágenes y slug incremental"""
        url = reverse('producto:producto-list')
        
        # Datos del producto
        p1_data = {
            'nombre': 'Pizza',
            'descripcion': 'Rica pizza',
            'precio': '1200.00',
            'categoria_id': self.categoria.id,
            'subir_imagenes': [generate_photo_file(), generate_photo_file()]
        }
        
        # --- PRIMER PRODUCTO ---
        response = self.client.post(url, p1_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.get(id=response.data['id']).slug, 'pizza')
        
        # --- SEGUNDO PRODUCTO (Mismo nombre, debe generar slug pizza-1) ---
        response2 = self.client.post(url, p1_data, format='multipart')
        
        # Si falla, imprimimos el error para saber qué pasó
        if response2.status_code != 201:
            print("\n--- ERROR EN SEGUNDA CREACIÓN ---")
            print(f"Status: {response2.status_code}")
            print(f"Data: {response2.data}")
            print("----------------------------------")

        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.get(id=response2.data['id']).slug, 'pizza-1')

    def test_producto_muestra_categoria_anidada(self):
        """Verifica que el GET devuelva el objeto categoría completo"""
        prod = Producto.objects.create(
            nombre="Hamburguesa", 
            precio=500, 
            categoria=self.categoria
        )
        url = reverse('producto:producto-detail', args=[prod.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verificamos que 'categoria' sea un diccionario con el nombre correcto
        self.assertEqual(response.data['categoria']['nombre'], 'Comida')