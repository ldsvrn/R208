import math

class Point:
    def __init__(self, coords: tuple = (0, 0)):
        self.__coords = coords

    def get_coords(self) -> tuple:
        return self.__coords

    def set_coords(self, coords: tuple = (0, 0)):
        self.__coords = coords

    def distance(self, point: tuple) -> float:
        return math.sqrt((point[0] - self.__coords[0])**2 + (point[1] - self.__coords[1])**2)