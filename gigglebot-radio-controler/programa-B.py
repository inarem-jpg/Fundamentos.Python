from microbit import *
import radio
def main():
    uart.init(baudrate=115200)
    radio.on()
    radio.config(channel=7,
                 group=34,
                 power=6,
                 queue=3,
                 length=32)

    while True:
        sleep(1000)
        received = radio.receive_full()

        if received != None:
            # Separamos los 3 valores de la tupla. La marca de tiempo no la usaremos
            msg = received[0]
            dBm = received[1]
            ts = received[2]

            # En msg los primeros 3 bytes de la lista son una cabecera que descartamos
            # Convertimos el resto de bytes a un string con codificación UTF8
            msg = str(msg[3:], 'utf8')
            print(msg)

            display.scroll("sent: " + msg)
            display.clear()

if __name__ == "__main__":
    main()
