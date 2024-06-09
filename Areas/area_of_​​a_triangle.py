# Area of ​​a triangle
"""
>>> English:

Program that asks the user for data to calculate the area of
a triangle (▲), finally display the result on the screen.

Formula: Area of the triangle
area = (base*height)/2

>>> Español:

Programa que solicite al usuario los datos para calcular el area de
un triangulo (▲), finalmente mostrar el resultado en pantalla.

Formula: Area del triangulo
area = (base*altura)/2
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
        print("Area of a triangle")

        a = float(input('Enter base: '))
        h = float(input('Enter height: ')) 
        area = (a * h) / 2

        print(f"The area of the triangle is: {area:.1f} cm²")
        break
    elif option == 2:

        print(">>> Español:")
        print("Area de un triangulo")

        a = float(input('Ingrese base: '))
        h = float(input('Ingrese altura: '))
        area = (a * h) / 2

        print(f"El area del triangulo es: {area:.1f} cm²")
        break
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    else:
        print("Invalid choice\tElección no valida")
        break