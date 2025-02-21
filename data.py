#!/usr/bin/python3

# Importamos los módulos que utilizaremos
import argparse
import sys
import statistics

# Funciones necesarias para el funcionamiento del script
def lista_valida(argumento):
    '''Comprobamos quw se pasan 2 números como mínimo y 4 como máximo'''
	
    if not (2 <= len(args.floats) <= 4):
        print("ERROR, debe introducir como mínimo 2 números y como máximo 4")
        sys.exit(1)
		

def media(numero1):
    '''Función para calcular la media con el módulo statics'''
	
    print("La media de estos números es: ", statistics.mean(numero1))
    sys.exit(0)
		

def mediana(numero2):
    '''Función para calcular la mediana con el módulo statics'''
	
    print("La mediana de estos números es: ", statistics.median(numero2))
    sys.exit(0)
	
# -----------CÓDIGO PRINCIPAL PYTHON SCRIPTING
# Creamos el parser
parser = argparse.ArgumentParser(
    prog="data.py",
    description="Programa que acepta entre 2 y 4 números float para hacerles el máximo, mínimo, media, o la mediana")
	
# Argumento float obligatorio
parser.add_argument('floats', metavar='FLOAT', type=float, nargs='+',
    help='introducir número float')
			
#Argumentos float opcionales
parser.add_argument("--max", dest="max", action="store_const", const=max, help="Devuelve el máximo")
parser.add_argument("--min", dest="min", action="store_const", const=min, help="Devuelve el mínimo")
parser.add_argument("-m", "--mean", dest="mean", action="store_true", help="Devuelve la media")
parser.add_argument("--med", dest="med", action="store_true", help="Devuelve la mediana")

# Parseamos los argumentos
args = parser.parse_args()
lista_valida(args)


#-----------CÓDIGO PRINCIPAL NORMAL
if args.mean:
    media(args.floats)
elif args.med:
    mediana(args.floats)
elif args.max:
    print("El máximo número es: ", args.max(args.floats))	
elif args.min:
    print("El mínimo número es: ", args.min(args.floats))
		
sys.exit()
