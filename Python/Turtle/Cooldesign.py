import turtle

pantalla = turtle.Screen()
pantalla.title("Espiral")
pantalla.bgcolor("black")

def espiral(sides, turn, color, width):

    t=turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range (sides):
        t.forward(n)
        t.right(turn)

espiral(500, 60, "orange", 5)