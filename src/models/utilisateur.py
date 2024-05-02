class Utilisateur:
    def __init__(self, id: int, name: str, prenom: str, email: str, gender: str, password: str, old_password: str) -> None:
        self.__id = id
        self.__name = name
        self.__prenom = prenom
        self.__email = email
        self.__gender = gender
        self.__password = password
        self.__old_password = old_password

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def old_password(self):
        return self.__old_password

    @old_password.setter
    def old_password(self, value):
        self.__old_password = value

    def __str__(self) -> str:
        return f"id: {self.__id}, name: {self.__name},
                    prenom: {self.__prenom}, email: {self.__email},
                        gender: {self.__gender}, password: {self.__password},
                            old_password: {self.__old_password}"
    