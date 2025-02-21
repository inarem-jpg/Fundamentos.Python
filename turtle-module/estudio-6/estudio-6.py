import galapagar

NUMERO_DE_ESTUDIO = 6
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():
    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray", ANCHURA_VENTANA,
                                ALTURA_VENTANA)   

galapagar.cuadrados (100,50,-157,83)
main()