# MCM

"""
Crea un programa para calcular el 
minimo comun multiplo de dos numeros
"""

# MCM: Es el numero positivo mas pequeño que es multiplo de dos numeros

def mcm(x, y):
    z = max(x, y)

    while True:
        if (z % x == 0) and (z % y ==  0):
            return z
        z += 1

print(mcm(2,4))
print(mcm(13, 32))
print(mcm(15,17))