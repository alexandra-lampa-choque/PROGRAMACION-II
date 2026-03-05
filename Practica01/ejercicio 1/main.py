import random
from cronometro import Cronometro

def seleccion(lista):
    n = len(lista)

    for i in range(n - 1):
        minimo = i

        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j

        temp = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = temp

numeros = []

for i in range(100000):
    numeros.append(random.randint(1, 100000))

cronometro = Cronometro()

cronometro.inicia()

seleccion(numeros)

cronometro.detener()

print("Tiempo en milisegundos:", cronometro.lapsoDeTiempo())