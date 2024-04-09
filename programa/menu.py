from usuario import registro as reg
from usuario import consulta as con
from usuario import actualizacion as act
from programa import conexionBD as bd
import os

def menuP():
    while True:
        print(chr(27)+"[0;34m"+f"{10*'*'}"+" GESTION DE USUARIOS "+f"{10*'*'}")
        #print("(10 * chr(27)+'[*')")
        print("Escoga una opcion:\n")
        print("1) Para registrar usuario\n2) Consultar usuarios registrados\n3) Eliminar usuario\n4) Actualizar usuario\n5) Salir")
        print(f"{10 * '*'}*******************{10 * '*'}")
        opcion = int(input("Ingresa el numero: "))
        if opcion == 1:
            os.system("cls")
            user = input("Ingresa el nombre del usuario: ")
            reg.registro_usuario(user)
        elif opcion == 2:
            con.consulta_usuarios()
        elif opcion == 3:
            os.system("cls")
            print("Usuarios registrados en sistema: \n")
            con.consulta_usuarios()
            id = int(input("Ingresa el número de id del usuario a eliminar: "))
            con.consultaId(id)
        elif opcion == 4:
            os.system("cls")
            act.actualizarUser()
        elif opcion == 5:
            os.system("cls")
            print(chr(27)+"[1;36m"+"Hasta luego fue un gusto poder ayudarte")
            bd.connectBD.closeConectDB
            break
        else:
            os.system("cls")
            print("Opción no valida")
    