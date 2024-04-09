# Area de un triangulo
"""
Crea un programa para calcular 
el area de un triangulo
"""

base = None
altura = None
# se usa 'try' para confirmar que el usuario ingrese un numero y no un caracter

while True:
    try:
        base = float(input('Ingrese la base del triangulo: '))
        break
    except:
        print('debe ingresar un numero')
while True:
    try:
        altura = float(input('Ingrese la altura del triangulo: '))
        break
    except:
        print('debe ingresar un numero')

# Dado el numero por el usuario se hace la operacion para allar el area del triangulo
        
area = base * altura / 2
print('El area del triangulo es igual: {}'.format(area))