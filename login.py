def registrar():
    usuario= "vectoreg"
    contraseña= "elnoob567"

    nombre_usuario= input("ingrese su nombre usuario: ")
    password= input("ingrese la contraseña: ")

    if usuario == nombre_usuario and contraseña == password:
        return True
    else:
        return False
    
if __name__ == "__main__":
    registrar()

