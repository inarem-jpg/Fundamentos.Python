from microbit import *
from gigglebot import *

def main():
    strip = init()
# speed needs to be set according to your line and battery level.
# do not go too fast though.
    set_speed(65, 65)

    threshold = 100
    while True:
        derecha, izda = read_sensor(LINE_SENSOR, BOTH)
        if izda < threshold and derecha < threshold:
        # both sensors detect the line
            strip[2]=(0,255,0)
                    strip[8]=(0,255,0)
                    strip.show()
                    drive(FORWARD)
                elif derecha > threshold and izda > threshold:
                # neither sensor detects the line
                    stop()
                    strip[2]=(255,0,0)
                    strip[8]=(255,0,0)
                    strip.show()
                    break
                elif izda > threshold and derecha < threshold:
               # only the right sensor detects the line
                    strip[2]=(0,255,0)
                    strip[8]=(0,0,0)
                    strip.show()
                    turn(RIGHT)
                elif derecha > threshold and izda < threshold:
                    # only the left sensor detects the line
                    strip[2]=(0,0,0)
                    strip[8]=(0,255,0)
                    strip.show()
                    turn(LEFT)
            stop()

