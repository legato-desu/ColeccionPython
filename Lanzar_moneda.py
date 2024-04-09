# lanzar la moneda
"""
Crea un programa para lanzar la moneda 
y saber si cae cara o cruz
"""
import random
lista = ["Cara"," Cruz"]
elemento = random.choice(lista)
if elemento == "Cara":
    print("Ha salido cara")
else:
    print("Ha salido cruz")    