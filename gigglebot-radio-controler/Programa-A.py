import image
import time
import serial
import serial.tools.list_ports as list_ports

img_start = image.Image('tesela1.png')
img_curva = image.Image('tesela2.png')
img_linea = image.Image('tesela3.png')
img_wave = image.Image('tesela4.png')
img_t = image.Image('tesela5.png')

win = image.ImageWin(900, 900)

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1

# Look for serial port where micro:bit is connected
def find_comport(pid, vid, baud):
    #return a serial port 
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        print('port: {}'.format(p))
        try:
            print('pid: {} vid: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None

def movimiento_msg1(message):
    #cuenta las veces que aparece f,r o l en un trozo del mensaje, 
    # selecciona la opcion que más aparece, la guarda y crea un nuevo mensaje con todas las opciones más guardadas 
    message1 = message[0:15]
    str_teselas1 = ""
    msg_r = 0
    msg_l = 0
    msg_f = 0
    index = 0
    for i in range(len(message1)):
        if message1[index] == "r":
            msg_r = msg_r + 1 
            index = index + 1

        elif message1[index] == "l":
            msg_l = msg_l + 1
            index = index + 1

        elif message1[index] == "f":
            msg_f = msg_f + 1
            index += 1

    if max(msg_r, msg_l, msg_f) == msg_f:
        str_teselas1 = str_teselas1 + "f"
    elif max(msg_l, msg_f, msg_r ) == msg_l:
        str_teselas1 = str_teselas1 + "l"
    elif max(msg_r, fmsg_f, msg_l) == msg_r:
        str_teselas1 = str_teselas1 + "r"
    else:
        if max(msg_r, msg_l, msg_f) != msg_f and max(msg_r, msg_l, msg_f) != msg_r and max(msg_r, msg_l, msg_f) != msg_l:
            str_teselas1 = str_teselas1 + "w"

    return str_teselas1

def movimiento_msg2(message):
    #cuenta las veces que aparece f,r o l en un trozo del mensaje, 
    # selecciona la opcion que más aparece, la guarda y crea un nuevo mensaje con todas las opciones más guardadas 
    message2 = message[15:30]
    str_teselas2 = ""
    msg_r = 0
    msg_l = 0
    msg_f = 0
    index = 0
    for i in range(len(message2)):
        if message2[index] == "r":
            msg_r = msg_r + 1 
            index = index + 1

        elif message2[index] == "l":
            msg_l = msg_l + 1
            index = index + 1

        elif message2[index] == "f":
            msg_f = msg_f + 1
            index += 1

    if max(msg_r, msg_l, msg_f) == msg_f:
        str_teselas2 = str_teselas2 + "f"
    elif max(msg_l, msg_f, msg_r ) == msg_l:
        str_teselas2 = str_teselas2 + "l"
    elif max(msg_r, fmsg_f, msg_l) == msg_r:
        str_teselas2 = str_teselas2 + "r"
    else:
        if max(msg_r, msg_l, msg_f) != msg_f and max(msg_r, msg_l, msg_f) != msg_r and max(msg_r, msg_l, msg_f) != msg_l:
            str_teselas2 = str_teselas2 + "w"

    return str_teselas2

def movimiento_msg3(message):
    #cuenta las veces que aparece f,r o l en un trozo del mensaje, 
    # selecciona la opcion que más aparece, la guarda y crea un nuevo mensaje con todas las opciones más guardadas 
    message3 = message[30:45]
    str_teselas3 = ""
    msg_r = 0
    msg_l = 0
    msg_f = 0
    index = 0
    for i in range(len(message3)):
        if message3[index] == "r":
            msg_r = msg_r + 1 
            index = index + 1

        elif message3[index] == "l":
            msg_l = msg_l + 1
            index = index + 1

        elif message3[index] == "f":
            msg_f = msg_f + 1
            index += 1

    if max(msg_r, msg_l, msg_f) == msg_f:
        str_teselas3 = str_teselas3 + "f"
    elif max(msg_l, msg_f, msg_r ) == msg_l:
        str_teselas3 = str_teselas3 + "l"
    elif max(msg_r, fmsg_f, msg_l) == msg_r:
        str_teselas3 = str_teselas3 + "r"
    else:
        if max(msg_r, msg_l, msg_f) != msg_f and max(msg_r, msg_l, msg_f) != msg_r and max(msg_r, msg_l, msg_f) != msg_l:
            str_teselas3 = str_teselas3 + "w"

    return str_teselas3

def movimiento_msg4(message):
    #cuenta las veces que aparece f,r o l en un trozo del mensaje, 
    # selecciona la opcion que más aparece, la guarda y crea un nuevo mensaje con todas las opciones más guardadas 
    message4 = message[45:60]
    str_teselas4 = ""
    msg_r = 0
    msg_l = 0
    msg_f = 0
    index = 0
    for i in range(len(message4)):
        if message4[index] == "r":
            msg_r = msg_r + 1 
            index = index + 1

        elif message4[index] == "l":
            msg_l = msg_l + 1
            index = index + 1

        elif message4[index] == "f":
            msg_f = msg_f + 1
            index += 1

    if max(msg_r, msg_l, msg_f) == msg_f:
        str_teselas4 = str_teselas4 + "f"
    elif max(msg_l, msg_f, msg_r ) == msg_l:
        str_teselas4 = str_teselas4 + "l"
    elif max(msg_r, fmsg_f, msg_l) == msg_r:
        str_teselas4 = str_teselas4 + "r"
    else:
        if max(msg_r, msg_l, msg_f) != msg_f and max(msg_r, msg_l, msg_f) != msg_r and max(msg_r, msg_l, msg_f) != msg_l:
            str_teselas4 = str_teselas4 + "w"

    return str_teselas4

def movimiento_msg5(message):
    #cuenta las veces que aparece f,r o l en un trozo del mensaje, 
    # selecciona la opcion que más aparece, la guarda y crea un nuevo mensaje con todas las opciones más guardadas 
    message5 = message[60:75]
    str_teselas5 = ""
    msg_r = 0
    msg_l = 0
    msg_f = 0
    index = 0
    for i in range(len(message5)):
        if message4[index] == "r":
            msg_r = msg_r + 1 
            index = index + 1

        elif message4[index] == "l":
            msg_l = msg_l + 1
            index = index + 1

        elif message4[index] == "f":
            msg_f = msg_f + 1
            index += 1

    if max(msg_r, msg_l, msg_f) == msg_f:
        str_teselas5 = str_teselas5 + "f"
    elif max(msg_l, msg_f, msg_r ) == msg_l:
        str_teselas5 = str_teselas5 + "l"
    elif max(msg_r, fmsg_f, msg_l) == msg_r:
        str_teselas5 = str_teselas5 + "r"
    else:
        if max(msg_r, msg_l, msg_f) != msg_f and max(msg_r, msg_l, msg_f) != msg_r and max(msg_r, msg_l, msg_f) != msg_l:
            str_teselas5 = str_teselas5 + "w"
    
    return str_teselas5

def movimiento_final():
    #junta en un solo string todas las ordenes de movimiento final de las teselas y añade la tesela final "stop"
    str_teselas1 = movimiento_msg1(message)
    str_teselas2 = movimiento_msg2(message)
    str_teselas3 = movimiento_msg3(message)
    str_teselas4 = movimiento_msg4(message)
    str_teselas5 = movimiento_msg5(message)
    str_teselas = str_teselas1 + str_teselas2 + str_teselas3 + str_teselas4 + str_teselas5 + "t"

    return str_teselas

str_teselas = movimiento_final()
print(str_teselas)


def img_giro(imagen, str_teselas):
    #en caso de detectar una curva, gira esta para que tenga la orientacion correcta

    ancho = imagen.getWidth()
    alto = imagen.getHeight()
    new_curva = image.EmptyImage(ancho, alto)

    index = 0
    for i in range(len(str_teselas))
        if message[index] == "l":
            for row in range(ancho):
                for col in range(alto):
                    pixel = imagen.getPixel(col, row)
                    new_col = row
                    new_row = alto - col - 1
                    new_curva.setPixel(new_col, new_row, pixel)
                    index = index + 1
        else:
            index = index +1

    return new_curva

def imgT_giro(image, str_teselas):
    #en caso de detectar una curva, gira esta para que tenga la orientacion correcta

    new_t = image.EmptyImage(100, 100)
    ancho = img_curva.getWidth()
    alto = img_curva.getHeight()

    for row in range(ancho):
        for col in range(alto):
            pixel = img_t.getPixel(col, row)
            new_col = ancho - row - 1
            new_row = col
            new_t.setPixel(new_col, new_row, pixel)

    return new_t

str_teselas = movimiento_final()
new_curva = curva_giro(image,str_teselas)
new_t = imgT_giro(image, str_teselas)
print(str_teselas)


def crear_imagen(str_teselas):
    index = 1
    coordenada_x = 300
    coordenada_y = 400
    img_start.setPosition(300, 300)
    img_start.draw(win)

    for i in range (len(str_teselas)):
        if str_teselas[index] == "f":
            img_linea.setPosition(coordenada_x,coordenada_y)
            img_linea.draw(win)
            index = index + 1
            coordenada_x = coordenada_x +100
            coordenada_y = coordenada_y 

        elif str_teselas[index] == "r":
            img_curva.setPosition(coordenada_x,coordenada_y)
            img_curva.draw(win)
            index = index + 1
            coordenada_x = coordenada_x +100
            coordenada_y = coordenada_y +100
        elif str_teselas[index] == "l":
            new_curva.setPosition(coordenada_x,coordenada_y)
            new_curva.draw(win)
            index = index + 1
            coordenada_x = coordenada_x +100
            coordenada_y = coordenada_y 
        elif str_teselas[index] == "w":
            img_wave.setPosition(coordenada_x,coordenada_y)
            img_wave.draw(win)
            index = index + 1
            coordenada_x = coordenada_x +100
            coordenada_y = coordenada_y 
        else:
            img_t.setPosition(coordenada_x,coordenada_y)
            img_t.draw(win) 

    win.exitonclick()

def main():
    uart.init(baudrate=115200)
    print('looking for microbit')
    ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
    if not ser_micro:
        print('microbit not found')
        return
    print('opening and monitoring microbit port')
    ser_micro.open()

    while True:
        sleep(1000)
        message = uart.read()

        if message != None:
            display.show(str(msg, 'UTF-8'))
            # Sends a msg replying to the one received
            print("ACK: ", str(msg, 'UTF-8'))
            crear_imagen(str_teselas)
        else:
            display.clear()

if __name__ == "__main__":
    main()
