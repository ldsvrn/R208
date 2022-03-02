#!/usr/bin/env python3

import sys
from Patisserie import Patisserie
from Patissier import Patissier
import pickle


def main():
    pat = Patisserie(250, "tarte")
    pat2 = Patisserie(200, "gateau")

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

    pat.set_poids(200)

    if pat == pat2:
        print("Poids égal!")
    else:
        print("Pas le même poids!")

    print(Patisserie(100, 'gateau') + Patisserie(50, 'gateau'))
    print(Patisserie(100, 'gateau') + Patisserie(50, 'tarte'))

    with open("/tmp/data.pickle", 'wb') as file:
        pickle.dump(pat, file)

    with open("/tmp/data.pickle", 'rb') as file:
        backup = pickle.load(file)

    print("\n\t- Objet récupéré de /tmp/data.pickle:")
    print(backup)

    # a trier:
    patissier = Patissier("Foo", "Bar", [Patisserie(50, 'tarte'), Patisserie(45, 'gateau'), Patisserie(75, 'tarte')])
    print(patissier)
    for i in patissier.get_patisseries():
        print(i)

    print("\n\t- Tri:")
    patissier.tri__patisseries()
    for i in patissier.get_patisseries():
        print(i)

if __name__ == "__main__":
    sys.exit(main())
