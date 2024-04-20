from application import connection as con
from tabulate import tabulate
import os


# De manera similar, `Registrator` no es una `con.Connection` pero utiliza una para realizar sus operaciones.
# Igualmente, aquí deberíamos pasarle un objeto de `con.Connection`.

class Registrator:
    
    def __init__(self, connection: con.Connection):
        self.connection = connection

    def registerUser(self, user):
        os.system("cls")
        query = "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users';"
        result = self.connection.execute_query(query)
        if len(result)<1:
            self.connection.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);')
        else:
            query = f"SELECT name FROM users where name = '{user}'"
            user_register = self.connection.execute_query(query)
            if len(user_register)<1:
                self.connection.execute_query(f"INSERT INTO users (name) VALUES ('{user}')")
                print(chr(27)+"[3;31m"+f"Usuario {user} creado correctamente en tabla users\n")
            else:
                print(chr(27)+"[3;31m"+f"Usuario {user} ya se encuentra creado\n")
    
    def allUser(self):
        result = self.connection.execute_query("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users';")
        if len(result)<1:
            self.connection.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);')
            print("Se creo la tabla users correctamente")
        else:
            #Se consulta usuarios registrados
            user_register = self.connection.execute_query("SELECT * FROM users")
            if (len(user_register)<=0):
                print(f"Sin registro de usuarios...\n")
            elif (len(user_register)==1):
                print(f"Usuario registrado:\n")
                print(tabulate(user_register, headers=['Id','Usuario'],tablefmt='fancy_grid'))
                print("")
            elif (len(user_register)>1):
                print(chr(27)+"[0;32m"+f"Usuarios registrados:\n")
                print(tabulate(user_register, headers=['Id','Usuario'],tablefmt='fancy_grid'))
                print("")

    def deleteById(self, id):
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        result = ""
        for a in id:
            if (a in numbers) == False:
                return
            else:
                result+=a
        id=result
        result = self.connection.execute_query(f"SELECT ID, NAME FROM USERS WHERE id = {id}")
        if len(result)<1:
            print(f"El {id} no se encuentra registrado en el sistemas por favor validar\n")
        else:
            print(chr(27)+"[3;31m"+f"Esta seguro que deseas eliminar el Id {result[0][0]} para el usuario {result[0][1]}")
            print("")
            resp = input("Ingresa 1)Si / 2)No: \n")
            if resp.isalnum():
                if resp == "1":
                    self.connection.execute_query(f"DELETE FROM USERS WHERE ID = {id}")
                    print(f"Se eliminó el Id {result[0][0]} para el usuario {result[0][1]}\n")
                else:
                    print(f"No se eliminó el {id} de la tabla")
                    os.system("cls")
                        
    def updateUser(self):
                #Inicio del proceso
                os.system("cls")
                self.allUser()
                print("")
                id = input(chr(27)+"[0;34m"+"Ingresa el Id del usuario a actualizar: ")
                if id.isalnum():
                    id = int(id)
                    newData =input("Ingresa el valor para actualizar: ")
                    print("")
                    result = self.connection.execute_query(f"SELECT id, name FROM users where id = {id};")
                    if len(result)==1:
                        result2 = self.connection.execute_query(f"SELECT name FROM users where name = '{newData}';")
                        if len(result2)>0:
                                print(chr(27)+"[3;31m"+f"El nombre {newData} ya existe, por favor validar\n")
                        else:
                                self.connection.execute_query(f"UPDATE USERS SET NAME = '{newData}' where id = {id}")
                                print(chr(27)+"[3;31m"+f"Se actualizó {result[0][1]} por {newData} para el id {id} correctamente")
                                print("")
                    else:
                        print(chr(27)+"[3;31m"+f"Id {id} no existe\n")
                else:
                    print("No haz ingresado un id valido, por favor validar")
                    pass
