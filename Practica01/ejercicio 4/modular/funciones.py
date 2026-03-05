import math
def promedio(lista):
    suma = sum(lista)
    return suma / len(lista)
def desviacion(lista):
    prom = promedio(lista)
    suma = 0
    for x in lista:
        suma += (x - prom) ** 2
    return math.sqrt(suma / (len(lista) - 1))