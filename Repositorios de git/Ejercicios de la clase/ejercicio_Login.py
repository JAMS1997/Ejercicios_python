def ingresar(correo, contrasena):

    if correo in usuarios and contrasena == contrasenas[usuarios.index(correo)]:
        print("Has iniciado sesión.")
    else:
        print("Usuario o contraseña incorrecta.")

def registrar(correo, contrasena):

    usuarios.append(correo)
    contrasenas.append(contrasena)
    print("Guardado con éxito.")


usuarios = []
contrasenas = []

while True:
    print("Menú:")
    print("1. Ingresar")
    print("2. Registrarse")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        correo = input("Ingrese su correo electrónico: ")
        contrasena = input("Ingrese su contraseña: ")
        ingresar(correo, contrasena)
        break
    elif opcion == "2":
        correo = input("Ingrese su correo electrónico: ")
        contrasena = input("Ingrese su contraseña: ")
        registrar(correo, contrasena)
        break
    else:
        print("Opción inválida. Intente de nuevo.")