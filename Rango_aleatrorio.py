"""
Generar un conjunto de numeros aleatorios y determinar cuales son impares

K mod 2 == 1
"""
from random import randint

numeros_aleatorios = [randint(1,100)for _ in range(2)]

print(numeros_aleatorios)

numeros_impares = filter(lambda n: n % 2 == 1, numeros_aleatorios) 

print()

print(list(numeros_impares))
"""
Metodo mas largo sin el lambda
print()

def encontrar_impares(lista):
    impares = []

    for n in lista:
        if n % 2 == 1:
            impares.append(n)
    return impares
print(encontrar_impares(numeros_aleatorios))            
"""