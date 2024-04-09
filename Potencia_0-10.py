# Tabla de potencias
"""
Crea un codigo que potencie un numero base
desde 0 a 10 y enseña el resultado de cada potencia
"""

base = int(input("> Introduce el numero a elevar: "))

for exponente in range(0,10):
    potencia = base ** exponente
    print(f"{base} elevado a {exponente} es {potencia}")