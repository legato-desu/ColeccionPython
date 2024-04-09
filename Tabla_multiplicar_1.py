# Tabla de multiplicar de un numero
"""
► Enunciado:
Escribir un programa en el cual se solicite al usuario un número y 
se imprima la tabla de multiplicar del 1 al 10 del valor introducido.
"""
print(">>> TABLA DE MULTIPLICAR<<<")
numero = int(input('>>> Ingrese el numero a multiplicar: '))

for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=",resultado)