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

def poligonos (t, l, a):
    for i in range(2):
        t.forward(l)
        t.left(90)
        t.forward(a)
        t.left(90)

def movimiento(t,l,a, x,y,z):
    t.penup()
    t.goto(-x,-x)
    t.pendown()
    poligonos(t, l, a)
    t.penup()
    t.goto(-x,y)
    t.pendown()
    poligonos(t, l, a)
    t.penup()
    t.goto(z,-x)
    t.pendown()
    poligonos(t, l, a)
    t.penup()
    t.goto(z,y)
    t.pendown()
    poligonos(t, l, a)

def rectangulos ():
    gabi= turtle.Turtle()
    gabi.color("green") 
    gabi.pensize(5)
    gabi.shape("turtle")
    movimiento(gabi,100,50,390,340,290)

def cuadrados ():
    gabi= turtle.Turtle()
    gabi.color("blue")
    gabi.pensize(2)
    gabi.shape("triangle")
    movimiento(gabi,60,60,390,330,330)

def finish (window):
    """Espera a que se haga click en window para cerrar la ventana 
    Se debe llamar al final de un programa que use turtle.
    Parámetros: una ventana creada con turtle"""

    window.exitonclick()  

