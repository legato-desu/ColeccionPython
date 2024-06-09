# Taller 5: ciclo FOR
"""
Haz un programa que pida un entero positivo n y almacene en 
una variable M la matriz identidad de n × n (la que tiene unos (1) 
en la diagonal principal y ceros (0) en el resto de celdas). Imprime 
la matriz en pantalla.

                1 0 0 0
        M    =  0 1 0 0 
                0 0 1 0
                0 0 0 1
"""
M = []
longitud = 0
dimension = 0

dimension = int(input(">>> Dimension de la matriz de tamaño n x n: "))

for elemento in range(dimension):
        M.append ([0] * dimension)
for fila in range(dimension):
    for columna in range(dimension):
        if fila == columna:
            M[fila][columna] = 1

print("\n>>> MATRIZ M(%dx%d): %s\n" %(dimension,dimension,M))

longitud = len(M)

for valor in range(longitud):
    print(M[valor])