from .db_config import load_conf
import mysql.connector
# import json

# def load_conf() -> dict:
#     with open('src/config/config.json','r') as f:
#         return json.load(f)['mysql']    
class MyConnection:
    
    __connection = None
    __cursor = None
    
    def __init__(self):
        __datasource = load_conf()
        self.__connection = mysql.connector.connect(**__datasource)
        self.__cursor = self.__connection.cursor()
        
    def query(self, sql_request: str, params: list) -> None:
        self.__cursor.execute(sql_request, params)
        return self.__cursor
    
    def rollback(self, sql_request: str, params: list) -> None:
        self.__cursor.execute(sql_request, params)
        self.__connection.rollback()
        return self.__cursor
    
    def start(self):
        self.__connection.start_transaction()

    def close(self):
        self.__cursor.close()
        self.__connection.close()
    
    def commit(self):
        self.__connection.commit()