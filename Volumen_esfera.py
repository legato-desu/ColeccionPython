# Volumen de una esfera
"""
Crea un programa para calcular el volumen de una esfera a partir del radio dado
"""

from math import pi

r = float(input("Ingrese el radio de la esfera: "))

volumen = 4/3 * pi * r ** 3

print(f"El volumen de la esfera es {volumen:.1f} cm³")