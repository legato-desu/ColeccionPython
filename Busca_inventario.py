# Busqueda en inventario
"""
Crea un diccionario con unas frutas y sus cantidades
luego con el uso de "get" enseñar la cantidad de frutas
segun lo almacenado en el inventario 
"""

frutas = {
    "Peras":23,
    "Manzanas":50,
    "Sandias":7,
    "Melocotones":21,
    "Fresas":100,
    "Uvas":150,
}

busqueda = input("Introduce una fruta: ")
busqueda=str(busqueda)
busqueda = busqueda.capitalize()

numero = frutas.get(busqueda,0)

print(f"Hay {numero} {busqueda} en el inventario")