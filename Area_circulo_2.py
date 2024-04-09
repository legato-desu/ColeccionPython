# Area de un circulo
"""
Crea un programa que pide al usuario el radio de un
circulo y se muestra su area
"""

# Importar la libreria matemarica para obtener PI

from math import pi

r = float(input('Ingrese el Radio del circulo: '))

# Utilizamos la variable "z" para guardar el valor dado por el usuario y realizar a continuacion la operacion del area del circulo

area = pi * r ** 2

print('El area del circulo es {}'.format(area))