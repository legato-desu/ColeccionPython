# Radar de velocidad
"""
Un radar común de detección de velocidad de la policía de 
caminos emite un rayo de microondas a una frecuencia f0. 
El rayo es reflejado por un automóvil que se aproxima y el rayo 
reflejado es captado y analizado por la unidad de radar. La 
frecuencia del rayo reflejado es cambiada ligeramente de f0 a f1 
debido al movimiento del automóvil.
La relación entre la velocidad del automóvil, v, en millas por 
hora, y las dos frecuencias de microondas es:

v=(6.685 x 10**8)(f1-f0)/(f1+f0)

Donde las ondas emitidas tienen una frecuencia de:
f0 = 2 x10^10 sec ^-1

Usando la fórmula dada, escriba un programa para calcular y 
desplegar la velocidad correspondiente a una frecuencia recibida 
de 2.0000004 x 10^10 sec-1.

Ahora aplicamos el procedimiento de desarrollo de software a 
este problema.

► Variables:
· Velocidad : Velocidad del Vehículo.
· Frecuencia0: Frecuencia inicial.
· Frecuencia1: Frecuencia Final.

►Salida:

----------------------------------------
        RADAR DE VELOCIDAD           
----------------------------------------
>>> La Velocidad es: 66.85 millas/hora. 
----------------------------------------
"""
ancho = 40
relleno_1 = "-"
relleno_2 = " "
cadena_vacia = ""

Mmensaje_inicial = "RADAR DE VELOCIDAD"
velocidad   = 0.0
frecuencia_0 = 2e-10            
frecuencia_1 = 2.0000004e-10  

formato_respuesta = ">>> La Velocidad es: %0.2f millas/hora."
print(cadena_vacia.center(ancho,relleno_1))
print(Mmensaje_inicial.center(ancho,relleno_2))

velocidad = 6.685e8*(frecuencia_1-frecuencia_0)/(frecuencia_1+frecuencia_0)

print(cadena_vacia.center(ancho,relleno_1))
print(formato_respuesta.center(ancho,relleno_2) %(velocidad))
print(cadena_vacia.center(ancho,relleno_1))