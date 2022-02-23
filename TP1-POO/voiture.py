class Voiture:
    def __init__(self, marque = None,  modele = None, chevaux = 0, couleur = None, options = []):
        self.__marque = marque
        self.__modele = modele
        self.__chevaux = chevaux
        self.__couleur = couleur
        self.__options = options

    def __str__(self):
        return f"voiture: {self.__marque}, {self.__modele}, {self.__chevaux} ch, {self.__couleur}, " \
               f"options: {self.__options}"

    def get_model(self):
        return self.__modele

    def get_brand(self):
        return self.__marque

    def get_hp(self):
        return self.__chevaux

    def get_color(self):
        return self.__couleur

    def get_options(self):
        return self.__options

    def set_model(self, model):
        self.__modele = model

    def set_brand(self, brand):
        self.__marque = brand

    def set_hp(self, hp):
        self.__chevaux = hp

    def set_options(self, options = []):
        self.__options = options

    def add_option(self, opts):
        self.__options.append(opts)

    def remove_option(self, opts):
        self.__options.remove(opts)

    def is_option_present(self, opts):
        return opts in self.__options