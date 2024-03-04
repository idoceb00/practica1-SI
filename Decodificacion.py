#Importación de librerias
import fractions
import decimal
#Declaración de variables

l_palabra = 0
#Relleno la lista de caracteres
abecedario = []
for i in range(97,123):
    abecedario.append(chr(i))
    if i == 110:
        abecedario.append(chr(164))
abecedario.append(" ")
abecedario.append(".")

#Relleno la lista de probabilidades
prob = [fractions.Fraction(numerator = j, denominator = len(abecedario)) for j in range (len(abecedario))]

#Defino funciones

#Funcion que comprueba el numero actual del mensaje codfificado y añade la letra correspondiente al mensaje. Devuelve el intervalo.
def devuelveCarac(n_codif,palabra:list):

    listaProb = []
    #Bucle que comprueba a que letra pertenece el numero
    for i in range(0,len(abecedario)): 
        #Comprueba si la probabilidad es mayor y, por lo tanto, pertenece al intervalo
        if prob[i + 1] > n_codif:
            #Añade la letra a la variable donde almacenaremos la palabra decodificada y devuelve el intervalo
            palabra.append(abecedario[i])

            listaProb.append(prob[i])
            listaProb.append(prob[i+1])

            return listaProb
        
    return listaProb
        

#Funcion que actaliza el valor del numero para seguir obteniendo las letras de la palabra
def actualizaNum(n_codif, prob1):

    numN = (fractions.Fraction(n_codif) - prob1)/fractions.Fraction(numerator = 1, denominator = 29)
    return numN


#MAIN
func = input("Introduce la función a realizar:")
palabra = []
#Opcion decodificacion
if func == 'd' or func == 'D':

    #Bucle que solicita al usuario la longitud. Comprueba que la longitud es valida y si no lo es pide el dato hasta que sea valida
    while l_palabra <= 0:
        l_palabra = int(input("Introduce la longitud de la palabra: "))
        if l_palabra <= 0:
            print("La longitud de la palabra debe de ser un número natural.")

    #Bucle que solicita al usuario el numero a decodificar. Comprueba que el valor es valido y si no lo solicita hasta que sea valido
    #n_codif = 0
    #while n_codif <= 0:
    n_codif = decimal.Decimal(0.419109252056655118764546349)
        #if n_codif <= 0:
            #print("El numero a decodificar debe de ser un número racional positivo.")

    #Bucle que realizara la codificacion de la palabra dependiendo de la longitud dada de esta.
    for i in range (0, l_palabra):
        n_codif = actualizaNum((n_codif), fractions.Fraction(devuelveCarac(n_codif,palabra)[0]))
        print(palabra[i])

#Opcion codificacion
elif func == 'c' | func == 'C':
    
    #Bucle que solicita al usuario la longitud. Comprueba que la longitud es valida y si no lo es pide el dato hasta que sea valida
    while palabra.isAlpha() | palabra.isspace() | palabra.find(".") in range(0,len(palabra)):
        palabra = input("Introduce la palabra a codificar: ")
        if l_palabra <= 0:
            print("La palabra solo debe contener letras, '.' o ' '")
    
    #

else: 
    print("Por favor, introduce una opción válida.")
