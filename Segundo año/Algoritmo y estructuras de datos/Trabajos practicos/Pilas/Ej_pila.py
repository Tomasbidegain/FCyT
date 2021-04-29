from tda_pila_dinamica import Pila, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint, choice

pila = Pila()
pila_aux = Pila()

def cargarPila_str(pila, palabra):
    while (tamanio(pila) < len(palabra)):
        for i in range(0, len(palabra)):
            apilar(pila, palabra[i])

def cargarPila_palabra(pila):
    while(tamanio(pila) < 5):
        palabra = input('Ingrese una palabra para añadir a la pila: ')
        apilar(pila, palabra)

def cargarPila(pila):
    while(tamanio(pila) < 5):
        elemento = int(input('Ingrese un elemento para añadir a la pila: '))
        apilar(pila, elemento)

#******************************************************************************************************************************
#======================================================Ejercicio 1=============================================================
#******************************************************************************************************************************

"""
1.Determinar el número de ocurrencias de un determinado elemento en una pila. 
"""

def ocurrencias(pila, bus):
    cont = 0
    while (not pila_vacia(pila)):
        if (cima(pila) == bus):
            cont = cont + 1
        aux = desapilar(pila)
        print(aux)
    return cont

"""
cargarPila(pila)
buscado = int(input('Ingrese el numero a buscar dentro de la pila: '))
print('Numero de ocurrencias:', ocurrencias(pila, buscado))
"""

#******************************************************************************************************************************
#======================================================Ejercicio 2=============================================================
#******************************************************************************************************************************

"""
2.Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden  números pares. 
"""


def pares(pila, pila_aux):

    print("pila normal")
    
    while(not pila_vacia(pila)):
        x = desapilar(pila)
        if ((x % 2) == 0):
            apilar(pila_aux, x)
        print(x)

    while(not pila_vacia(pila_aux)):
        aux = desapilar(pila_aux)
        apilar(pila, aux)

    return pila

"""
cargarPila(pila)

print(pares(pila, pila_aux))

print('Pila par')
while(not pila_vacia(pila)):
    print(desapilar(pila))
"""  


#******************************************************************************************************************************
#======================================================Ejercicio 3=============================================================
#******************************************************************************************************************************

"""
3.Reemplazar todas las ocurrencias de un determinado elemento en una pila
"""

"""
cargarPila(pila)

ocurrencia = int(input('Ingrese la ocurrencia a cambiar: '))
nueva_ocurrencia = int(input('Ingrese el nuevo numero: '))

while (not pila_vacia(pila)):
    x = desapilar(pila)
    if (x == ocurrencia):
        apilar(pila_aux, nueva_ocurrencia)
    else:
        apilar(pila_aux, x)
        
#Acomodo la pila
while(not pila_vacia(pila_aux)):
    aux = desapilar(pila_aux)
    apilar(pila, aux)

print ('Pila modificada: ')

while(not pila_vacia(pila)):
    print(desapilar(pila))
"""

#******************************************************************************************************************************
#======================================================Ejercicio 4=============================================================
#******************************************************************************************************************************

"""
4.Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura  extra. 
"""

"""
cargarPila(pila)

print ("pila normal")

while (not pila_vacia(pila)):
    x = desapilar(pila)
    apilar(pila_aux, x)
    print(x)

pila = pila_aux
print("pila invertida")

while (not pila_vacia(pila)):
    print(desapilar(pila))
"""

#******************************************************************************************************************************
#======================================================Ejercicio 5=============================================================
#******************************************************************************************************************************

"""
5.Determinar si una cadena de caracteres es un palíndromo. 
"""

"""
palabra = input('Ingrese una palabra ')
cargarPila_str(pila, palabra)

#Desapilo la pila original y la apilo en la pila auxiliar
while (not pila_vacia(pila)):
    x = desapilar(pila)
    apilar(pila_aux, x)

#Aca vuelvo a cargar la pila original con la palabra ya cargada anteriormente 
for i in range(0,len(palabra)):
    apilar(pila, palabra[i])

#Comparo si las letras son iguales, en caso contrario ya descarto que sea palindromo
while (not pila_vacia(pila)):
    x = desapilar(pila)
    aux = desapilar(pila_aux)
    if (x == aux):
        palindromo = True
    else: 
        palindromo = False

if (palindromo == True):
    print('La palabra es palindromo')
else:
    print('La palabra no es palindromo')
"""

#*****************************************************************************************************************************
#=====================================================Ejercicio 6=============================================================
#*****************************************************************************************************************************

"""
6. Leer una palabra y visualizarla en forma inversa. 
"""

"""
palabra = input('Ingrese una palabra ')
cargarPila_str(pila, palabra)

print ("Palabra normal")

while (not pila_vacia(pila)):
    x = desapilar(pila)
    apilar(pila_aux, x)
    print(x)

pila = pila_aux
print("Palabra invertida")

while (not pila_vacia(pila)):
    print(desapilar(pila))
"""

#******************************************************************************************************************************
#======================================================Ejercicio 7=============================================================
#******************************************************************************************************************************

"""
7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras. 
"""

"""

cargarPila_palabra(pila)
palabra = input('Ingrese la palabra que quiere eliminar de la pila: ')

while(tamanio(pila)):
    aux = desapilar(pila)
    print(aux)
    if(aux != palabra ):
        apilar(pila_aux, aux)

print('Pila sin el elemento: ',palabra )

while(not pila_vacia(pila_aux)):
    x = desapilar(pila_aux)
    apilar(pila, x)
    aux = desapilar(pila)
    print(aux)
"""


#******************************************************************************************************************************
#======================================================Ejercicio 8=============================================================
#******************************************************************************************************************************

"""
8. Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un  mazo de cartas de baraja española–,resolver las siguientes actividades: 
a. Generar las cartas del mazo de forma aleatoria; 
b. Separar la pila mazo en cuatro pilas una por cada palo; 
c. Ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente. 
"""

"""
mazo_aux = Pila()
mazo = Pila()
espada = Pila()
basto = Pila()
copa = Pila()
oro = Pila()

palos = ['espada', 'basto', 'copa', 'oro']

while(tamanio(mazo) < 10):
    dato = ['', 0]
    dato[0] = choice(palos)
    dato[1] = randint(1, 12)
    apilar(mazo, dato)

print("Maso de cartas: ") 
while(not pila_vacia(mazo)):
    carta = desapilar(mazo)
    print(carta)
    if carta[0] == "espada":
        if(pila_vacia(espada)):
            apilar(espada, carta)
        else:
            if(cima(espada) <= carta):
                apilar(espada, carta)
            else:
                while(not pila_vacia(espada) and cima(espada) > carta):
                    daux = desapilar(espada)
                    apilar(mazo_aux, daux)
                apilar(espada, carta)
                while(not pila_vacia(mazo_aux)):
                    daux = desapilar(mazo_aux)
                    apilar(espada, daux)

    elif (carta[0] == "basto"):
        apilar(basto, carta)
    elif (carta[0] == "copa"):
        apilar(copa, carta)
    else:
        apilar(oro, carta)


print("maso espada")
while (tamanio(espada)):
    x = desapilar(espada)
    print(x)

print("maso basto")
while(tamanio(basto)):
    b = desapilar(basto)
    print(b)

print("maso copa")
while(tamanio(copa)):  
    c = desapilar(copa)
    print(c)

print("maso oro")
while(tamanio(oro)):
    o = desapilar(oro)
    print(o)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 9=============================================================
#******************************************************************************************************************************

"""
9. Resolver el problema del factorial de un número utilizando una pila. 
"""

"""
elemento = int(input('Ingrese el numero a calcular el factorial: '))
num = elemento
while (elemento > 0):
    apilar(pila, elemento)
    elemento = elemento - 1

factorial = 1
while (not pila_vacia(pila)):
    aux = desapilar(pila)
    factorial = factorial * aux

print('El factorial de ',num,' es: ',factorial)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 10=============================================================
#******************************************************************************************************************************

"""
10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de  una pila con nombres de dioses griegos. 
"""

"""
dioses = Pila()
dioses_aux = Pila()

archivo = open('dioses')

linea = archivo.readline()

print('Pila con los dioses griegos(sin Atenea)')
while linea:
    linea = linea.replace('\n','')
    print(linea)
    apilar(dioses, linea)
    linea = archivo.readline()

posicion = int(input('En que posicion quiere ingresar a la diosa Atenea?: '))

i = 0
while (not pila_vacia(dioses)):
    x = desapilar(dioses)
    i += 1
    if (i == posicion):
        apilar(dioses_aux, 'Atenea')
    else:
        apilar(dioses_aux, x)

dioses = dioses_aux

print('Pila con la diosa atenea en la posicion ', posicion)
while (not pila_vacia(dioses)):
    d = desapilar(dioses)
    print(d)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 11============================================================
#******************************************************************************************************************************

"""
11. Dada una pila de letras determinar cuántas vocales contiene. 
"""

"""

archivo = open('vocales')

linea = archivo.readline()

print('Pila con letras')
while linea:
    linea = linea.replace('\n','')
    print(linea)
    apilar(pila, linea)
    linea = archivo.readline()

vocal = 0
while (not pila_vacia(pila)):
    x = desapilar(pila)
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' ):
        vocal += 1

print('La pila tiene ',vocal, ' vocales.')
"""

#******************************************************************************************************************************
#======================================================Ejercicio 12============================================================
#******************************************************************************************************************************

"""
12. Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una  función que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder  los datos. 
"""


"""
pila_personajes = Pila()
personajes_aux = Pila()

archivo = open('personajes')

linea = archivo.readline()

print('Pila con personajes')
while linea:
    linea = linea.replace('\n','')
    print(linea)
    apilar(pila_personajes, linea)
    linea = archivo.readline()

while (not pila_vacia(pila_personajes)):
    aux = desapilar(pila_personajes)
    apilar(personajes_aux, aux)
    if (aux == 'Leia Organa'):
        print('Leia Organa esta en la pila.')
    elif (aux == 'Boba Fett'):
        print('Boba Fett esta en la pila.')
"""


#******************************************************************************************************************************
#======================================================Ejercicio 13============================================================
#******************************************************************************************************************************

"""
13. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente. 
Solo puede utilizar una pila auxiliar como estructura extra –no se pueden utilizar métodos de ordenamiento–. 
""" 

"""
numero = int(input('Ingrese un numero '))

while numero != 0:
    if(pila_vacia(pila)):
        apilar(pila, numero)
    else:
        if(cima(pila) <= numero):
            apilar(pila, numero)
        else:
            while(not pila_vacia(pila) and cima(pila) > numero):
                daux = desapilar(pila)
                apilar(pila_aux, daux)
            apilar(pila, numero)
            while(not pila_vacia(pila_aux)):
                daux = desapilar(pila_aux)
                apilar(pila, daux)

    numero = int(input('ingrese un numero '))

print('Numeros ordenados de forma creciente')
while (not pila_vacia(pila)):
    print(desapilar(pila))
"""


#******************************************************************************************************************************
#======================================================Ejercicio 14============================================================
#******************************************************************************************************************************

"""
14. Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente. 
"""

#******************************************************************************************************************************
#======================================================Ejercicio 15============================================================
#******************************************************************************************************************************
"""
15. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” 
y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, 
es decir los personajes que aparecen en ambos episodios. 
"""


"""
ep5 = Pila()
ep7 = Pila()
paux = Pila()

while not pila_llena(ep5):
    x = input('ingrese nombre personaje ')
    apilar(ep5, x)

while not pila_llena(ep7):
    x = input('ingrese nombre personaje ')
    apilar(ep7, x)

print("interseccion")

while(not pila_vacia(ep5)):
    x = desapilar(ep5)

    while(not pila_vacia(ep7)):
        xaux = desapilar(ep7)

        if(x == xaux):
            print(x)
        apilar(paux, xaux)

    while(not pila_vacia(paux)):
        xaux = desapilar(paux)
        apilar(ep7, xaux)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 16============================================================
#******************************************************************************************************************************
"""
16. Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonantes y 
otros caracteres que no sean letras (signos de puntuación números, 
espacios, etc.). Luego utilizando las operaciones de pila resolver las siguientes consignas: 
a. Cantidad  de caracteres que hay de cada tipo (vocales, consonantes y otros); 
b. Cantidad de espacios en blanco; 
c. Porcentaje que representan las vocales respecto de las consonantes sobre el total  de caracteres del párrafo; 
d. Cantidad de números; 
e. Determinar si la cantidad de vocales y otros caracteres son iguales; 
f. Determinar si existe al menos una z en la pila de consonantes. 
"""

"""
pila = Pila()
vocales = Pila()
consonantes = Pila()
caracteres = Pila()

parrafo = 'hola, como andais? espero que bien,! saludos.'
cargarPila_str(pila, parrafo)

vocal = 'aeiouAEIOU'
abcdario = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
caract = '1234567890.,-_!"?¿/()*+%$#@°='
numeros = '1234567890'

voc = 0
conso = 0
caracter = 0
espacios = 0
porcentaje = 0
c_num = 0
z = 0

while (not pila_vacia(pila)):
    x = desapilar(pila)
   
    if (x in vocal):
        apilar(vocales, x)
        voc += 1
   
    elif (x in abcdario):
        apilar(consonantes, x)
        conso += 1
        if (x == 'z'):
            z += 1
   
    elif(x in caract):
        apilar(caracteres, x)
        caracter += 1
        if (x in numeros):
            c_num += 1
   
    elif (x == ' '):
        espacios += 1

porcentaje = (voc / conso) * 100

print('La cantidad de vocales que hay es: ',voc)
print('La cantidad de consonantes que hay es: ',conso)
print('La cantidad de caracteres que hay es: ',caracter)
print('La cantidad de numeros que hay es: ', c_num)
print('La cantidad de espacios que hay es: ', espacios)
print('Porcentaje que representan las vocales respecto de las consonantes sobre el total  de caracteres del párrafo es: ',porcentaje,'%')

if (z > 0):
    print('Hat ', z,' z en el parrafo')

if (voc == conso):
    print('La cantidad de vocales es igual a la cantidad de consonantes.')

if (voc == caracter):
    print('La cantidad de vocales es igual a la cantidad de caracteres.')
"""

#******************************************************************************************************************************
#======================================================Ejercicio 17============================================================
#******************************************************************************************************************************
"""
17. Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por  ejemplo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su  peso –del objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como 
estructuras extras, no se pueden utilizar métodos de ordenamiento. 
"""

"""
objetos = Pila()
ob_aux = Pila()

dato = [0,'kg','']

dato[2] = input('Ingrese el nombre del objeto ')
dato[0] = float(input('Ingrese el peso del objeto '))
while dato[2] != '':
    if(pila_vacia(objetos)):
        apilar(objetos, dato)
    else:
        if(cima(objetos) <= dato):
            apilar(objetos, dato)
        else:
            while(not pila_vacia(objetos) and cima(objetos) > dato):
                daux = desapilar(objetos)
                apilar(ob_aux, daux)
            apilar(objetos, dato)
            while(not pila_vacia(ob_aux)):
                daux = desapilar(ob_aux)
                apilar(objetos, daux)
    dato = [0,'kg','']
    dato[2] = input('Ingrese el nombre del objeto ')
    if (dato[2] != ''):
        dato[0] = float(input('Ingrese el peso del objeto '))

while(not pila_vacia(objetos)):
    print(desapilar(objetos))
"""

#******************************************************************************************************************************
#======================================================Ejercicio 18============================================================
#******************************************************************************************************************************
"""
18. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de  estreno, desarrollar las funciones necesarias para resolver las siguientes actividades: 
a. Mostrar los nombre películas estrenadas en el año 2014; 
b. Indicar cuántas películas se estrenaron en el año 2018; 
c. Mostrar las películas de Marvel Studios estrenadas en el año 2016. 
"""

"""
pila_peliculas = Pila()
pila_2014 = Pila()
pila_2018 = Pila()
pila_marvel = Pila()


archivo = open('pelicula')

linea = archivo.readline()

while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = int(linea[1])
    linea[2] = linea[2].title()
    apilar(pila_peliculas, linea)
    linea = archivo.readline()

while(not pila_vacia(pila_peliculas)):
    aux = desapilar(pila_peliculas)
    if (aux[1] == 2014):
        apilar(pila_2014, aux)
    if (aux[1] == 2018):
        apilar(pila_2018, aux)
    if (aux[2] == ' Marvel Studios'):
        apilar(pila_marvel, aux)

print("Peliculas estrenadas en 2014:")
while (not pila_vacia(pila_2014)):
    aux = desapilar(pila_2014)
    print(aux[0])

print("Peliculas estrenadas en 2018:")
while (not pila_vacia(pila_2018)):
    aux = desapilar(pila_2018)
    print(aux[0])

print("Peliculas estrenadas por Marvel Studios en 2016:")
while (not pila_vacia(pila_marvel)):
    aux = desapilar(pila_marvel)
    print(aux[0])
"""

#******************************************************************************************************************************
#======================================================Ejercicio 19============================================================
#******************************************************************************************************************************
"""
19. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan  son cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho 
direcciones: norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo que genere la secuencia de movimientos necesarios para hacer 
volver al robot a su lugar de partida, retornando por el mismo camino que fue.  
"""

#******************************************************************************************************************************
#======================================================Ejercicio 20============================================================
#******************************************************************************************************************************
"""
20. Realizar un algoritmo que ingrese en una pila los dos valores iniciales de la sucesión de 
Fibonacci –o condiciones de fin de forma recursiva– y a partir de estos calcular los  siguientes valores de dicha sucesión, hasta obtener el valor correspondiente a un número 
n ingresado por el usuario.  
"""

"""
def fibonacci(numero, pila):
    if numero == 1: 
        return 0
    elif numero == 2: 
        return 1
    else:
        numero -= 2
        apilar(pila, 0)
        apilar(pila, 1)

        while numero > 0:
            #sacamos el ultimo
            cim = desapilar(pila)

            #tambien sacamos el anteultimo
            cim_2 = desapilar(pila)

            #calculamos el actual
            n_actual = cim + cim_2 
            
            #metemos los 3
            apilar(pila, cim_2) 
            apilar(pila, cim)
            apilar(pila, n_actual)
            
            numero -= 1
        return cima(pila)

print(fibonacci(8, pila))
"""

#******************************************************************************************************************************
#======================================================Ejercicio 21============================================================
#******************************************************************************************************************************
"""
21. Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de  abril, obtener la siguiente información sin perder los datos: 
a. Determinar el rango de temperatura del mes, temperatura  mínima y máxima; 
b. Calcular el promedio de temperatura (o media) del total de valores; 
c. Determinar la cantidad de valores por encima y por debajo de la media. 
"""

pila_temp = Pila()

def ambiente(pila_temp):
    contador = 0
    suma = 0    
    mayores_a_media = 0
    menores_a_media = 0

    maximo = cima(pila_temp)
    minimo = cima(pila_temp)

    while not cima(pila_temp):
        cim = cima(pila_temp)
        desapilar(pila_temp)

        if (cim > maximo):
               maximo = cim
        if (cim < minimo):
               minimo = cim
        suma += cim
        contador += 1
        apilar(pila_aux, cim)

    media = ((1.0 * suma) / contador)

    while not pila_vacia(pila_aux):
        cim = cima(pila_aux)
        desapilar(pila_aux)

        if cim > media:
            mayores_a_media += 1
        elif cim < media:
            menores_a_media += 1
        
        apilar(pila_temp, cim)

    return {
            'maximo':maximo, 
            'minimo':minimo,
            'media':media,
            'mayores_a_media':mayores_a_media,
            'menores_a_media':menores_a_media
            }

import random
for i in range(0, 30):
    apilar(pila_temp, randint(-10, 50))

print(ambiente(pila_temp))

#******************************************************************************************************************************
#======================================================Ejercicio 22============================================================
#******************************************************************************************************************************
"""
22. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se  dispone de su nombre y 
la cantidad de películas de la saga en la que participó, 
implementar las funciones necesarias para resolver las siguientes actividades: 
a. Determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando 
como posición uno la cima de la pila; 
b. Determinar los personajes que participaron en más de 5 películas de la saga, 
además indicar la cantidad de películas en la que aparece; 
c. Determinar en cuantas películas participo la Viuda Negra (Black Widow); 
d. Mostrar todos los personajes cuyos nombre empiezan con C, D y G.  
"""