#!/usr/bin/env python3
import sys

from guerrier import Guerrier

def main():
    g1 = Guerrier("guerrier_test1", 2)
    g2 = Guerrier("guerrier_test2", 2)
    print(g1.combat(g2))
    print(g1.is_dead(), g2.is_dead())
    return 0


if __name__ == '__main__':
    sys.exit(main())