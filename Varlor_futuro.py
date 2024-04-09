# Valor futuro
"""
Calcular el valor futuro para la cantidad, 
interes, y numero de años especificos.
"""

# VF = VA (1 + I)**n

def valor_futuro(vp, i, n):
    """
    Calcula el valor futuro
    """
    return vp * (1 + i) ** n
valor_presente = 10000
interes = 3.5
periodos = 7

print(valor_futuro(valor_presente, interes/100, periodos))