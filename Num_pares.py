# imprimir numeros pares hasta un numero dado
"""
► Enunciado:

Escribir un programa que imprima los números pares de forma 
creciente hasta un número introducido por el usuario.
"""
numero = int(input('>>> Ingrese un numero: '))

for pares in range(0,numero + 1):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)