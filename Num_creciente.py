# Imprimir numeros de forma creciente 
"""
Escribir un programa que imprima los números pares entre 0 y 
200 de forma creciente.
"""
print('Imprimir los numeros pares entre 0 y 200 de forma Creciente')

for pares in range(0,201):
    if pares == int(pares/2)*2 and pares>0:
        print(pares, end=". ")