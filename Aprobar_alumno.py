# Aprobacion alumno
"""
Crear un programa que reciba tres calificaciones
las promedie y diga si el alumno aprobo o no
"""

calificacion_1 = input("Ingrese la primera calificacion: ")
try:
    calificacion_1 = float(calificacion_1)
except:
    print("Ingrese una calificacion valida")
    exit()
calificacion_2 = input("Ingrese la segunda calificacion: ")
try:
    calificacion_2 = float(calificacion_2)
except:
    print("Ingrese una calificacion valida")
    exit()
calificacion_3 = input("Ingrese la tercera calificacion: ")
try:
    calificacion_3 = float(calificacion_3)
except:
    print("Ingrese una calificacion valida")
    exit()

promedio = (calificacion_1+calificacion_2+calificacion_3)/3

if promedio >= 7:
    print(f"El alumno aprobo con:{promedio}")
else:
    print(f"El alumno reprobo con:{promedio}")