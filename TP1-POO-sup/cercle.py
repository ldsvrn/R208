from points import Point
import math


class Cercle:
    def __init__(self, centre: Point, arg):
        self.centre = centre
        if isinstance(arg, Point):
            self.rayon = arg.distance(arg.x, arg.y)
        else:
            self.rayon = arg

    def get_diametre(self) -> float:
        return float(self.rayon * 2)

    def get_perimetre(self) -> float:
        return float(2 * math.pi * self.rayon)

    def get_surface(self) -> float:
        return float(math.pi * self.rayon**2)

    def is_intersect(self, cercle) -> bool:
        return self.centre.distancefrom(cercle.centre) < self.rayon + cercle.rayon