# Inventory Search
"""
>>> English:

Create a dictionary with some fruits and their quantities then with the 
use of (get), show the amount of fruits as stored in The inventory

>>> Español:

Crea un diccionario con unas frutas y sus cantidades luego con el 
uso de (get), enseñar la cantidad de frutas segun lo almacenado en 
el inventario 
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
        print("Inventory Search")

        fruit = {
            "Pears":23,
            "Apples":50,
            "Watermelons":7,
            "Peaches":21,
            "Strawberries":100,
            "Grapes":150,
        }

        search = input("Enter a fruit: ")
        search = search.capitalize()
        number = fruit.get(search,0)

        print(f"There is {number} {search} on the inventory")
        break
    elif option == 2:
        
        print(">>> Español:")
        print("Busqueda de inventario")

        frutas = {
            "Peras":23,
            "Manzanas":50,
            "Sandias":7,
            "Melocotones":21,
            "Fresas":100,
            "Uvas":150,
        }

        busqueda = input("Ingrese una fruta: ")
        busqueda = busqueda.capitalize()
        numero = frutas.get(busqueda,0)

        print(f"Hay {numero} {busqueda} en el inventario")
        break
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    else:
        print("Invalid choice\tElección no valida")
        break