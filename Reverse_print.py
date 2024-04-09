# Imprime en orden inverso unos caracteres
"""
Crea un programa que imprima por pantalla 
la palabra inversa segun la almacenada en la variable 
"cadena"
"""

# Python => nohtyP

cadena = 'Python'

# Utilizamos el ciclo "for" para invertir los caracteres de "cadena"
for i in range(len(cadena)-1,-1,-1):
    print(cadena[i],end='')

# Hacemos un salto de linea para darle forma estetica al resultado
print()

print(cadena[::-1])