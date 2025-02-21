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

def poligonos (t, l, a):
    for i in range(2):
        t.forward(l)
        t.left(90)
        t.forward(a)
        t.left(90)    

def movimiento(t,l,a, x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    poligonos(t, l, a)
    t.penup()
    t.goto(x+100,y)
    t.forward(15)
    t.pendown()
    poligonos(t, l, a)
    t.penup()
    t.goto(x+200,y)
    t.forward(35)
    t.pendown()
    poligonos(t, l, a)
    

def cuadrados (l,a,x,y):
    gabi = datos("blue", 10, "turtle")

    for i in range(2):
        movimiento(gabi,l,a,x,y)
        y= y-115
    
        


def finish (window):
    """Espera a que se haga click en window para cerrar la ventana 
    Se debe llamar al final de un programa que use turtle.
    Parámetros: una ventana creada con turtle"""

    window.exitonclick()  

