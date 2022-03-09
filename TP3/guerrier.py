import random
import re

class Guerrier:
    def __init__(self, name="", lvl=1, artifact=0):
        if Guerrier.chk_name(name):
            self.__name = name
        else:
            self.__name = ""
        self.__lvl = lvl
        self.__hp = lvl
        self.__artifact = artifact

    def __str__(self):
        return f"Guerrier: name: {self.__name}, lvl: {self.__lvl}, hp: {self.__hp}, artifact: {self.__artifact}"

    @staticmethod
    def chk_name(name) -> bool:
        m = re.compile("^guerrier_[a-zA-Z]+[0-9]*$").match(name)
        if m:
            return True
        else:
            return False

    def damage(self, damage):  # On empêche les hp d'être inférieur à 0
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0

    def attack(self, other):  # Attaque de base = lvl/2 + buff de l'artefact random
        buff = random.randint(self.__artifact/2, self.__artifact)
        other.damage(int((self.__lvl/2) * (100 + buff) / 100))

    def heal(self):
        self.__hp = self.__lvl

    def combat(self, other):
        while not self.is_dead() and not other.is_dead():
            if random.randint(1, 2) == 1:
                self.attack(other)
            else:
                other.attack(self)

        if self.is_dead():
            return other.get_name()
        else:
            return self.__name

    def is_dead(self) -> bool:
        return self.__hp <= 0

    def get_name(self) -> str:
        return self.__name

    def get_lvl(self) -> int:
        return self.__lvl

    def set_lvl(self, lvl):
        self.__lvl = lvl

    def get_hp(self) -> int:
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp

    def get_artifact(self) -> int:
        return self.__artifact

    def set_artifact(self, artifact):
        self.__artifact = artifact
