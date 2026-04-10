import math

class Fraccion:
    def __init__(self, a, b):
        self.__numerador = a
        self.__denominador = b

    def __add__(self, o):
        num = self.__numerador * o.__denominador + o.__numerador * self.__denominador
        den = self.__denominador * o.__denominador
        return Fraccion(num, den)

    def __sub__(self, o):
        num = self.__numerador * o.__denominador - o.__numerador * self.__denominador
        den = self.__denominador * o.__denominador
        return Fraccion(num, den)

    def __str__(self):
        return "{}/{}".format(self.__numerador, self.__denominador)

    # ====== INCISO 1 ======
    def __mul__(self, o):
        num = self.__numerador * o.__numerador
        den = self.__denominador * o.__denominador
        return Fraccion(num, den)

    # ====== INCISO 2 ======
    def __truediv__(self, o):
        if o.__numerador == 0:
            raise ZeroDivisionError("No se puede dividir entre una fracción con numerador 0")
        num = self.__numerador * o.__denominador
        den = self.__denominador * o.__numerador
        return Fraccion(num, den)

    # ====== INCISO 3 ======
    def __eq__(self, o):
        return (self.__numerador * o.__denominador ==
                o.__numerador * self.__denominador)

    # ====== INCISO 4 ======
    def convertirADecimal(self):
        if self.__denominador == 0:
            raise ZeroDivisionError("Denominador no puede ser 0")
        return self.__numerador / self.__denominador

    # ====== INCISO 5 ======
    def esInverso(self, o):
        resultado = self * o
        return resultado.__numerador == resultado.__denominador

    # ====== INCISO 6 ======
    @staticmethod
    def parseFraccion(cadena):
        num, den = cadena.split("/")
        return Fraccion(int(num), int(den))

    # ====== INCISO 7 ======
    def simplifica(self):
        mcd = math.gcd(self.__numerador, self.__denominador)
        num = self.__numerador // mcd
        den = self.__denominador // mcd
        return Fraccion(num, den)