# MCD
"""
Crea un programa para calcular el maximo comun divisor de dos numeros
"""

def mcd(x, y):
    mcd = 1
    if x % y == 0:
        return y
    for k in range(int(y/2),0,-1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break
    return mcd

x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))

print(f"El maximo comun divisor de {x} y {y} es: {mcd(x,y)}")