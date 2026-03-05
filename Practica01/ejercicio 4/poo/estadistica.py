import math

class Estadistica:

    def __init__(self, lista):
        self.lista = lista

    def promedio(self):
        return sum(self.lista) / len(self.lista)

    def desviacion(self):
        prom = self.promedio()
        suma = 0

        for x in self.lista:
            suma += (x - prom) ** 2

        return math.sqrt(suma / (len(self.lista) - 1))