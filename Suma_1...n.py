# Suma de numeros positivos

"""
escribir un programa que lea un entero positivo, introducido por
el usuario y despues muestre en pantalla la suma de todos los
enteros desde 1. La suma de los primeros enteros positivos
puede ser calculada de la siguiente forma:

suma = n(n+1)
        2
"""
suma = 0
numero = input("Ingrese un numero entero ")
try:
    numero = int(numero)
except:
    print("Ingrese un numero entero valido") 
    exit()
    
suma = numero * (numero + 1 )/2

print("La suma desde 1 hasta " + str(numero) + " es "+ str(suma))