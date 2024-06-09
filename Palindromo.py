# Palindromo
"""
Escriba un algoritmo para determinar si una palabra es un palíndromo. 
Un palíndromo es una palabra que se lee igual al revés que al derecho

"""

print("COMPROBAR PALINDROMOS")
cadena = input("Ingresa la frase a analizar: ")
cadena = cadena.lower()
cadena = cadena.replace(' ','')
if str(cadena) == str(cadena)[::-1]:
    print(f"La frase - {cadena} - es Palindromo")
else:
    print(f"La frase - {cadena} - no es Palindromo")