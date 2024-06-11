# Check vowel
"""
>>> English:

Create a program to check if a given character is a vowel.
c = 'i' ['a','e','i','o','u'] => true
c = 'z' ['a','e','i','o','u'] => false

>>> Español:

Crea un programa para comprobar si un caracter dado es una vocal.
c = 'i' ['a','e','i','o','u'] => true
c = 'z' ['a','e','i','o','u'] => false
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
        print("check vowel")
        
        def es_vowel(c):
            
            if len(c) == 1:
                vowels = 'aeiou'
                c = c.lower()
                return c in vowels
            else:
                return False

        letter = input("Enter a vowel: ")

        print(es_vowel(letter))
        break
        
    elif option == 2:

        print(">>> Español:")
        print("Comprobar vocal")
        
        def es_vocal(c):
            
            if len(c) == 1:
                vocales = 'aeiou'
                c = c.lower()
                return c in vocales
            else:
                return False

        letra = input("Ingrese una vocal: ")

        print(es_vocal(letra))
        break
    
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    
    else:
        print("Invalid choice\tElección no valida")
        break