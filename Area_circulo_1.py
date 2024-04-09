# Area de un circulo
"""
Programa que solicite al usuario los datos para calcular el area de
un circulo (○), finalmente mostrar el resultado en pantalla.

Formula: Area del circulo
area = PI*(radio**2)
"""
import math
area = 0
radio = input("Ingrese el radio ")
try:
    radio = int(radio)
except:
    print("Ingrese un numero valido") 
    exit()
area = math.pi*(radio**2) 

print("El area del circulo es: " '{0:.2f}'.format(area),"(m)²")