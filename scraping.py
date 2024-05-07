import requests
from bs4 import BeautifulSoup
import json

# Inicializar una lista para almacenar todos los productos
productos_totales = []

# URLs de interés
urls = [
    'https://www.ikea.com/es/es/search/?q=camas',
    'https://www.ikea.com/es/es/search/?q=colchon',
    'https://www.ikea.com/es/es/search/?q=mesita%20de%20noche',
    'https://www.ikea.com/es/es/search/?q=escritorio',
    'https://www.ikea.com/es/es/search/?q=sillas%20escritorio',
    'https://www.ikea.com/es/es/search/?q=armarios'
]
categorias = ['Cama', 'Colchón', 'Escritorio', 'Silla', 'Armario', 'Mesita de noche', 'Cómoda']

# Recorrer las URLs
for url in urls:
    headers = {
    "referer": url,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
      }
    response = requests.get(url,headers=headers)
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html5lib')
        productos = soup.find_all('div', class_='plp-fragment-wrapper')
        
        print(productos)
        for producto in productos:
            modelo = producto.find('span', class_='notranslate plp-price-module__product-name').text.strip()
            descripcion = producto.find('span', class_='plp-price-module__description').text.strip()
            precio = producto.find('span', class_='plp-price__sr-text').text.strip()
            print(modelo)
            print(descripcion)
            print(precio)
            # Inicializar el diccionario para almacenar los datos del producto
            producto_data = {}

            # Verificar la categoría del producto
            categoria_encontrada = False
            for categoria in categorias:
                if categoria.lower() in descripcion.lower():
                    # Almacenar los datos del producto en el diccionario
                    producto_data = {
                        'categoria': categoria,
                        'nombre': modelo,
                        'descripcion': descripcion,
                        'precio': precio
                    }
                    # Agregar el diccionario a la lista de productos
                    productos_totales.append(producto_data)
                    categoria_encontrada = True
                    break  # Salir del bucle una vez que se ha encontrado la categoría

            # Manejar el caso en que no se encuentre ninguna categoría
            if not categoria_encontrada:
                producto_data = {
                    'categoria': 'No categorizado',
                    'nombre': modelo,
                    'descripcion': descripcion,
                    'precio': precio
                }
                productos_totales.append(producto_data)
    else:
        print(f'Error al acceder a URL: {url}')
print(productos_totales)
# Guardar los datos en un archivo JSON
with open('productos_ikea.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(productos_totales, jsonfile, ensure_ascii=False, indent=4)
