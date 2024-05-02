from typing import Iterable, Optional
from config.my_connection import MyConnection
from dao.generique_dao import GenericDao
from models.compte import Compte


class CompteDao(GenericDao[Compte]):
    __db = None
    
    def __init__(self) -> None:
        self.__db = MyConnection()
        
    def save(self, Compte: Compte) -> Compte:
        pass
 
    def update(self, Compte: Compte) -> Compte:
        pass
 
    def delete(self, Compte: Compte) -> None:
        self.__db.query("DELETE FROM compte WHERE id = %s;", (Compte.id,))
 
    def find_all(self) -> Iterable[Compte]:
        return self.__db.query("SELECT * FROM compte", None).fetchall()
 
    def find_by_id(self, id: int) -> Optional[Compte]:
        return self.__db.query("SELECT * FROM compte WHERE num = %s", (id,)).fetchone()