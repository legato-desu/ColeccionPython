# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
"""
Un año es bisiesto en el calendario Gregoriano, 
si es divisible entre 4 y no divisible entre 100, 
y también si es divisible entre 400.
"""

def bisiesto (año):
    if año % 4 != 0:
        return False 
    elif año % 4 == 0 and año % 100 != 0:
        return True
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        return False
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        return True
    
print(bisiesto(2022))
print(bisiesto(2024))
print(bisiesto(2100))
print(bisiesto(2052))