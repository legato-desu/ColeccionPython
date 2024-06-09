# Diferencia de dos fechas
"""
Crea un programa para calcular la diferencia en dias de dos fechas
"""
from datetime import date

hoy = date(1995,6,25)

otro_dia = date(2025,1,6)

delta = otro_dia - hoy

print(delta)
print(delta.days)