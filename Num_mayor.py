# Mayor de 5 numeros
"""
Escribir un programa que solicite al usuario 5 números, 
compararlos y decir cual es mayor.
"""
print("Ingrese 5 numeros a continuacion: ")
numero_1 = float(input("Ingrese el primer numero: "))
numero_2 = float(input("Ingrese el segundo numero: "))
numero_3 = float(input("Ingrese el tercer numero: "))
numero_4 = float(input("Ingrese el cuarto numero: "))
numero_5 = float(input("Ingrese el quinto numero: "))

maximo = numero_1

if numero_2 > maximo:
    maximo = numero_2

if numero_3 > maximo:
    maximo = numero_3

if numero_4 > maximo:
    maximo = numero_4

if numero_5 > maximo:
    maximo = numero_5

total = maximo

print(f"El numero mayor es: {total}")