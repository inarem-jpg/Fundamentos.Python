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

def datos (color, size, shape):
    t = turtle.Turtle()
    t.color(color) 
    t.pensize(size)
    t.shape(shape)
    return t

def poligonos (t, l,a):
    for i in range(2):
        t.forward(l)
        t.left(90)
        t.forward(a)
        t.left(90)     

def posicion(t,w):
    t.penup()
    t.right(135)
    t.forward(w)
    t.pendown()
    t.left(135)

def cuadrados (l,a):
    gabi = datos("blue", 3, "turtle")
    gabi.penup()
    gabi.goto(-390,300)
    gabi.pendown()
    for n in range (10):
        poligonos(gabi,l,a)
        posicion(gabi,13.5)
        l= l + 20
        a= a + 20

def cuadrados2 (l,a):
    gabi = datos("blue", 3, "turtle")
    gabi.penup()
    gabi.goto(260,190)
    gabi.pendown()
    for n in range (10):
        poligonos(gabi,l,a)
        posicion(gabi,17.5)
        l= l + 24
        a= a + 24

def finish (window):
    """Espera a que se haga click en window para cerrar la ventana 
    Se debe llamar al final de un programa que use turtle.
    Parámetros: una ventana creada con turtle"""

    window.exitonclick()  

