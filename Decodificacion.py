#Importación de librerias



#Declaración de variables
palabra = ""


#Defino funciones

#Funcion que comprueba el numero actual del mensaje codfificado y añade la letra correspondiente al mensaje. Devuelve el intervalo.
def devuelveCarac(n_codif):

    #Bucle que comprueba a que letra pertenece el numero
    for i in range(0,len(abecedario)-1): 

        #Comprueba si la probabilidad es mayor y, por lo tanto, pertenece al intervalo
        if prob[i] > n_codif:

            #Añade la letra a la variable donde almacenaremos la palabra decodificada y devuelve el intervalo
            palabra.join(abecedario[i])
            return (prob[i], prob[i-1])
        

#Funcion que actaliza el valor del numero para seguir obteniendo las letras de la palabra
def actualizaNum(n_codif, prob1, prob2):

    numN = (n_codif - prob1)/(prob2 - prob1)
    return numN


#main

#Opcion decodificacion
if func == 'd' | func == 'D':
    
    #Bucle que realizara la codificacion de la palabra dependiendo de la longitud dada de esta.
    for i in range (0, longitud_msj):
        n_codif = actualizaNum(n_codif, devuelveCarac(n_codif)[0], devuelveCarac(n_codif)[1])
    print(palabra)

#Opcion codificacion
elif func == 'c' | func == 'C':
    print()
