# Specific calendar
"""
>>> English:

Create a program to print the month and year requested by the user

>>> Español:

Crea un programa para imprimir el mes y año pedido por usuario
"""

import calendar

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
        print("Specific calendar")

        year = int(input("enter the year: "))
        month = int(input("enter the month: "))

        print(calendar.month(year, month))
        
        break
    elif option == 2:
            
        print(">>> Español:")
        print("Calendario especifico")

        anio = int(input('Ingrese el año: '))
        mes = int(input('Ingrese el mes: '))
        
        print(calendar.month(anio, mes))
            
        break
    
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    else:
        print("Invalid choice\tElección no valida")
        break