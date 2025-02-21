import radio
from microbit import sleep, display, Image

def MESSAGE():
    movA = [FORWARD , RIGHT , STOP]
    movB = [BACKWARD, LEFT, STOP]
    x = 0
    y = 0
    z = 1000
    w = 500
    if button_a.was_pressed(): and x==0:
        radio.send(drive(movA[x],z)
        x = x+1
        if x > 2:
            x = 0
    elif button_a.was_pressed(): and (x==1 or x==2):
        radio.send(turn(movA[x], w)
        x = x+1
        if x > 2:
            x = 0
    else:
    if button_b.was_pressed(): and y==0:
        radio.send(movB[y],z)
        y = y + 1
        if y > 2:
            y = 0
    elif button_b.was_pressed(): and (y==1 or y==2):
        radio.send(turn(movB[y],w)
        y = y+1
        if y > 2:
            y = 0
def main():
    # String con un identificador del emisor, cámbialo para no coincidir con el
    # de otros microbits que puedan estar transmitiendo cerca de ti
    IDENTIFIER = "Gabi"
    # Periodo de emisión del mensaje, en milisegundos
    PERIOD = 10000

    # Enciende la radio
    radio.on()


    radio.config(channel =7, group = 13, power= 6, queue= 4, length = 32)
    while True:
        # Muestra dos recuadros en pantalla para indicar que va a enviar un mensaje
        display.show(Image.SQUARE_SMALL)
        sleep(1000)
        # Envía el mensaje
        radio.send(IDENTIFIER)
        radio.send(MESSAGE())
        sleep(1000)
        display.clear()
        sleep(PERIOD-1000)  # ya se han esperado 1000ms al mostrar las imágenes

if __name__ == "__main__":
    main()
