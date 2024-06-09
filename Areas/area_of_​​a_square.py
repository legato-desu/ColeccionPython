# Area of ​​a square
"""
>>> English:

Program that asks the user for data to calculate the area of 
a square (▀), finally display the result on the screen.

Formula: Area of the square
area = side ** 2

>>> Español:

Programa que solicite al usuario los datos para calcular el area de 
un cuadrado (▀), finalmente mostrar el resultado en pantalla.

Formula: Area del cuadrado
area = lado ** 2
"""

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
        print("Area of a square")

        side = float(input("Enter the side of the square: "))
        area = side ** 2

        print(f"The area of the square is: {area:.0f} cm²")
        break
    elif option == 2:

        print(">>> Español:")
        print("Area de un cuadrado")

        lado = float(input("Ingrese el lado para calcular su area "))
        area = lado ** 2

        print(f"El area del cuadrado es: {area:.0f} cm²")
        break
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    else:
        print("Invalid choice\tElección no valida")
        break