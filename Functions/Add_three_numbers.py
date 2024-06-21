# Add three numbers
"""
>>> English:

Create a function with three parameters that are 
numbers that add to each other.

>>> Español:

Crear una función con tres parámetros que sean 
números que se suman entre sí.
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
        print("Add three numbers")
        
        def add (x, y, z):  
            return x + y + z

        x = int(input('First number: '))
        y = int(input('Second number: '))
        z = int(input('Third number: '))

        print(f"{x} + {y} + {z} = {add(x,y,z)}")
        break
    
    elif option == 2:
        
        print(">>> Español:")
        print("Suma tres números")
        
        def suma (x, y, z):  
            return x + y + z

        x = int(input('Primer Numero: '))
        y = int(input('Segundo Numero: '))
        z = int(input('Tercer Numero: '))

        print(f"{x} + {y} + {z} = {suma(x,y,z)}")
        break

    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    
    else:
        print("Invalid choice\tElección no valida")
        break