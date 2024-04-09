# Matriz nula
"""
► Teoría:
En matemáticas, en particular en álgebra lineal, una matriz cero 
o matriz nula es una matriz con todos sus elementos iguales a 
cero. Algunos ejemplos de matrices nulas son:
                            0,0         0,0,0
        0(1.1) = [0],0(22)= 0,0 , 0(23) 0,0,0 = 0,etc
                                        
Por lo tanto, una matriz nula de orden m x n definida sobre un 
anillo K asume la forma:
                0k  0k .... 0k
                0k  0k .... 0k
        0(k) =  .   .  .... .   
                .   .  .... .
                0k  0k .... 0k

Crear una matriz consiste, pues, en crear una lista de listas. Si 
deseamos crear una matriz nula (una matriz cuyos componentes 
sean todos igual a 0) de tamaño 2 × 2, bastará con escribir:

# Matriz nula de tamaño 2x2
m = [ [0, 0], [0, 0] ]
Al construir matrices, hay que asegurarse de que cada fila es una 
lista diferente.

Matriz = []
# Se agregan los elementos a la Matriz
for elemento in range(3):
    Matriz.append ([0] * 6)
print(Matriz)

► Salida:
­[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

► Enunciado:

Haz un programa para crear una matriz nula Mmxn, donde se le 
solicite al usuario su dimensión m x n, (m son las filas y n son las 
columnas). Imprime cada fila de la matriz en pantalla.


                0  0  0
        M    =  0  0  0
                0  0  0

► Salida:

>>> MATRIZ M(3x4): [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
"""
longitud = 0
m_filas = 0
n_columnas = 0

m_filas    = int(input(">>> Numero de filas (m): "))
n_columnas = int(input(">>> Numero de columnas (n): "))

M = []

for elemento in range(m_filas):
    M.append ([0] * n_columnas)

longitud = len(M)

print("\n>>> MATRIZ M(%dx%d): %s\n" %(m_filas,n_columnas,M))

for fila in range(longitud):
    print(M[fila])