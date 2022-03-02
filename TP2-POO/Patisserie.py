import pickle


class Patisserie:
    __createur = "ratatouille"

    def __init__(self, poids = 0, categorie = None):
        self.__poids = poids
        if categorie in self.get_cat_autorise():
            self.__cat = categorie
        else:
            self.__cat = None

    def __str__(self) -> str:
        return f"Patisserie: poids={self.__poids}, categorie={self.__cat}, createur={self.__createur}"

    def __eq__(self, other):
        return self.__poids == other.__poids

    def __add__(self, other):
        if self.__cat == other.__cat:
            return Patisserie(self.__poids + other.__poids, self.__cat)
        else:
            return Patisserie(self.__poids + other.__poids, None)

    def sauvegarder(self, chemin):
        with open(chemin, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def charger(chemin):
        with open(chemin, "rb") as file:
            return pickle.load(file)

    @staticmethod
    def get_cat_autorise():
        return ["gateau", "tarte"]

    # Accesseurs:
    def get_poids(self) -> int:
        return self.__poids

    def set_poids(self, poids):
        self.__poids = poids

    def get_cat(self) -> str:
        return self.__cat

    def set_cat(self, cat):
        self.__cat = cat

    def get_createur(self) -> str:
        return self.__createur

    def set_createur(self, createur):
        self.__createur = createur

    @classmethod
    def get_createur_cls(cls) -> str:
        return cls.__createur

    @classmethod
    def set_createur_cls(cls, createur):
        cls.__createur = createur