#!/usr/bin/env python3

from points import Point
from cercle import Cercle


def main():
    point = Point()
    point2 = Point(5, 5)
    print(point2)

    test = Cercle(point, point2)
    print(test.rayon)


if __name__ == '__main__':
    main()
