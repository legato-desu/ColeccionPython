# Tabla de potencias de un numero
"""
Escribir un programa en el cual se solicite al usuario un número y 
se imprima la tabla de potencias del 1 al 10 del valor introducido.
"""
print(">>> TABLA DE POTENCIAS<<<")
numero = int(input('>>> Ingrese el numero a elevar: '))

for potencia in range(1,11):
    resultado = numero ** potencia
    print(numero, "^", potencia, "=",resultado)