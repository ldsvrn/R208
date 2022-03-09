#!/usr/bin/env python3
import sys

from guerrier import Guerrier
from joueur import Joueur


def main():
    g1 = Guerrier("guerrier_test1", 30)
    g2 = Guerrier("guerrier_test2", 2)
    player = Joueur("test", "test.testing@example.com", [g1, g2])
    print(player)
    player.add_guerrier(Guerrier("guerrier_test3", 10))
    for i in player.get_guerriers():
        print(i)

    print("")

    player.sort_guerrier()
    print(player)
    for i in player.get_guerriers():
        print(i)
    return 0


if __name__ == '__main__':
    sys.exit(main())
