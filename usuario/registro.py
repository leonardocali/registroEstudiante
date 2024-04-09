from programa import conexionBD as bd
import os

def registro_usuario(user):
    #Inicio del proceso
    os.system("cls")
    inicial = bd.connectBD()
    result = inicial.execute_query("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users';")

    if len(result)<1:
        proceso_1 = inicial
        proceso_1.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);')
        print(chr(27)+"[3;31m"+"Se creó la tabla users correctamente")
    
    #Se registra usuario
    proceso_2 = inicial
    usuarios_registrados = proceso_2.execute_query(f"SELECT name FROM users where name = '{user}'")
    if len(usuarios_registrados)<1:
        proceso_2.execute_query(f"INSERT INTO users (name) VALUES ('{user}')")
        print(chr(27)+"[3;31m"+f"Usuario {user} creado correctamente en tabla users\n")
    else:
        print(chr(27)+"[3;31m"+f"Usuario {user} ya se encuentra creado\n")