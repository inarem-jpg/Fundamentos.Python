import galapagar

NUMERO_DE_ESTUDIO = 9
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():
    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray", ANCHURA_VENTANA,
                                     ALTURA_VENTANA)   

galapagar.rejilla(140,140,0,0) 
galapagar.cuadrados(10,10)

main()