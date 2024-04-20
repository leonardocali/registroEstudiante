import sqlite3
from application import singleton as sin 


class Connection(sin.Singleton):
    
    def __init__(self):
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
    
    def close_connect_db(self): # Debería ser un método de instancia, no un método de clase. Como va conocer la conexión?
        self.connect.close()    # Los nombres de los métodos deben ser en minúsculas y separados por guiones bajos.
