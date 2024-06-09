# Dia de la semana
"""
Se desea diseñar un programa que escriba los nombres de los dias de la 
semana en funcion del valor de una variable DIA introducida por teclado
"""

print("Ingresa un numero y se mostrara el dia de la semana correspondiente")
dia = int(input("Ingrese un numero entre el 1 al 7: "))

if dia == 1:
    print("Lunes")  
elif dia == 2:
    print("Martes")     
elif dia == 3:
    print("Miercoles")    
elif dia == 4:
    print("Jueves")  
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")                           
elif dia == 7:
    print("Domingo")
else:
    print("Numero no valido")