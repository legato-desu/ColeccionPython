# Identity matrix
"""

>>> English:

Make a program that asks for a positive integer n and stores in 
a variable M the n x n identity matrix (the one with ones (1) 
on the main diagonal and zeros (0) in the rest of the cells). Print 
the matrix on the screen.

                1 0 0 0
        M    =  0 1 0 0 
                0 0 1 0
                0 0 0 1

>>> Español:

Haz un programa que pida un entero positivo n y almacene en 
una variable M la matriz identidad de n x n (la que tiene unos (1) 
en la diagonal principal y ceros (0) en el resto de celdas). Imprime 
la matriz en pantalla.

                1 0 0 0
        M    =  0 1 0 0 
                0 0 1 0
                0 0 0 1
"""

def menu():
    print("\t╔═══════════════════════════════════╗\n\
        ║\tLanguage\t(Idioma)    ║\n\
        ╠═══════════════════════════════════╣\n\
        ║    1.  English\t(Ingles)    ║\n\
        ║    2.  Spanish\t(Español)   ║\n\
        ║    3.  Exit\t\t(Salir)     ║\n\
        ╚═══════════════════════════════════╝")

while True:

    menu()
    option = int(input("Choice\t(Eleccion): "))
    
    if option == 1:
        
        print(">>> English:")
        print("Identity matrix")
    
        M = []
        length = 0
        dimension = 0

        dimension = int(input("Dimension of size matrix n x n: "))

        for element in range(dimension):
                M.append ([0] * dimension)
        for row in range(dimension):
            for column in range(dimension):
                if row == column:
                    M[row][column] = 1

        print("\nMATRIX M(%dx%d): %s\n" %(dimension,dimension,M))

        length = len(M)

        for worth in range(length):
            print(M[worth])
        break
    
    elif option == 2:
        
        print(">>> Español:")
        print("Matriz identidad")
        
        M = []
        longitud = 0
        dimension = 0

        dimension = int(input("Dimension de la matriz de tamaño n x n: "))

        for elemento in range(dimension):
                M.append ([0] * dimension)
        for fila in range(dimension):
            for columna in range(dimension):
                if fila == columna:
                    M[fila][columna] = 1

        print("\nMATRIZ M(%dx%d): %s\n" %(dimension,dimension,M))

        longitud = len(M)

        for valor in range(longitud):
            print(M[valor])
        break

    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    
    else:
        print("Invalid choice\tElección no valida")
        break