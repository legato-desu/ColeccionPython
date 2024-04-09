# Extresion algebraica
"""
Crea un programa para 
Resolver la expresion algebraica 
(x + y ) * (x + y).
"""

# (x + y) + (x + y) = x**2 + 2xy + y**2

def evaluar_expresion (x, y):
    """
    Resuelve la exprecion algebraica (x + y ) * (x + y)
    """
    return x**2 + 2 * x * y + y**2

x = float(input('Escriba el valor de x: '))
y = float(input('Escriba el valor de y: '))

print(evaluar_expresion(x, y))