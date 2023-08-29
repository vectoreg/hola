import turtle

import random



# configurar la ventana

pantalla= turtle.Screen()

pantalla.title("JUEGO DE LA TORTUGA")

pantalla.bgpic("fondo (3).png")

pantalla.setup(width=800, height=600)



# crear la tortuga

tortuga= turtle.Turtle()

tortuga.shape("turtle")

tortuga.color("green")

tortuga.penup()



# crear gemas

objetos = []

num_objetos = 6

for _ in range(num_objetos):

    gema= turtle.Turtle()

    gema.shape("circle")

    gema.color("blue")

    gema.penup()

    gema.goto(random.randint(-300, 300),random.randint(-150,70))

    objetos.append(gema)

   

obstaculos= []

num_obstaculos= 10

for _ in range(num_obstaculos):

    obstaculo= turtle.Turtle()

    obstaculo.shape("square")

    obstaculo.color("red")

    obstaculo.penup()

    obstaculo.goto(random.randint(-300, 300),random.randint(-150,70))

    obstaculos.append(obstaculo)

   

# variable global

score= 0

puntaje= turtle.Turtle()

puntaje.color("white")

puntaje.penup()

puntaje.hideturtle()

puntaje.goto(0, 250)

puntaje.write(f"PUNTAJE: {score}",font=("Arial",24, "bold"))

game_over= False



# Funciones

def mover_tortuga():

    """ esta funcion tiene como objetivo mover la tortuga para atrapar las gemas"""



    global score

    tortuga.forward(20) #se moverá cada 20 pixeles

    score += 1 #cuando se mueva la tortuga le asignamos un punto y cuando la atrape son 10



def girar_izquierda():

    """ """

    tortuga.left(30) #en un angulo de 30 grados



def girar_derecha():

    """ """

    tortuga.right(30)



# Manejo de errores en módulos



pantalla.onkeypress(mover_tortuga, "Up")

pantalla.onkeypress(girar_izquierda, "Left")

pantalla.onkeypress(girar_derecha, "Right")

pantalla.listen()



while game_over == False: #mientras game sea falso esto se ejecuta y true para romper el bucle

    for gema in objetos:

        if tortuga.distance(gema) < 20:# distancia tortuga con la gema me suma puntos menos de 20

            gema.goto(random.randint(-300, 300), random.randint(-150, 70))

            score += 10

            puntaje.clear()

            puntaje.write(f"Puntaje: {score}",font=("Arial",24,"bold"))

    for obstaculo in obstaculos:

        if tortuga.distance(obstaculo) < 20:

            game_over = True

            pantalla.done() #para cerrar la pantalla

    pantalla.update() #para actualizar la pantalla




# Mantener la ventana abierta hasta que el usuario la cierre

pantalla.mainloop()