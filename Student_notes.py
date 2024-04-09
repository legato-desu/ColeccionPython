# Calificaciones estudiante
"""
La clase "Alumno" define un objeto de estudiante con 
atributos de nombre y calificación, y métodos para imprimir
la información del estudiante y determinar si aprobó o reprobó.
"""
class Alumno():

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def resultados(self):
        print("El alumno:",self.nombre,"con nota:",self.nota)

    def calculo(self):
        if self.nota < 5:
            print("Ha suspendido")
        else:
            print("Ha aprobado")

alumno1 = Alumno("Jennifer",8)
alumno1.resultados()
alumno1.calculo()

alumno2 = Alumno("David",4)
alumno2.resultados()
alumno2.calculo()

alumno3 = Alumno("Mary",10)
alumno3.resultados()
alumno3.calculo()