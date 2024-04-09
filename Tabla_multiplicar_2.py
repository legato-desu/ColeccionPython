# Tabla de multiplicar
"""
Diseñe un programa que imprima la tabla 
de multiplicar de un numero introducido 
por teclado, desde el factor 1 hasta el 12
"""
numero = input("Ingrese el numero: ")
try:
    numero = int(numero)
except:
    print("Ingrese un numero valido")  
    exit() 
contador = 1

while contador <= 12:
    print(f"{numero} X {contador} = "+str(numero*contador))
    contador+=1
print(f"Tabla del numero {numero} elaborada ")    