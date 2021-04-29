from tda_lista_lista import Lista, barrido, busqueda, eliminar, insertar, lista_vacia, tamanio
from random import randint,choice
from datetime import date

lista = Lista()

def cargar_lista(lista):
    for i in range(10):
        insertar(lista, randint(0,100))

def cargar_lista_letras(lista):
    for i in range(10):
        insertar(lista, chr(randint(65,122)))

# ******************************************************************************************************************************#
# ====================================================== Ejercicio 1 ===========================================================#
# ******************************************************************************************************************************#

"""
1.Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
"""
def cantidad_de_nodos():
    cargar_lista(lista)
    cont_nodo = 0
    aux = lista.inicio
    while(aux is not None):
        cont_nodo += 1
        aux = aux.sig
    return cont_nodo

"""
print("La cantidad de nodos es", cantidad_de_nodos())
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 2 ===========================================================
# ******************************************************************************************************************************
"""
2.Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de
caracteres.
"""
vocales = ["a","e","i","o","u","A","E","I","O","U"]

def eliminar_vocales():
    cargar_lista_letras(lista)
    barrido(lista)
    aux = lista.inicio
    for i in range(tamanio(lista)):
        if (aux.info in vocales):
            eliminar(lista, aux.info)
        aux = aux.sig
    print("lista modificada")
    return print(barrido(lista))

"""
eliminar_vocales()
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 3 ===========================================================
# ******************************************************************************************************************************
"""
3.Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en
dos, una que contenga los números pares y otra para los números impares.
"""

def dividir_listas():
    lista_aux = Lista()

    cargar_lista(lista)
    print("Lista: ")
    barrido(lista)
    aux = lista.inicio
    while(aux is not None):
        if ((aux.info % 2) == 0):
            insertar(lista_aux, aux.info)
            eliminar(lista, aux.info)
        aux = aux.sig
    print("Lista par:")
    barrido(lista_aux)
    print("Lista impar:" )
    barrido(lista)
"""
print(dividir_listas())
"""
# ******************************************************************************************************************************
# ====================================================== Ejercicio 4 ===========================================================
# ******************************************************************************************************************************
"""
4.Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
"""
def insertar_iesimo(lista,pos,elemento):
    nodo = nodoLista()
    nodo.info = elemento
    aux = lista.inicio
    if pos >= 0 and pos <= lista.tamanio:
        if pos < lista.tamanio:
            for i in range(1, pos):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
        else:
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nodo

"""
cargar_lista_letras(lista)
pos = int(input('Ingrese la posicion en que quiere insertar el elemento: '))
pos = pos-1
elemento = input('Ingrese el elemento que quiere insertar: ')
print(insertar_iesimo(lista, pos, elemento))
barrido(lista)
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 5 ===========================================================
# ******************************************************************************************************************************
"""
5.Dada una lista de números enteros eliminar de estas los números primos.
"""

def nro_primo():
    cargar_lista(lista)
    print('Lista:')
    barrido(lista)
    aux = lista.inicio
    while(aux is not None):
        cont = 0
        for i in range (1, aux.info + 1):
            if ((aux.info % i) == 0):
                cont += 1
        if cont == 2:
            eliminar(lista, aux.info)
        aux = aux.sig  
    print("lista modificada")
    return barrido(lista)
"""
print(nro_primo())
"""
# ******************************************************************************************************************************
# ====================================================== Ejercicio 6 ===========================================================
# ******************************************************************************************************************************
"""
6.Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año
aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la
funciones necesarias para poder realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la
palabra “traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea
anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que cominezan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.
"""

def personajesMDC():
    lista_personajes = Lista()
    personajes = ['', '', '', '']
    archivo = open('personajes')
    linea = archivo.readline()
    while linea:
        linea = linea.replace('\n', '')
        linea = linea.split(';')
        linea[0] = linea[0].title()
        linea[1] = int(linea[1])
        linea[2] = linea[2].title()
        linea[3] = linea[3].title()
        insertar(lista_personajes, linea)
        linea = archivo.readline()
    print("Lista de personajes:")
    barrido(lista_personajes)

    contMarvel = 0
    contDC = 0
    aux = lista_personajes.inicio
    while (aux is not None):
        personajes = aux.info
        if personajes[0] == "Linterna Verde":
            eliminar(lista_personajes, personajes)
            print("Se elimino el nodo de",personajes[0])
        elif personajes[0] == "Wolverine":
            print('El año de aparicion de Wolverine es en año', personajes[1])
        elif personajes[0] == "Dr. Strange":
            personajes[2] = "Marvel"
            print("El personaje",personajes[0],"cambio su casa de DC a",personajes[2])
        if 'traje' in personajes[3] or 'armadura' in personajes[3]:
            print('El personaje', personajes[0], 'tiene la palabra traje o armadura en su biografia')
        if personajes[1] < 1963:
            print('El personaje',personajes[0],'con su casa',personajes[2],'tiene su aparicion antes del 1963.')
        if(personajes[0] == "Capitana Marvel" or personajes[0] == "Mujer Maravilla"):
            print("El personaje",personajes[0],"pertence a la casa",personajes[2])
        if(personajes[2] == "Marvel"):
            contMarvel += 1
        else:
            contDC += 1
        aux = aux.sig
    print("La casa Marvel tiene",contMarvel,"personajes y la casa DC tiene",contDC,"personajes")
    print("Lista modificada: ")
    return barrido(lista_personajes)

#print(personajesMDC())

# ******************************************************************************************************************************
# ====================================================== Ejercicio 7 ===========================================================
# ******************************************************************************************************************************
"""
7.Implementar los algoritmos necesarios para resolver las siguientes tareas:
a. concatenar dos listas, una atrás de la otra;
b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su
orden;
c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección
de ambas;
d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

"""
lista1 = Lista()
lista_conc = Lista()
#A
def lista_concatenada(lista,lista1):
    print('Lista 1')
    barrido(lista)
    print('Lista 2')
    barrido(lista1)
    aux = lista1.inicio
    for i in range(0,tamanio(lista1)):
        insertar(lista,aux.info)
        aux = aux.sig
    print('Lista concatenada')
    return barrido(lista)

#B y C
def lista_concatenada_or(lista, lista1):
    repetidos = 0
    lista_conc = Lista()
    aux = lista.inicio
    while(aux is not None):
        pos = busqueda(lista_conc, aux.info)
        if(pos is None):
            insertar(lista_conc, aux.info)
        else:
            repetidos += 1
        aux = aux.sig
  
    print("Lista concatenada sin repetidos")
    barrido(lista_conc)
    return print('Hay ',repetidos,' elementos repetidos')

#D
def eliminar_nodos(lista):
    aux = lista.inicio
    while aux is not None:
        eliminar(lista, aux.info)
        print('Se elimino el elemento:', aux.info)
        aux = aux.sig
    

"""
cargar_lista(lista)
cargar_lista(lista1)    
print(lista_concatenada(lista,lista1))
print(lista_concatenada_or(lista,lista1))
print(eliminar_nodos(lista))
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 9 ===========================================================
# ******************************************************************************************************************************
"""
9.Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos
con la siguiente información: materia que rindió, nota obtenida y fecha de parcial.
Desarrollar un algoritmo que permita realizar la siguientes actividades:
a. mostrar los alumnos ordenados alfabéticamente por apellido;
b. indicar los alumnos que no desaprobaron ningún parcial;
c. determinar los alumnos que tienen promedio mayor a 8,89;
d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
e. mostrar el promedio de cada uno de los alumnos;
f. debe modificar el TDA para implmentar lista de lista.
"""
alumnos = ['Tomas', 'Fernando', 'Joaquin', 'Mateo', 'Rafael', 'Antonella']
apellidos = ['Bidegain','Picart','Traverso','Barbera','Rozzin','Greissing']
materias = ['Algoritmos y estructuras de datos','Calculo diferencial e integral','Ingenieria de software']

class Alumno(object):
    def __init__(self,nombre,apellido,legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo

    def __str__(self):
        return '===    ' + self.nombre + ' - ' + self.apellido + ' - ' + str(self.legajo) + '    ==='

class Parciales(object):
    def __init__(self,materia,nota,fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return '===    ' + self.materia + '| Nota = '+ str(self.nota) + '| fecha = ' + str(self.fecha) + '    ==='

estudiantes = Lista()
def parciales_alumnos(estudiantes):
    print('Alumnos: ')
    for i in range(len(alumnos)):
        legajo = i+1
        dato = Alumno(alumnos[i],apellidos[i],legajo)
        insertar(estudiantes, dato, 'apellido')
    barrido(estudiantes)
    print(' ')

    for i in range(tamanio(estudiantes)):
        i += 1
        for j in range(1,3):
            pos = busqueda(estudiantes,i,'legajo')
            dato = Parciales(materias[j],randint(4,10),date(2020,randint(1,12),randint(1,30)))
            insertar(pos.sublista, dato, 'materia')
    aux = estudiantes.inicio
    while aux is not None:
        print(aux.info)
        barrido(aux.sublista)
        aux = aux.sig
    
    print(' ')

    aux = estudiantes.inicio
    p = 0
    while aux != None:
        aprobado = True
        c = 0
        promedio = 0
        pos = aux.sublista.inicio
        while pos != None:
            c += 1
            if pos.info.nota < 7:
                aprobado = False
            promedio += pos.info.nota
            pos = pos.sig
        
        if aprobado == True:
            print(aux.info[0] + ' ' + aux.info.apellido + ' tiene todas las materias aprobadas')
        if ((promedio / c) > 8.89):
            p += 1
            print(aux.info[0] + ' ' + aux.info.apellido + ' presenta un promedio mayor a 8,89 con: ' + str(round(prom/c,2)))
        aux = aux.sig
    if (p < 1):
        print('No existen alumnos con promedio mayor a 8,89.')
    print('')

    print('Alumnos con apellido cuya inicial es la L')
    aux = estudiantes.inicio
    while aux != None:
        if aux.info.apellido[0] == 'L':
            print(aux.info[0] + ' ' + aux.info.apellido + ';  legajo ' + str(aux.info.legajo))
        aux = aux.sig

    print('')
    print('Promedio de todos los alumnos:')
    aux = estudiantes.inicio
    while aux != None:
        suma_notas = 0
        c = 0
        pos = aux.sublista.inicio
        while pos != None:
            suma_notas += pos.info.nota
            c += 1
            pos = pos.sig
        promedio = (suma_notas / c)
        print('El promedio de el alumno ' + aux.info[0] + ' ' + aux.info.apellido + ' es ' + str(round(promedio,2)))
        aux = aux.sig
"""
print(parciales_alumnos(estudiantes))
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 10 ===========================================================
# ******************************************************************************************************************************
"""
10.Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o
artista, duración y cantidad de reproducciones durante el último mes. Desarrollar un
algoritmo que permita realizar las siguientes actividades:
a. obtener la información de la canción más larga;
b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
c. obtener todas las canciones de la banda Arctic Monkeys;
d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
"""
def Spotify():
    canciones = ['La jeepeta', 'C90','Relacion','Porfa','Fabuloso','Me gusta lo simple','Golden trunks','Star treatment']
    artistas = ['Nio Garcia','Jhon C','Sech','Justin Quiles','Justin Quiles','Duki','Arctic Monkeys','Arctic Monkeys']
    spoti = Lista()
    una_pal = Lista()
    for i in range(len(artistas)):
        duracion = randint(2,6)
        reproducciones = randint(20000,80000)
        dato = [canciones[i],artistas[i],duracion,reproducciones]
        insertar(spoti,dato)
    print('| Titulo de cancion | Artista / Banda | Duracion | Reproducciones |')
    barrido(spoti)

    aux = spoti.inicio
    mayor = 0
    top5 = 0
    top10 = 0
    top40 = 0
    while aux is not None:
        #a
        if aux.info[2] > mayor:
            mayor = aux.info[2]
            cancion = aux.info
        #b
        if aux.info[3] > top5:
            top5 = aux.info[3]
            top_5 = aux.info
        elif aux.info[3] > top10:
            top10 = aux.info[3]
            top_10 = aux.info
        elif aux.info[3] > top40:
            top40 = aux.info[3]
            top_40 = aux.info
        aux = aux.sig
    
    print('Cancion con mayor reproducciones: ')
    print(cancion)
    print('')
    print('Top 5:')
    print(top_5)
    print('Top 10')
    print(top_10)
    print('Top 40')
    print(top_40)
    print('Canciones de la banda Arctic Monkeys:')
    aux = spoti.inicio
    espacio = False 
    while aux is not None:
        if aux.info[1] == 'Arctic Monkeys':
            print(aux.info[0])
        dat = aux.info[1]
        for i in range(len(aux.info[1])):
            if aux.info[1][i] == ' ':
                espacio = False
                break
            else:
                espacio = True
        if espacio == True:
            insertar(una_pal, aux.info)
        aux = aux.sig
    
    print('Bandas o artistas cuyo nombre sea una sola palabra: ')
    barrido(una_pal)
"""
print(Spotify())
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 11 ===========================================================
# ******************************************************************************************************************************
"""
11.Dada una lista que contiene información de los personajes de la saga de Star Wars con la
siguiente información nombre, altura, edad, género, especie, planeta natal y episodios en
los que apareció, desarrollar los algoritmos que permitan realizar las siguientes
actividades:
a. listar todos los personajes de género femenino;
b. listar todos los personajes de especie Droide que aparecieron en los primeros seis
episodios de la saga;
c. mostrar toda la información de Darth Vader y Han Solo;
d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y
VI;
g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
h. mostrar toda la información de los personajes cuya altura es menor a 70
centímetros;
i. determinar en qué episodios aparece Chewbacca y mostrar además toda su
información.
"""

def personajes_2():
    personajes = Lista()
    episodios = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    archivo = open('personajes2')
    linea = archivo.readline()
    while linea:
        linea = linea.replace('\n', '')
        linea = linea.split(';')
        linea[0] = linea[0].title()
        linea[1] = float(linea[1])
        linea[2] = int(linea[2])
        linea[3] = linea[3].title()
        linea[4] = linea[4].title()
        linea[5] = linea[5].title()
        insertar(personajes, linea)
        linea = archivo.readline()
    
    aux = personajes.inicio
    while aux is not None:
        cant = (randint(1,15))
        lista_epis = []
        for i in range(cant):
            epis = choice(episodios)
            if len(lista_epis) == 0:
                lista_epis.append(epis)
                insertar(aux.sublista,epis)
            if epis not in lista_epis:
                insertar(aux.sublista,epis)
                lista_epis.append(epis)
        aux = aux.sig
    print('Personajes segun Planetas Natales: ')
    barrido(personajes)
    print()
    aux = personajes.inicio
    # A
    print('Lista de personajes femeninos')
    while aux != None:
        if aux.info[3] == 'F':
            print(aux.info)
        aux = aux.sig
    print()
    # B
    print('Personajes Droide, que participaron en los primeros seis episodios de la saga:')
    aux = personajes.inicio
    while not aux == None:
        pos = aux.sublista.inicio
        while not pos == None:
            if pos.info == 1:
                print(aux.info[0] + ' participo en el capitulo 1.')
            elif pos.info == 2:
                print(aux.info[0] + ' participo en el capitulo 2.')
            elif pos.info == 3:
                print(aux.info[0] + ' participo en el capitulo 3.')
            elif pos.info == 4:
                print(aux.info[0] + ' participo en el capitulo 4.')
            elif pos.info == 5:
                print(aux.info[0] + ' participo en el capitulo 5.')
            elif pos.info == 6:
                print(aux.info[0] + ' participo en el capitulo 6.')
            else:
                break
            pos = pos.sig
        aux = aux.sig
    # C
    print()
    print('Información de Darth Vader y Han Solo')
    aux = personajes.inicio
    while aux != None :
        if (aux.info[0] == 'Darth Vader') or (aux.info[0] == 'Han Solo'):
            print(aux.info)
        aux = aux.sig
    # D
    print()
    print('Personajes que aparecen en el episodio VII y en los tres anteriores:')
    aux = personajes.inicio
    p = 0
    while aux != None:
        pos = aux.sublista.inicio
        c = 0
        while pos != None:
            if pos.info == 4:
                c += 1
            elif pos.info == 5:
                c += 1
            elif pos.info == 6:
                c +=1
            elif pos.info == 7:
                c += 1
                if c == 4:
                    print(aux.info[0] +', aparecio en los capitulos 4,5,6 y 7.')
                    p += 1
            pos = pos.sig
        aux = aux.sig
    if p == 0:
        print('No hay personajes que mostrar en esta lista.')
    # E
    print()
    print('Personajes con edad mayor a 850 años')
    aux = personajes.inicio
    mayor = ''
    ed = 0
    while aux != None:
        if aux.info[2] > 850:
            print(aux.info[0] + ': tiene ' + str(aux.info[2]) + ' años.')
        if ed < aux.info[2]:
            mayor = aux.info[0]
            ed = aux.info[2]
        aux = aux.sig
    print()
    print(' El personaje de mayor edad es: '+ mayor+ ', con '+ str(ed) +' años ')
    # F
    print()
    print('Se eliminaran los personajes que hayan aparecido solamente en los capitulos: 4,5 y 6')
    aux = personajes.inicio
    p = 0
    while aux != None:
        pos = aux.sublista.inicio
        c = 0
        n = 0
        while pos != None:
            if pos.info == 4:
                c += 1
            elif pos.info == 5:
                c += 1
            elif pos.info == 6:
                c += 1
            else:
                n += 1
                break
            pos = pos.sig
        if (c == 3) and (n == 0):
            eliminar(personajes,aux.info[0],'nombre')
            print('Se ha eliminado al personaje '+ aux.info[0])
            p += 1
        aux = aux.sig
    if p == 0:
        print('No hay personajes que mostrar en esta lista.')
    print()
    # G
    print('Personajes Humanos cuyo planeta de origen es Alderaan;')
    aux = personajes.inicio
    while aux != None:
        if (aux.info[4] == 'Humano') and (aux.info[5] == 'Alderaan'):
            print(aux.info[0] +': es Humano y su planeta natal es: ' + aux.info[5]) 
        aux = aux.sig
    print()
    # H
    print('Personajes cuya altura es menor a 70 centímetros;')
    aux = personajes.inicio
    while aux != None:
        if aux.info[1] < 0.70:
            print(aux.info)
        aux = aux.sig
    print()
    # I
    aux = personajes.inicio
    while aux != None:
        if aux.info[0] == 'Chewbacca':
            print('- Informacion de Chewbacca:')
            print(aux.info)
            print('Episodios en los que aparece:')
            pos = aux.sublista.inicio
            while pos != None:
                print(pos.info)
                pos = pos.sig
        aux = aux.sig
"""
print(personajes_2())
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 12 ===========================================================
# ******************************************************************************************************************************
"""
12.Desarrollar un algoritmo que elimine el anteúltimo nodo de una lista independientemente
de la información del mismo, utilizando lista simplemente enlazada y después con lista
doblemente enlazada.
"""

def eliminar_anteultimo():
    eliminar_anteul = Lista()
    cargar_lista(eliminar_anteul)
    print('Lista sin modificar')
    barrido(eliminar_anteul)
    aux = eliminar_anteul.inicio
    i = 0
    while aux != None:
        if tamanio(eliminar_anteul)-2 == i:
            eliminar(eliminar_anteul,aux.info)
            print('')
        i += 1
        aux = aux.sig
    print('Lista modificada sin su anteultimo nodo: ')
    barrido(eliminar_anteul)
"""
print(eliminar_anteultimo())
"""
# ******************************************************************************************************************************
# ====================================================== Ejercicio 14 ===========================================================
# ******************************************************************************************************************************
"""
14.Un grupo de amigos se reúnen a jugar un juego de dados, suponga que dichos jugadores
están cargados en una lista de acuerdo a un número asignado de manera aleatoria y su
nombre. Desarrollar un algoritmo que contemple las siguientes condiciones:
a. simular la tirada de un dado –de seis lados D6– en cada turno del jugador;
b. el orden de turno de los jugadores es el mismo en el que están cargados en la
lista;
c. después de que tira el último jugador de la lista debe seguir el primero;
d. el juego termina cuando uno de los jugadores saca un 5, en ese caso mostrar su
nombre;
e. Debe modificar el TDA para implementar lista circular.
"""

def juego_dados():
    jugadores = ['Tomas','Fernando','Joaquin','Mateo','Checho']
    juego = Lista()
    for i in range(len(jugadores)):
        numero = randint(1,10)
        dados = randint(1,6)
        dato = [jugadores[i], numero, dados]
        insertar(juego,dato)
    print('En la forma en que aparecen en la siguente lista es como son los turnos: ')
    barrido(juego)
    print('== COMIENZA EL JUEGO ==')
    aux = juego.inicio
    while aux is not None:
        print('Es el turno de ',aux.info[0])
        print('Tirando dado..')
        if aux.info[2] == 5:
            print('El jugador ',aux.info[0],' gano por que saco el N°',aux.info[2],' en el dado!!!')
            break
        else:
            print('El jugador ',aux.info[0],' saco el N°',aux.info[2],' en el dado')
        aux = aux.sig
        if aux == None:
            for i in range(len(jugadores)):
                aux = juego.inicio
                aux.info[2] = randint(1,6)
                aux = aux.sig
            aux = juego.inicio
"""            
print(juego_dados())
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 15 ===========================================================
# ******************************************************************************************************************************
"""
15.Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce:
nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas
ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y
subtipo. Se pide resolver las siguientes actividades utilizando lista de lista implementando
las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos
ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons:
Tyrantrum, Terrakion o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del
entrenador como del Pokémon deben ser ingresados; además si el entrenador
tiene al Pokémon se deberán mostrar los datos de ambos;
"""

entrenadores = ['Ash','Brock','Dawn','Oak','Misty','Gary oak','Bonnie']

pokemon = { 'Bulbasaur' : ['panta','veneno'] , 'Charmander' : ['fuego','None'] , 'Squirtle': ['Agua','None'],
            'Pelipper' : ['agua','volador'] , 'Wingull' : ['agua','volador'], 'Cyndaquil' : ['fuego','planta'],
            'Caterpie' : ['bicho','None'] , 'Pikachu' : ['electrico','None'] , 'Nidoran' : ['veneno','None'], 
            'Vulpix' : ['Fuego','None'] , 'Jigglypuff' : ['Normal','Hada'] , 'Psyduck' : ['agua','None'],
            'Abra' : ['psiquico','None'] , 'Machop' : ['lucha','None'] , 'Onix' : ['roca','tierra'], 
            'Terrakion' : ['roca','dragon'] , 'Hitmonlee' : ['lucha','None'] , 'Magikarp' : ['agua','None'] ,
            'Eevee' : ['normal','None'] ,'Snorlax' : ['normal','None'] , 'Mewtwo' : ['psiquico','None'] ,
            'Tyrantrum' : ['roca','dragon'] , 'Articuno' : ['hielo','volador']}


class Entrenador(object):
    def __init__(self,nombre,t_ganados,bat_ganadas,bat_perdidas,cant_pok):
        self.nombre = nombre
        self.t_ganados = t_ganados
        self.bat_ganadas = bat_ganadas
        self.bat_perdidas = bat_perdidas
        self.cant_pok = cant_pok
    
    def __str__(self):
        return self.nombre + ' | torneos: ' + str(self.t_ganados) + ' | gano ' + str(self.bat_ganadas) + ' batallas y perdio ' + str(self.bat_perdidas) + '| Tiene ' +str(self.cant_pok)+ ' Pokemones'

class Pokemon(object):
    def __init__(self, nombre,tipo,subtipo,nivel):
        self.nombrepok = nombre
        self.tipo = tipo
        self.subtipo = subtipo
        self.nivel = nivel

    def __str__(self):
        return self.nombrepok + ' tipo: ' + self.tipo + '/'+ self.subtipo + '. su nivel es ' + str(self.nivel)

def pokemones(lista):
    for i in range(len(entrenadores)):
        aux = Entrenador(entrenadores[i],randint(0,10),randint(0,100),randint(0,100),randint(1,10))
        insertar(lista,aux,'t_ganados')
    barrido(lista)
    print('')
    aux = lista.inicio
    while not aux == None:
        print(aux.info)
        print('---- Pokemones')
        cant = aux.info.cant_pok
        for j in range (cant):
            pok = choice(list(pokemon.keys()))
            dato = Pokemon(pok, pokemon[pok][0], pokemon[pok][1], randint(1,50))
            print(dato)
            insertar(aux.sublista,dato,'nivel')
        aux = aux.sig
        print('')
    #b
    print('')
    print('<<<<< Entrenadores que han ganado MAS de 3 torneos Pokemon >>>>>')
    aux = lista.inicio
    c = 0
    while not aux == None:
        if aux.info.t_ganados > 3 :
            print(aux.info)
            c += 1
        aux = aux.sig
    print(' - Hay ' + str(c) + ' entrenadores que ganaron mas de 3 torneos Pokemon.')
    print('')
    # C
    torn = 0
    ent = None
    aux = lista.inicio
    nv = 0
    pok = None
    while not aux == None:
        if aux.info.t_ganados > torn:
            torn = aux.info.t_ganados
            max_torn = aux.info.nombre
            ent = aux.sublista.inicio
            while not ent == None:
                if nv < ent.info.nivel:
                    nv = ent.info.nivel
                    pok = ent.info.nombrepok
                ent = ent.sig
        aux = aux.sig
    print('- El entrenador que mas Torneos Pokemon ha ganado es: ' + max_torn + ', con ' + str(torn)+ ' Torneos ganados.')
    print('- Su pokemon de mayor nivel es: ' + pok + ' de nivel ' + str(nv))
    print('')
    nom = input('ingrese Entrenador a mostrar sus datos y pokemones: ')
    pos = busqueda(lista,nom,'nombre')
    if not pos == None:
        print(pos.info)
        print('_____Pokemones:')
        aux = pos.sublista.inicio
        while not aux == None:
            print(aux.info)
            aux = aux.sig
    print('')
    # e
    print('- ENTRENADORES CON PORCENTAJE DE VICTORIA MAYOR A 79% :')
    aux = lista.inicio
    x = False
    while aux is not None:
        bat_tot = aux.info.bat_ganadas + aux.info.bat_perdidas
        porcentaje = (aux.info.bat_ganadas * 100)/bat_tot
        if porcentaje > 79:
            x = True
            print(aux.info.nombre +' tiene un porcentaje de ' +str(round(porcentaje,2)) + '% batalladas ganadas.')
        aux = aux.sig
    if x == False:
        print('No hay Entrenadores con un porcentaje mayor a 79.')
    print()
    # f
    aux = lista.inicio
    while aux is not None:
        sub = aux.sublista.inicio
        while sub is not None:
            if (sub.info.tipo == 'fuego'):
                if (sub.info.subtipo == 'planta'):
                    print(aux.info.nombre, ': tiene un pokemon tipo fuego y subtipo planta, ' + sub.info.nombrepok)
            if (sub.info.tipo == 'agua'):
                if (sub.info.subtipo == 'volador'):
                    print(aux.info.nombre, ': tiene un pokemon tipo agua y subtipo volador, ' + sub.info.nombrepok)
            sub = sub.sig
        aux = aux.sig
        print('-')
    print('')
    # g
    nom = input('ingrese Entrenador a sacar promedio de nivel de sus Pokemones: ')
    pos = busqueda(lista,nom,'nombre')
    if not pos == None:
        print(pos.info)
        niveles = 0
        cant = 0
        sub = pos.sublista.inicio
        while sub is not None:
            cant += 1
            print(sub.info)
            niveles += sub.info.nivel
            sub = sub.sig
        prom = niveles / cant
        print('--- El promedio de nivel de sus pokemones es: '+ str(round(prom, 2)))
    print('')
    # H
    aux = lista.inicio
    cont = 0
    pok = input(str('Ingrese el nombre del pokemon a buscar: '))
    while aux is not None:
        pos = busqueda(aux.sublista, pok, 'nombrepok')
        if pos is not None:
            cont += 1
            print(aux.info.nombre +' tiene a ' + pok)
        aux = aux.sig
    print(str(cont) +' entrenadores tienen al pokemon '+ pok)
    print('')
    # J
    aux = lista.inicio
    while aux is not None:
        sub = aux.sublista.inicio
        while sub is not None:
            if (sub.info.nombrepok == 'Tyrantrum') or (sub.info.nombrepok == 'Terrakion') or (sub.info.nombrepok == 'Wingull'):
                print('El entrenador ' +aux.info.nombre + ', tiene al pokemon ' + sub.info.nombrepok)
            sub = sub.sig
        aux = aux.sig
    print('')
    # K
    pos = None
    n = None
    x = None
    while ent not in entrenadores:
        ent = input('Ingrese nombre del entrenador: ')
    pos = busqueda(lista,ent,'nombre')
    while n not in pokemon:
        n = input('Ingrese nombre de pokemon a buscar: ')
    if (not pos == None) and (not n == None):
        print('')
        b = False
        nom = pos.sublista.inicio
        while not nom == None:
            if (nom.info.nombrepok == n):
                b = True
                break
            nom = nom.sig
        if b == False:
            print('El entrenador '+ pos.info.nombre + ' no tiene al pokemon buscado.')
        elif b == True:
            print('Entrenador y pokemon encontrados.')
            print('Mostrando sus datos...')
            sleep(1.5)
            print(pos.info)
            sleep(0.7)
            print(nom.info)
"""
print(pokemones(lista))
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 16 ===========================================================
# ******************************************************************************************************************************
"""
16.Se deben administrar las actividades de un proyecto de software, de estas se conoce su
costo, tiempo de ejecución, fecha de inicio, fecha de fin estimada, fecha de fin efectiva y
persona a cargo. Desarrollar un algoritmo que realice las siguientes actividades:
a. tiempo promedio de tareas;
b. costo total del proyecto;
c. actividades realizadas por una determinada persona;
d. mostrar la información de las tareas a realizar entre dos fechas dadas;
e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada
por el usuario.
"""

def proyecto_software():
    proyectos = Lista()
    a_tiempo = Lista()
    fuera_de_tiempo = Lista()
    personal = ['Tomas', 'Fernando', 'Joaquin', 'Antonella', 'Facundo', 'Marta']
    actividades = ['Estudio de factibilidad','Planificacion','Recopilar informacion','Analisar la informacion','Codificar el sistema','Probar el sistema']
    promedio = 0
    costo_total = 0
    df = ''
    for i in range(len(personal)):
        costo = randint(0, 50000)
        tiempo_ejecucion = randint(1, 10)
        fecha_inicio = [2020, randint(1, 12), randint(1, 31)]
        fechaF_estimada = [2020, randint(1, 12), randint(1, 31)]
        fechaF_efectiva = [2020, randint(1, 12), randint(1, 31)]
        persona_cargo = choice(personal)
        actividad = actividades[i]
        tareas = [costo,actividad, tiempo_ejecucion, fecha_inicio, fechaF_estimada, fechaF_efectiva, persona_cargo]
        insertar(proyectos, tareas)
    print('Lista con actividades:')
    barrido(proyectos)
    aux = proyectos.inicio
    while aux is not None:
        #a
        promedio = promedio + aux.info[2]
        #b
        costo_total = costo_total + aux.info[0]
        #c
        if aux.info[5]:
            print('Persona a cargo:', aux.info[5])
            print('Actividades que realiza:',aux.info[1])
            print('Coste de la actividad:', aux.info[0])
            print('Tiempo de ejecucion:', aux.info[2])
        if aux.info[2] < 7:
            insertar(a_tiempo, aux.info[1])
        else:
            insertar(fuera_de_tiempo, aux.info[1])
        aux = aux.sig
    #d
    dato = [2020,randint(1,4),randint(1,12)] 
    dato1 = [2020,randint(5,12),randint(12,31)]
    print('Actividades entre ',dato,' y ',dato1) 
    aux = proyectos.inicio
    while aux is not None:
        if dato < aux.info[5] and dato1 > aux.info[5]:
            print(aux.info[1])
        aux = aux.sig   
    print('Tareas realizadas a tiempo: ')
    barrido(a_tiempo)
    print('Tareas realizadas fuera de tiempo: ')
    barrido(fuera_de_tiempo)

"""
print(proyecto_software())
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 17 ===========================================================
# ******************************************************************************************************************************
"""
17.Se cuenta con los vuelos del aeropuerto de Heraklion en Creta, de estos se sabe la
siguiente información: empresa, número del vuelo, cantidad de asientos del avión, fecha
de salida, destino, kms del vuelo. Y además se conoce los datos de cantidades de asientos
totales y ocupados por clase (primera y turista). Implemente las funciones necesarias que
permitan realizar las siguiente actividades:
a. mostrar los vuelos con destino a Atenas, Miconos y Rodas;
b. mostrar los vuelos con asientos clase turista disponible.;
c. mostrar el total recaudado por cada vuelo, considerando clase turista ($75 por
kilómetro) y primera clase ($203 por kilómetro);
d. mostrar los vuelos programados para una determinada fecha;
e. vender un asiento (o pasaje) para un determinado vuelo;
f. eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se debe indicar
la cantidad de dinero a devovler;
g. mostrar las empresas y los kilómetros de vuelos con destino a Tailandia.
"""
empresas = ['"British Airways"','"American Airlines"','"Lufthansa"','"Lion Air"']
destinos = ['Atenas','Miconos','Rodas','Argentina','China','Brasil','España','Francia','Tailandia']
asientos = [40,45,50,60,70,80]
km = [1000,2000,2500,5000,7000,10500]
clases = ['turista','primera']
tru = [False,True]

class Vuelo(object):
    def __init__(self,empresa,num_v,c_asientos,f_salida,destino,kms):
        self.empresa = empresa
        self.num_v = num_v
        self.c_asientos = c_asientos
        self.f_salida = f_salida
        self.destino = destino
        self.kms = kms

    def __str__(self):
        return 'datos: ' + self.empresa +': vuelo ' +str(self.num_v)+', asientos: ' + str(self.c_asientos)+'; Fecha: '+ str(self.f_salida)+ ', Destino: ' + self.destino+ ', kms: ' + str(self.kms) +'.'

class Asiento(object):
    def __init__(self,numero,ocupado,clase,precio):
        self.numero = numero
        self.ocupado = ocupado
        self.clase = clase
        self.precio = precio

    def __str__(self):
        return self.numero +'; Vendido = '+self.ocupado +', Clase: '+ self.clase +', Precio:'+ self.precio

def aeropuerto(lista):
    for i in range(len(destinos)):
        num_v = i+1
        d = randint(1,30)
        m = randint(1,12)
        a = randint(2020,2021)
        fecha = [d,m,a]
        kms = choice(km)
        cant = choice(asientos)
        dato = Vuelo(choice(empresas),num_v,cant,fecha,destinos[i],kms)
        insertar(lista,dato,'destino')
    aux = lista.inicio
    while aux != None:
        cant = aux.info.c_asientos
        p = cant//1.5
        precio = 0
        for i in range(cant):
            asiento = i+1
            ocupado = choice(tru)
            if asiento < p:
                clase = 'Turista'
                precio = (75*kms)
            else:
                clase = 'Primera'
                precio = (203*kms)
            dato = Asiento(asiento,ocupado,clase,precio)
            insertar(aux.sublista,dato,'numero')
        aux = aux.sig
    # A
    aux = lista.inicio
    while not aux == None:
        if aux.info.destino == 'Atenas':
            print('Destino a Atenas: ')
            print(aux.info)
        if aux.info.destino == 'Miconos':
            print('Destino a Miconos: ')
            print(aux.info)
        if aux.info.destino == 'Rodas':
            print('Destino a Rodas: ')
            print(aux.info)
        aux = aux.sig
    print('')
    # B
    aux = lista.inicio
    while not aux == None:
        print()
        s_n = input('Desea ver los asientos libres de la clase turista del destino '+ aux.info.destino + '?? S/N: ')
        if (s_n == 'S') or (s_n == 's'):
            pos = aux.sublista.inicio
            while not pos == None:
                if pos.info.clase == 'Turista' and pos.info.ocupado == False:
                    print('El asiento '+ str(pos.info.numero) + ' esta desocupado')
                pos = pos.sig
        aux = aux.sig
    # C
    print()
    print('Total recaudado por cada vuelo')
    aux = lista.inicio
    while not aux == None:
        recaudado = 0
        pos = aux.sublista.inicio
        while pos != None:
            if pos.info.ocupado == True:
                recaudado += pos.info.precio
            pos = pos.sig
        print('El vuelo nro '+str(aux.info.num_v)+', a '+ aux.info.destino +' recaudo: '+ str(recaudado)+ ' dinero.')
        aux = aux.sig
    print()
    # E
    s_n = None
    while (s_n != 'n') and (s_n != 'N'):
        s_n = input('Quiere comprar un nuevo pasaje? S/N: ')
        if (s_n == 'S') or (s_n == 's'):
            destino = input('Indique su destino: ')
            bus = None
            bus = busqueda(lista,destino,'destino')
            if bus != None:
                compra = False
                while compra == False:
                    pas = int(input('Elija numero de pasaje: (1/'+ str(bus.info.c_asientos) +') : '))
                    pos = bus.sublista.inicio
                    while pos != None:
                        if pos.info.numero == pas:
                            if pos.info.ocupado == False:
                                pos.info.ocupado = True
                                print('Compra de pasaje exitosa.')
                                print()
                                compra = True
                                break
                            else:
                                print('Lo siento, ese pasaje esta ocupado.')
                                print()
                                break
                        pos = pos.sig
    # F
    print()
    elim = None
    while (elim != 'n') and (elim != 'N'):
        elim = input('Desea eliminar algun vuelo? S/N: ')
        if (elim == 's') or (elim == 'S'):
            vuelo = int(input('Indique con numero, el Nro de vuelo a eliminar: '))
            bus = None
            bus = busqueda(lista,vuelo,'num_v')
            if bus != None:
                b = input('Seguro que desea eliminar el vuelo con destino a '+ bus.info.destino+' ? S/N: ')
                if (b == 's') or (b == 'S'):
                    eliminar(lista,bus.info.num_v,'num_v')
                    print('Se ha eliminado el vuelo Nro: '+str(bus.info.num_v)+', con destino a '+ bus.info.destino )
                    pos= bus.sublista.inicio
                    recaudado = 0
                    while pos != None:
                        if pos.info.ocupado == True:
                            recaudado += pos.info.precio
                        pos = pos.sig
                    print(' La cantidad de dinero a devolver es igual a: ' + str(recaudado))
                    print()
    # G
    print()
    print('Empresas y kilómetros de vuelos con destino a Tailandia:')
    aux = lista.inicio
    while aux != None:
        if aux.info.destino == 'Tailandia':
            print('La empresa '+aux.info.empresa + ' tiene un viaje a Tailandia de '+str(aux.info.kms)+' KMs.')
        aux = aux.sig

"""
print(aeropuerto(lista))
"""


# ******************************************************************************************************************************
# ====================================================== Ejercicio 18 ===========================================================
# ******************************************************************************************************************************

"""
18.Se tienen los usuarios colaboradores de un repositorio de GitHub y de cada uno de estos
se tiene una lista de los commit realizados, de los cuales se cuenta con su timestamp (en
formato fecha y hora), mensaje de commit, nombre de archivo modificado, cantidad de
líneas agregadas/eliminadas (puede ser positivo o negativo) –suponga que solo puede
modificar un archivo en cada commit que se haga–. Desarrollar un algoritmo que permita
realizar las siguientes actividades:
a. obtener el usuario con mayor cantidad de commits –podría llegar a ser más de
uno–;
b. obtener el usuario que haya agregado en total mayor cantidad de líneas y el que
haya eliminado menor cantidad de líneas;
c. mostrar los usuarios que realizaron cambios sobre el archivo test.py después de
las 19:45 sin importar la fecha;
d. indicar los usuarios que hayan realizado al menos un commit con cero líneas
agregados o eliminadas;
e. determinar el nombre del usuario que realizó el último commit sobre el archivo
app.py indicando toda la información de dicho commit;
f. deberá utilizar el TDA lista de lista.
"""

class Usuario():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Commit():
    def __init__(self, archivo, timestamp, mensaje, cant_lineas):
        self.archivo = archivo
        self.timestamp = timestamp
        self.mensaje = mensaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        return 'Archivo: '+ self.archivo +'; Timestamp: '+ self.timestamp + ', Mensaje: ' + self.mensaje + ', Modificó: ' + str(self.cant_lineas)+ ' lineas'


def github(lista):
    lista = Lista()
    user = Usuario('Camilo')
    insertar(lista, user, 'nombre')
    user = Usuario('Federico')
    insertar(lista, user, 'nombre')
    user = Usuario('Flavia')
    insertar(lista, user, 'nombre')
    user = Usuario('Anastacia')
    insertar(lista, user, 'nombre')
    commit = Commit('test.py', '11-11-20 19:00', 'testeo de la app', 46)
    pos = busqueda(lista, 'Camilo', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('data.py', '11-11-20 19:00', 'correccion error', 12)
    pos = busqueda(lista, 'Camilo', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('object.java', '11-11-20 19:00', 'modelado del objeto', -37)
    pos = busqueda(lista, 'Federico', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('app.py', '11-11-20 19:00', 'basta chicos', 34)
    pos = busqueda(lista, 'Flavia', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('front.html', '11-11-20 19:00', 'update', 47)
    pos = busqueda(lista, 'Anastacia', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('vista.css', '11-11-20 19:00', 'update', -2)
    pos = busqueda(lista, 'Anastacia', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    print('Lista de colaboradores: ')
    barrido(lista)
    print()
    # a
    aux = lista.inicio
    mayor = 0
    while aux is not None:
        if tamanio(aux.sublista) > mayor:
            mayor = tamanio(aux.sublista)
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if tamanio(aux.sublista) == mayor:
            print('Colaborador con mayor cantidad de commits: ' + aux.info.nombre)
            print('Cantidad de commits: '+ str(mayor))
        aux = aux.sig
    print()
    # b
    mayor = 0
    usuario = ''
    aux = lista.inicio
    while aux is not None:
        pos = aux.sublista.inicio
        mayor_aux = 0
        while pos is not None:
            mayor_aux += pos.info.cant_lineas
            pos = pos.sig
        if mayor_aux > mayor:
            mayor = mayor_aux
            usuario = aux.info.nombre
        aux = aux.sig
    print(usuario +', agrego la mayor cantidad de lineas: ' +str(mayor))
    menor = 0
    usuario_menor = ''
    aux = lista.inicio
    while aux is not None:
        pos = aux.sublista.inicio
        menor_aux = 0
        while pos is not None:
            menor_aux += pos.info.cant_lineas
            pos =pos.sig
        if menor_aux < menor:
            menor = menor_aux
            usuario_menor = aux.info.nombre
        aux = aux.sig
    print(usuario_menor+ ' elimino la mayor cantidad de lineas: '+ str(menor))
    print()
    # C
    aux = lista.inicio
    while aux is not None:
        pos = busqueda(aux.sublista,'test.py','archivo')
        if pos is not None:
            print(aux.info.nombre + ', ha realizado cambios en test.py')
        aux = aux.sig
    # D
    print()
    aux = lista.inicio
    while aux is not None:
        pos = busqueda(aux.sublista,0,'cant_lineas')
        if pos is not None:
            print(aux.info.nombre + ' ha realizado un commit con 0 lineas')
        aux = aux.sig
    print()
    # E
    aux = lista.inicio
    while aux is not None:
        pos = busqueda(aux.sublista,'app.py','archivo')
        if pos is not None:
            print(aux.info.nombre + ', ha realizado cambios en app.py')
            aux2 = lista.inicio
            while(aux2 is not None):
                print(aux2.info)
                barrido(aux2.sublista)
                aux2 = aux2.sig   
        aux = aux.sig

"""
print(github(lista))
"""
# ******************************************************************************************************************************
# ====================================================== Ejercicio 19 ===========================================================
# ******************************************************************************************************************************
"""
19.Los astilleros de propulsores Kuat, son la mayor corporación de construcción de naves
militares que provee al imperio galáctico –dentro de sus productos más destacados están
los cazas TIE, destructores estelares, transporte acorazado todo terreno (AT-AT),
transporte de exploración todo terreno (AT-ST), ejecutor táctico todo terreno (AT-TE),
entre otros– y nos solicita desarrollar las funciones necesarias para resolver las siguientes
necesidades:
a. debe procesar los datos de las ventas de naves que están almacenados en un
rudimentario archivo de texto, en el cual cada línea tiene los siguientes datos:
código del astillero que lo produjo, producto (los mencionados previamente),
precio en créditos galácticos, si fue construido con partes recicladas o no
(booleano), quien realizo la compra (en algunos casos se desconoce quién realizo
la compra y este campo tiene valor desconocido), todos estos datos están
separados por “;” en cada línea del archivo;
b. cargar los datos procesados en el punto anterior en dos listas, en la primera las
ventas de las que se conocen el cliente y la segunda las que no;
c. el código del astillero son tres caracteres el primero en una letra mayúscula de la
“A” hasta la “K” seguido de dos dígitos;
d. obtener el total de ingresos de créditos galácticos y cuantas unidades se
vendieron;
e. listar los nombres de todos los clientes, los repetidos deberán mostrarse una sola
vez, puede utilizar una estructura auxiliar para resolverlo;
f. realizar un informe de las compras realizadas por Darth Vader;
g. se le debe realizar un descuento del 15 por ciento a los clientes que compraron naves que
fueron fabricadas con partes recicladas, mostrar los clientes y los montos a
devolver a cada uno;
h. determinar cuánto ingreso genero la producción de naves cuyos modelos
contengan la sigla “AT”.
"""

def venta_naves():
    lista_ventas = Lista()
    clientes = Lista()
    sin_clientes = Lista()
    nombre_clientes = Lista()
    informe = Lista()
    #A
    archivo = open('naves')
    linea = archivo.readline()
    while linea:
        linea = linea.replace('\n', '')
        linea = linea.split(';')
        linea[0] = linea[0].upper()
        linea[1] = linea[1].upper()
        linea[2] = float(linea[2])
        linea[3] = linea[3].title()
        linea[4] = linea[4].title()
        insertar(lista_ventas, linea)
        linea = archivo.readline()
        
    print('Lista de ventas de naves')
    barrido(lista_ventas)
    aux = lista_ventas.inicio
    cont = 0
    ac = 0
    devolver = 0
    ingresoAT = 0
    while aux is not None:
        #B
        if aux.info[4] == 'Desconocido':
            insertar(sin_clientes, aux.info)
        else:
            insertar(clientes,aux.info)
            pos = busqueda(nombre_clientes, aux.info[4],4)
            #E
            if pos == None:
                insertar(nombre_clientes,aux.info[4])
        #D
        cont += 1
        ac = ac + aux.info[2]
        #F
        if aux.info[4] == 'Darth Vader':
            insertar(informe, aux.info)
        #H
        if aux.info[1] == 'AT-AT' or aux.info == 'AT-ST' or aux.info == 'AT-TE':
            ingresoAT = ingresoAT + aux.info[2]
        aux = aux.sig

    print('Total de ingresos de creditos galacticos: ')
    print(ac)
    print('Total de naves vendidas:')
    print(cont)
    print('Listado de clientes')
    barrido(nombre_clientes)
    print('Informe de Darth Vader')
    barrido(informe)
    print('Clientes con naves construidas con material reciclado y monto a devoler:')
    aux2 = lista_ventas.inicio
    while aux2 is not None:
        #G
        if aux2.info[3] == 'Si':
            devolver = (100 / 15) * aux2.info[2]
            print('Cliente: ', aux2.info[4])
            print('Monto a devolver: ',devolver)
        aux2 = aux2.sig
    print('El ingreso que genero la producción de naves cuyos modelos contienen la sigla “AT” es de :')
    print(ingresoAT)
"""  
print(venta_naves())
"""
# ******************************************************************************************************************************
# ====================================================== Ejercicio 20 ===========================================================
# ******************************************************************************************************************************
"""
20.Una empresa meteorológica necesita registrar los datos de sus distintas estaciones en las
cuales recolecta la siguiente información proveniente de sus distintas estaciones de
adquisición de datos diariamente, implemente las funciones para satisfacer los siguientes
requerimientos:
a. se deben poder cargar estaciones meteorológicas, de cada una de estas se sabe su
país de ubicación, coordenadas de latitud, longitud y altitud;
b. estas estaciones registran mediciones de temperatura, presión, humedad y estado
del clima –como por ejemplo soleado, nublado, lloviendo, nevando, etcétera– en
distintos lapsos temporales, estos datos deberán guardarse en la lista junto con la
fecha y la hora de la medición;
c. mostrar el promedio de temperatura y humedad de todas las estaciones durante
el mes de mayo;
d. indicar la ubicación de las estaciones meteorológicas en las que en el día actual
está lloviendo o nevando;
e. mostrar los datos de las estaciones meteorológicas que hayan registrado estado
del clima tormenta eléctrica o huracanes;
f. debe implementar el TDA lista de lista.
"""

paises = ['Argentina','Uruguay','Brasil','Chile','Paraguay','Mexico','Colombia','Venezuela']
estados_clima = ['soleado','nublado','lloviendo','nevando','tormenta eléctrica','vientos fuertes','huracanes']
estaciones = ['verano','otoño','invierno','primavera']

class Pais():
    def __init__(self,pais,latitud,longitud,altitud):
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def __str__(self):
        return 'Pais: '+ self.pais +'|| Ubicacion: Latitud '+ str(self.latitud) + ', Longitud: '+ str(self.longitud) +', Altitud: '+str(self.altitud)

class Medicion():
    def __init__(self,fecha,temperatura,presion,humedad,clima):
        self.fecha = fecha
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
        self.clima = clima

    def __str__(self):
        return '- Fecha: '+str(self.fecha)+'. Temperatura: '+str(self.temperatura)+ ' grados, Presion: '+str(self.presion)+ ', Humedad: '+str(self.humedad)+ ' % , Clima: '+self.clima
    
def empresa_meteorologica():
    # A
    for i in range(len(paises)):
        dato = Pais(paises[i],randint(0,100),randint(0,100),randint(0,100))
        insertar(lista,dato,'pais')
    aux = lista.inicio
    # B
    while not aux == None:
        print(aux.info)
        for i in range(12):
            d = randint(1,30)
            m = i+1
            a = randint(2020,2021)
            fecha = [d,m,a]
            dato = Medicion(fecha,randint(-10,50),randint(0,20),randint(0,100),choice(estados_clima))
            print(dato)
            insertar(aux.sublista,dato,'fecha')
        print('')
        aux = aux.sig
    # C
    print('Promedios de Temperatura y Humedad:')
    aux = lista.inicio
    while not aux == None:
        pos = aux.sublista.inicio
        temp = 0
        hum = 0
        cont = 0
        while not pos == None:
            temp += pos.info.temperatura
            hum += pos.info.humedad
            cont += 1
            pos = pos.sig
        print(aux.info.pais + ': El promedio de Temperatura es: ' + str(round(temp/cont , 2)))
        print(aux.info.pais + ': El promedio de Humedad es: ' + str(round(hum/cont , 2)))
        aux = aux.sig
        print('')
    # D
    aux = lista.inicio
    while aux is not None:
        pos = aux.sublista.inicio
        while not pos == None:
            if pos.info.clima == 'lloviendo':
                print('En la fecha '+str(pos.info.fecha)+', en el pais ' +aux.info.pais + ' esta lloviendo.')
            elif pos.info.clima == 'nevando':
                print('En la fecha '+str(pos.info.fecha)+', en el pais ' +aux.info.pais + ' esta nevando.')
            pos = pos.sig
        aux = aux.sig
    print('')
    # E
    print('Registros de estado del clima con tormenta eléctrica o huracanes:')
    aux = lista.inicio
    while aux is not None:
        pos = aux.sublista.inicio
        while pos is not None:
            if pos.info.clima == 'huracanes':
                print(aux.info.pais + ' registro clima de huracanes en la fecha ' + str(pos.info.fecha))
            elif pos.info.clima == 'tormenta eléctrica':
                print(aux.info.pais+ ' registro clima de Tormenta Electrica en la fecha ' + str(pos.info.fecha))
            pos = pos.sig
        aux = aux.sig
"""
print(empresa_meteorologica())
"""

# ******************************************************************************************************************************
# ====================================================== Ejercicio 21 ===========================================================
# ******************************************************************************************************************************
"""
21.Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes
datos: nombre, valoración del público –es un valor comprendido entre 0-10–, año de
estreno y recaudación. Desarrolle los algoritmos necesarios para realizar las siguientes
tareas:
a. permitir filtrar las películas por año –es decir mostrar todas las películas de un
determinado año–;
b. mostrar los datos de la película que más recaudo;
c. indicar las películas con mayor valoración del público, puede ser más de una;
d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá
utilizar una lista auxiliar–:
i. por nombre,
ii. por recaudación,
iii. por año de estreno,
iv. por valoración del público.
"""

class Pelicula():
    def __init__(self,nombre,valoracion,estreno,recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.estreno = estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return 'PELICULA: ' + self.nombre + ' VALORACION: ' + str(self.valoracion) + '. AÑO DE ESTRENO : ' + str(self.estreno) + '. RECAUDO: ' + str(self.recaudacion)

pelis = ['Iron Man','Harry Potter','Stars Wars','Avengers','Spider Man','El señor de los anillos','Capitan America']

def lista_peliculas(lista):
    for i in range(len(pelis)):
        dato = Pelicula(pelis[i],randint(1,10),randint(1970,2020),randint(100000,10000000))
        insertar(lista,dato,'nombre')
    barrido(lista)
    print('')
    # A
    pos = int(input('Ingrese un año de estreno: '))
    aux = lista.inicio
    vacio = False
    while aux is not None:
        if pos == aux.info.estreno:
            print(aux.info.nombre +' se estreno en el año: '+ str(aux.info.estreno))
            vacio = True
        aux = aux.sig
    if vacio == False:
        print('Ninguna pelicula se ha estrenado en ese año.')
    print('')
    # B
    mas_rec = 0
    mayor_p = ''
    aux = lista.inicio
    while aux is not None:
        if aux.info.recaudacion > mas_rec:
            mas_rec = aux.info.recaudacion
            mayor_p = aux.info
        aux = aux.sig
    print('Pelicula que mas recaudo y sus datos:')
    print(mayor_p)
    print('')
    # C
    print('Valoracion mas Alta:')
    aux = lista.inicio
    max_v = 0
    while aux is not None:
        if aux.info.valoracion > max_v:
            max_v = aux.info.valoracion
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if aux.info.valoracion == max_v:
            print('- ' +aux.info.nombre +' tiene la valoracion mas alta,y su puntaje es de ' + str(max_v) + ' puntos.')
        aux = aux.sig
    print('')
    # D
    print('Peliculas por criterio:')
    crit = None
    lista_aux = Lista()
    print('CRITERIOS: nombre / valoracion / estreno / recaudacion : ')
    while crit == None:
        crit = input('Ingrese criterio por el que quiere mostrar: ')
        if (crit != 'nombre') and (crit != 'recaudacion') and (crit != 'estreno') and (crit != 'valoracion'):
            crit = None
            print('Error !!: Criterio incorrecto, vuelva a intentar...')
    print('')
    aux = lista.inicio
    while aux is not None:
        insertar(lista_aux, aux.info, crit)
        aux = aux.sig
    print('Mostrando Peliculas por ' + crit +'...')
    #sleep(2)
    barrido(lista_aux)
"""
print(lista_peliculas(lista))
"""