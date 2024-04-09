# Diferencia de dos fechas
"""
Crea un programa para calcular 
la diferencia en dias de dos fechas
"""
from datetime import date

# Se otorga la fecha a unas variables y se calcula el tiempo entre una y otra

today = date(1995,6,25)

another_day = date(2023,2,7)

delta = another_day - today

print(delta)
print(delta.days)