import math

class Vector:

    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __add__(self, o):
        return Vector(self.a1 + o.a1, self.a2 + o.a2, self.a3 + o.a3)

    def escalar(self, r):
        return Vector(r*self.a1, r*self.a2, r*self.a3)

    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def normal(self):
        m = self.magnitud()
        return Vector(self.a1/m, self.a2/m, self.a3/m)

    def producto_punto(self, o):
        return self.a1*o.a1 + self.a2*o.a2 + self.a3*o.a3

    def producto_cruz(self, o):
        return Vector(
            self.a2*o.a3 - self.a3*o.a2,
            self.a3*o.a1 - self.a1*o.a3,
            self.a1*o.a2 - self.a2*o.a1
        )

    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"