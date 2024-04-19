from application import registrator as reg

import os

class UserManagement(reg.Registrator):
        def __init__(self):
                pass
        
        def runapp():
                while True:
                        print(chr(27)+"[0;34m"+f"{10*'*'}"+" GESTION DE USUARIOS "+f"{10*'*'}")
                        print("Escoga una opción:\n")
                        print("1) Para registrar usuario\n2) Consultar usuarios registrados\n3) Eliminar usuario\n4) Actualizar usuario\n5) Salir")
                        print(f"{10 * '*'}*******************{10 * '*'}")
                        option = int(input("Ingresa el numero: "))
                        if option == 1:
                                os.system("cls")
                                user = input("Ingresa el nombre del usuario: ")
                                UserManagement.registerUser(user)
                        elif option == 2:
                                UserManagement.allUser()
                        elif option == 3:
                                os.system("cls")
                                print("Usuarios registrados en sistema: \n")
                                cantUser = UserManagement.allUser()
                                if cantUser == 'NoneType':
                                        pass
                                else:
                                        id = int(input("Ingresa el número de id del usuario a eliminar: "))
                                        UserManagement.deleteById(id)
                        elif option == 4:
                                os.system("cls")
                                UserManagement.updateUser()
                        elif option == 5:
                                os.system("cls")
                                print(chr(27)+"[1;36m"+"Hasta luego fue un gusto poder ayudarte")
                                bd.connectBD.closeConectDB
                                break 
                        else:
                                os.system("cls")
                                print("Opción no valida")