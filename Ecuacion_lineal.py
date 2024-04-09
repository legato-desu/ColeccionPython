# Ecuacion de primer grado
"""
► Enunciado:
Crear un Algoritmo que permita hallar la solución a una ecuación 
de primer grado, de la forma: ax + b = 0
El objetivo es despejar la x y validar los posibles datos para
arrojar la respuesta.

Al despejar la x tendremos que:

x = -b/a
Por lo tanto tendremos los siguientes escenarios:
1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.
2) Si a es IGUAL a 0 (a == 0) tendremos que:
Si b es DIFERENTE de 0 (b != 0) la ecuación no tiene solución.
Si b es IGUAL a 0 (b == 0) la ecuación tiene Infinitas Soluciones.

► Variables:
a: Coeficiente principal.
b: Término Independiente.
x: Incógnita.

► Datos de Prueba.
a) a = 2 y b = 6.
b) a = 0 y b = 3.
c) a = 0 y b = 0.

► Salida:
----------------------------------------
    ECUACION DE PRIMER GRADO: ax + b = 0  
----------------------------------------
>>> Valor de a: 2
>>> Valor de b: 6
----------------------------------------
ECUACION: 2.0 x + 6.0 = 0
----------------------------------------
>>> SOLUCION: x =  -3.0
----------------------------------------
"""
ancho = 40
relleno_1 = "-"
relleno_2 = " "
vacia = ""

mensaje_inicial = "Ecuacion de primer grado: ax + b = 0"

a = 0 
b = 0 
x = 0 

Formato_Ecuacion = "ECUACION: {} x + {} = 0"

print(vacia.center(ancho,relleno_1))
print(mensaje_inicial.center(ancho,relleno_2))
print(vacia.center(ancho,relleno_1))


a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))

print(vacia.center(ancho,relleno_1))
print(Formato_Ecuacion.format(a,b))
print(vacia.center(ancho,relleno_1))

try:
    x = -b/a
    print(">>> SOLUCION: x = ", x)
except:
    if b != 0:
        print("La ECUACION no tiene solucion.")
    else:
        print("La ECUACION tiene infinitas soluciones.")

print(vacia.center(ancho,relleno_1))