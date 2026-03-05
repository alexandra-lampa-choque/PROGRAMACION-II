from funciones import promedio, desviacion
if __name__ == "__main__":
    print("Ingrese 10 numeros:")
    entrada = input()  
    numeros = list(map(float, entrada.split())) 
    prom = promedio(numeros)
    des = desviacion(numeros)
    print("El promedio es", round(prom, 2))
    print("La desviación estándar es", round(des, 5))