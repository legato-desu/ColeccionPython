"""
Crea un script que le pida al usuario una lista de países 
(separados por comas). Éstos se deben almacenar en una lista. 
No debería haber países repetidos (haz uso de set). Finalmente, 
muestra por consola la lista de países ordenados alfabéticamente 
y separados por comas.
"""

items = input("Ingrese los paises separados por comas: :\n")

paises = [pais for pais in items.split(",")]

print(",".join(sorted(list(set(paises)))))