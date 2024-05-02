from typing import Iterable, Optional
from config.my_connection import MyConnection
from dao.generique_dao import GenericDao
from models.utilisateur import Utilisateur


class UtilisateurDao(GenericDao[Utilisateur]):
    __db = None
    
    def __init__(self) -> None:
        self.__db = MyConnection()
        
    def save(self, utilisateur: Utilisateur) -> Utilisateur:
        pass
 
    def update(self, utilisateur: Utilisateur) -> Utilisateur:
        pass
 
    def delete(self, utilisateur: Utilisateur) -> None:
        self.__db.query("DELETE FROM utilisateur WHERE id = %s;", (utilisateur.id,))
 
    def find_all(self) -> Iterable[Utilisateur]:
        return self.__db.query("SELECT * FROM utilisateur", None).fetchall()
 
    def find_by_id(self, id: int) -> Optional[Utilisateur]:
        return self.__db.query("SELECT * FROM utilisateur WHERE num = %s", (id,)).fetchone()