from Patisserie import Patisserie

class Patissier:
    def __init__(self, nom=None, prenom=None, patisseries=[]):
        self.__nom = nom
        self.__prenom = prenom
        self.__patisseries = patisseries
        for i in self.__patisseries:
            i.set_createur(f"{self.__nom} {self.__prenom}")

    def __str__(self) -> str:
        return f"Patissier: nom/prenom={self.__nom} {self.__prenom}, patisseries={self.__patisseries}"

    def creer_patisserie(self, poids, categorie):
        pat = Patisserie(poids, categorie)
        pat.set_createur(f"{self.__nom} {self.__prenom}")
        if pat not in self.__patisseries:
            self.__patisseries.append(pat)

    def __eq__(self, other):
        return self.__patisseries == other.__patisseries

    def tri__patisseries(self):
        if self.__is_trier():
            return 0

        n = len(self.__patisseries)
        for i in range(n - 1):
            for j in range(n - 1):
                current = self.__patisseries[j].get_poids()
                next = self.__patisseries[j+1].get_poids()
                if current > next:
                    temp = current
                    self.__patisseries[j].set_poids(next)
                    self.__patisseries[j+1].set_poids(temp)

    def __is_trier(self):
        liste = []
        for i in self.__patisseries:
            liste.append(i.get_poids())

        return sorted(liste) == liste

    def get_patisseries(self):
        return self.__patisseries
