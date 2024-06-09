# MCM
"""
Crea un programa para calcular el minimo comun multiplo de dos numeros
"""

def mcm(x, y):
    z = max(x, y)

    while True:
        if (z % x == 0) and (z % y ==  0):
            return z
        z += 1

x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))

print(f"El minimo comun multiplo de {x} y {y} es: {mcm(x,y)}")