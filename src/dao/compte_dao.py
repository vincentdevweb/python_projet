from typing import Iterable, Optional
from src.config.my_connection import MyConnection
from .generique_dao import GenericDao
from src.models.compte import Compte


class CompteDao(GenericDao[Compte]):
    __db = None
    
    def __init__(self) -> None:
        self.__db = MyConnection()
        
    def start(self) -> None:
        self.__db.start()
        
    def commit(self) -> None:
        self.__db.commit()
    
    def close(self) -> None:
        self.__db.close()
        
    def save(self, compte: Compte) -> Compte:
        return self.__db.query("INSERT INTO compte (cle, sel, id_utilisateur) VALUES (%s,%s,%s)",(compte.cle, compte.sel, compte.id_utilisateur,))

    def update(self, compte: Compte) -> Compte:
        query = "UPDATE compte SET cle = %s, sel = %s, id_utilisateur = %s WHERE id = %s"
        self.__db.query(query, (compte.cle, compte.sel, compte.id_utilisateur, compte.id))
        return compte
 
    def delete(self, Compte: Compte) -> None:
        self.__db.query("DELETE FROM compte WHERE id = %s;", (Compte.id,))
 
    def find_all(self) -> Iterable[Compte]:
        return self.__db.query("SELECT * FROM compte", None).fetchall()
 
    def find_by_id(self, id: int) -> Optional[Compte]:
        return self.__db.query("SELECT * FROM compte WHERE id = %s", (id,)).fetchone()