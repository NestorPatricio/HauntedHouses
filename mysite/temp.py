import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from m7_python.models import Inmueble

def get_list_inmuebles(name: str = '', description: str = '') -> list:
    lista_inmuebles = Inmueble.objects.filter(name__contains = name).filter(description__contains = description)

    file1 = open('datos.txt', 'w', encoding = 'utf-8')
    for inmueble in lista_inmuebles:
        file1.write(f"""{inmueble.name}.
Descripción: {inmueble.description}.
Dirección: {inmueble.adress}, en la comuna de {inmueble.comuna.municipality}, {inmueble.region.region}.
Tipo de inmueble: {inmueble.tipo_inmueble.property_type}. Precio: ${inmueble.rent_price}.
Terreno de {inmueble.builded_sqm} metros cuadrados con {inmueble.terrain_sqm} metros cuadrados construidos.
Dormitorios: {inmueble.rooms}. Baños: {inmueble.bathrooms}. Estacionamientos: {inmueble.parkings}.
Aviso puesto por: {inmueble.user.first_name} {inmueble.user.last_name}.
\n""")
    file1.close()

    return lista_inmuebles
