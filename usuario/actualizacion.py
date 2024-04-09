from programa import conexionBD as bd
from usuario import consulta as con
import os

def actualizarUser():
    #Inicio del proceso
    os.system("cls")
    con.consulta_usuarios()
    print("")
    id = int(input(chr(27)+"[0;34m"+"Ingresa el Id del usuario a actualizar: "))
    nuevoDato =input("Ingresa el valor para actualizar: ")
    print("")
    inicial = bd.connectBD()
    result = inicial.execute_query(f"SELECT id, name FROM users where id = {id};")
    if len(result)==1:
        result2 = inicial.execute_query(f"SELECT name FROM users where name = '{nuevoDato}';")
        if len(result2)>0:
            print(chr(27)+"[3;31m"+f"El nombre {nuevoDato} ya existe, por favor validar\n")
        else:
            proceso_1 = inicial
            proceso_1.execute_query(f"UPDATE USERS SET NAME = '{nuevoDato}' where id = {id}")
            print(chr(27)+"[3;31m"+f"Se actualizó {result[0][1]} por {nuevoDato} para el id {id} correctamente")
            print("")
    else:
        print(chr(27)+"[3;31m"+f"Id {id} no existe\n")