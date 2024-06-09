# Tabla de multiplicar de un numero
"""
Escribir un programa en el cual se solicite al usuario un número y 
se imprima la tabla de multiplicar del 1 al 10 del valor introducido.
"""

print(">>> TABLA DE MULTIPLICAR <<<")

numero = int(input("Ingrese un numero: "))

for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")