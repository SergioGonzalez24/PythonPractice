import turtle
import time
import random

tiempo = 0.1

score=0
high_score=0

pantalla = turtle.Screen()
pantalla.title("Snake")
pantalla.bgcolor("black")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)

#Cabeza de Serpiente
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida de Serpiente
comida=turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.color("white")
comida.penup()
comida.goto(0,100) 

#Cuerpo
segmentos = []

#Text
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0               High Score: 0  ", align="center", font=("Courier",24,"normal"))


#Funciones 
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right" 

def mov(): 
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20)

#Teclado
pantalla.listen()
pantalla.onkeypress(arriba,"Up")
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(izquierda,"Left")
pantalla.onkeypress(derecha,"Right")

while True:
 
    pantalla.update()

    #choques
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #hide
        for segmento in segmentos:
            segmento.goto(1000,1000)

        #limpiar segmentos
        segmentos.clear()

        #reset marcador
        score=0
        texto.clear()
        texto.write("Score: {}            High Score: {}  ".format(score,high_score), align="center", font=("Courier",24,"normal"))



    if cabeza.distance(comida)<15:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento=turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("white")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #aumentar puntaje
        score+=10

        if score > high_score:
            high_score=score

        texto.clear()
        texto.write("Score: {}            High Score: {}  ".format(score,high_score), align="center", font=("Courier",24,"normal"))

    #movimiento serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1,0,-1):
        x=segmentos[index-1].xcor()
        y=segmentos[index-1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg>0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #Choques de Cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            for segmento in segmentos:
                segmento.goto(1000,1000)

            segmentos.clear()
            
            #reset marcador
            score=0
            texto.clear()
            texto.write("Score: {}            High Score: {}  ".format(score,high_score), align="center", font=("Courier",24,"normal"))


        




 
    time.sleep(tiempo)
 
