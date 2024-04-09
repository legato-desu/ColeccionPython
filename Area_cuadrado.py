# Area de un cuadrado
"""
Programa que solicite al usuario los datos para calcular el area de 
un cuadrado (▀), finalmente mostrar el resultado en pantalla.

Formula: Area del cuadrado
area = lado ** 2
"""
area = 0
lado = input("Ingrese el lado para calcular su area ")
try:
    lado = int(lado)
except:
    print("Ingrese un numero valido") 
    exit()
area = lado ** 2

print("el area del cuadrado es ",area,"(m)²")