from ecuacion_lineal import EcuacionLineal

print("Ingrese a, b, c, d, e, f:")
a, b, c, d, e, f = map(float, input().split())

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")