# Fecha y hora actuales en el sistema
"""
Crea un programa que enseña la hora y fecha
actuales desde el sistema
"""

# Se importa el datetime para adquirir los datos de la fecha y hora

import datetime

ahora = datetime.datetime.now()

# Se imprime en pantalla los datos importados en la variante "ahora"

print(ahora)

print(type(ahora))

# Organizar la fecha Dia/Mes/Año/hora

print(f"{ahora.strftime('%d/%m/%y\t%H:%M:%S')}")