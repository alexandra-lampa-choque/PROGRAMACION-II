import math

class AlgebraVectorial:

    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __add__(self, o):
        return AlgebraVectorial(self.a1 + o.a1, self.a2 + o.a2, self.a3 + o.a3)

    def __sub__(self, o):
        return AlgebraVectorial(self.a1 - o.a1, self.a2 - o.a2, self.a3 - o.a3)

    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def producto_punto(self, o):
        return self.a1*o.a1 + self.a2*o.a2 + self.a3*o.a3

    def producto_cruz(self, o):
        return AlgebraVectorial(
            self.a2*o.a3 - self.a3*o.a2,
            self.a3*o.a1 - self.a1*o.a3,
            self.a1*o.a2 - self.a2*o.a1
        )

    def perpendicular1(self, b):
        return abs((self + b).magnitud() - (self - b).magnitud()) < 1e-6

    def perpendicular2(self, b):
        return abs((self - b).magnitud() - (b - self).magnitud()) < 1e-6

    def perpendicular3(self, b):
        return self.producto_punto(b) == 0

    def perpendicular4(self, b):
        return abs((self + b).magnitud()**2 - (self.magnitud()**2 + b.magnitud()**2)) < 1e-6

    def paralela1(self, b):
        if b.a1 != 0:
            r = self.a1 / b.a1
            return self.a2 == r*b.a2 and self.a3 == r*b.a3
        return False

    def paralela2(self, b):
        cruz = self.producto_cruz(b)
        return cruz.a1 == 0 and cruz.a2 == 0 and cruz.a3 == 0

    def proyeccion(self, b):
        escalar = self.producto_punto(b) / (b.magnitud()**2)
        return AlgebraVectorial(b.a1*escalar, b.a2*escalar, b.a3*escalar)

    def componente(self, b):
        return self.producto_punto(b) / b.magnitud()