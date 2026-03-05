import time

class Cronometro:

    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = 0
    def getInicia(self):
        return self.__inicia
    def getFinaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time()
    def detener(self):
        self.__finaliza = time.time()
    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000
    