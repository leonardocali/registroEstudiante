from programa import conexionBD as bd
import os
from tabulate import tabulate
inicial = bd.connectBD()

def consulta_usuarios():
        os.system("cls")
        result = inicial.execute_query("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users';")

        if len(result)<1:
            proceso_1 = inicial
            proceso_1.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);')
            print("Se creo la tabla users correctamente")
        
        #Se consulta usuarios registrados
        if inicial:
            user_register = inicial.execute_query("SELECT * FROM users")
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
        else:
            print("Tabla users no existe")

def consultaId(id):
    result = inicial.execute_query(f"SELECT ID, NAME FROM USERS WHERE id = {id};")
    if len(result)<1:
        print(f"El {id} no se encuentra registrado en el sistemas por favor validar\n")
    else:
        print(chr(27)+"[3;31m"+f"Esta seguro que deseas eliminar el Id {result[0][0]} para el usuario {result[0][1]}")
        print("")
        resp = int(input("Ingresa 1)Si / 2)No: \n"))
        if resp == 1:
            inicial.execute_query(f"DELETE FROM USERS WHERE ID = {id}")
            print(f"Se eliminó el Id {result[0][0]} para el usuario {result[0][1]}\n")
            os.system("cls")
        else:
            print(f"No se eliminó el {id} de la tabla")
            os.system("cls")