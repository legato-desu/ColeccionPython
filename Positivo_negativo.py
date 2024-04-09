# Numeros positivos y negativos
"""
Escribir un programa que solicite al usuario un número entero y 
muestre en pantalla si el número es Positivo (+) o Negativo (-). En
caso de que el número sea igual a cero (0) se debe mostrar en 
pantalla: El número no es Positivo ni Negativo.
"""

numero = input("Ingrese un numero: ")
try:
    numero = float(numero)
except:
    print("Ingrese un numero entero valido") 
    exit()
if numero == 0:
    print("El numero no es ni Positivo ni Negativo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es positivo")        