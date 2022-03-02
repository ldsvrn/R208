class Patisserie:
    __createur = "ratatouille"

    def __init__(self, poids = 0, categorie = None):
        self.__poids = poids
        self.__cat = categorie

    def __str__(self) -> str:
        return f"Patisserie: poids={self.__poids}, categorie={self.__cat}"

    @staticmethod
    def get_cat_autorise():
        return ["gateau", "tarte"]

    # Accesseurs:
    def get_poids(self) -> float:
        return self.__poids

    def set_poids(self, poids):
        self.__poids = poids

    def get_cat(self) -> str:
        return self.__cat

    def set_cat(self, cat):
        self.__cat = cat

    @classmethod
    def get_createur(cls) -> str:
        return cls.__createur

    @classmethod
    def set_createur(cls, createur):
        cls.__createur = createur