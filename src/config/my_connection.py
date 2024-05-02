from .db_config import load
import mysql.connector

class MyConnection:
    
    __connection = None
    __cursor = None
    
    def __init__(self):
        __datasource = load()
        self.__connection = mysql.connector.connect(**__datasource)
        self.__cursor = self.__connection.cursor()
    
    def start_transaction(self):
        self.__connection.start_transaction()
        
    def query(self, sql_request: str, params: list) -> None:
        self.__cursor.execute(sql_request, params)
        return self.__cursor
    
    def rollback(self, sql_request: str, params: list) -> None:
        self.__cursor.execute(sql_request, params)
        self.__connection.rollback()
        return self.__cursor

    def close_and_commit(self):
        self.__connection.commit()
        self.__cursor.close()
        self.__connection.close()