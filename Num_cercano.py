# Numero mas cercano
"""
Escribir un programa en el cual Dados 5 números enteros 
solicitados al usuario, determinar cuál de los 4 números enteros 
es más cercano al primero. 
"""

print(">> Ingrese 5 numeros enteros a continuacion: ")

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
numero_3 = int(input("Ingrese el tercer numero: "))
numero_4 = int(input("Ingrese el cuarto numero: "))
numero_5 = int(input("Ingrese el quinto numero: "))

# Se realizan las restas para hallar la menor diferencia
Resta_1 = numero_1 - numero_2
Resta_2 = numero_1 - numero_3
Resta_3 = numero_1 - numero_4
Resta_4 = numero_1 - numero_5

menor = Resta_1

if Resta_2 < menor and Resta_2 >= 0:
    menor = Resta_2
else:
    if Resta_2 > menor and Resta_2 <= 0:
        menor = Resta_2

if Resta_3 < menor and Resta_3 >= 0:
    menor = Resta_3
else:
    if Resta_3 > menor and Resta_3 <= 0:
        menor = Resta_3

if Resta_4 < menor and Resta_4 >= 0:
    menor = Resta_4
else:
    if Resta_4 > menor and Resta_4 <= 0:
        menor = Resta_4

mas_cercano = numero_1 - menor

print(f"El numero mas cercano a ",numero_1 ," es", mas_cercano) 
