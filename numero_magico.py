import random

def numero_magico():
    vidas= 3
    numero= random.randit(0,100)

    while vidas > 0:
        seleccion_usuario= int(input("ingrese un numero: "))

        if seleccion_usuario == numero:
            print(f"Acercate, el numero es{numero}")
            break
    
    else:
        vidas= vidas -1
        print("perdiste una vida, sigue intentando. . . ")
if __name__== "__main__":
    numero_magico()
    