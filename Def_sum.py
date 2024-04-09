# Suma de numeros
"""
Crear una función con tres parámetros que 
sean números que se suman entre sí.
"""
def suma (x, y, z):  
    return x + y + z
x = int(input('Ingrese el primer valor: '))
y = int(input('Ingrese el segundo valor: '))
z = int(input('Ingrese el tercer valor: '))

print('la suma es: '+str((suma(x,y,z))))