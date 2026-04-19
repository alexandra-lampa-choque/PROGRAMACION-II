from juego1 import JuegoAdivinaNumero
from juego2 import JuegoAdivinaNumero2, JuegoAdivinaPar, JuegoAdivinaImpar

def main():
    print("\n========= JUEGO 1 =========")
    juego1 = JuegoAdivinaNumero(3)
    juego1.juega()

    print("\n========= JUEGO 2 =========")
    
    print("\n--- Normal ---")
    juego2 = JuegoAdivinaNumero2(3)
    juego2.juega()

    print("\n--- Par ---")
    juegoPar = JuegoAdivinaPar(3)
    juegoPar.juega()

    print("\n--- Impar ---")
    juegoImpar = JuegoAdivinaImpar(3)
    juegoImpar.juega()


if __name__ == "__main__":
    main()