# Dimension de una matriz 
"""
Cuando deseábamos saber cuál era la longitud de una lista 
utilizábamos la función len(). ¿Funcionará también sobre 
matrices? Hagamos la prueba.

► Entrada:

matriz = [[1, 0], [0, 1], [0, 0]]
­len(matriz)
► Salida:

3

No funciona correctamente: solo nos devuelve el número de 
filas (que es el número de componentes de la lista de listas que 
es la matriz). ¿Cómo averiguar el número de columnas?

► Entrada: Función len()

matriz = [[1, 0], [0, 1], [0, 0]]
­len(matriz[0])
► Salida:

2

___

► Enunciado:

Crea una matriz 3x3 que almacene los valores del 1 al 9. El 
tamaño de la matriz indica la cantidad de filas. Imprime cada fila 
de la matriz en pantalla.

                7   8   9
            M   4   5   6   
                1   2   3   


► Salida:

>>> matriz: [[7, 8, 9], [4, 5, 6], [7, 8, 9]]
>>> FILA 1: [7, 8, 9]
>>> FILA 2: [4, 5, 6]
>>> FILA 3: [7, 8, 9]
"""
matriz = []
longitud = 0

matriz = [[7, 8, 9], [4, 5, 6,], [7, 8, 9]]

longitud = len(matriz)

print("Matriz: %s" %(matriz))

for fila in range(longitud):
    print("Fila %d: %s" %(fila+1, matriz[fila]))