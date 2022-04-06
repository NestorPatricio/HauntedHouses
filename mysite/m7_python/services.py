from m7_python.models import Inmueble

def insertar_inmueble(datos: list) -> None:
    """Create an Inmueble's instance."""
    description = datos[0]
    builded_sqm = datos[1]
    terrain_sqm = datos[2]
    parkings = datos[3]
    rooms = datos[4]
    bathrooms = datos[5]
    adress = datos[6]
    rent_price = datos[7]
    user = datos[8]
    tipo_inmueble = datos[9]
    comuna = datos[10]
    region = datos[11]

    Inmueble.objects.create(
        description = description,
        builded_sqm = builded_sqm,
        terrain_sqm = terrain_sqm,
        parkings = parkings,
        rooms = rooms,
        bathrooms = bathrooms,
        adress = adress,
        rent_price = rent_price,
        user = user,
        tipo_inmueble = tipo_inmueble,
        comuna = comuna,
        region = region,
        )

def obtener_un_inmueble(id_inmueble: int) -> object:
    """Get an Inmueble's instance."""
    return Inmueble.objects.get(pk = id_inmueble)

def obtener_todos_los_inmuebles() -> list:
    """Get all Inmueble's instances."""
    return Inmueble.objects.all()

def actualizar_descrip_inmueble(id_inmueble: int, nueva_descrip: str) -> None:
    """Update the description of an Inmueble's instance."""
    Inmueble.objects.filter(pk = id_inmueble).update(descripcion = nueva_descrip)

# La función anterior es equivalente a la siguiente forma:
#def actualizar_descrip_inmueble(id_inmueble: int, nueva_descrip: str) -> None:
    #inmueble = Inmueble.objects.get(pk = id_inmueble)
    #inmueble.descripcion = nueva_descrip
    #inmueble.save()

def actualizar_precio_inmueble(id_inmueble: int, nuevo_precio: str) -> None:
    """Update the price of an Inmueble's instance."""
    Inmueble.objects.filter(pk = id_inmueble).update(rent_price = nuevo_precio)

def eliminar_inmueble(id_inmueble: int) -> None:
    """Delete an Inmueble's instance."""
    Inmueble.objects.get(pk = id_inmueble).delete()