#!/usr/bin/env python3

def main():
    file = open("file.txt", "r")
    for lc, line in enumerate(file):
        print(f"Ligne {lc}: {line.rstrip()}")
    file.close()


if __name__ == '__main__':
    main()
