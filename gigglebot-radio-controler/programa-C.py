from microbit import *
import gigglebot
import radio

longitud_max=90

def movimiento(threshold, left, right, str_movimientos):
    threshold = 110
    strip = gigglebot.init()
    gigglebot.set_speed(70, 70)
    if left < threshold and right < threshold:
            # ambos sensores detectan la linea
        strip[2]=(0,255,0)
        strip[8]=(0,255,0)
        strip.show()
        gigglebot.drive(gigglebot.FORWARD,70)
        str_movimientos = str_movimientos + "f"
        sleep(100)

    elif right > threshold and left < threshold:
            # solo el sensor derecho detecta la linea
        strip[2]=(0,255,0)
        strip[8]=(0,0,0)
        strip.show()
        gigglebot.turn(gigglebot.RIGHT,70)
        str_movimientos = str_movimientos + "r"
        sleep(100)

    elif left > threshold and right < threshold:
    # solo el sensor izquierdo detecta la linea
        strip[2]=(0,0,0)
        strip[8]=(0,255,0)
        strip.show()
        gigglebot.turn(gigglebot.LEFT,70)
        str_movimientos = str_movimientos + "l"
        sleep(100)

    else:
        strip[2] = (0, 0, 0)
        strip[8] = (0, 0, 0)
        strip.show()
        gigglebot.stop()

    return str_movimientos


def main():
    identifier = "Gabi"
    period = 10000
    # Enciende la radio
    radio.on()
    radio.config(channel=7, group=34, power=6, queue=3, length=32)
    right , left = 50,50
    str_movimientos= ""
    movimiento (threshold, left, right, str_movimientos)
    while True:
        try :
            while len(str_movimientos) < longitud_max:
                left,right = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)
                str_movimientos = movimiento(threshold, left, right, str_movimientos)
        except OSError:
            pass

        radio.send(str_movimientos)
        display.scroll("sent")
        sleep(1000)

if __name__ == "__main__":
    main()

