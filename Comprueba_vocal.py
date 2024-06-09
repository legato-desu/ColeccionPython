# Comprueba vocal
"""
Crea un programa para comprobar si un caracter dado es una vocal.
c = 'i' ['a','e','i','o','u'] => true
c = 'z' ['a','e','i','o','u'] => false
"""
def es_vocal(c):
    
    if len(c) == 1:
        vocales = 'aeiou'
        c = c.lower()
        return c in vocales
    else:
        return False

letra = input("Ingrese una vocal: ")

print(es_vocal(letra))