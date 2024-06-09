# Imprimir de forma bonita 

"""
Uso de la libreria -pprint- para imprimir de forma ordenada y 
bonita el codigo
"""
import pprint

class Vehiculo:

    """ Inicia atributos color,ruedas,puertas """
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    """ Simulacion para mostrar por consola """
    def caracteristicas(self):
        print("color:", self.color, ",ruedas:", self.ruedas, ",puertas:", self.puertas)    

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas,velocidad,cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def caracteristicas(self):
        super().caracteristicas()
        print("velocidad:",self.velocidad,"km/h","Cilindrada",self.cilindrada,"cc")

""" Asignar valores a la clase Coche y su herencia y enseñar por consola """
c1 = Coche("negro","4","5","80","1.000")
c1.caracteristicas()

print("")

c2 = Coche("gris","4","3","100","1.300")
c2.caracteristicas()