# Convert uppercase to lowercase
"""
>>> English:

Create a program that switches between upper and lower case
the words stored in the variables

>>> Español:

Crea un programa que cambie entre mayusculas y minusculas
las palabras almacenadas en las variables
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
        print("Convert uppercase to lowercase")
        
        small = "hello word"
        mixed = "HELLO word"
        big = "HELLO WORD"

        small = small.upper() 
        mixed = mixed.swapcase()  
        big = big.lower() 
        
        print(small)
        print(mixed)
        print(big)
        break
    
    elif option == 2:
        
        print(">>> Español:")
        print("Convertir mayusculas a minusculas")
        
        minus = "hola mundo"
        mixto = "HOLA mundo"
        mayus = "HOLA MUNDO"

        minus = minus.upper() 
        mixto = mixto.swapcase()
        mayus = mayus.lower() 

        print(minus)
        print(mixto)
        print(mayus)
        break
    
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    
    else:
        print("Invalid choice\tElección no valida")
        break