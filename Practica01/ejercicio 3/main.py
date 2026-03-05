from ecuacion_cuadratica import EcuacionCuadratica

print("Ingrese a, b, c:")
a, b, c = map(float, input().split())

ecuacion = EcuacionCuadratica(a, b, c)

discriminante = ecuacion.getDiscriminante()

if discriminante > 0:
    print("La ecuación tiene dos raíces",
          ecuacion.getRaiz1(),
          "y",
          ecuacion.getRaiz2())

elif discriminante == 0:
    print("La ecuación tiene una raíz",
          ecuacion.getRaiz1())

else:
    print("La ecuación no tiene raíces reales")