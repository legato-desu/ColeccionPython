# Area of ​​a circle
"""
>>> English:

Program that asks the user for data to calculate the area of
a circle (O), finally display the result on the screen.

Formula: Area of the circle:
area = PI*(radius**2)

>>> Español:

Programa que solicite al usuario los datos para calcular el area de
un circulo (O), finalmente mostrar el resultado en pantalla.

Formula: Area del circulo:
area = PI*(radio**2)
"""

import math

def menu():
    print("\t╔═══════════════════════════════════╗\n\
        ║\tLanguage\t(Idioma)    ║\n\
        ╠═══════════════════════════════════╣\n\
        ║    1.  English\t(Ingles)    ║\n\
        ║    2.  Spanish\t(Español)   ║\n\
        ║    3.  Exit\t\t(Salir)     ║\n\
        ╚═══════════════════════════════════╝")

while True:

    menu()
    option = int(input("Choice\t(Eleccion): "))
    
    if option == 1:
    
        print(">>> English:")
        print("Area of a circle")

        radius = float(input("Enter the radius: "))
        area = math.pi*(radius**2) 

        print(f"The area of ​​the circle is: {area:.2f} cm²")
        break
    
    elif option == 2:
        
        print(">>> Español:")
        print("Area de un circulo")

        radio = float(input("Ingrese el radio: "))
        area = math.pi*(radio**2) 

        print(f"El area del circulo es: {area:.2f} cm²")
        break
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    else:
        print("Invalid choice\tElección no valida")
        break