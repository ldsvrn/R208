import math


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x} y: +{self.y}"

    def distance(self, x, y) -> float:
        return math.sqrt((x - self.x)**2 + (y - self.y)**2)

    def distancefrom(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
