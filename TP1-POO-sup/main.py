#!/usr/bin/env python3

from formes import Point


def main():
    point = Point((6.5, 6))
    print(point.distance((5, 5)))


if __name__ == '__main__':
    main()
