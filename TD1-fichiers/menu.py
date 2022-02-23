#!/usr/bin/env python3

import os

def main():
    while True:
        print("1. Spécifier le nom du fichier à traiter\n"
              "2. Générer un fichier anonymisé\n"
              "3. Afficher le fichier anonymisé\n"
              "4. Afficher la note de l’étudiant en fonction de son numéro d’étudiant\n"
              "5. Afficher la note de l’étudiant en fonction de son nom\n"
              "6. Afficher la ou les notes de l’étudiants en fonction de son prénom\n"
              "7. Afficher les noms, prénoms, numéros dont la note est comprise dans un "
              "intervalle donné par l’utilisateur\n"
              "8. Quitter\n")

        while True:
            try:
                menu = int(input("Entrez votre choix (1-8): "))
                if 1 <= menu <= 8:
                    break
                continue
            except ValueError:
                print("Entrez en nombre entier entre 1 et !")
                continue

        filepath = ""
        anonout = ""

        match menu:
            case 1:
                filepath = input("\n\t- Entrez le nom du fichier: ")
                if not os.path.isfile(filepath):
                    print(f"Le fichier {filepath} n'existe pas!")
                    filepath = ""
                continue

            case 2:
                anonout = input("\n\t- Entrez le nom du fichier à générer (overwrite): ")
                if os.path.exists(anonout):
                    os.remove(anonout)
                anon(filepath, anonout)
                continue

            case 3:
                showfile(anonout)
                continue

            case 4:
                no = input("\n\t- Entrez le N°Etudiant: ")
                print(f"Note de l'étudiant n°{no}: {getgradebyno(filepath, no)}")
                continue

            case 8:
                break

def anon(infile, outfile):
    with open(infile, 'r') as input, open(outfile, 'a') as output:
        output.write("N°Etudiant;Groupe;Note")
        for line in input.readlines()[1:]:
            line = line.rstrip().split(";")
            output.write(f"\n{line[1]};{line[4]};{line[5]}")


def showfile(filepath):
    with open(filepath, "r") as file:
        for lc, line in enumerate(file):
            print(f"Ligne {lc}: {line.rstrip()}")


def getgradebyno(filename, no):
    etu = {}
    with open(filename, 'r') as file:
        for line in file.readlines()[1:]:
            line = line.rstrip().split(";")
            etu[line[1]] = line[5]
    return etu[no]



if __name__ == '__main__':
    main()
