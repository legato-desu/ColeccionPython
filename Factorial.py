# Factorial
"""
Escriba un algoritmo para calcular la factorial de un número. 
Recuerda que la factorial de un número n es el producto de todos los números
enteros positivos desde 1 hasta n
"""
print('CALCULO DEL FACTORIAL DE UN NUMERO')

n = int(input('Ingrese el numero para calcular su factorial: '))

def factorial(n):
    
    if (n ==0):
        return 1
    else:
        return n * factorial(n-1)
    
print(f"El factorial de {n} es {factorial(n)}")