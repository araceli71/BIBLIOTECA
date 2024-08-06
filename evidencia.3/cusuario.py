nombre_usuario = ""
contraseña_usuario = ""

def usuario():
    global nombre_usuario, contraseña_usuario
    nombre_usuario = input("Nombre: ")
    email = input("Email: ")
    contraseña_usuario = input("Contraseña: ")

def retiro():
    vnombre = input("Ingrese su nombre de usuario: ")
    vcontraseña = input("Ingrese su contraseña: ")

    if vnombre in nombre_usuario and vcontraseña in contraseña_usuario:
        libro= input('libro:')
        fechaderetiro= input('fecha de retiro:')
        fechadevuelta= input('fecha de vuelta:')
        print ("Todo correcto.Gracias por venir a la biblioteca")
    else:
        print("Nombre de usuario o contraseña incorrectos.")