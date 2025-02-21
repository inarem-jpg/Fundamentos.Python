####################
# Playing tennis with buttons A & B of microbit
######################

# Imports go at the top
from microbit import *
import random

#función del botón A 
def botonA(rax, ray, Ioff, Imax):
   if button_a.was_pressed():
            display.set_pixel(rax,ray, Ioff)
        
            ray = ray +1
            if ray >4 :
                ray = 0 
            display.set_pixel(rax,ray, Imax)
   return ray

#función del botón B
def botonB(rax, ray, Ioff, Imax):
    if button_b.was_pressed():
            display.set_pixel(rax,ray, Ioff)
            
            ray = ray -1
            if ray < 0:
                ray = 4
            display.set_pixel(rax,ray, Imax)
    return ray

#código principal
def main():
    #intensidades de led
    Imax = 9
    Ioff = 0
    
    Pausa = 1000
    #coordenadas de la raqueta
    rax = 4
    ray = 2
   # cordenada x de la pelota
    pex = 0
    puntos = 0
    
    seguir = True
    
    #bucle principal
    while seguir == True:
        rax = 4
        ray = 2
        pex = 0
        pey = random.randrange(0,5)
        display.set_pixel(rax, ray,Imax)
        display.set_pixel(pex, pey, Imax)
        
        for _ in range(4):
            ray = botonA(rax, ray, Ioff, Imax)
            ray = botonB(rax, ray, Ioff, Imax)
            sleep(Pausa)
            pex = pex +1
            display.set_pixel(pex, pey, Imax)

        display.clear()

        # puntuación
        if rax == pex and ray == pey :
            puntos = puntos +1

        if puntos == 10:
            seguir = False
main()
