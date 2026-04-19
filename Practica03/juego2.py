import random
from juego1 import JuegoAdivinaNumero

class JuegoAdivinaNumero2(JuegoAdivinaNumero):
    
    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while True:
            print("Adivina un número entre 0 y 10:")
            intento = int(input())

            if not self.validaNumero(intento):
                print("Número inválido")
                continue

            if intento == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print("El número es MAYOR")
                    else:
                        print("El número es MENOR")
                else:
                    break


class JuegoAdivinaPar(JuegoAdivinaNumero2):
    def validaNumero(self, num):
        if not (0 <= num <= 10):
            return False
        if num % 2 != 0:
            print("Error: debe ser PAR")
            return False
        return True


class JuegoAdivinaImpar(JuegoAdivinaNumero2):
    def validaNumero(self, num):
        if not (0 <= num <= 10):
            return False
        if num % 2 == 0:
            print("Error: debe ser IMPAR")
            return False
        return True