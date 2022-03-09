import re


class Joueur:
    def __init__(self, name="", email=""):
        self.__name = name
        if Joueur.chk_email(email):
            self.__email = email
        else:
            self.__email = ""

    @staticmethod
    def chk_email(email) -> bool:
        m = re.compile("^[a-z]+\.[a-z]+@example.com$").match(email)
        if m:
            return True
        else:
            return False
