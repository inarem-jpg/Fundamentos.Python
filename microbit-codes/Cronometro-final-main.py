from microbit import *

#esto define los leds que se encenderán para mostrar cada número.
zero = "99999:99999"
one  = "00000:99999"
two = "90999:99909"
three = "90909:99999"
four = "99900:09999"
five = "99909:90999"
six = "99999:90999"
seven = "90900:99999"
eight = "99099:99099"
nine = "99900:99999"

nums = (zero,one,two,three,four,five,six,seven,eight,nine)

#esta función define los numeros de un digito.
def showtime(time):
    if time >= 10:
        time = dos_nums(time)

    A = -1
    B = 0
    numero = nums[time]
    numerosplit = numero.split(":")

    for i in range(3 , 5):
        for x in range(0 , 5): 
            A = A +1
            B = B
            
            if A == 5:
                A = 0
                B = 1 
                
            display.set_pixel(i, x, int(numerosplit[B][A]))
            
#esta funcion define los numeros de dos digitos.
def dos_nums(time):
    st_sec = str(time)
    a = int(st_sec[0])
    b = int(st_sec[1])  
    numeroa = nums[a]
    numeroa_sp = numeroa.split(":")
    A = -1
    B = 0

    
    for i in range(0 , 2):
        for x in range(0 , 5):
            A = A + 1
            B = B
            if A == 5:
                A = 0
                B = 1
                
            display.set_pixel (i , x, int(numeroa_sp[B][A]))
            
    time = b
    return time 

# en la funcion main definiremos el cronometro en si, lo que pasa cuando se pulsan los botones y
#cuenta el tiempo.
def main():
    sec = 0
    min = 0
    horas = 0
    true = 1
    
    while true == 1:
        for i in range(0,5):
            for x in range(0,5):
                display.set_pixel(i,x,0)
        
        if button_a.was_pressed():
            time = horas
            showtime(time)
            
        elif button_b.was_pressed():
            time = min
            showtime(time)

        else:
            time = sec
            showtime(time)

        if sec == 60:
            sec = 0
            min = min + 1

        if min == 60:
            min = 0 
            horas = horas + 1

        sleep(1000)
        sec = sec + 1

if __name__ == "__main__":
    main()
