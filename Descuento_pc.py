# Calcular descuento
"""
En una fabrica de computadoras se planea 
ofrecer a los clientes un descuento 
que dependera del numero de computadoras que compre. 
si las computadoras son menos de cinco se 
les dara un 10% de descuenrto sobre el total de 
la cantidad_compra; si el numero de computadoras 
es mayor o igual a cinco pero menos de diez 
se le otorgara un 20% de descuento; y 
si son 10 o mas se les da un 40% 
de descuento. el precio de cada computadora es de $700.
"""
cantidad_compra = input("Ingrese la cantidad de computadoras compradas: ")

try:
    cantidad_compra = int(cantidad_compra)
except:
    print("Cantidad no valida")
    exit()

sumatoria = cantidad_compra*700    

if cantidad_compra < 5:
    total = sumatoria-(sumatoria*0.10)
elif cantidad_compra >= 5 and cantidad_compra < 10:
    total = sumatoria-(sumatoria*0.20)
elif cantidad_compra >= 10:
    total = sumatoria-(sumatoria*0.40)     
print(f"El total es de: ${total}")       