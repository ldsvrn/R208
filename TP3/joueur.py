import re


class Joueur:
    def __init__(self, name="", email="", guerriers = []):
        self.__name = name
        self.__guerriers = guerriers
        if Joueur.chk_email(email):
            self.__email = email
        else:
            self.__email = ""

    def __str__(self):
        return f"Joueur: name: {self.__name}, email: {self.__email}, guerriers: {self.__guerriers}"

    @staticmethod
    def chk_email(email) -> bool:
        m = re.compile("^[a-z]+\.[a-z]+@example.com$").match(email)
        if m:
            return True
        else:
            return False

    def set_guerrier_properties(self, idx, name, lvl, artifact):
        try:
            guerrier = self.__guerriers[idx]
            guerrier.set_name(name)
            guerrier.set_lvl(lvl)
            guerrier.artifact(artifact)
        except IndexError:
            print("Oups, ce guerrier n’existe pas")

    def sort_guerrier(self):
        n = len(self.__guerriers)
        for i in range(n - 1):
            for j in range(n - 1):
                current = self.__guerriers[j].get_lvl()
                next = self.__guerriers[j+1].get_lvl()
                if current > next:
                    temp = current
                    self.__guerriers[j].set_lvl(next)
                    self.__guerriers[j+1].set_lvl(temp)

    def is_all_dead(self):
        for i in self.__guerriers:
            if not i.is_dead():
                return False
        return True

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email):
        if Joueur.chk_email(email):
            self.__email = email

    def get_guerriers(self):
        return self.__guerriers

    def add_guerrier(self, guerrier):
        self.__guerriers.append(guerrier)
