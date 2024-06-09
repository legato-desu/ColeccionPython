# Student approval
"""
>>> English:

Create a program that receives three ratings, average them and 
say if the student passed or not

>>> Español:

Crear un programa que reciba tres calificaciones las promedie y 
diga si el alumno aprobo o no
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
        
        print(">>> English")
        print("Student approval")

        qualification_1 = float(input("Enter first grade: "))
        qualification_2 = float(input("Enter second grade: "))
        qualification_3 = float(input("Enter the third grade: "))

        average = (qualification_1 + qualification_2 + qualification_3) / 3

        if average >= 3.5:
            print(f"The student passed with: {average:.1f}")
        else:
            print(f"The student failed with: {average:.1f}")
        break
    elif option == 2:
                
        print(">>> Español")
        print("Aprobacion del estudiante")

        calificacion_1 = float(input("Ingrese la primera calificacion: "))
        calificacion_2 = float(input("Ingrese la segunda calificacion: "))
        calificacion_3 = float(input("Ingrese la tercera calificacion: "))

        promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

        if promedio >= 3.5:
            print(f"El alumno aprobo con: {promedio:.1f}")
        else:
            print(f"El alumno reprobo con: {promedio:.1f}")
        break
    elif option == 3:
        print("Program completed\tPrograma finalizado")
        break
    else:
        print("Invalid choice\tElección no valida")
        break