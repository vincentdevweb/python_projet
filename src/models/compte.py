class Compte:
    def __init__(self, id: int =0 , cle: str = "", sel: str ="" ,id_utilisateur: int=0):
        self.__id = id
        self.__cle = cle
        self.__sel = sel
        self.__id_utilisateur = id_utilisateur

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def cle(self):
        return self.__cle

    @cle.setter
    def cle(self, value):
        self.__cle = value

    @property
    def sel(self):
        return self.__sel

    @sel.setter
    def sel(self, value):
        self.__sel = value

    @property
    def id_utilisateur(self):
        return self.__id_utilisateur

    @id_utilisateur.setter
    def id_utilisateur(self, value):
        self.__id_utilisateur = value

    def __str__(self) -> str:
        return f"id: {self.__id}, cle: {self.__cle}, sel: {self.__sel}, id_utilisateur: {self.__id_utilisateur}"