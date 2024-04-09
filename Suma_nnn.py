# Suma de n + nn + nnnn ...
"""
solicitar al usuario un numero n y calcular n + nn + nnn

El codigo usara el numero ingresado por usuario y lo concanetara 
con el mismo +1 para sumarle

ejemplo:
n = 2
2 + 22 + 222
>>> 246
"""
n = input('Ingrese el valor de n: ')

nn = int('{}{}'.format(n,n))

nnn = int('%s%s%s'%(n,n,n))

n = int(n)

suma = n + nn + nnn

print(suma)