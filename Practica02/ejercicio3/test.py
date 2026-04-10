from mi_punto import MiPunto
from algebra_vectorial import AlgebraVectorial
from vector import Vector

# PARTE 1
print("=== MiPunto ===")
p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print("Distancia:", p1.distancia(p2))
print("Distancia con x,y:", p1.distancia_xy(10, 30.5))

# PARTE 2
print("\n=== AlgebraVectorial ===")
a = AlgebraVectorial(1, 2, 3)
b = AlgebraVectorial(2, 4, 6)

print("Perpendicular:", a.perpendicular3(b))
print("Paralela:", a.paralela2(b))
print("Proyección:", a.proyeccion(b))
print("Componente:", a.componente(b))

# PARTE 3
print("\n=== Vector ===")
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Suma:", v1 + v2)
print("Escalar:", v1.escalar(2))
print("Magnitud:", v1.magnitud())
print("Normal:", v1.normal())
print("Producto punto:", v1.producto_punto(v2))
print("Producto cruz:", v1.producto_cruz(v2))