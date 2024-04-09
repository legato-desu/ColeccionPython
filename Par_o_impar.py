#Numero par o impar
"""
Introducir un número por teclado y que se muestre un mensaje 
indicando si es par o impar.
"""
numero = input("Ingrese un numero: ")
try:
    numero = int(numero)
except:
    print("Ingrese un numero entero")
    exit()
if numero == (numero // 2) * 2:
    print(f"El numero {numero} es par.")
else:
    print(f"El numero {numero} es impar.")
