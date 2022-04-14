import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from m7_python.models import Inmueble, Region, Comuna

def get_list_inmuebles(name: str = '', description: str = '') -> list:
    lista_inmuebles = Inmueble.objects.filter(name__contains = name).filter(description__contains = description)

    file1 = open('inmuebles.txt', 'w', encoding = 'utf-8')
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

# Consultas usando Django

def get_list_inmuebles_comuna(comuna: str) -> list:
    comuna_obj = Comuna.objects.get(municipality__contains = comuna)
    
    lista_inmuebles = Inmueble.objects.filter(comuna_id = comuna_obj.id)
    file1 = open('inmuebles_por_comuna.txt', 'w', encoding = 'utf-8')
    file1.write(f"En la comuna de {comuna_obj.municipality} existen las siguientes ofertas:\n\n")
    
    for inmueble in lista_inmuebles:
        file1.write(f"- {inmueble.name}.\n")
    file1.close()

    return lista_inmuebles

def get_list_inmuebles_region(region: str) -> list:
    region_obj = Region.objects.get(region__contains = region)
    
    lista_inmuebles = Inmueble.objects.filter(region_id = region_obj.id)
    file1 = open('inmuebles_por_region.txt', 'w', encoding = 'utf-8')
    file1.write(f"En la {region_obj.region} existen las siguientes ofertas:\n\n")
    
    for inmueble in lista_inmuebles:
        file1.write(f"- {inmueble.name}.\n")
    file1.close()

    return lista_inmuebles

# Consultas usando SQL.

def get_list_inmueble_by_comuna(comuna: str) -> list:
    query = f"""SELECT inmueble.id, inmueble.name, inmueble.description
    FROM m7_python_inmueble AS inmueble
    INNER JOIN m7_python_comuna AS comuna
    ON inmueble.comuna_id = comuna.id
    WHERE comuna.municipality LIKE '%%{str(comuna)}%%'
    """
    results = Inmueble.objects.raw(query)
    
    file1 = open('datos_por_comuna.txt', 'w', encoding = 'utf-8')
    for inmueble in results:
        file1.write(f"{inmueble.name}:\n\t{inmueble.description}.\n")
    file1.close()

    return results

def get_list_inmueble_by_region(region: str) -> list:
    query = f"""SELECT inmueble.id, inmueble.name, inmueble.description
    FROM m7_python_inmueble AS inmueble
    INNER JOIN m7_python_region AS region
    ON inmueble.region_id = region.id
    WHERE region.region LIKE '%%{str(region)}%%'
    """
    results = Inmueble.objects.raw(query)
    
    file1 = open('datos_por_region.txt', 'w', encoding = 'utf-8')
    for inmueble in results:
        file1.write(f"{inmueble.name}:\n\t{inmueble.description}.\n")
    file1.close()

    return results