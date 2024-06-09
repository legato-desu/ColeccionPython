# Calcular descuento
"""
En una fabrica de computadoras se planea ofrecer a los clientes 
un descuento que dependera del numero de computadoras que compre. 
si las computadoras son menos de cinco se les dara un 10% de 
descuenrto sobre el total de la computadoras; si el numero de 
computadoras es mayor o igual a cinco pero menos de diez 
se le otorgara un 20% de descuento; y si son 10 o mas se les da un 40% 
de descuento. el precio de cada computadora es de $700.
"""

computadoras = int(input("Ingrese la cantidad de computadoras compradas: "))

total = computadoras * 700    

if computadoras < 5:
    total = total - (total * 0.10)
elif computadoras >= 5 and computadoras < 10:
    total = total - (total * 0.20)
elif computadoras >= 10:
    total = total - (total * 0.40)     

print(f"El total es de: ${total:,.0f}")       