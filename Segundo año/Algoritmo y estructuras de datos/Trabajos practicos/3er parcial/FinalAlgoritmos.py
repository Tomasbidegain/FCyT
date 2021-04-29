from tda_arbol_binario_avl import busqueda_archivo_personajes, busqueda_archivo_personajes_cm, busqueda_archivo_personajes_pos, busqueda_archivo_personajes_pos_c, busqueda_proximidad_archivo_personajes
from tda_pila_dinamica import desapilar, pila_vacia
from tda_archivo import abrir,cerrar,guardar,modificar, leer
from tda_grafo import Grafo, barrido_grafo_maravilla, buscar_vertice_puestos, buscar_vertice_ubicacion, dijkstra, dijkstra_costo, dijkstra_tiempo, insertar_arista_puestos, insertar_vertice_puestos, kruskal_costo, prim_puesto
from random import randint
from tda_arbol import nodoArbol,insertar_nodo, preorden

#EJ1

class Personajes():
    def __init__(self, nombre, edad, altura, codigo):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.codigo = codigo

arbol_edad = None
arbol_codigo = None

datos = [['Yoda', '29', 10, 123], ['Darth Vader','200', 210, 456],
         ['Kit Fitso','170', 18, 789], ['Personaje 4','230', 90, 101], 
         ['Personaje 5','150', 189, 121], ['Personaje 6','54', 120, 314],
         ['General Grievous','74', 156, 151], ['Personaje 8','65', 150, 617]]

file = abrir('personaje')
for dato in datos:
    x = Personajes(dato[0], dato[1], dato[2], dato[3])
    guardar(file, x)
cerrar(file)

#Se cargan datos del archivo en el arbol
pos = 0
file = abrir('personaje')
while pos < len(datos):
    aux = leer(file, pos)
    arbol_edad = insertar_nodo(arbol_edad, aux.edad, pos)
    arbol_codigo = insertar_nodo(arbol_codigo, aux.codigo , pos)
    pos += 1

print('Informacion de Yoda: ')
busqueda_archivo_personajes(arbol_edad,'Yoda',file )
print()
print('Informacion de Darth Vader:')
busqueda_archivo_personajes(arbol_edad,'Darth Vader',file )
print()
busqueda_archivo_personajes_pos(arbol_edad,'170',file)
print()
busqueda_archivo_personajes_pos_c(arbol_codigo,123,file)
print()
print('Personajes con una altura menor a 80 cm')
busqueda_archivo_personajes_cm(arbol_edad,80,file)
print()
print('En el arbol hay ',pos,'personajes')
busqueda_archivo_personajes(arbol_edad,'General Grievous',file)

cerrar(file)



#EJ2
"""class Puesto():
    def __init__ (self, nombre, direccion, ubicacion):
        self.nombre = nombre
        self.direccion = direccion
        self.ubiacion = ubicacion 

class Trayectoria():
    def __init__(self, costo, tiempo):
        self.costo = costo
        self.tiempo = tiempo

datos = [['Puesto 1','Vicente Lopez 133','Hospital'],['Puesto 2','Misiones 488','Isla del puerto'],
         ['Puesto 3','Sartorio 455','Sur'],['Puesto 4','Bv. Diaz Velez 378','Este'],
         ['Puesto 5','Galarza 1200','Oeste'],['Puesto 6','Sarmiento 892','Norte'],
         ['Puesto 7','Irigoyen 2000','Ubicacion A'], ['Puesto 8',' Sarmiento 100','Ubicacion B']]

g = Grafo()

for i in datos:
    aux = Puesto(i[0],i[1],i[2])
    insertar_vertice_puestos(g,aux)

ori = buscar_vertice_puestos(g, 'Puesto 1')
des = buscar_vertice_puestos(g, 'Puesto 2')
dato = Trayectoria(randint(1,50),randint(1,50))
insertar_arista_puestos(g,dato,ori,des)

ori = buscar_vertice_puestos(g, 'Puesto 2')
des = buscar_vertice_puestos(g, 'Puesto 3')
dato = Trayectoria(randint(1,50),randint(1,50))
insertar_arista_puestos(g,dato,ori,des)

ori = buscar_vertice_puestos(g, 'Puesto 7')
des = buscar_vertice_puestos(g, 'Puesto 4')
dato = Trayectoria(randint(1,50),randint(1,50))
insertar_arista_puestos(g,dato,ori,des)

ori = buscar_vertice_puestos(g, 'Puesto 6')
des = buscar_vertice_puestos(g, 'Puesto 5')
dato = Trayectoria(randint(1,50),randint(1,50))
insertar_arista_puestos(g,dato,ori,des)

ori = buscar_vertice_puestos(g, 'Puesto 5')
des = buscar_vertice_puestos(g, 'Puesto 6')
dato = Trayectoria(randint(1,50),randint(1,50))
insertar_arista_puestos(g,dato,ori,des)

ori = buscar_vertice_puestos(g, 'Puesto 4')
des = buscar_vertice_puestos(g, 'Puesto 7')
dato = Trayectoria(randint(1,50),randint(1,50))
insertar_arista_puestos(g,dato,ori,des)

ori = buscar_vertice_puestos(g, 'Puesto 3')
des = buscar_vertice_puestos(g, 'Puesto 8')
dato = Trayectoria(randint(1,50),randint(1,50))
insertar_arista_puestos(g,dato,ori,des)

print('Por costo:')
pila = dijkstra_costo(g,'Puesto 1','Puesto 2')
distancia = None
fin = 'Puesto 2'
while not pila_vacia(pila):
    dato = desapilar(pila)
    if distancia is None and fin == dato[1][0].info.nombre:
        distancia = dato[0]
print('El camino a recorrer para ir desde el Hospital hasta la Isla del puerto es de', distancia,'km')
print()
print('Por tiempo:')
pila = dijkstra_tiempo(g,'Puesto 1','Puesto 2')
distancia = None
fin = 'Puesto 2'
while not pila_vacia(pila):
    dato = desapilar(pila)
    if distancia is None and fin == dato[1][0].info.nombre:
        distancia = dato[0]
print('El camino a recorrer para ir desde el Hospital hasta la Isla del puerto es de', distancia,'hs')
print()
print('Bosque de expansion minima en base a el costo: ')
bosque = kruskal_costo(g)

for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()"""