# Puntos cartesianos.

"""
Crea un programa para calcular la distancia entre dos puntos cartesianos 

    PI(x1, y1), P2(x2, y2)
"""

from math import sqrt

class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def calcular_distancia(p1, p2):
    
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

punto1 = punto(3, 2)
punto2 = punto(-3, -5)

print(calcular_distancia(punto1, punto2))