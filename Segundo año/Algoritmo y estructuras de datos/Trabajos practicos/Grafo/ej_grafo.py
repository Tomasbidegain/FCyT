from tda_grafo import Grafo, adyacentes, barrido_amplitud_red, barrido_grafo, barrido_grafo_maravilla, barrido_profundidad, barrido_profundidad_red, buscar_vertice_aeropuerto, buscar_vertice_maravilla, buscar_vertice_red, dijkstra, dijkstra_costo, dijkstra_distancia, dijkstra_duracion, dijkstra_red, eliminar_arista_red, existe_paso_aero, insertar_arista_maravilla, insertar_arista_red, insertar_arista_viaje, insertar_vertice_aeropuerto, insertar_vertice_maravilla, insertar_vertice_red, kruskal, marcar_no_visitado, prim, prim_arq, prim_nat, prim_red
from tda_pila_dinamica import desapilar, pila_vacia
from random import randint, choice
from datetime import time


#******************************************************************************************************************************
#======================================================Ejercicio 1=============================================================
#******************************************************************************************************************************
"""
1. Implementar un grafo no dirigido que permita administrar vuelos internacionales
contemplando los siguientes requerimientos:
a. de cada aeropuerto se conoce: su nombre, ubicación (latitud y longitud) y
cantidad de pistas;
b. cada arista representa un viaje de un aeropuerto a otro, en cada una de esta
puede haber más de un vuelo, de los cuales se conoce: hora de salida, hora
de arribo, nombre de la empresa, costo del pasaje –considere que todos los
pasajes cuestan lo mismo–, duración del viaje y distancia en km;
c. debe persistir los datos del grafo en archivos;
d. el grafo debe contener los aeropuertos de los siguientes países: Argentina, China, Brasil, Tailandia, Grecia, Alemania, Francia, Estados Unidos, Japón y
Jamaica;
e. calcular el camino más corto desde el aeropuerto de Argentina a Tailandia
considerando los siguientes criterios:
i. menor distancia,
ii. menor duración de tiempo,
iii. menor costo,
iv. menor número de escalas. 
v. determinar todos los aeropuertos a los que se puede arribar desde Grecia de manera directa o indirecta.
"""

g = Grafo(False)

class Aeropuerto():
    def __init__(self, nombre, latitud, longitud, pistas):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.pistas = pistas

    def __str__(self):
        return self.nombre + ' | ' + str(self.latitud) + ' | ' + str(self.longitud) + ' | ' + str(self.pistas)

class Vuelos ():
    def __init__(self, h_salida, h_arribo, nombre_empresa, costo, duracion, distancia):
        self.h_salida = h_salida
        self.h_arribo = h_arribo
        self.nombre_empresa = nombre_empresa
        self.costo = costo
        self.duracion = duracion
        self.distancia = distancia
    
    def __str__(self):
        return '- ' + self.nombre_empresa + ' - ' + str(self.h_salida) + ' - ' + str(self.h_arribo) + ' - ' + str(self.costo) + ' - ' + str(self.duracion)+ ' - ' + str(self.distancia)

aeropuertos = ['Alemania','Argentina','Brasil','China','EEUU','Francia','Grecia','Jamaica','Japón','Tailandia']
america = ['Argentina', 'Brasil', 'EEUU', 'Jamaica']
europa = ['Alemania', 'Francia', 'Grecia']
asia = ['China', 'Japón', 'Tailandia']
empresas = ['Austral','LATAM','British Airways','Lufthansa','SEAIR','Air Philippines']

#Cargo los vertices(paises)

for i in range(len(aeropuertos)):
    dato = Aeropuerto(aeropuertos[i], randint(1,100),randint(1,100), randint(10, 50))
    insertar_vertice_aeropuerto(g, dato)

#Cargo las aristas(vuelos)
for i in range (0,3):
    ori = buscar_vertice_aeropuerto(g, choice(europa))
    des = buscar_vertice_aeropuerto(g, choice(asia))
    dato = Vuelos(time(randint(0, 23), 00), time(randint(0, 23), 00), choice(empresas), 1000, randint(7,10), randint(2000,8000))
    insertar_arista_viaje(g,dato,ori,des)

for i in range (0,3):
    ori = buscar_vertice_aeropuerto(g, choice(asia))
    des = buscar_vertice_aeropuerto(g, choice(america))
    dato = Vuelos(time(randint(0, 23), 00), time(randint(0, 23), 00), choice(empresas), 1000, randint(7,10), randint(2000,8000))
    insertar_arista_viaje(g,dato,ori,des)

for i in range (0,3):
    ori = buscar_vertice_aeropuerto(g, choice(america))
    des = buscar_vertice_aeropuerto(g, choice(asia))
    dato = Vuelos(time(randint(0, 23), 00), time(randint(0, 23), 00), choice(empresas), 1000, randint(7,10), randint(2000,8000))
    insertar_arista_viaje(g,dato,ori,des)

print('Aeropuertos')
barrido_grafo(g)

#Vuelo desde Argentina a Tailandia
ori = buscar_vertice_aeropuerto(g, aeropuertos[1])
des = buscar_vertice_aeropuerto(g, aeropuertos[9])
dato = Vuelos(time(randint(0, 23), 00), time(randint(0, 23), 00), choice(empresas), 1000, randint(7,10), randint(2000,8000))
insertar_arista_viaje(g,dato,ori,des)

print('Caminos mas cortos desde Argentina a Tailandia')
print()

print('Caminos mas corto por menor distancia')
print()
camino_mas_corto = dijkstra_distancia(g, 'Argentina', 'Tailandia')
fin = 'Tailandia'
distancia = None
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if distancia is None and fin == dato[1][0].info.nombre:
        distancia = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('Distancia mas corta: ',distancia, 'km')
print()

print('Caminos mas corto por menor duración de tiempo')
print()
camino_mas_corto = dijkstra_duracion(g, 'Argentina', 'Tailandia')
fin = 'Tailandia'
duracion = None
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if duracion is None and fin == dato[1][0].info.nombre:
        duracion = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('Camino con menos duracion: ',duracion, 'hs.')
print()

print('Camino de menor costo')
print()
camino_mas_corto = dijkstra_costo(g, 'Argentina', 'Tailandia')
fin = 'Tailandia'
coste_pasaje = None
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if coste_pasaje is None and fin == dato[1][0].info.nombre:
        coste_pasaje = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('Camino mas barato: $' ,coste_pasaje)
print()

print('v) Viajes a Grecia de manera directa')
print()

vertices = buscar_vertice_aeropuerto(g, 'Grecia')
if vertices is not None:
    adyacentes(vertices)
else:
    print('No hay vuelos a Grecia')
print()

print('v) Viajes a Grecia de manera indirecta')
datos = ['Argentina', 'Alemania', 'Brasil', 'China', 'EEUU', 'Francia', 'Japón', 'Jamaica', 'Tailandia']
pos = 0
for i in range(len(datos)):
    ori = buscar_vertice_aeropuerto(g, datos[pos])
    des = buscar_vertice_aeropuerto(g, 'Grecia')
    if existe_paso_aero(g, ori, des):
        print('Existe paso indirecto a Grecia desde:', datos[pos])
    pos += 1


#******************************************************************************************************************************
#======================================================Ejercicio 2=============================================================
#******************************************************************************************************************************
"""
2. Cargar el esquema de red de la siguiente figura en un grafo e implementar los
algoritmos necesarios para resolver las tareas, listadas a continuación:
a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
b. realizar un barrido en profundidad y amplitud partiendo desde la tres
notebook: Red Hat, Debian, Arch;
c. encontrar el camino más corto para enviar a imprimir un documento desde
la pc: Manjaro, Red Hat, Fedora hasta la impresora;
d. encontrar el árbol de expansión mínima;
e. determinar desde que pc (no notebook) es el camino más corto hasta el
servidor “Guaraní”;
f. indicar desde que computadora del switch 01 es el camino más corto al
servidor “MongoDB”;

g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto
b;
h. debe utilizar un grafo no dirigido.
"""
""""
class Tipo():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def __str__(self):
        return ' Nombre: '+ self.nombre + ' Tipo: ' + self.tipo

g = Grafo(False)

pc = ['Ubuntu','Mint','Fedora','Manjaro','Parrot']
note = ['Debian','Red Hat','Arch']
servidor = ['Guarani','MongoDB']
router = ['Router 1','Router 2','Router 3']
switch = ['Switch 1','Switch 2']
impresora = ['Impresora']

#Cargamos vertices en el grafo
for i in range (len(pc)):
    dato = Tipo(pc[i], 'PC')
    insertar_vertice_red(g, dato)

for i in range (len(note)):
    dato = Tipo(note[i], 'Notebook')
    insertar_vertice_red(g, dato)

for i in range (len(servidor)):
    dato = Tipo(servidor[i], 'Servidor')
    insertar_vertice_red(g, dato)

for i in range (len(router)):
    dato = Tipo(router[i], 'Router')
    insertar_vertice_red(g, dato)

for i in range (len(switch)):
    dato = Tipo(switch[i], 'Switch')
    insertar_vertice_red(g, dato)

for i in range (len(impresora)):
    dato = Tipo(impresora[i], 'Impresora')
    insertar_vertice_red(g, dato)


#Cargamos aristas
#A
ori = buscar_vertice_red(g,'Switch 1')
des = buscar_vertice_red(g, 'Debian')
dato = 17
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 1')
des = buscar_vertice_red(g, 'Ubuntu')
dato = 18
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 1')
des = buscar_vertice_red(g, 'Impresora')
dato = 22
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 1')
des = buscar_vertice_red(g, 'Mint')
dato = 80
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 1')
des = buscar_vertice_red(g, 'Router 1')
dato = 29
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Router 1')
des = buscar_vertice_red(g, 'Router 2')
dato = 37
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Router 1')
des = buscar_vertice_red(g, 'Router 3')
dato = 43
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Router 2')
des = buscar_vertice_red(g, 'Red Hat')
dato = 25
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Router 2')
des = buscar_vertice_red(g, 'Guarani')
dato = 29
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Router 2')
des = buscar_vertice_red(g, 'Router 3')
dato = 50
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Router 3')
des = buscar_vertice_red(g, 'Switch 2')
dato = 61
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 2')
des = buscar_vertice_red(g, 'Fedora')
dato = 3
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 2')
des = buscar_vertice_red(g, 'Arch')
dato = 56
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 2')
des = buscar_vertice_red(g, 'MongoDB')
dato = 5
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 2')
des = buscar_vertice_red(g, 'Parrot')
dato = 12
insertar_arista_red(g,dato,ori,des)

ori = buscar_vertice_red(g,'Switch 2')
des = buscar_vertice_red(g, 'Manjaro')
dato = 40
insertar_arista_red(g,dato,ori,des)

#B
bus = buscar_vertice_red(g,'Red Hat')
print('Barrido en profundidad Red Hat')
barrido_profundidad_red(g, bus)
print()
marcar_no_visitado(g)

print('Barrido en amplitud Red Hat')
barrido_amplitud_red(g, bus)
print()
marcar_no_visitado(g)

bus = buscar_vertice_red(g,'Debian')
print('Barrido en profundidad Debian')
barrido_profundidad_red(g, bus)
print()
marcar_no_visitado(g)


print('Barrido en amplitud Debian')
barrido_amplitud_red(g, bus)
print()
marcar_no_visitado(g)

bus = buscar_vertice_red(g,'Arch')
print('Barrido en profundidad Arch')
barrido_profundidad_red(g, bus)
print()
marcar_no_visitado(g)

print('Barrido en amplitud Arch')
barrido_amplitud_red(g, bus)
print()
marcar_no_visitado(g)

#C
distanciaMenor = ['Manjaro','Red Hat', 'Fedora']
for i in range(0,len(distanciaMenor)):
    ori = distanciaMenor[i]
    distancia = None
    fin = 'Impresora'
    camino_mas_corto = dijkstra_red(g,ori,'Impresora')
    while not pila_vacia(camino_mas_corto):
        dato = desapilar(camino_mas_corto)
        if distancia is None and fin == dato[1][0].info.nombre:
            distancia = dato[0]
    print('El camino mas corto desde',ori,'hasta impresora es: ',distancia)


#D
bosque = prim_red(g)

print('Arbol de expansion minima:')
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()

#E
menor = 200
for i in range(0,len(pc)):
    ori = pc[i]
    distancia = None
    fin = 'Guarani'
    camino_mas_corto = dijkstra_red(g,ori,'Guarani')
    while not pila_vacia(camino_mas_corto):
        dato = desapilar(camino_mas_corto)
        if distancia is None and fin == dato[1][0].info.nombre:
            distancia = dato[0]
    if distancia < menor:
        menor_nombre = ori
        menor = distancia

print(menor_nombre,'es el camino mas corto hasta el servidor guarani con un peso de', menor)

#F
s1 = ['Debian','Ubuntu','Impresora','Mint']
menor = 218
for i in range(0,len(s1)):
    ori = s1[i]
    distancia = None
    fin = 'MongoDB'
    camino_mas_corto = dijkstra_red(g,ori,'MongoDB')
    while not pila_vacia(camino_mas_corto):
        dato = desapilar(camino_mas_corto)
        if distancia is None and fin == dato[1][0].info.nombre:
            distancia = dato[0]
    if distancia < menor:
        menor_nombre = ori
        menor = distancia
print(menor_nombre,'es el camino mas corto hasta el servidor MongoDB con un peso de', menor)

#G
"Eliminamos las aristas de impresora a sw1"
ori = buscar_vertice_red(g, 'Switch 1')
eliminar_arista_red(g, ori, 'Impresora')
ori = buscar_vertice_red(g, 'Impresora')
eliminar_arista_red(g, ori, 'Switch 1')

"Insertamos las aristas de impresora a router 2"
ori = buscar_vertice_red(g, 'Impresora')
des = buscar_vertice_red(g, 'Router 2')
insertar_arista_red(g, 22, ori, des)
"""
#******************************************************************************************************************************
#======================================================Ejercicio 3=============================================================
#******************************************************************************************************************************
"""
3. Se requiere implementar un grafo para almacenar las siete maravillas
arquitectónicas modernas y naturales del mundo, para lo cual se deben tener en
cuenta las siguientes actividades:
a. de cada una de las maravillas se conoce su nombre, país de ubicación
(puede ser más de uno en las naturales) y tipo (natural o arquitectónica);
b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se
debe almacenar la distancia que las separa;
c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
d. determinar si existen países que dispongan de maravillas arquitectónicas y
naturales;
e. determinar si algún país tiene más de una maravilla del mismo tipo;
f. deberá utilizar un grafo no dirigido.
"""
"""
class Maravillas():
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo


g = Grafo(False)

#A
dato = Maravillas('La ciudad de Petra', 'Jordania', 'Arquitectonica')
insertar_vertice_maravilla(g, dato)

dato = Maravillas('El Taj Mahal', 'India', 'Arquitectonica')
insertar_vertice_maravilla(g, dato)

dato = Maravillas('El Machu Picchu', 'Perú', 'Natural')
insertar_vertice_maravilla(g, dato)

dato = Maravillas('La pirámide de Chichén Itza', 'México', 'Arquitectonica')
insertar_vertice_maravilla(g, dato)

dato = Maravillas('El Coliseo', 'Roma', 'Arquitectonica')
insertar_vertice_maravilla(g, dato)

dato = Maravillas('La Gran Muralla', 'China', 'Arquitectonica')
insertar_vertice_maravilla(g, dato)

dato = Maravillas('La estatua del Cristo Redentor', 'Brasil', 'Arquitectonica')
insertar_vertice_maravilla(g, dato)

#B
#Cuidad de petra
ori = buscar_vertice_maravilla(g, 'La ciudad de Petra')
des = buscar_vertice_maravilla(g, 'El Taj Mahal')
insertar_arista_maravilla(g, 12000,ori,des)

des = buscar_vertice_maravilla(g, 'El Machu Picchu')
insertar_arista_maravilla(g, 12400,ori,des)

des = buscar_vertice_maravilla(g, 'La pirámide de Chichén Itza')
insertar_arista_maravilla(g, 11000,ori,des)

des = buscar_vertice_maravilla(g, 'El Coliseo')
insertar_arista_maravilla(g, 4159,ori,des)

des = buscar_vertice_maravilla(g, 'La Gran Muralla')
insertar_arista_maravilla(g, 12274,ori,des)

des = buscar_vertice_maravilla(g, 'La estatua del Cristo Redentor')
insertar_arista_maravilla(g, 10260,ori,des)

#Machu Picchu
ori = buscar_vertice_maravilla(g, 'El Machu Picchu')
des = buscar_vertice_maravilla(g, 'El Taj Mahal')
insertar_arista_maravilla(g, 9580,ori,des)

des = buscar_vertice_maravilla(g, 'La pirámide de Chichén Itza')
insertar_arista_maravilla(g, 15894,ori,des)

des = buscar_vertice_maravilla(g, 'El Coliseo')
insertar_arista_maravilla(g, 9540,ori,des)

des = buscar_vertice_maravilla(g, 'La Gran Muralla')
insertar_arista_maravilla(g, 3985,ori,des)

des = buscar_vertice_maravilla(g, 'La estatua del Cristo Redentor')
insertar_arista_maravilla(g, 9100,ori,des)

#La pirámide de Chichén Itza

ori = buscar_vertice_maravilla(g, 'La pirámide de Chichén Itza')
des = buscar_vertice_maravilla(g, 'El Taj Mahal')
insertar_arista_maravilla(g, 7580,ori,des)

des = buscar_vertice_maravilla(g, 'El Coliseo')
insertar_arista_maravilla(g, 10540,ori,des)

des = buscar_vertice_maravilla(g, 'La Gran Muralla')
insertar_arista_maravilla(g, 13985,ori,des)

des = buscar_vertice_maravilla(g, 'La estatua del Cristo Redentor')
insertar_arista_maravilla(g, 11100,ori,des)

#El Coliseo


ori = buscar_vertice_maravilla(g, 'El Coliseo')
des = buscar_vertice_maravilla(g, 'El Taj Mahal')
insertar_arista_maravilla(g, 12520,ori,des)

des = buscar_vertice_maravilla(g, 'La Gran Muralla')
insertar_arista_maravilla(g, 9845,ori,des)

des = buscar_vertice_maravilla(g, 'La estatua del Cristo Redentor')
insertar_arista_maravilla(g, 6500,ori,des)

#La Gran Muralla
ori = buscar_vertice_maravilla(g, 'La Gran Muralla')
des = buscar_vertice_maravilla(g, 'El Taj Mahal')
insertar_arista_maravilla(g, 2520,ori,des)

des = buscar_vertice_maravilla(g, 'La estatua del Cristo Redentor')
insertar_arista_maravilla(g, 6700,ori,des)

#La estatua del Cristo Redentor


ori = buscar_vertice_maravilla(g, 'La estatua del Cristo Redentor')
des = buscar_vertice_maravilla(g, 'El Taj Mahal')
insertar_arista_maravilla(g, 15520,ori,des)

#C
print('Arbol de expansion minimo de maravillas arquitectonicas:')
bosque = []
bosque = prim_arq(g)
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()

print('Arbol de expansion minimo de maravillas naturales:')

bosque = []
bosque = prim_nat(g)
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()

"""