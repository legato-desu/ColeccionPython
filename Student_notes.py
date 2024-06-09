# Calificaciones estudiante
"""
La clase (Alumno) define un objeto de estudiante con atributos de 
nombre y calificación, y métodos para imprimir la información del 
estudiante y determinar si aprobó o reprobó.
"""
class Alumno():

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def resultados(self):
        print(f"El alumno {self.nombre} con nota {self.nota}",end=" ")

    def calculo(self):
        if self.nota < 5:
            print("Ha suspendido")
        else:
            print("Ha aprobado")

nombres = input("Ingrese el nombre del alumno: ")
nombres = nombres.capitalize()

notas = int(input("Ingrese la nota: "))

alumno = Alumno(nombres,notas)
alumno.resultados()
alumno.calculo()