from application.registrator import Registrator 
from application.connection import Connection

import os

# La gestión de usuarios no debería heredar de `reg.Registrator`,
# sino recibirlo como un objeto en el constructor.
# Recuerda que siempre debes preguntarte si la clase A es una clase B.
# Por ejemplo, ¿la clase Dog (Animal) significa que un perro es un animal? Si es, verdad?
# Pero aquí: la gestión de usuarios no es un registrador, pero sí utiliza un registrador para gestionar sus usuarios.
# La gestión de usuarios puede tener más funcionalidades utilizando tipos adicionales de objetos.
# Por ejemplo, `EmailSender` puede utilizarse para enviar correos electrónicos.
# Entonces, la gestión de usuarios puede recibir tanto `Registrator`
# como `EmailSenders` como objetos en el constructor; son funcionalidades que proporciona la gestión de usuarios.


class UserManagement:
    def __init__(self, registrator: Registrator):
        self.registrator = registrator
        

    def runapp(self):  # Se debe agregar el parámetro self para que la función pueda ser llamada desde una instancia de la clase.
        while True:
                print(chr(27) + "[0;34m" + f"{10 * '*'}" + " GESTION DE USUARIOS " + f"{10 * '*'}")
                print("Escoga una opción:\n")
                print(
                "1) Para registrar usuario\n2) Consultar usuarios registrados\n3) Eliminar usuario\n4) Actualizar usuario\n5) Salir")
                print(f"{10 * '*'}*******************{10 * '*'}")
                option = input("Ingresa el número: ")
                if option.isalnum():
                        if option == "1":
                                #os.system("cls")
                                user = input("Ingresa el nombre del usuario: ")
                                self.registrator.registerUser(user)
                        elif option == "2":
                                self.registrator.allUser()
                        elif option == "3":
                                os.system("cls")
                                print("Usuarios registrados en sistema: \n")
                                cantUser = self.registrator.allUser()
                                if cantUser is None:
                                        pass
                                else:
                                        numberInput = input("Ingresa el número de id del usuario a eliminar:")
                                        self.registrator.deleteById(numberInput)
                        elif option == "4":
                                os.system("cls")
                                cantUser = self.registrator.allUser()
                                if cantUser is None:
                                        pass
                                else:
                                        self.registrator.updateUser()
                        elif option == "5":
                                os.system("cls")
                                print(chr(27) + "[1;36m" + "Hasta luego fue un gusto poder ayudarte")
                                self.registrator.connection.close_connect_db() # De donde llega bd.connectBD? No se ha importado en este archivo.
                                break
                        else:
                                os.system("cls")
                                print("Opción no valida\n")            
