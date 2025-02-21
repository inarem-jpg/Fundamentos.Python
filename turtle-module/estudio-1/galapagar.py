import turtle

def init (title, color, width, height):
    """crea una ventana para poder dibujar el modulo de python turtle
    Parámetros : título, color de fondo, ancho y alto de la ventana 
    creada. Devuelve la ventana creada """

    window = turtle.Screen()
    turtle.setup(width, height)
    window.bgcolor(color)
    window.title(title)

    return window

def cuadrados (t ,l):
    for i in range(4):
        t.forward(l)
        t.left(90)

def movimiento (t):
    t.penup()
    t.goto(-390,-390)
    t.pendown()
    cuadrados(t,50)
    t.penup()
    t.goto(-390,340)
    t.pendown()
    cuadrados(t,50)
    t.penup()
    t.goto(340,-390)
    t.pendown()
    cuadrados(t,50)
    t.penup()
    t.goto(340,340)
    t.pendown()
    cuadrados(t,50)

def losdatos ():
    gabi = turtle.Turtle()
    gabi.color("red")
    movimiento(gabi)

def finish (window):
    """Espera a que se haga click en window para cerrar la ventana 
    Se debe llamar al final de un programa que use turtle.
    Parámetros: una ventana creada con turtle"""

    window.exitonclick()  

