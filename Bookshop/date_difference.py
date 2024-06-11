# Date difference
"""
>>> English:

Create a program to calculate the difference in days of two dates

>>> Español:

Crea un programa para calcular la diferencia en dias de dos fechas
"""

from datetime import date

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
        print("Date difference")

        today = date(1995,6,25)
        another_day = date(2024,9,6)
        
        result = another_day - today

        print(result)
        break
    
    elif option == 2:
        
        print(">>> Español:")
        print("Diferencia de fechas")
        
        hoy = date(1995,6,25)
        otro_dia = date(2024,9,6)
        
        delta = otro_dia - hoy

        print(delta)
        break
    
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    
    else:
        print("Invalid choice\tElección no valida")
        break