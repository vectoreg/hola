import login
import numero_magico

def principal():
    print("bienvenidos al juego de numero magico")

    if login():
        numero_magico()

    else:
        print("vuelve a ingresar")