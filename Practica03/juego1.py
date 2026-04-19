import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        print("\n--- Nueva Partida ---")

    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Vidas restantes:", self.numeroDeVidas)
        
        if self.numeroDeVidas > 0:
            return True
        else:
            print("Sin vidas")
            return False


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while True:
            print("Adivina un número entre 0 y 10:")
            intento = int(input())

            if intento == self.numeroAAdivinar:
                print("🎉 Acertaste!!")
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