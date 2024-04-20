from application import user_management as um
from application.registrator import Registrator
from application.connection import Connection

if __name__ == '__main__':
    registrator = Registrator(
        connection=Connection())

    #Sin los paréntesis, Python trataría a UserManagement como una referencia a la clase misma,
    # no como una instancia de la misma.
    runapp = um.UserManagement(
        registrator=registrator)

    runapp.runapp()
