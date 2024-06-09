# Modulo time
"""
crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. 
Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y 
en caso contrario, haréis una operación para calcular 
el tiempo que queda de trabajo.
"""

import time

hora = time.strftime('%H') 
minutos = time.strftime('%M') 

if int(hora) >= 19:
	print ("Es hora de irse a casa") 
else:
    
    print(f"Restan {18-int(hora)} horas y {59-int(minutos)} minutos para ir a casa")