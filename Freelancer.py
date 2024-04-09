# Calculadora freelancer
"""
Un Freelancer desea saber cuánto puede cobrar por su trabajo 
semanal y mensualmente, para ello solo necesita establecer el 
precio de su trabajo por hora.

Se estiman 40 horas de trabajo a la semana.
Las Fórmulas para calcular el pago Semanal y Mensual son:

1) Pago_Semanal = (DolaresPorHora x 40)
2) Pago_Mensual = (DolaresPorHora x 160)

► Variables:

Dolares_Por_Hora: Cantidad de Dólares que gana el 
Freelancer por hora.

Pago_Semanal: Almacena el resultado del pago semanal.
Pago_Mensual: Almacena el resultado del pago mensual.

► Salida:

----------------------------------------
    CALCULADORA FREELANCER (USD)      
----------------------------------------
>>> Precio en dolares por Hora: 20
----------------------------------------
>>> PAGO SEMANAL: 800.00
>>> PAGO MENSUAL: 3200.00
----------------------------------------
"""
ancho = 40
relleno_1 = "-"
relleno_2 = " "
cadena_vacia = ""

horas_semanales = 40
horas_mensuales = 160

mensaje_inicial = "Calculadora Freelancer (USD)"
solicitar_precio = ">>> Precio en dolares por Hora: "
error_formato = "Solo se permiten numeros"
pago_semanal, pago_mensual , dolares_por_hora,  = 0.0 , 0.0, 0.0
formato_respuesta = ">>> Pago Semanal: %4.2f\n>>> Pago Mensual: %4.2f"
print(cadena_vacia.center(ancho,relleno_1))
print(mensaje_inicial.center(ancho,relleno_2))
print(cadena_vacia.center(ancho,relleno_1))
try:
    dolares_por_hora   = float(input(solicitar_precio))
    pago_semanal = dolares_por_hora * horas_semanales
    pago_mensual = dolares_por_hora * horas_mensuales
    print(cadena_vacia.center(ancho,relleno_1))
    print(formato_respuesta %(pago_semanal,pago_mensual))

except ValueError:
    print(cadena_vacia.center(ancho,relleno_1))
    print(error_formato.center(ancho,relleno_2))
print(cadena_vacia.center(ancho,relleno_1))