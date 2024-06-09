# Suma de numeros positivos

"""
escribir un programa que lea un entero positivo, introducido por
el usuario y despues muestre en pantalla la suma de todos los
enteros desde 1. La suma de los primeros enteros positivos
puede ser calculada de la siguiente forma:

suma = n(n+1)
        2
"""

numero = int(input("Ingrese un numero entero "))
    
suma = numero * (numero + 1 )/2

print(f"La suma desde 1 hasta {numero} es {suma:.0f}")