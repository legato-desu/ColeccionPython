# Fahrenheit to Celsius
"""
>>> English:

Program that asks the user for data to keep grades
Fahrenheit to degrees celsius.

Formula: Degrees Fahrenheit to Degrees Celsius
celsius = (Fahrenheit - 32.0) * 5.0 / 9.2

>>> Español:

Programa que solicite al usuario los datos para llever grados
Fahrenheit a grados celsius.

Formula: Grados Fahrenheit a grados celsius
celsius = (Fahrenheit - 32.0) * 5.0 / 9.2
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
        print("Fahrenheit to Celsius")

        Fahrenheit = float(input("Enter degrees in Fahrenheit: "))
        celsius = (Fahrenheit - 32.0) * 5.0 / 9.2

        print(f"{Fahrenheit:.0f}°F = {celsius:.0f}°C")
        break
    elif option == 2:
        
        print(">>> Español:")
        print("Fahrenheit a Celsius")

        Fahrenheit = float(input("Ingrese los grados en Fahrenheit "))
        celsius = (Fahrenheit - 32.0) * 5.0 / 9.2

        print(f"{Fahrenheit:.0f}°F = {celsius:.0f}°C")
        break
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    else:
        print("Invalid choice\tElección no valida")
        break