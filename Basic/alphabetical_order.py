# Alphabetical order
"""
>>> English:

Create a (script) that prompts the user for a list of countries
separated by commas (,). These must be stored in a list.
There should not be repeated countries make use of (set). Finally,
shows the list of countries in alphabetical order via console 
and separated by commas.

>>> Español:

Crea un (script) que le pida al usuario una lista de países 
separados por comas. Éstos se deben almacenar en una lista. 
No debería haber países repetidos haz uso de (set). Finalmente, 
muestra por consola la lista de países ordenados alfabéticamente 
y separados por comas.
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
        print("Alphabetical order")

        items = input("Enter countries separated by comma (,):\n")

        paises = [pais for pais in items.split(",")]

        print(",".join(sorted(list(set(paises)))))
        break
    
    elif option == 2:
        
        print(">>> Español:")
        print("Orden alfabetico")
        
        items = input("Ingrese los paises separados por coma (,):\n")

        paises = [pais for pais in items.split(",")]

        print(",".join(sorted(list(set(paises)))))
        break
    
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    
    else:
        print("Invalid choice\tElección no valida")
        break