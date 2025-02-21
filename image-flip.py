
import image

def main():

    imagen = input("Introduce el nombre del archivo: ")

    while imagen != "0":

        img = image.Image(imagen)
        win = image.ImageWin(img.getWidth() * 2, img.getHeight() * 2)
        img.draw(win)


        #Creamos la n imagen
        img_giro_vertical = image.Image(imagen)

        #Dibujamos la imagen que vamos a transformar
        img_giro_vertical.draw(win, 0, img_giro_vertical.getHeight())

        #giramos la imagen verticalmente
        for fila in range(img_giro_vertical.getHeight()):
            for columna in range(img_giro_vertical.getWidth()):
                pix = img.getPixel(columna, img_giro_vertical.getHeight() - 1 - fila)
                img_giro_vertical.setPixel(col, row, pix)


        #Creamos la imagen
        img_giro_horizontal = image.Image(imagen)

        #Dibujamos la imagen que vamos a girar horizontalmente
        img_giro_horizontal.draw(win, img_giro_horizontal.getWidth(), 0)

        #giramos la imagen horizontalmente.
        for fila in range(img_giro_horizontal.getHeight()):
            for columna in range(img_giro_horizontal.getWidth()):
                pix = img.getPixel(img_giro_horizontal.getWidth() - 1 - columna, fila)
                img_giro_horizontal.setPixel(columna, fila, pix)

        imagen = input("Introduce un nuevo nombre de archivo: ")

    else:
        return

if __name__ == "__main__":
    main()