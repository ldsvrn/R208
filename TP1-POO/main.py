#!/usr/bin/env python3

import sys
from voiture import Voiture


def main():
    myCar = Voiture("Mercedes", "Classe A", 340, "rouge")
    empty = Voiture()

    # Ne fonctionne pas car l'attribut est privé
    try:
        print(myCar.__modele)
    except AttributeError:
        pass

    print(myCar)
    # Avant la modification de __str__:
    # <voiture.Voiture object at 0x7faf700382e0>

    # Après la modif:
    # voiture: Mercedes, Classe A, 340 ch

    myCar.add_option("gps")
    myCar.add_option("volant chauffant")
    print(myCar)
    print(myCar.is_option_present("gps"))

    myCar.remove_option("gps")
    print(myCar)
    print(myCar.is_option_present("gps"))

    myCar.set_options(["Hello", "World"])
    print(myCar.get_options())
    return (0)


if __name__ == "__main__":
    sys.exit(main())
