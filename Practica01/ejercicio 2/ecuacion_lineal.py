class EcuacionLineal:
    
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def tieneSolucion(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return determinante != 0

    # x
    def getX(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return (self.__e * self.__d - self.__b * self.__f) / determinante

    # y
    def getY(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return (self.__a * self.__f - self.__e * self.__c) / determinante