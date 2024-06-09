# Convertir de mayusculas a minusculas
"""
Crea un programa que cambie entre mayusculas y minusculas
las palabras almacenadas en las variables
"""

# Definir las variables
minus = "hola mundo"
mix = "HOLA mundo"
mayus = "HOLA MUNDO"
# Hacer la convercion
minus = minus.upper() # Pasa a mayusculas
mayus = mayus.lower() # Pasa a minusculas
mix = mix.swapcase()  # las mayus a minus y minus a mayus

# Enseñar en pantalla el resultado
print(minus)
print(mayus)
print(mix)