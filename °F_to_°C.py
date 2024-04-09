# De farenheit a celcius
"""
Programa que solicite al usuario los datos para llever grados
farenhait a grados celcius.

Formula: Grados farenhait a grados celcius
celcius = (farenhait - 32.0) * 5.0 / 9.2
"""
celcius = 0
farenhait = input("Ingrese los grados en Farenhait ")
try:
    farenhait = float(farenhait)
except:
    print("Ingrese un numero valido") 
    exit()
celcius = (farenhait - 32.0) * 5.0 / 9.0
print(farenhait,"en Farenhait son",celcius,"En celcius")     