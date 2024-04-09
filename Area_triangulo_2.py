# Area de un triangulo
"""
Programa que solicite al usuario los datos para calcular el area de
un triangulo (▲), finalmente mostrar el resultado en pantalla.

Formula: Area del triangulo
area = (base*altura)/2
"""
area = 0
base = input("Ingrese la base ")
altura = input("Ingrese la altura ")
try:
    altura = int(altura)
    base = int(base)
except:
    print("Ingrese un numero valido") 
    exit()
area = (base*altura)/2    
print("El area del triangulo es ",area)