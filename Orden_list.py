"""
Implementa un algoritmo que ordene una lista de números de menor a mayor
"""

print("ORDENAR NUMEROS DE MENOR A MAYOR")
lista =[10, 6, 1, 4, 2, 5, 8, 3, 9, 7]
print(lista)
print("↓ Orden ↓")
for recorrer in range(1,len(lista)):
    for posicion in range(len(lista) - recorrer):
        if lista[posicion] > lista[posicion + 1]:
            temp = lista[posicion]
            lista[posicion] = lista[posicion + 1]
            lista[posicion + 1] = temp
print(lista)