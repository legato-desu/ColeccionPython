# Multiplos de 3
"""
Introducir un número por teclado y que se muestre un mensaje 
indicando si es múltiplo de 3.
"""
numero = input("Ingrese un numero: ")
try:
    numero = int(numero)
except:
    print("Ingrese un numero entero")
    exit()
if numero == (numero // 3) * 3:
    print(f"El numero {numero} es multiplo de 3.")
else:
    print(f"El numero {numero} no es multiplo de 3.")