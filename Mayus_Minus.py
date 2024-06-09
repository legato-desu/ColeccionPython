# Mayusculas y Minusculas
"""
► Teoría:
En la práctica, existe un código estándar, el código ASCII (código 
estándar americano para intercambio de información), que 
relaciona cada letra, número o símbolo con una cifra del 0 al 255 
(con una secuencia de 8 bits):

La "a" es el número 97
La "b" es el número 98
La "A" es el número 65,
La "B" es el número  67.
El  "0" es el número 48
El  "1" es el número 49, etc.

Así se tiene una forma muy cómoda de almacenar la información 
en ordenadores, ya que cada letra ocupará exactamente un byte 
(8 bits: 8 posiciones elementales de memoria).

► Enunciado:

Escribir un programa que solicite al usuario una letra y diga 
si esta es MAYÚSCULA o minúscula.
"""
letra = input('Introduce una letra: ')

if letra <= 'z'  and letra >= 'a':  
    print(f"La letra ({letra}) es minuscula")
elif letra <= 'Z' and letra >= 'A': 
    print(f"La letra ({letra}) es mayuscula")
else:
    print(f"({letra}) No es una letra")
