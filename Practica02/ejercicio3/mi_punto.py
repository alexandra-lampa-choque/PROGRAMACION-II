import math

class MiPunto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distancia(self, otro):
        return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)

    def distancia_xy(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)