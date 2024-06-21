# Calculate discount
"""
>>> English:

In a computer factory, it is planned to offer customers 
a discount that will depend on the number of computers you buy. 
If the computers are less than five, they will be given a 10% discount. 
discount on the total of computers; If the number of 
computers is greater than or equal to five but less than ten 
You will be given a 20% discount; and if there are 10 or more they are given 40% 
off. The price of each computer is $700.

>>> Español:

En una fabrica de computadoras se planea ofrecer a los clientes 
un descuento que dependera del numero de computadoras que compre. 
si las computadoras son menos de cinco se les dara un 10% de 
descuenrto sobre el total de la computadoras; si el numero de 
computadoras es mayor o igual a cinco pero menos de diez 
se le otorgara un 20% de descuento; y si son 10 o mas se les da un 40% 
de descuento. el precio de cada computadora es de $700.
"""

def menu():
    print("\t╔═══════════════════════════════════╗\n\
        ║\tLanguage\t(Idioma)    ║\n\
        ╠═══════════════════════════════════╣\n\
        ║    1.  English\t(Ingles)    ║\n\
        ║    2.  Spanish\t(Español)   ║\n\
        ║    3.  Exit\t\t(Salir)     ║\n\
        ╚═══════════════════════════════════╝")

while True:

    menu()
    option = int(input("Choice\t(Eleccion): "))
    
    if option == 1:
        
        print(">>> English:")
        print("Calculate discount")

        computers = int(input("Number of computers purchased:: "))

        total = computers * 700    

        if computers < 5:
            total = total - (total * 0.10)
        elif computers >= 5 and computers < 10:
            total = total - (total * 0.20)
        elif computers >= 10:
            total = total - (total * 0.40)     

        print(f"The total is: ${total:,.0f}")       
        break
    
    elif option == 2:
        
        print(">>> Español:")
        print("Calcular descuento")
        
        computadoras = int(input("Cantidad de computadoras compradas: "))

        total = computadoras * 700    

        if computadoras < 5:
            total = total - (total * 0.10)
        elif computadoras >= 5 and computadoras < 10:
            total = total - (total * 0.20)
        elif computadoras >= 10:
            total = total - (total * 0.40)     

        print(f"El total es de: ${total:,.0f}")       
        break
    
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    
    else:
        print("Invalid choice\tElección no valida")
        break