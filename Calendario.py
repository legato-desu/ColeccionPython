# Calendario para un año y mes especifico 
"""
Crea un programa para imprimr el mes y año 
pedido por usuario 
"""

import calendar

# Dado el año y mes ingresado por el usuario se imprime tipo calendario de la fecha ingresada

year = int(input('Escribe el año: '))
month = int(input('Escriba el mes: '))

print(calendar.month(year, month))