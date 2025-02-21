####################
# Counts how many times a string appears in a dictionary of words
###################

diccionario_strings = {}
condicion = "0"

max_veces_que_aparece = 0
mayor_string = ""

def max_pos(lista):
    #encuentra los valores maximos de una lista y devuelve el indice 
    max_value = lista[0]
    max_pos = [0]

    for i in range(1, len(lista)):
        if lista[i] > max_value:
            max_value = lista[i]
            max_pos = [i]
        elif lista[i] == max_value:
            max_pos = max_pos + [i]

    return max_pos

def Cuenta_String(texto,string_a_buscar):
    #cuenta las veces que aparece un cierto string
    total = 0 
    for i in range(len(texto)):
        if texto[i] == string_a_buscar:
            total == total + 1
    return total

def main():
    cuenta = 1
    veces_string_aparece = []

    string = input("Introduce string (0 para terminar): ")

    while string != condicion:
       diccionario_strings[cuenta] = string
       cuenta = cuenta + 1

       string = input("Introduce string (0 para terminar): ")

    nuevo_string = input("Introduce nuevo string de búsqueda: ")

    for nombre_de_variable in diccionario_strings:
       veces_string_aparece = veces_string_aparece+ [Cuenta_String(diccionario_strings[nombre_de_variable], nuevo_string)]

    max_pos_list = max_pos(veces_string_aparece)
 
    if len(max_pos_list) >= 1:
        for index in max_pos_list:
            if nuevo_string in diccionario_strings[index+1]:
                print(diccionario_strings[index+1])
    else:
        #No se porque no hace print a cadena no encontrada
        print ("cadena no encontrada.")

if __name__ == '__main__':
    main()
