import galapagar

NUMERO_DE_ESTUDIO = 2
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():
    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray", ANCHURA_VENTANA,
                                    ALTURA_VENTANA)

    galapagar.rectangulos()
    galapagar.cuadrados()

    galapagar.finish(the_window)

main()