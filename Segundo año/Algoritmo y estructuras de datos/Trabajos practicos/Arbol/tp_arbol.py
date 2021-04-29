from tda_arbol_binario_avl import actualizaraltura, altura, balancear, busqueda, busqueda_archivo_letra, busqueda_archivo_libros, busqueda_archivo_sable, busqueda_proximidad, busqueda_proximidad_archivo_autor, busqueda_proximidad_archivo_jedis, busqueda_proximidad_archivo_libros, contar, cortar_por_nivel, eliminar_nodo, inorden, nodoArbolHuffman, padre, por_nivel, postorden, preorden
from random import randint 
from tda_archivo import abrir, cerrar, leer, guardar, modificar
from tda_arbol import busqueda_nario, contar_nodos, insertar_nario, insertar_nodo, insertar_nodo_huffman, insertar_nodo_morse, nodoArbol, nodoArbolGreek, nodoArbolHuffman, por_nivel_nario, preorden


arbol = None

#******************************************************************************************************************************
#======================================================Ejercicio 1=============================================================
#******************************************************************************************************************************

"""
1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de
manera aleatoria– que resuelva las siguientes actividades:
a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol
generado;
b. determinar si un número está cargado en el árbol o no;
c. eliminar tres valores del árbol;
d. determinar la altura del subárbol izquierdo y del subárbol derecho;
e. determinar la cantidad de ocurrencias de un elemento en el árbol;
f. contar cuántos números pares e impares hay en el árbol. 
"""
"""
for i in range(0,1000):
    arbol = insertar_nodo(arbol,randint(50,57))
  
#A
print('barrido inorden')
inorden(arbol)
a = input()
print('barrido preorden')
preorden(arbol)
a = input()
print('barrido postorden')
postorden(arbol)
a = input()
print('barrido por nivel')
por_nivel(arbol)
a = input()

#B
buscado = int(input('Ingrese el valor a buscar '))
pos = busqueda(arbol, buscado)

if(pos is not None):
    print('El valor existe en el arbol')
else:
     print('El valor no existe en el arbol')

#C
for i in range(0,3):
    clave = int(input('Ingrese el dato que quiere eliminar del arbol: '))
    pos=busqueda(arbol, clave)
    if pos is not None:
        eliminar_nodo(arbol, clave)
    else:
        print('El valor que introdujo no se encuentra en el arbol')

print('Arbol modificado:')
inorden(arbol)
    
#D

#E
def ocurrencias(raiz, bus, ocu ):
    if(raiz is not None):
        if raiz.info == bus:
            ocu =+ 1
            ocu = ocurrencias(raiz.izq, bus, ocu)
        elif raiz.info < bus:
            ocu = ocurrencias(raiz.der, bus, ocu)
        else:
            ocu = ocurrencias(raiz.izq, bus, ocu)

    return ocu

bus = 7
ocu = 0
ocu = ocurrencias(arbol, bus, ocu)
print('el numero ',bus,' tiene una ocurrencia de:',ocu )

#F
def pares_impares(raiz, cp, ci):
    if(raiz is not None):
        if(raiz.info % 2 == 0):
            cp += 1
        else:
            ci += 1
        cp, ci = pares_impares(raiz.izq, cp, ci)
        cp, ci = pares_impares(raiz.der, cp, ci)
    return cp, ci

cp, ci = 0,0
cp, ci = pares_impares(arbol, cp, ci)
print('Cantidad de numeros pares:',cp)
print('Cantidad de numeros impares:', ci)

"""
#******************************************************************************************************************************
#======================================================Ejercicio 2=============================================================
#******************************************************************************************************************************

"""
2. Implementar una función que permita cargar una expresión matemática en un árbol
binario (no balanceado), y resuelva lo siguiente:
a. determinar cuál de los barridos muestra la expresión en el orden correcto;
b. resolver la expresión matemática y muestre el resultado. 
"""
# NO SE HACE


#******************************************************************************************************************************
#======================================================Ejercicio 3=============================================================
#******************************************************************************************************************************

"""
3. Desarrollar un algoritmo que permita cargar el índice del libro Ingeniería de Software de Ian Summerville de manera automática desde un archivo de texto, transformando el árbol n-ario del índice en un árbol binario no balanceado mediante el uso de la transformada de Knuth, para resolver las siguientes actividades:
a. listar el índice en su orden original;
b. mostrar la parte del índice correspondiente al subtitulo “Diseño de software
de tiempo real”;
c. deberá almacenar además del texto de índice la página del libro donde está
dicho tema;
d. determinar cuántos capítulos tiene;
e. determinar todos los temas que contengan las palabras modelo y métrica.
"""
# NO SE HACE


#******************************************************************************************************************************
#======================================================Ejercicio 4=============================================================
#******************************************************************************************************************************

"""
4. Implementar un algoritmo que contemple dos funciones, la primera que devuelva el
hijo derecho de un nodo y la segunda que devuelva el hijo izquierdo. 
"""
"""
for i in range(0, 20):
    arbol = insertar_nodo(arbol, randint(0, 50000))

def hijo_der(arbol):
    if(arbol.der is None):
        print(arbol.der)
    else:
        print(arbol.der.info)

def hijo_izq(arbol):
    if(arbol.izq is None):
        print(arbol.izq)
    else:
        print(arbol.izq.info)

preorden(arbol)

clave = int(input("Ingrese el nodo a mostrar sus hijos "))

pos = busqueda(arbol, clave)
if pos is not None:
    hijo_der(pos)
    hijo_izq(pos)
"""
#******************************************************************************************************************************
#======================================================Ejercicio 5=============================================================
#******************************************************************************************************************************

"""
5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel
Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará
un campo booleano que indica si es un héroe o un villano, True y False
respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por
proximidad para encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los
superhéroes y otro a los villanos, luego resolver las siguiente tareas:
    i. determinar cuántos nodos tiene cada árbol;
    ii. realizar un barrido ordenado alfabéticamente de cada árbol. 
"""

def listado_villanos(arbol):
    if(arbol is not None):
        listado_villanos(arbol.izq)
        if arbol.nrr == False:
            print(arbol.info)
        listado_villanos(arbol.der)

def super_c(arbol):
    if(arbol is not None):
        super_c(arbol.izq)
        if (arbol.nrr == True) and (arbol.info[0] == "C"):
            print(arbol.info)
        super_c(arbol.der)

def contador_s(arbol, cont):
    if arbol is not None:
        cont = contador_s(arbol.izq, cont)
        if arbol.nrr == True:
            cont += 1
        cont = contador_s(arbol.der, cont)
    return cont

def arbol_vs(arbol, arbol_villano, arbol_superheroe):
    if(arbol is not None):
        arbol_villano, arbol_superheroe = arbol_vs(arbol.izq, arbol_villano, arbol_superheroe)
        if arbol.nrr == False:
            arbol_villano = insertar_nodo(arbol_villano, arbol.info)
        else:
            arbol_superheroe = insertar_nodo(arbol_superheroe, arbol.info)
        arbol_villano, arbol_superheroe = arbol_vs(arbol.der, arbol_villano, arbol_superheroe)
    return arbol_villano, arbol_superheroe
        
"""
#A
arbol = insertar_nodo(arbol,'Iron Man',True)
arbol = insertar_nodo(arbol,'Thor',True)
arbol = insertar_nodo(arbol,'Loki',False)
arbol = insertar_nodo(arbol,'Ultrón',False)
arbol = insertar_nodo(arbol,'Hulk',True)
arbol = insertar_nodo(arbol,'Thanos',False)
arbol = insertar_nodo(arbol,'Capitán América',True)
arbol = insertar_nodo(arbol,'Doctor Strange',True)

#B
print('Listado de los villanos en orden alfabetico: ')
listado_villanos(arbol)

#C
print('Superheroes que comienzan con la letra "C":')
super_c(arbol)

#D
cont = 0
print('Cantidad de superheroes en el arbol:'+str(contador_s(arbol,cont)))

#E

#G
arbol_villano, arbol_superheroe = None, None
arbol_villano, arbol_superheroe = arbol_vs(arbol, arbol_villano, arbol_superheroe)
print('Arbol de villanos:')
inorden(arbol_villano)
print('Arbol de superheroes:')
inorden(arbol_superheroe)

#i
nodo_v = 0
nodo_s = 0
nodo_v = contar_nodos(arbol_villano, nodo_v)
nodo_s = contar_nodos(arbol_superheroe,nodo_s)
print('El arbol de villanos tiene ',nodo_v,' nodos y el arbol de superheroes tiene ',nodo_s,' nodos')

#ii
print('Arbol de villanos ordenado alfabeticamente:')
inorden(arbol_villano)
print('Arbol de superheroes ordenado alfabeticamente:')
inorden(arbol_superheroe)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 6=============================================================
#******************************************************************************************************************************

"""
6. Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año
de nacimiento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y
maestro, los últimos tres campos pueden tener más de un valor. Escribir las
funciones necesarias para resolver las siguientes consignas:
a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
b. realizar un barrido inorden del árbol por nombre y ranking;
c. realizar un barrido por nivel de los árboles por ranking y especie;
d. mostrar toda la información de Yoda y Luke Skywalker;
e. mostrar todos los Jedi con ranking “Jedi Master”;
f. listar todos los Jedi que utilizaron sabe de luz color verde;
g. listar todos los Jedi cuyos maestros estan en el archivo;
h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su
nombre. 

"""
class Jedis():
    def __init__(self, nombre, especie, anio, color_sable, ranking, maestro):
        self.nombre = nombre
        self.especie = especie
        self.anio = anio
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestro = maestro
    
    def __str__(self):
        return 'Nombre:' + str(self.nombre) + '\nEspecie: ' + str(self.especie) + '\nAño de nacimiento: ' + str(self.anio) + '\nColor del sable: ' + str(self.color_sable) + '\nRanking: ' + str(self.ranking) + '\nMaestro: ' +str(self.maestro)

"""
datos = [['Yoda','Desconocida','1800','Verde','Jedi Knight','Luke Skywalker'],
         ['Luke Skywalker','Humano','1450','Verde','Jedi Master','Obi-Wan Kenobi'],
         ['Sifo-Dyas','Cerean','1600','Verde','Jedi Knight','Conde Dooku'],
         ['Shaak Ti','Togruta','1800','Azul','Padawan','Zett Jukassa'],
         ['Aayla Secura','Twi’lek','1500','Azul','Jedi Master','Quinlan Vos'],
         ['Zett Jukassa','Cerean','1650','Azul','Padawan','Yoda'],
         ['Qui-Gon Jinn','Humano','','Verde','Jedi Master','Conde Dooku']]


def maestros_archivo(raiz, buscado, archivo):
    if(raiz is not None):
        x = leer(archivo, raiz.nrr)
        if(x.maestro == buscado):
            print('------------')
            print('Nombre:' + str(x.nombre) + '\nEspecie: ' + str(x.especie) + '\nAño de nacimiento: ' + str(x.anio) + '\nColor del sable: ' + str(x.color_sable) + '\nRanking: ' + str(x.ranking) + '\nMaestro: ' +str(x.maestro))
            print('------------')
        maestros_archivo(raiz.izq, buscado, archivo)
        maestros_archivo(raiz.der, buscado, archivo)


#A
arbol_nombre = None
arbol_ranking = None
arbol_especie = None

file = abrir('jedis')

#Se guardan los datos en el archivo

for dato in datos:
    x = Jedis(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
    guardar(file, x)
cerrar(file)
#Se cargan datos del archivo en los arboles

pos = 0

file = abrir('jedis')
while pos < len(datos):
    jedis = leer(file, pos)
    arbol_nombre = insertar_nodo(arbol_nombre, jedis.nombre, pos)
    arbol_ranking = insertar_nodo(arbol_ranking, jedis.ranking , pos)
    arbol_especie = insertar_nodo(arbol_especie, jedis.especie , pos)
    pos += 1
cerrar(file)

#B
print('Barrido inorden del arbol de nombres: ')
inorden(arbol_nombre)

a=input()

print('Barrido inorden del arbol de ranking: ')
inorden(arbol_ranking)

a=input()

#C
print('Barrido por nivel del arbol de ranking: ')
por_nivel(arbol_ranking)

a=input()

print('Barrido por nivel del arbol de especies: ')
por_nivel(arbol_especie)

a = input()
print()
#D
file =  abrir('jedis')

print('Informacion de Yoda: ')
busqueda_proximidad_archivo_jedis(arbol_nombre, 'Yoda', file)
print()
a = input()
print('Informacion de Luke Skywalker: ')
busqueda_proximidad_archivo_jedis(arbol_nombre, 'Luke Skywalker', file)
print()

a = input()

#E

print('Informacion de los Jedis con ranking “Jedi Master”: ')
busqueda_proximidad_archivo_jedis(arbol_ranking, 'Jedi Master', file)
print()

a=input()

#F

print('Informacion de los Jedis que utilizan sable de color Verde: ')
busqueda_archivo_sable(arbol_nombre, 'Verde', file)
print()

a = input()
#G
print('Jedis cuyos maestros esten en el archivo')
for dato in datos:
    buscado = dato[0]
    maestros_archivo(arbol_nombre, buscado, file)

print()

a = input()
#H
print('Jedis de especie “Togruta”:')
busqueda_proximidad_archivo_jedis(arbol_especie,'Togruta', file)
print()

a = input()
print('Jedis de especie  “Cerean”:')
busqueda_proximidad_archivo_jedis(arbol_especie,'Cerean', file)
print()

a=input()
#I
        
print('Jedis que comienzan con la letra A y los que contienen un “-” en su nombre:')
busqueda_proximidad_archivo_jedis(arbol_nombre,'A',file)
busqueda_archivo_letra(arbol_nombre,'-',file)

cerrar(file)
"""
#******************************************************************************************************************************
#======================================================Ejercicio 7=============================================================
#******************************************************************************************************************************
"""

7. Partiendo del árbol n-ario del directorio, que se observa en la siguiente figura,
implementar los algoritmos necesarios para poder transformarlo a un árbol binario
no balanceado –utilizando la transformada de Knuth–. Tener en cuenta que los
archivos serán nodos hojas –es decir que estos no pueden tener hijos– y además
resolver las siguientes actividades:
a. el nodo deberá tener un campo que indique si es un directorio o un archivo;
b. realizar un barrido inorden del árbol;
c. listar el contenido de la carpeta /Imágenes;
d. contar cuantos archivos hay en cada carpeta;
e. mostrar todos los archivos
"""
# NO SE HACE


#******************************************************************************************************************************
#======================================================Ejercicio 8=============================================================
#******************************************************************************************************************************

"""
8. Desarrollar un algoritmo que implemente dos funciones, una para obtener el
mínimo nodo del árbol y la segunda para obtener el máximo. 
"""
"""
arbol = insertar_nodo(arbol, 8)
arbol = insertar_nodo(arbol, 7)
arbol = insertar_nodo(arbol, 10)
arbol = insertar_nodo(arbol, 9)
arbol = insertar_nodo(arbol, 4)
arbol = insertar_nodo(arbol, 5)

def minimo(raiz):
    if raiz.izq is not None:
        raiz = minimo(raiz.izq)
    return raiz

def maximo(raiz):
    if raiz.der is not None:
        raiz = maximo(raiz.der)
    return raiz

minimo = minimo(arbol)
print('El minimo nodo del arbol es:' + str(minimo.info))
maximo = maximo(arbol)
print('El maximo nodo del arbol es:'+ str (maximo.info))
"""
#******************************************************************************************************************************
#======================================================Ejercicio 9=============================================================
#******************************************************************************************************************************
"""
9. Poe Dameron, líder del escuadrón negro de la Resistencia, tiene dificultades para
transmitir los mensajes a la base de la Resistencia, dado que los mismos son muy
largos y los satélites espías de la Primera Orden los intercepta, en un lapso muy
corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que
permita comprimir los mensajes para enviarlos más rápido y no puedan ser
interceptados. Contemplando los siguientes requerimientos, implementar un
algoritmo que los resuelva:
a. crear un árbol de Huffman a partir de la siguiente tabla:

Símbolo Frecuencia
A 0.2
F 0.17
1 0.13
3 0.21
0 0.05
M 0.09
T 0.15

b. desarrollar las funcionas para comprimir y descomprimir un mensaje. 
"""

tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]

dic = {'A' : '00', '3': '01', '1' : '100', 'T': '110', 'F' : '111', '0': '1010', 'M' : '1011'}

"""
def como_comparo(elemento):
    return elemento[1]

def como_comparo_nodo(elemento):
    return elemento.valor

tabla.sort(key=como_comparo)

bosque = []

for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

for elemento in bosque:
    print(elemento.info, elemento.valor)
print()
while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)


#por_nivel(bosque[0])

def generar_tabla(raiz, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, cadena)


generar_tabla(bosque[0])

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += dic[caracter]
    return cadena_cod

cadena = "AA31TF0AAMMMMMM0000"
from sys import getsizeof
cadena_cod = codificar(cadena, dic)
print('Cadena codificada: ')
print(cadena_cod)
print(getsizeof(cadena_cod), getsizeof(b'000001100110111101000001011101110111011101110111010101010101010'))
print('Cadena decodificada:')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)
"""
#******************************************************************************************************************************
#======================================================Ejercicio 10=============================================================
#******************************************************************************************************************************

"""
10. Desarrollar dos algoritmos, el primero que permita calcular en el número de nodos
de un nivel del árbol –a partir de un nivel ingresado–. La segunda que cuente los
nodos que hay en dicho nivel –dado que podría no estar completo–, para responder
las siguientes actividades:
a. determinar si el nivel del árbol está completo;
b. ¿cuántos nodos faltan para completar dicho nivel?
"""
# NO SE HACE


#******************************************************************************************************************************
#======================================================Ejercicio 11=============================================================
#******************************************************************************************************************************

"""
11. Escribir un algoritmo que permita resolver las siguientes actividades:
a. contar el número de nodos del árbol;
b. determinar el número de hojas del árbol;
c. mostrar la información de los nodos hojas;
d. determinar el padre de un nodo;
e. determinar la altura de un árbol. 
"""
"""
arbol = insertar_nodo(arbol, 8)
arbol = insertar_nodo(arbol, 7)
arbol = insertar_nodo(arbol, 10)
arbol = insertar_nodo(arbol, 9)
arbol = insertar_nodo(arbol, 4)
arbol = insertar_nodo(arbol, 5)
#A
cont=0
cont=contar_nodos(arbol,cont)
print('La cantidad de nodos del arbol son:',cont)

#B C
def cantidadHojas(raiz, cont):
    if raiz is not None:
        if (raiz.der == None) and (raiz.izq == None):
            cont += 1
            print('Info nodo hoja:', raiz.info)
        cont = cantidadHojas(raiz.izq , cont)
        cont = cantidadHojas(raiz.der, cont)
    return cont
#D
bus = int(input('Ingrese el nodo a buscar su padre: '))
padre(arbol, bus)
   
#E
cont = 0
cont = cantidadHojas(arbol, cont)
print('La cantidad de hojas que tiene el arbol son:', cont)

"""

            
#******************************************************************************************************************************
#======================================================Ejercicio 12=============================================================
#******************************************************************************************************************************

"""
12. Generar un árbol binario que tenga nueve niveles, luego diseñar los algoritmos
necesarios para resolver las siguientes actividades:
a. generar un bosque cortando los tres primeros niveles del árbol;
b. contar cuántos nodos tiene cada árbol del bosque;
c. realizar un barrido preorden de cada árbol del bosque;
d. determinar cuál es el árbol con mayor cantidad de nodos;
e. indicar que árboles del bosque están completos. 
"""
"""
arbol = None
for i in range(1,1024):
    arbol = insertar_nodo(arbol, i)
cantidad = [0]
contar(arbol, cantidad)
print(altura(arbol), cantidad[0])
bosque = []
cortar_por_nivel(arbol, bosque)
print(len(bosque))
for arbol in bosque:
    print('raiz del arbol', arbol.info)
    cantidad = [0]
    contar(arbol, cantidad)
    print('cantidad de nodos del arbol', cantidad[0])
"""
#******************************************************************************************************************************
#======================================================Ejercicio 13=============================================================
#******************************************************************************************************************************
""" 
13. Nick Fury, líder de la agencia S.H.I.E.L.D., tiene la difícil tarea de decidir qué
vengador asignará a cada nueva misión –por ahora considere que solo se asignará
un superhéroe por cada misión–. Por lo que nos solicita desarrollar un árbol de
decisión para resolver esta tarea con los siguientes requerimientos:
a. cada nodo hoja del árbol debe ser un superhéroe y en cada nodo intermedio
inclusive el raíz debe haber una pregunta;
b. si la respuesta es sí, se debe desplazar hacia el subárbol izquierdo, si es no al
subárbol derecho;
c. desarrollar una función que determine el superhéroes para una misión;
d. los Guardianas de la Galaxia son ideales para misiones intergalácticas en equipo;
e. Ant-Man es excelente en misiones de recuperación donde sea necesario no se
detectado;
f. para misiones de destrucción Hulk es una excelente opción;
g. el Capitán América es un supersoldado de ética incorruptible ideal para
comandar misiones de defensa y de recuperación;
h. Capitana Marvel es muy poderosa y puede viajar por las distintas galaxias;
Spider-Man es muy hábil y puede ser útil para v 
"""
# NO SE HACE


#******************************************************************************************************************************
#======================================================Ejercicio 14=============================================================
#******************************************************************************************************************************


"""
14. Desarrollar un algoritmo que permita decodificar mensajes en código morse, para
ello deberá resolver las siguientes consignas:
a. generar un árbol que contenga todo el alfabeto y los dígitos del 0 al 9, cuyos
códigos morse están en la siguiente figura:

b. cada nodo del árbol contendrá una letra o un digito, el cual se debe
construir de manera manual (en un árbol que no sea auto balanceado), cuya
raíz es vacía y, a partir de esta, la izquierda significa punto y la derecha guion
–y se cargaran según su codificación morse, como se observa en la siguiente
figura:

c. el espacio separa cada letra de una palabra y la “/” separa cada palabra;
d. descifrar los siguientes mensajes:
"""
"""
mensaje = ''
arbol = None
tabla = [[10000, ''],[5000, 'E'],[15000, 'T'],[2500, 'I'],[7500, 'A'],[12500, 'N'],[17500, 'M'],[1500, 'S'],[3500, 'U'],[6500, 'R'], [8500, 'W'],[11500, 'D'], [13500, 'K'],[16500, 'G'], [18500, 'O'],[1000, 'H'], [2000, 'V'], [3000, 'F'], [4000, ''],[6000, 'L'], [7000, ''] , [8000, 'P'], [9000, 'J'],[11000, 'B'], [12000, 'X'], [13000, 'C'], [14000, 'Y'],      [16000, 'Z'], [17000, 'Q'], [18000, ''], [19000, ''],[750, '5'], [1250, '4'],[2250,'3'],[4250, '2'],[9250, '1'], [10750, '6'],[15750, '7'], [17750, '8'], [18750, '9'], [19250, '0']]
#A Generar un árbol que contenga todo el alfabeto y los dígitos del 0 al 9.
#B Cuya raíz es vacía y, a partir de esta, la izquierda significa punto y la derecha guion, y se cargaran según su codificación morse.
for letra in tabla:
    arbol = insertar_nodo_morse(arbol, letra)
def decodificar_morse(raiz, cadena):
    cadena_deco = ''
    raiz_aux = raiz
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '.'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
    if (raiz_aux is not None):
        cadena_deco += raiz_aux.info[1]
    raiz_aux = raiz
    return cadena_deco
def descifrar_morse(msj, mensaje):
    for palabra in msj.split('/'):
        x = ''
        for letra in palabra.split(' '):
            x += decodificar_morse(arbol, letra)
        mensaje += x
        mensaje += ' '
    return mensaje
#D Descifrar los siguientes mensajes.
msj1 = '.--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- . - .- -- . / .- .-.. --. --- / --.- ..- . / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- / ... .. -. --- / ..- -. / -... ..- . -. / .... --- -- -... .-. . .-.-.'
msj2 = '-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-.'
msj3 = '-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-.'
msj4 = '-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-.'
msj5 = '.--. --- -.. .-. .. .- / .... .- -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. / -.. .. .- .-.-.'
print('Mensaje 1 (Dr. Abraham Erskine): ',descifrar_morse(msj1, mensaje))
print()
print('Mensaje 2 (Rocket Raccoon): ',descifrar_morse(msj2, mensaje))
print()
print('Mensaje 3 (Natasha Romanoff): ',descifrar_morse(msj3, mensaje))
print()
print('Mensaje 4 (Tony Stark): ',descifrar_morse(msj4, mensaje))
print()
print('Mensaje 5 (Steve Rogers): ',descifrar_morse(msj5, mensaje))
print()
"""
#******************************************************************************************************************************
#======================================================Ejercicio 15=============================================================
#******************************************************************************************************************************

"""
15. Desarrollar un algoritmo que permita implementar un árbol como índice para hacer
consultas a un archivo que contiene personajes de la saga de Star Wars, de los
cuales se sabe su nombre, altura y peso. Además deberá contemplar los siguientes
requerimientos:
a. en el árbol se almacenara solo el nombre del personaje, además de la
posición en la que se encuentra en el archivo (nrr);
b. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus
campos) y darlo de baja;
c. mostrar toda la información de Yoda y Boba Fett;
d. mostrar un listado ordenado alfabéticamente de los personajes que miden
más de 1 metro;

e. mostrar un listado ordenado alfabéticamente de los personajes que pesan
menos de 75 kilos;
f. deberá utilizar el TDA archivo desarrollado en el capítulo V;
"""
"""
class Personajes():
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

datos = [['Chewbacca', 1.99, 90],['Boba Fett', 1.90, 85],['C-3PO', 1,50, 87],['Yoda', 1.40, 51],['Darth Vader', 1.75, 97],['Han Solo', 1.74, 70],['Jabba el Hutt', 2.00, 110], ['Darth Maul', 1.85, 78]]

file = abrir('personajesStarwars')

#Se guardan los datos en el archivo

for dato in datos:
    x = Personajes(dato[0], dato[1], dato[2])
    guardar(file, x)

#Se cargan datos del archivo en el arbol

pos = 0

while pos < len(datos):
    aux = leer(file, pos)
    arbol = insertar_nodo(arbol, aux.nombre, pos)
    pos += 1

cerrar(file)

def darAlta(arbol):
    abrir('personajesStarwars')
    nombre = input('Ingrese el nombre del personaje que quiere dar de alta: ')
    print('Comprobando que el personaje no esta en el arbol...')
    pos = busqueda(arbol, nombre)
    if pos is not None:
        print('Puede cargar el personaje ',nombre)
        altura = input('Ingrese la altura de ',nombre,': ')
        peso = input('Ingrese el peso de ',nombre,': ')
        dato = Personajes(nombre,altura, peso)
        arbol = insertar_nodo(arbol, dato.nombre)
        guardar(file, dato)
        cerrar(file)
        datos.append([nombre, altura, peso])
    else:
        print('El personaje ya esta cargado :(')

def DarBaja(arbol):
    file = abrir('personajesStarwars')
    buscado = input('Ingrese nombre del personaje a dar de baja: ')
    arbol, x = eliminar_nodo(arbol, buscado)
    print('El personaje ', x,'Se ha eliminado con exito')

def Modificar(arbol):
    file = abrir('personajesStarwars')
    buscado = input('Ingrese nombre del personaje a modificar: ')
    val = busqueda(arbol, buscado)
    if val is not None:
        print('_______________')
        print('| 1 | Nombre  |')
        print('|-------------|')
        print('| 2 | Altura  |')
        print('|-------------|')
        print('| 3 | Peso    |')
        print('|_____________|')
        op = input('Elija campo a modificar: ')
        ar = leer(file, pos)
        if op == '1':
            nombre = input('Ingrese el nuevo nombre: ')
            dato = Personajes(nombre, ar.altura, ar.peso)
            modificar(file, pos, dato)
            ar = leer(file, pos)
            arbol = insertar_nodo(arbol, ar.nombre, pos)
        elif op == '2':
            altura = int(input('Ingrese la nueva altura: '))
            dato = Personajes(ar.nombre, altura, ar.peso)
            modificar(file, pos, dato)
            ar = leer(file, pos)
            arbol = insertar_nodo(arbol, ar.nombre, pos)
        elif op == '3':
            peso = int(input('Ingrese el nuevo peso: '))
            dato = Personajes(ar.nombre, ar.altura, peso)
            modificar(file, pos, dato)
            ar = leer(file, pos)
            arbol = insertar_nodo(arbol, ar.nombre, pos)
        else:
            print('ERROR')
    else:
        print('El personaje no existe')
    cerrar(file)

print('Arbol con los personajes de starwars: ')
inorden(arbol)
print('________________________________')
print('| 1 | Dar de alta un personaje |')
print('|------------------------------|')
print('| 2 | Dar de baja un personaje |')
print('|------------------------------|')
print('| 3 | Modificar un personaje   |')
print('|------------------------------|')
print('| 4 | Salir                    |')
print('|______________________________|')

opcion = input('Ingrese una opcion: ')
if opcion == '1':
    darAlta(arbol)
elif opcion == '2':
    DarBaja(arbol)
elif opcion == '3':
    Modificar(arbol)
elif opcion == '4':
    print()
else:
    print('ERROR')
print()
"""
#******************************************************************************************************************************
#======================================================Ejercicio 16=============================================================
#******************************************************************************************************************************
"""
16. Una empresa de nano satélites dedicada al monitoreo de lotes campo destinados al
agro, tiene problemas para la transmisión de los datos recolectados, dado que la
ventana de tiempo que dispone para enviar los datos antes de una nueva medición
es muy corta, por lo que nos solicita desarrollar un algoritmo que permita comprimir
la información para poder enviarla más rápido, para lo cual se debe tener en cuenta
los siguientes requerimientos:

a. la información transmitida por el nano satélite son estado del tiempo, humedad del suelo, y tres dígitos que identifican el lote al cual pertenecen
los datos;

b. desarrollar un árbol de Huffman que permita comprimir la información para
transmitirla, la frecuencia de la información transmitida se observa en la
siguiente tabla:

c. comprimir un mensaje y descomprimirlo, para ver si no se pierde
información durante el proceso de codificación, la trama enviada por el
nano satélite tiene el siguiente formato (estado del clima-humedad del
suelo-cod1-cod2-cod3), por ejemplo la siguiente trama es válida
“NubladoBaja157”, –los guiones son a fines de comprender como está
formada la trama pero no forman parte de la misma–;
d. determinar la diferencia en tamaño de memoria utilizada por la trama
original y la trama comprimida –puede utilizar la función getsizeof() de la
librería sys–.
"""
"""

tabla = []

archivo = open('valores')

linea = archivo.readline()

print('archivo')
while linea:
    linea = linea.replace('\n', '')
    tabla.append(linea.split(';'))
    linea = archivo.readline()

dic = {}


def como_comparo(elemento):
    return elemento[1]

def como_comparo_nodo(elemento):
    return elemento.valor

tabla.sort(key=como_comparo)

bosque = []

for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

# for elemento in bosque:
#     print(elemento.info, elemento.valor)
# print()

while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)


#por_nivel(bosque[0])

def generar_tabla(raiz, dic, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            dic[raiz.info] = cadena
            #print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, dic, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, dic, cadena)


generar_tabla(bosque[0],dic)
print(dic)

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena.split('-'):
        cadena_cod += dic[caracter]
    return cadena_cod

cadena = "Nublado-Baja-1-5-7"
cadena_cod = codificar(cadena, dic)
print(cadena_cod)
print('cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)

"""
#******************************************************************************************************************************
#======================================================Ejercicio 17=============================================================
#******************************************************************************************************************************
"""
17. Se tiene un archivo con los Pokémons de las 8 generaciones cargados de manera
desordenada (890 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, para el cual debemos construir tres árboles para
acceder de manera eficiente a los datos almacenados en el archivo, contemplando
lo siguiente:
a. los índices de cada uno de los árboles deben ser nombre, número y tipo;
b. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco
“bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o
contengan dichos caracteres–;
c. mostrar todos los nombres de todos los Pokémons de un determinado tipo
agua, fuego, planta y eléctrico;
d. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
e. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y
Tyrantrum;

f. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.
"""
"""
datos = [['Bulbasaur', 1, 'planta/veneno', 'fuego/psiquico'],
         ['Bulivysaur', 2, 'planta/veneno', 'fuego/psiquico'], 
         ['Charmander', 4, 'fuego', 'agua/tierra'],
         ['Charizard', 6, 'fuego/volador', 'agua/electrico'], 
         ['Squirtle', 7, 'agua', 'planta/electrico'], 
         ['Butterfree', 12, 'bicho/volador', 'fuego/electrico/hielo'], 
         ['Pidgeotto', 17, 'normal/volador', 'hielo/roca'], 
         ['Rattata', 19, 'normal', 'lucha'], 
         ['Weedle', 13, 'bicho/veneno', 'fuego/psiquico/volador'], 
         ['Pikachu', 25, 'electrico', 'tierra'], 
         ['Raichu', 26, 'electrico', 'tierra'], 
         ['Meowth', 52, 'normal', 'lucha'],
         ['Growlithe', 58, 'fuego', 'agua/roca'], 
         ['Tentacool', 72, 'agua/veneno', 'psiquico/electrico'], 
         ['Weepinbell', 70, 'planta/veneno', 'fuego/volador/hielo']]

arbol = None
arbol_nombre = None
arbol_numero = None
arbol_tipo = None

class Pokemon():
    def __init__(self, nombre, numero , tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad

def inorden_tipo(raiz, archivo):
    if raiz is not None:
        inorden_tipo(raiz.izq, archivo)
        poke = leer(archivo, raiz.nrr)
        if poke.tipo.find('agua') > -1 or poke.tipo.find('fuego') > -1 or poke.tipo.find('planta') > -1 or poke.tipo.find('electrico') > -1:
            print(raiz.info,'es de tipo', poke.tipo)
        inorden_tipo(raiz.der, archivo)

def inorden_poke_nombre(raiz, archivo):
    if raiz is not None:
        inorden_poke_nombre(raiz.izq, archivo)
        poke = leer(archivo, raiz.nrr)
        if poke.nombre:
            print(raiz.info,'-', poke.numero)
        inorden_poke_nombre(raiz.der, archivo)


def inorden_poke_numero(raiz, archivo):
    if raiz is not None:
        inorden_poke_numero(raiz.izq, archivo)
        poke = leer(archivo, raiz.nrr)
        if poke.numero:
            print(raiz.info,'-', poke.nombre)
        inorden_poke_numero(raiz.der, archivo)


def inorden_debilidad(raiz, archivo, clave):
    if raiz is not None:
        inorden_debilidad(raiz.izq, archivo, clave)
        poke = leer(archivo, raiz.nrr)
        if poke.debilidad.find(clave) > -1:
            print(raiz.info, 'presenta debilidad al tipo', clave, '-', poke.debilidad)
        inorden_debilidad(raiz.der, archivo, clave)

file = abrir('pokemon')

#Cargamos los datos en el archivo

for pok in datos:
    x = Pokemon(pok[0], pok[1], pok[2], pok[3])
    guardar(file,x)

pos = 0
while pos < len(datos):
    pok = leer(file, pos)
    arbol = insertar_nodo(arbol, [pok.nombre, pok.numero, pok.tipo, pok.debilidad], pos)
    arbol_nombre = insertar_nodo(arbol_nombre, pok.nombre, pos)
    arbol_numero = insertar_nodo(arbol_numero, pok.numero, pos)
    arbol_tipo = insertar_nodo(arbol_tipo, pok.tipo, pos)
    pos += 1
cerrar(file)

busc = input('Ingrese el nombre del pokemon a buscar: ')
busqueda_proximidad(arbol_nombre, busc)

print('Pokemones de tipo: agua, fuego, planta o electrico')
inorden_tipo(arbol_nombre, file)
print()
print('Barrido pokemon por nombre')
inorden_poke_nombre(arbol_nombre, file)
print()
print('Barrido pokemon por numero')
inorden_poke_numero(arbol_numero, file)
print()
print('Barrido pokemon por nivel')
por_nivel(arbol_nombre)
print()
deb = input('Ingrese tipo de debilidad: ')
inorden_debilidad(arbol_nombre, file, deb)
print()
cerrar(file)

"""

#******************************************************************************************************************************
#======================================================Ejercicio 18=============================================================
#******************************************************************************************************************************
"""
18. La armería de la base Starkiller, central de la primera orden, almacena los registros
de los reportes de fallos en armas de las tropas de sus principales generales –Kylo
Ren, general Hux y capitana Phasma–. Para dicha labor, se solicita desarrollar un
algoritmo que permita resolver las siguientes tareas:
a. se debe registrar el nombre del general a cargo de la misión, fecha de la
misión –a los fines del ejercicio considere como máximo 20 fechas de
misiones–, código de blaster generado de manera aleatoria –de 8 dígitos y
no puede estar repetido–, estado del blaster (si falló o no) y el tipo de
soldado que portaba el blaster –Imperial Stromtrooper, Imperial Scout
Trooper, Imperial Death Trooper, Sith Trooper o First Order Stromtrooper–;
b. debe generar y cargar al menos 10 000 registros;
c. determinar el total de armas que fallaron por general;
d. indicar la cantidad y tipo de soldado de las misiones de Kylo Ren;
e. determinar cuántos Sith Troopers salieron en misiones y a cuantos les
fallaron los blasters;
f. listar los códigos de los blasters de las misiones de una determinada fecha,
indicando además el porcentaje de armas que fallaron;

g. mostrar los datos del blaster código “75961380” si fue utilizado en alguna
misión. 
"""
# NO SE HACE


#******************************************************************************************************************************
#======================================================Ejercicio 19=============================================================
#******************************************************************************************************************************
"""
19. Desarrollar los algoritmos necesarios que permitan almacenar libros, de los cuales se
conoce su título, ISBN, autores, editorial y cantidad páginas en un archivo, contemplando los siguientes requerimientos y tareas:
a. utilizar el TDA archivo desarrollado en el capítulo V;
b. deberá cargar al menos 100 libros;
c. implementar tres árboles para manejar los índices de acceso, estos serán
por título, ISBN y autores. En cada nodo del árbol se almacenará el campo
clave correspondiente y la posición en el archivo donde está el resto de la
información;
d. las búsquedas deberán ser de la siguiente manera:
i. por exactitud en el árbol de ISBN,
ii. que esté contenido en el árbol de autores –es decir si son más de un
autor y busco por uno debería encontrarlo–,
iii. por proximidad en el inicio del nombre en el árbol de título –si busco
“Alg” debería encontrar todos los libros cuyo nombres comienzan
así– Ahora resuelva las siguientes consultas mostrando toda la información de los libros
correspondiente:
a. los libros de los autores Tanenbaum, Connolly, Rowling, Riordan, Morgan
Kass;
b. mostrar los libros de “minería de datos”, “algoritmos” y “bases de datos”;
c. mostrar los libros de más de 873 páginas;
d. mostrar los datos del libro ISBN 9789504967453;
e. mostrar el autor del libro “los 100”.
"""

class Libros:
    def __init__(self, titulo, isbn, autores, editorial, cantidadPag): 
        self.titulo = titulo 
        self.isbn = isbn
        self.autores = autores
        self.editorial = editorial
        self.cantidadPag = cantidadPag
"""
datos = [['Mineria de datos' ,'1234', 'Tanenbaum' , 'Santillan' ,'256'],
         ['Algoritmos I' ,'4567', 'Connolly' , 'Acantilado' ,'380'],
         ['Algoritmos II' ,'8910', 'Rowling' , 'Santillan' ,'450'],
         ['Los 100' ,'1112', 'Riordan' , 'Acantilado' ,'360'],
         ['Bases de datos' ,'1314', 'Morgan Kass' , 'Santillan' ,'880'],
         ['Algoritmos y estructuras de datos' ,'9789504967453', 'Tanenbaum' , 'Acantilado' ,'950']]


arbol_titulo = None
arbol_isbn = None
arbol_autores = None

file = abrir('libros')

#Se guardan los datos en el archivo

for dato in datos:
    x = Libros(dato[0], dato[1], dato[2], dato[3], dato[4])
    guardar(file, x)
cerrar(file)
#Se cargan datos del archivo en el arbol

pos = 0

file = abrir('libros')
while pos < len(datos):
    aux = leer(file, pos)
    arbol_titulo = insertar_nodo(arbol_titulo, aux.titulo, pos)
    arbol_isbn = insertar_nodo(arbol_isbn, aux.isbn , pos)
    arbol_autores = insertar_nodo(arbol_autores, aux.autores , pos)
    pos += 1
cerrar(file)

pos = (str(input('Ingrese el isbn del libro a buscar: ')))
pos = busqueda(arbol_isbn, pos)
if (pos is not None):
    file = abrir('libros')
    x = leer(file, pos.nrr)
    print( 'Titulo:', x.titulo, '\nISBN:', x.isbn, '\nAutor / Autores: ', x.autores, '\nEditorial:', x.editorial, '\nCantidad de paginas:', x.cantidadPag)
    cerrar(file)

bus = str(input("Ingrese una palabra para hacer una busqueda por proximidad de los libros: "))
file = abrir('libros')
busqueda_proximidad_archivo_libros(arbol_titulo, bus, file)

a = input()

print('Libros del autor Tanenbaum: ')
busqueda_proximidad_archivo_libros(arbol_autores, 'Tanenbaum', file)

a = input()

print('Libros del autor Connolly: ')
busqueda_proximidad_archivo_libros(arbol_autores, 'Connolly', file)

a = input()

print('Libros del autor Rowling: ')
busqueda_proximidad_archivo_libros(arbol_autores, 'Rowling', file)

a = input()

print('Libros del autor Riordan: ')
busqueda_proximidad_archivo_libros(arbol_autores, 'Riordan', file)

a = input()

print('Libros del autor Morgan Kass: ')
busqueda_proximidad_archivo_libros(arbol_autores, 'Morgan Kass', file)

a = input()

print('Datos de los libros de Mineria de datos')
busqueda_proximidad_archivo_libros(arbol_titulo, 'Mineria de datos', file)

a = input()

print('Datos de los libros de Algoritmos')
busqueda_proximidad_archivo_libros(arbol_titulo, 'Algoritmos', file)

a = input()

print('Datos de los libros de Base de datos')
busqueda_proximidad_archivo_libros(arbol_titulo, 'Bases de datos', file)

a = input()

print('Datos de los libros con mas 873 paginas: ')
busqueda_archivo_libros(arbol_autores, '873', file)
a=input()

print('Datos del libro ISBN 9789504967453')
busqueda_proximidad_archivo_libros(arbol_isbn, '9789504967453', file)

a = input()

bus = str(input('Ingrese un titulo de un libro para conocer su autor: '))
busqueda_proximidad_archivo_autor(arbol_titulo,bus, file)
cerrar(file)
"""
#******************************************************************************************************************************
#======================================================Ejercicio 20=============================================================
#******************************************************************************************************************************
"""
20. Implementar un algoritmo que permita generar un árbol de decisión meteorológico
para la predicción del estado del tiempo basado en las reglas de la siguiente figura, considerando los siguientes requerimientos:
a. los 5 posibles estados del tiempo son despejado, parcialmente nublado, mayormente nublado, nublado y lluvia;
b. los nodos hojas del árbol representan los estados del tiempo que predice el
árbol –en la figura están con negrita–;

c. en cada nodo deberá almacenar el nombre de la variable o campo que se
utilizará en ese nodo para la decisión y el valor umbral: se avanza hacia la
izquierda si el valor es menor o igual y se avanza a la derecha cuando el valor
es mayor;
d. dado un nuevo registro con datos meteorológicos del cual se conoce
temperatura, presión, humedad, visibilidad, velocidad del viento, se debe
predecir el estado del tiempo de manera automática.
"""

"""tabla = []

archivo = open('valores')

linea = archivo.readline()

while linea:
    linea = linea.replace('\n', '')
    tabla.append(linea.split(';'))
    linea = archivo.readline()

dic = {}


def como_comparo(elemento):
    return elemento[1]

def como_comparo_nodo(elemento):
    return elemento.valor

tabla.sort(key=como_comparo)

bosque = []

for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

# for elemento in bosque:
#     print(elemento.info, elemento.valor)
# print()

while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)


#por_nivel(bosque[0])

def generar_tabla(raiz, dic, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            dic[raiz.info] = cadena
            #print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, dic, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, dic, cadena)


generar_tabla(bosque[0],dic)

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena.split('-'):
        cadena_cod += dic[caracter]
    return cadena_cod

cadena = "Nublado-Baja-1-5-7"
print('Mensaje a codificar:', cadena)
print()
cadena_cod = codificar(cadena, dic)
print('Cadena codificada')
print(cadena_cod)
print()
print('Cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)
"""
#******************************************************************************************************************************
#======================================================Ejercicio 21=============================================================
#******************************************************************************************************************************
"""
Parta de la base del árbol genealógico “greek-gods” (n-arios) que se observa en el
siguiente link:
https://drive.google.com/file/d/13lMB6A2k4zO2zq-wuTgdxZdgwUKLl4Tr/view?usp=
sharing, y utilice la transformada de Knuth para convertirlo en un árbol binario que
permita realizar las siguiente actividades (no se deben utilizar árboles balanceados):
a. la raíz del árbol debe ser Urano;
b. además del nombre de los dioses, deberá cargar una breve descripción de
quien es o lo que representa, no más de 20 palabras;
c. listar el árbol por niveles, es decir, mostrando primero los hermanos. Para
esto desarrolle una función barrido llamada “hermanos(raíz)” que devuelva

todos los hijos derechos de un determinado nodo de un árbol general
transformado a binario;
d. solo se representarán las relaciones padre-hijo, a excepción de los dioses
que en la imagen no tengan padre, –en este caso se deberá cargar la
relación madre-hijo–, en los demás la madre será almacenada en un campo
del nodo;
e. dado el nombre de un dios mostrar los hijos de este;
f. dado el nombre de un dios mostrar su nombre, madre, hermanos y
sus hijos;
g. realizar un barrido inorden, preorden y por nivel de dicho árbol;
h. realizar un barrido inorden mostrando el nombre de cada dios y el de su
madre;
i. mostrar todos los ancestros de un determinado dios;
j. generar un bosque eliminando el nodo Uranos:
i. determinar cuántos árboles forman dicho bosque,
ii. realizar un barrido inorden de cada árbol del bosque,
iii. determinar cuántos nodos hay en cada árbol y cuál es el nombre del
dios del nodo raíz del árbol más grande;

k. mostrar todos los hijos de Tea.
"""
"""
arbol = None


archivo = open('greek_gods')

linea = archivo.readline()

print('archivo')
while linea:        
    linea = linea.replace('\n', '')
    dios = linea.split(';')
    nodo = nodoArbolGreek(dios[0], dios[2])
    print('insertar', dios[0])
    if(arbol is None):
        arbol = nodo
    else:
        pos = []
        busqueda_nario(arbol, dios[1], pos)
        print('resultado de busqueda', pos[0].info)
        insertar_nario(pos[0], nodo)

    preorden(arbol)
    a = input()
    linea = archivo.readline()


archivo.close()

por_nivel_nario(arbol)

pos = []
busqueda_nario(arbol, 'zeus', pos)

hijo = pos[0].izq

while(hijo is not None):
    print(hijo.info)
    hijo = hijo.der

bosque = []
hijo = arbol.izq

while(hijo is not None):
    aux = hijo.der
    hijo.der = None
    bosque.append(hijo)
    hijo = aux

print('cantidad de arboles del bosque', len(bosque))
for arbol in bosque:
    print('raiz ------------------>', arbol.info)
    inorden(arbol)
    print()
"""
#******************************************************************************************************************************
#======================================================Ejercicio 22=============================================================
#******************************************************************************************************************************
"""
22. Implementar un algoritmo que permita generar un árbol con los datos de la
siguiente tabla y resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de
criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el
nombre del héroe o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y
Jabalí de Erimanto indicando que Heracles las atrapo;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;

k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que
Heracles derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles.
"""
# NO SE HACE


#******************************************************************************************************************************
#======================================================Ejercicio 23=============================================================
#******************************************************************************************************************************
"""
23. Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la
siguiente tabla –para lo cual deberá calcular primero las frecuencias de cada
carácter a partir de la cantidad de apariciones del mismo–, para resolver las
siguientes actividades:
a. la generación del árbol debe hacerse desde los caracteres de menor
frecuencia hasta los de mayor, en el caso de que dos caracteres tengan la
misma frecuencia, primero se toma el que este primero en el alfabeto, el
carácter “espacio” y “coma” se consideraran anteúltimo y último
respectivamente en el orden alfabético;
b. descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la
misma manera que el ejemplo visto anteriormente:
i. Mensaje 1: “100010111010110000101110100011100000110110000001111001
1110100101100001101001110011010001011101011111110100001

1110011111100111101000110001100000010110101111011111110
1110101101101110011101101111001111111001010010100101000
0010110101100010110011010001110010010110000110010001101
0110101011111111111011011101110010000100101011000111111
1000100011101100110010110100011011111010110100011011100
0000011100100101010001111110000110010110101110011001111
0100011000110000001011010111110011100”
ii. Mensaje 2: “011010101101110010100011110101110011011101011011010000
1000111010100101111010011111110111001010001111010111001
1011101011000011000100110100011100100100011000101100110

01110010010000111101111010” c. finalmente, calcule el espacio de memoria requerido por el mensaje original
y el comprimido.
"""
#******************************************************************************************************************************
#======================================================Ejercicio 24=============================================================
#******************************************************************************************************************************
"""
24. A partir del organigrama de un empresa de desarrollo que se presenta en la
siguiente figura (árbol n-ario) implementar las funciones necesarias para resolver
los siguientes requerimientos:
a. utilizar la transformada de Knuth para convertirlo en un árbol binario;
b. realizar un barrido inorden y por nivel de dicho árbol;

c. agregue una persona a cada puesto de la empresa, salvo a los puesto de
desarrollador, tester y soporte al cliente, en estos cargue cinco personas;
d. mostrar todos los empleados dependiente del líder de proyecto;
e. mostrar todo los empleados dependientes directamente del director de
proyectos;
f. mostrar todos los empleados del nivel tres del organigrama(recuerde que la
raíz es el nivel uno).
"""

# NO SE HACE