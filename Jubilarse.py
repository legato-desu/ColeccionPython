# Jubilarse
"""
Pida a usuario la edad y el genero, 
para que la computadora le indique 
si ya puede jubilarse. Tome en cuenta 
que un Hombre se puede jubilar 
cuando tenga 60 años o mas, en cambio, 
una mujer mayor se jubilara si tiene mas de 54 años.
"""
genero = input("Genero: Digite M para Masculino o F para Femenino:... ")

edad= input("Ingrese su edad: ")

genero = genero.upper()
try: 
    edad = int(edad)
except:
    input("Ingrese una edad valida ")  
    exit()  
if genero == "M":
    if edad >= 60:
        print("Puede jubilarse")
    else:
        print("No puede jubilarse")
elif genero == "F":
    if edad >= 54:
        print("Puede jubilarse")
    else:
        print("No puede jubilarse")
else:
    print("Digite una de las opciones validas de genero (M o F)")            