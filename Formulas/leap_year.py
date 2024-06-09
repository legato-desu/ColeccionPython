# leap year
"""
>>> English:

A year is a leap year in the Gregorian calendar if it is divisible by 4 and 
not divisible by 100, and also if it is divisible by 400.

>>> Español:

Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y 
no divisible entre 100, y también si es divisible entre 400.
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
        print("Leap year")

        def leap (year):
            if year % 4 != 0:
                return "The year is not a leap year" 
            elif year % 4 == 0 and year % 100 != 0:
                return "The year is leap year"
            elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
                return "The year is not a leap year" 
            elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                return "The year is leap year"
            
        calculate = int(input("Enter the year to calculate (YYYY): "))

        print(leap(calculate))
        break
    elif option == 2:
        
        print(">>> Español:")
        print("Año bisiesto")
        def bisiesto (año):
            if año % 4 != 0:
                return "El año no es bisiesto" 
            elif año % 4 == 0 and año % 100 != 0:
                return "El año es bisiesto"
            elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
                return "El año no es bisiesto" 
            elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
                return "El año es bisiesto"
            
        calculo = int(input("Ingrese el año a calcular (YYYY): "))

        print(bisiesto(calculo))
        break
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    else:
        print("Invalid choice\tElección no valida")
        break