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

def posicion(t):
    t.penup()
    t.right(135)
    t.forward(13.5)
    t.pendown()
    t.left(135)


def cuadrados (l,a):
    gabi = datos("black", 5, "turtle")
    gabi.penup()
    gabi.goto(-5,5)
    gabi.pendown()
    for n in range (6):
        poligonos(gabi,l,a)
        posicion(gabi)
        l= l + 20
        a= a + 20

    

def finish (window):
    """Espera a que se haga click en window para cerrar la ventana 
    Se debe llamar al final de un programa que use turtle.
    Parámetros: una ventana creada con turtle"""

    window.exitonclick()  

