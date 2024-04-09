# Ecuacion de segundo grado
"""
► Enunciado:
Crear un Algoritmo que permita hallar la solución a una ecuación 
de segundo grado, de la forma:

                    ax**2 + bx + c = 0

Los datos del problema son los coeficientes a, b y c. Se desea 
calcular los valores de x que hacen cierta la ecuación. Dichos 
valores son:

x1 = -b +  √ b**2 - 4ac / 2a
x2 = -b -  √ b**2 - 4ac / 2a

► Consideraciones:

- En este programa se debe considerar la división por cero que 
tiene lugar cuando a vale 0 haciendo entonces al denominador, 
2a, nulo. Cuando a vale 0 la ecuación no es de segundo grado, 
sino de primer grado.

- Otra consideración que debemos tomar en cuenta es que el 
discriminante (b2- 4ac) no debe ser negativo, de ser negativo la 
ecuación no tiene soluciones reales.

Se deben tomar en cuenta los siguientes escenarios:

1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.
Si b es DIFERENTE de 0 (b! = 0) la ecuación no tiene solución.
Se b es IGUAL a 0 (b == 0) se produce la división por cero, y la ecuación tiene infinitas soluciones.

► Variables
a: Coeficiente principal.
b: Coeficiente secundario.
c: Término Independiente.
x1: Incógnita 1.
x2: Incógnita 2.
discriminante: Discriminante de la ecuación.

► Datos de Prueba.
a) a = 2 , b = 7, c = 2
b) a = 1 , b = 2, c = 3
c) a = 0 , b = 2, c = 3
d) a = 0 , b = 0, c = 3

► Salida:
-------------------------------------------------------
    ECUACION DE SEGUNDO GRADO: ax^2 + bx + c = 0      
-------------------------------------------------------
>>> Valor de a: 2
>>> Valor de b: 7
>>> Valor de c: 2
-------------------------------------------------------
>>> SOLUCIONES: x1 = -0.31 y x2 = -3.19
-------------------------------------------------------
"""
from math import sqrt

ancho = 55
relleno_1 = "-"
relleno_2 = " "
vacia = ""

mensaje_inicial = "ecuacion de segundo grado: ax^2 + bx + c = 0"

a, b, c = 0, 0, 0
x1, x2  = 0.0, 0.0
discriminante = 0


print(vacia.center(ancho,relleno_1))
print(mensaje_inicial.center(ancho,relleno_2))
print(vacia.center(ancho,relleno_1))


a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))
c = float(input(">>> Valor de c: "))

discriminante = b**2 - 4*a*c

try:
    x1 = (-b + sqrt(discriminante)) / (2 * a)
    x2 = (-b - sqrt(discriminante)) / (2 * a)

    print(vacia.center(ancho,relleno_1))

    if x1 == x2:
        print(">>> SOLUCION: x = %4.2f" % x1)
    else:
        print(">>> SOLUCIONES: x1 =     %4.2f y x2 = %4.2f" % (x1, x2))

except ZeroDivisionError:

    print(vacia.center(ancho,relleno_1))

    if b != 0:
        print("La ecuacion no tiene solucion.")
    else:
        print("La ecuacion tiene infinitas soluciones.")

except ValueError:

    print(vacia.center(ancho,relleno_1))
    print("No hay soluciones reales")

print(vacia.center(ancho,relleno_1))