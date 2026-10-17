# Solicita un usuario y una contraseña. Compara los datos con valores definidos y permite el acceso si ambos coinciden.

usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("Bienvenido al sistema")
else:
    print("Usuario o contraseña incorrectos")   