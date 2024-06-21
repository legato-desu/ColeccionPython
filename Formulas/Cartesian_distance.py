# Cartesian distance
"""
>>> English:

Create a program to calculate the distance between two Cartesian points
    PI(x1, y1), P2(x2, y2)

>>> Español:

Crea un programa para calcular la distancia entre dos puntos cartesianos 

    PI(x1, y1), P2(x2, y2)
"""

from math import sqrt

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
        print("Cartesian distance")

        class spot:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                
        def calculate_distance(p1, p2):
            return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

        spot1 = spot(3, 2)
        spot2 = spot(-3, -5)

        print(calculate_distance(spot1, spot2))
        break
    
    elif option == 2:
        print(">>> Español:")
        print("Distancia cartesiana")
        
        class punto:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                
        def calcular_distancia(p1, p2):
            return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

        punto1 = punto(3, 2)
        punto2 = punto(-3, -5)

        print(calcular_distancia(punto1, punto2))
        break
    
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    
    else:
        print("Invalid choice\tElección no valida")
        break