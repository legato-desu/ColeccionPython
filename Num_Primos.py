# Numeros primos
"""
Escribir un programa que imprima todos los números primos 
hasta un número introducido por el usuario.
"""

limite = int(input("Ingrese un mumero: "))

for numero in range(1, limite + 1):
    posible_primo = True
    for divisor in range(2,numero):
        if numero % divisor == 0:
            posible_primo = False
            break

    if posible_primo:
            print(numero)