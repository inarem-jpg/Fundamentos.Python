from microbit import *
import random

display.show(Image('33333:'
                   '33333:'
                   '33333:'
                   '33333:'
                   '33333'))  

numminas = 1
numfilas = 5
numcolumnas = 5 

#En esta función colocaremos la mina en 
#el tablero en un lugar aleatorio

def posicion_minas ():
    mfila = random.randint(0, numfilas - 1)
    mcolumna = random.randint(0, numcolumnas - 1)
    posicion_mina = (mcolumna , mfila)
    print(posicion_mina)
    return posicion_mina

#En esta función nos encargaremos de generar el cursor y de moverlo
#además definiremos lo que puede pasar en una partida
    
def main():
    cursor_fila=2
    cursor_columna=2 
    score = 0
    display.set_pixel(cursor_columna , cursor_fila , 9)
    brillo=3
    
    while cursor_fila != numfilas and cursor_columna!= numcolumnas:
        
        if accelerometer.was_gesture('right'):
            display.set_pixel(cursor_columna , cursor_fila , brillo)
            brillo= display.get_pixel(cursor_columna +1  ,cursor_fila)
            cursor_columna = cursor_columna + 1
            display.set_pixel(cursor_columna , cursor_fila , 9)
            
        if accelerometer.was_gesture('left'):
            display.set_pixel(cursor_columna , cursor_fila , brillo)
            brillo= display.get_pixel(cursor_columna -1 ,cursor_fila)
            cursor_columna = cursor_columna - 1 
            display.set_pixel(cursor_columna , cursor_fila , 9)  
            
        if accelerometer.was_gesture('down'): 
            display.set_pixel(cursor_columna , cursor_fila , brillo)
            brillo= display.get_pixel(cursor_columna,cursor_fila - 1)
            cursor_fila = cursor_fila - 1
            display.set_pixel(cursor_columna , cursor_fila , 9) 
            
        if accelerometer.was_gesture('up'):
            display.set_pixel(cursor_columna , cursor_fila , brillo)
            brillo= display.get_pixel(cursor_columna, cursor_fila + 1)
            cursor_fila = cursor_fila + 1
            display.set_pixel(cursor_columna , cursor_fila , 9)
            
        if button_a.was_pressed():
            if (cursor_columna,cursor_fila) == posicion_minas(): 
                display.scroll('YOU LOSE')
                display.show('score')
                display.show(score)
            elif score == 24:
                display.scroll('YOU WON')
                display.show('score')
                display.show(score)
            else:
                display.set_pixel(cursor_columna , cursor_fila , 0)
                brillo = display.get_pixel(cursor_columna,cursor_fila)
                sleep(250)
                display.set_pixel(cursor_columna , cursor_fila , 9)
                score = score +1
                
               
if __name__ == "__main__":
    main()
