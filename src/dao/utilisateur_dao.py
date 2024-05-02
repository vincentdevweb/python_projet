from typing import Iterable, Optional
from src.config.my_connection import MyConnection
from .generique_dao import GenericDao
from src.models.utilisateur import Utilisateur


class UtilisateurDao(GenericDao[Utilisateur]):
    __db = None
    
    def __init__(self) -> None:
        self.__db = MyConnection()
        
    def start(self) -> None:
        self.__db.start()
        
    def commit(self) -> None:
        self.__db.commit()
    
    def close(self) -> None:
        self.__db.close()
        
    def save(self, utilisateur: Utilisateur) -> Utilisateur:
        return self.__db.query("INSERT INTO utilisateur (nom, prenom, email, gender, password, old_password) VALUES (%s,%s,%s,%s,%s,%s)",(utilisateur.name, utilisateur.prenom, utilisateur.email, utilisateur.gender, utilisateur.password, utilisateur.old_password,))

    def update(self, utilisateur: Utilisateur) -> Utilisateur:
        query = "UPDATE utilisateur SET nom = %s, prenom = %s, email = %s, gender = %s, password = %s, old_password = %s WHERE id = %s"
        self.__db.query(query, (utilisateur.name, utilisateur.prenom, utilisateur.email, utilisateur.gender, utilisateur.password, utilisateur.old_password, utilisateur.id))
        return utilisateur
 
    def delete(self, utilisateur: Utilisateur) -> None:
        self.__db.query("DELETE FROM utilisateur WHERE id = %s;", (utilisateur.id,))
 
    def find_all(self) -> Iterable[Utilisateur]:
        return self.__db.query("SELECT * FROM utilisateur", None).fetchall()
 
    def find_by_id(self, id: int) -> Optional[Utilisateur]:
        return self.__db.query("SELECT * FROM utilisateur WHERE id = %s", (id,)).fetchone()