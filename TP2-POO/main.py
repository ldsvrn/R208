#!/usr/bin/env python3

import sys
from Patisserie import Patisserie


def main():
    pat = Patisserie()
    pat2 = Patisserie()

    print(pat.get_cat_autorise())

    # print(Patisserie.createur)
    #       retourne ratatouille

    # print(f"{pat.get_createur()} {pat2.get_createur()}")
    # Patisserie.set_createur("test")
    # print(f"{pat.get_createur()} {pat2.get_createur()}")
    # pat.set_createur("test2")
    # print(f"{pat.get_createur()} {pat2.get_createur()}")
    #       cela change le créateur pour les deux instances

    # pat3 = Patisserie()
    # print(f"{pat.get_createur()} {pat2.get_createur()} {pat3.get_createur()}")
    # la nouvelle garde la valeur définie avec set_createur()
    # print(Patisserie.get_createur()) retourne "test2"

    # En gros, self = pour l'instance et cls = pour toute la classe

    if pat == pat2:
        print("Poids égal!")
    else:
        print("Pas le même poids!")

    pat.set_poids(100)

    if pat == pat2:
        print("Poids égal!")
    else:
        print("Pas le même poids!")

    print(Patisserie(100, 'gateau') + Patisserie(50, 'gateau'))
    print(Patisserie(100, 'gateau') + Patisserie(50, 'tarte'))

    return 0


if __name__ == "__main__":
    sys.exit(main())
