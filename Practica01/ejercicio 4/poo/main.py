from estadistica import Estadistica
if __name__ == "__main__":
    print("Ingrese 10 números:")
    entrada = input() 
    numeros = list(map(float, entrada.split()))  
    est = Estadistica(numeros)
    print("El promedio es", round(est.promedio(), 2))
    print("La desviación estándar es", round(est.desviacion(), 5))