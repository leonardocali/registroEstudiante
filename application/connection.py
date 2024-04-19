import sqlite3
from application import singleton as sin 

class Connection(sin.Singleton):
    
    def __init__(self):
        pass
    
    def execute_query(query):
        connect = sqlite3.connect('usuarios.db')
        
        if query[0].upper() == 'I':
            cursor = connect.cursor()
            cursor.execute(query)
            connect.commit()
        elif query[0].upper() == 'S':
            cursor = connect.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        else:
            cursor = connect.cursor()
            cursor.execute(query)
            connect.commit()
    
    def closeConectDB():
        connect.close()