from tda_archivo import modificar
from tda_pila_dinamica import desapilar, pila_vacia
from TDA_Heap import busqueda_heap
from tda_grafo import Grafo, barrido_grafo_antena, barrido_grafo_maravilla, buscar_arista, buscar_vertice_antenas, buscar_vertice_antenas_codigo, buscar_vertice_templos, dijkstra, dijkstra_antena, dijkstra_distancia, dijkstra_red, insertar_arista_antenas, insertar_vertice_antenas,insertar_vertice_templos,insertar_arista_templo, kruskal_ant, prim_ant, prim_red
from random import randint
from tda_arbol import busqueda_proximidad_criaturas, eliminar_nodo, inorden, nodoArbol,insertar_nodo

#Ejercicio 1

"""class Templos():
    def __init__(self, nombre, ubicacion, longitud, latitud):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.longitud = longitud
        self.latitud = latitud
 
g = Grafo(False)

templos = [['Atenas','Partenon',randint(1,100),randint(1,100)],['Zeus','Olimpia',randint(1,100),randint(1,100)],
           ['Hera','Olimpia',randint(1,100),randint(1,100)], ['Apolo','Delfos',randint(1,100),randint(1,100)],
           ['Poseidon','Sunion',randint(1,100),randint(1,100)], ['Artemisa','Efeso',randint(1,100),randint(1,100)],
           ['Teatro de Dionisio','Acropolis',randint(1,100),randint(1,100)]]

for templo in templos:
    dato = Templos(templo[0],templo[1],templo[2],templo[3])
    insertar_vertice_templos(g,dato)

ori = buscar_vertice_templos(g, 'Atenas')
des = buscar_vertice_templos(g, 'Zeus')
insertar_arista_templo(g, 18, ori, des)

des = buscar_vertice_templos(g, 'Hera')
insertar_arista_templo(g, 15, ori, des)

des = buscar_vertice_templos(g, 'Apolo')
insertar_arista_templo(g, 19, ori, des)

des = buscar_vertice_templos(g, 'Poseidon')
insertar_arista_templo(g, 12, ori, des)

des = buscar_vertice_templos(g, 'Artemisa')
insertar_arista_templo(g, 11, ori, des)

des = buscar_vertice_templos(g, 'Teatro de Dionisio')
insertar_arista_templo(g, 16, ori, des)

ori = buscar_vertice_templos(g, 'Zeus')
des = buscar_vertice_templos(g, 'Hera')
insertar_arista_templo(g, 28, ori, des)

des = buscar_vertice_templos(g, 'Apolo')
insertar_arista_templo(g, 98, ori, des)

des = buscar_vertice_templos(g, 'Poseidon')
insertar_arista_templo(g, 8, ori, des)

des = buscar_vertice_templos(g, 'Artemisa')
insertar_arista_templo(g, 68, ori, des)

des = buscar_vertice_templos(g, 'Teatro de Dionisio')
insertar_arista_templo(g, 13, ori, des)

ori = buscar_vertice_templos(g, 'Hera')
des = buscar_vertice_templos(g, 'Apolo')
insertar_arista_templo(g, 10, ori, des)

des = buscar_vertice_templos(g, 'Poseidon')
insertar_arista_templo(g, 38, ori, des)

des = buscar_vertice_templos(g, 'Artemisa')
insertar_arista_templo(g, 58, ori, des)

des = buscar_vertice_templos(g, 'Teatro de Dionisio')
insertar_arista_templo(g, 10, ori, des)

ori = buscar_vertice_templos(g, 'Apolo')
des = buscar_vertice_templos(g, 'Poseidon')
insertar_arista_templo(g, 9, ori, des)

des = buscar_vertice_templos(g, 'Artemisa')
insertar_arista_templo(g, 3, ori, des)

des = buscar_vertice_templos(g, 'Teatro de Dionisio')
insertar_arista_templo(g, 4, ori, des)

ori = buscar_vertice_templos(g, 'Poseidon')
des = buscar_vertice_templos(g, 'Artemisa')
insertar_arista_templo(g, 60, ori, des)

des = buscar_vertice_templos(g, 'Teatro de Dionisio')
insertar_arista_templo(g, 21, ori, des)

ori = buscar_vertice_templos(g, 'Artemisa')
des = buscar_vertice_templos(g, 'Teatro de Dionisio')
insertar_arista_templo(g, 23, ori, des)

bosque = []
bosque = prim_red(g)
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()


ori = buscar_vertice_templos(g, 'Atenas')
distancia = None
fin = 'Apolo'
camino_mas_corto = dijkstra_red(g, 'Atenas', 'Apolo')
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if distancia is None and fin == dato[1][0].info.nombre:
        distancia = dato[0]
print('El camino mas corto desde',ori.info.ubicacion,'hasta Delfos es:',distancia)
"""


#Ejercicio 2
class Criatura():
    def __init__(self, nombre, derrotado):
        self.nombre = nombre
        self.derrotado = derrotado

criaturas = [['Tifon','Zeus'],['Ladon','Heracles'],['Medusa','Perseo'],['Ortro','Heracles'],
             ['Esfinge','Edipo'],['Piton','Apolo'],['Gerion','Heracles'],['Cloto','-'],['Talos','Medea']]

arbol = None

for i in criaturas:
    arbol = insertar_nodo(arbol, i[0], i[1])

inorden(arbol)

print('Toda la informacion de Talos:')
busqueda_proximidad_criaturas(arbol,'Talos')

mayor = 0

for i in range(len(criaturas)):
    cant = 0
    aux = criaturas[i][1]
    for j in range(len(criaturas)):
        if aux == criaturas[j][1]:
            nom = aux
            cant += 1
    if cant > mayor:
        nombre = nom
        mayor = cant

print('La criatura que fue mas veces derrotada es',nombre,'con una cantidad de',mayor,'veces')
print()

print('Criaturas derrotadas por Heracles:')
for i in range(len(criaturas)):
    if 'Heracles' == criaturas[i][1]:
        print('-',criaturas[i][0])
print()
print('Criaturas que no fueron derrotadas')
for i in range(len(criaturas)):
    if '-' == criaturas[i][1]:
        print('-',criaturas[i][0])
print()
bus = input('Ingrese una criatura a buscar ')
busqueda_proximidad_criaturas(arbol, bus)
print()
x = eliminar_nodo(arbol, 'Tifon')
if x: 
    print('Eliminado:',x)
else:
    print('No eliminado')



#Parcial 1
#Ejercicio 1
"""
class Antenas():
    def __init__(self,ubicacion, latitud, longitud,cod,velocidad):
        self.ubicacion = ubicacion
        self.latitud = latitud
        self.longitud = longitud
        self.cod = cod
        self.velocidad = velocidad

datos = [['Mendoza',randint(0,100),randint(0,100),'LPM-895',randint(0,3000)],
         ['Misiones',randint(0,100),randint(0,100),'OKY-310',randint(0,3000)],
         ['Gualeguaychú',randint(0,100),randint(0,100),'OPK-100',randint(0,3000)],
         ['Concepcion del Uruguay',randint(0,100),randint(0,100),'KLG-150',randint(0,3000)],
         ['Gualeguay',randint(0,100),randint(0,100),'TGK-783',randint(0,3000)]]

#A
g = Grafo(False)


#B

for i in datos:
    dato = Antenas(i[0],i[1],i[2],i[3],i[4])
    insertar_vertice_antenas(g,dato)

ori = buscar_vertice_antenas(g,'Mendoza')
des = buscar_vertice_antenas(g,'Misiones')
insertar_arista_antenas(g, 18, ori, des)

des = buscar_vertice_antenas(g,'Gualeguaychú')
insertar_arista_antenas(g, 20, ori, des)

des = buscar_vertice_antenas(g,'Concepcion del Uruguay')
insertar_arista_antenas(g, 11, ori, des)

des = buscar_vertice_antenas(g,'Gualeguay')
insertar_arista_antenas(g, 12, ori, des)

ori = buscar_vertice_antenas(g,'Misiones')
des = buscar_vertice_antenas(g,'Gualeguaychú')
insertar_arista_antenas(g, 31, ori, des)

des = buscar_vertice_antenas(g,'Concepcion del Uruguay')
insertar_arista_antenas(g, 8, ori, des)

des = buscar_vertice_antenas(g,'Gualeguay')
insertar_arista_antenas(g, 10, ori, des)

ori = buscar_vertice_antenas(g,'Gualeguaychú')
des = buscar_vertice_antenas(g,'Concepcion del Uruguay')
insertar_arista_antenas(g, 27, ori, des)

des = buscar_vertice_antenas(g,'Gualeguay')
insertar_arista_antenas(g, 19, ori, des)

ori = buscar_vertice_antenas(g,'Concepcion del Uruguay')
des = buscar_vertice_antenas(g,'Gualeguay')
insertar_arista_antenas(g, 15, ori, des)


#barrido_grafo_antena(g)

#C
print('Tamaño del grafo: ',g.tamanio)

#D
camino_mas_corto = dijkstra_antena(g,'Mendoza','Misiones')
distancia = None
fin = 'Misiones'
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if distancia is None and fin == dato[1][0].info.ubicacion:
        distancia = dato[0]
print('El camino mas corto desde la antena de Mendoza hasta la antena de Misiones tiene una distancia de: ', distancia)

#E
print('Bosque de expansion minima: ')
bosque = kruskal_ant(g)

for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()

#D
buscado = str(input('Ingrese un codigo a buscar: '))
bus = buscar_vertice_antenas_codigo(g,buscado)
if bus is not None:
    print('Ubicacion con el codigo ', buscado,' encontrado...')
    print('Toda la informacion de',bus.info.ubicacion)
    print('-Ubicacion: ',bus.info.ubicacion,'\n-Latitud: ', bus.info.latitud,'\n-Longitud: ',bus.info.longitud,'\n-Codigo: ',bus.info.cod,'\n-Velocidad: ',bus.info.velocidad)
"""