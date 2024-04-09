import sqlite3
from programa import singleton

class connectBD(singleton.Singleton):
    connect = None
    
    def __init__(self):
        if self.connect is None:
            self.connect = sqlite3.connect('usuarios.db')
    
    def execute_query(self, query):
        if query[0].upper() == 'I':
            cursor = self.connect.cursor()
            cursor.execute(query)
            self.connect.commit()
        elif query[0].upper() == 'S':
            cursor = self.connect.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        else:
            cursor = self.connect.cursor()
            cursor.execute(query)
            self.connect.commit()
    
    def closeConectDB(self):
        self.connect.close()