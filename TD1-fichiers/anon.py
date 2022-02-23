#!/usr/bin/env python3

def main():
    file = open("file.txt", "r")
    anon = open("anon.txt", "a")
    anon.write("N°Etudiant;Groupe;Note")
    for line in file.readlines()[1:]:
        line = line.rstrip().split(";")
        anon.write(f"\n{line[1]};{line[4]};{line[5]}")
    file.close()
    anon.close()


if __name__ == '__main__':
    main()
