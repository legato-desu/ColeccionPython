# Imprimir numeros de forma decreciente
"""
Escribir un programa que imprima los números pares entre el 0 y 
200 de forma decreciente.
"""
print('Imprimir los numeros pares entre 0 y 200 de forma decreciente')

for pares in range(200,-1,-1):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)