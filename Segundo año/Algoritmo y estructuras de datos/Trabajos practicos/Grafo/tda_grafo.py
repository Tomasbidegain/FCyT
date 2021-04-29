from tda_pila_dinamica import Pila, apilar, pila_vacia, desapilar
from tda_cola_dinamico import Cola, cola_vacia, arribo, atencion
from TDA_Heap import Heap, arribo_heap, atencion_heap, busqueda_heap_aero, heap_vacio, cambiar_prioridad, busqueda_heap, busqueda_heap_red
from math import inf


class Nodo_Arista():
    '''Clase nodo arista'''
    def __init__(self, info, destino):
        '''Crea un nodo arista con la información cargada'''
        self.info = info
        self.destino = destino
        self.sig = None


class Nodo_Vertice():
    '''Clase nodo vértice'''
    def __init__(self, info, datos=None):
        '''Crea un nodo vértice con la información cargada'''
        self.info = info
        self.datos = datos
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista() # lista de aristas


class Grafo():
    '''Clase grafo implementación lista de listas de adyacencia'''
    def __init__(self, dirigido=True):
        '''Crea un grafo vacio'''
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista():
    '''Clase lista de aristas implementación sobre lista'''
    def __init__(self):
        '''Crea una lista de aristas vacia'''
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato):
    '''Inserta un vértice al grafo'''
    nodo = Nodo_Vertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def insertar_vertice_aeropuerto(grafo, dato):
    '''Inserta un vértice al grafo aeropuerto'''
    nodo = Nodo_Vertice(dato)
    if grafo.inicio is None or grafo.inicio.info.nombre > dato.nombre:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info.nombre < nodo.info.nombre:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def insertar_vertice_red(grafo, dato):
    '''Inserta un vértice al grafo'''
    nodo = Nodo_Vertice(dato)
    if grafo.inicio is None or grafo.inicio.info.nombre > dato.nombre:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info.nombre < nodo.info.nombre:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def insertar_vertice_maravilla(grafo, dato):
    '''Inserta un vértice al grafo'''
    nodo = Nodo_Vertice(dato)
    if grafo.inicio is None or grafo.inicio.info.nombre > dato.nombre:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info.nombre < nodo.info.nombre:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    '''Inserta una arista desde el vértice origen al destino'''
    agregrar_arista(origen.adyacentes, dato, destino.info)
    if not grafo.dirigido:
        agregrar_arista(destino.adyacentes, dato, origen.info)


def agregrar_arista(origen, dato, destino):
    '''Agrega la arista desde el vértice origen al destino'''
    nodo = Nodo_Arista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1


def insertar_arista_viaje(grafo, dato, origen, destino):
    '''Inserta una arista desde el vértice origen al destino'''
    agregrar_arista_viaje(origen.adyacentes, dato, destino.info.nombre)
    if not grafo.dirigido:
        agregrar_arista_viaje(destino.adyacentes, dato, origen.info.nombre)


def agregrar_arista_viaje(origen, dato, destino):
    '''Agrega la arista desde el vértice origen al destino'''
    nodo = Nodo_Arista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1


def insertar_arista_red(grafo, dato, origen, destino):
    '''Inserta una arista desde el vértice origen al destino'''
    agregrar_arista_red(origen.adyacentes, dato, destino.info.nombre)
    if not grafo.dirigido:
        agregrar_arista_red(destino.adyacentes, dato, origen.info.nombre)


def agregrar_arista_red(origen, dato, destino):
    '''Agrega la arista desde el vértice origen al destino'''
    nodo = Nodo_Arista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1


def insertar_arista_maravilla(grafo, dato, origen, destino):
    '''Inserta una arista desde el vértice origen al destino'''
    agregrar_arista(origen.adyacentes, dato, destino.info.nombre)
    if not grafo.dirigido:
        agregrar_arista(destino.adyacentes, dato, origen.info.nombre)


def eliminar_vertice(grafo, clave):
    '''Elimina un vertice del grafo y lo devuelve si lo encuentra'''
    x = None
    if grafo.inicio.info == clave:
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info != clave:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if x is not None:
        aux = grafo.inicio
        while aux is not None:
            if aux.adyacentes.inicio is not None:
                quitar_arista(aux.adyacentes, clave)
            aux = aux.sig
        # aca terminar eliminar aristas adyacenes grafo no dirigido
    return x


def quitar_arista(vertice, destino):
    x = None
    if vertice.adyacentes.inicio.destino == destino:
        x = vertice.adyacentes.inicio.info
        vertice.adyacentes.inicio = vertice.adyacentes.inicio.sig
        vertice.adyacentes.tamanio -= 1
    else:
        ant = vertice.adyacentes.inicio
        act = vertice.adyacentes.inicio.sig
        while act is not None and act.destino != destino:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            vertice.adyacentes.tamanio -= 1
    return x


def eliminar_arista_red(grafo, vertice, destino):
    '''Elimina una arsita del vertice y lo devuelve si lo encuentra'''
    x = quitar_arista(vertice, destino)    
    if not grafo.dirigido:
        ori = buscar_vertice_red(grafo, destino)
        quitar_arista(ori, vertice.info)
    return x


def eliminar_arista_red(grafo, vertice, destino):
    '''Elimina una arsita del vertice y lo devuelve si lo encuentra'''
    x = quitar_arista(vertice, destino)    
    if not grafo.dirigido:
        ori = buscar_vertice_red(grafo, destino)
        quitar_arista(ori, vertice.info)
    return x


def barrido_grafo(grafo):
    '''Realiza un barrido de la grafo mostrando sus valores'''
    aux = grafo.inicio
    while aux is not None:
        print('vertice:', aux.info)
        print('adyacentes:')
        adyacentes(aux)
        print()
        aux = aux.sig


def barrido_grafo_red(grafo):
    '''Realiza un barrido de la grafo mostrando sus valores'''
    aux = grafo.inicio
    while aux is not None:
        print('NOMBRE | TIPO')
        print('vertice:', aux.info)
        print('adyacentes:')
        adyacentes_red(aux)
        print()
        aux = aux.sig


def barrido_grafo_maravilla(grafo):
    '''Realiza un barrido de la grafo mostrando sus valores'''
    aux = grafo.inicio
    while aux is not None:
        print('NOMBRE | UBICACION | TIPO')
        print('vertice:', aux.info.nombre)
        print('adyacentes:')
        adyacentes_marav(aux)
        print()
        aux = aux.sig


def adyacentes_red(vertice):
    '''Muestra los adyacentes del vertice'''
    aux = vertice.adyacentes.inicio
    while aux is not None:
        print(aux.destino, ' - Peso:',aux.info)
        aux = aux.sig


def adyacentes_marav(vertice):
    '''Muestra los adyacentes del vertice'''
    aux = vertice.adyacentes.inicio
    while aux is not None:
        print(aux.destino, '- Distancia:', aux.info, 'km')
        aux = aux.sig


def buscar_vertice(grafo, buscado):
    '''Devuelve la direccion del elemento buscado'''
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux


def buscar_vertice_aeropuerto(grafo, buscado):
    '''Devuelve la direccion del elemento buscado'''
    aux = grafo.inicio
    while aux is not None and aux.info.nombre != buscado:
        aux = aux.sig
    return aux


def buscar_vertice_red(grafo, buscado):
    '''Devuelve la direccion del elemento buscado'''
    aux = grafo.inicio
    while aux is not None and aux.info.nombre != buscado:
        aux = aux.sig
    return aux


def buscar_vertice_maravilla(grafo, buscado):
    '''Devuelve la direccion del elemento buscado'''
    aux = grafo.inicio
    while aux is not None and aux.info.nombre != buscado:
        aux = aux.sig
    return aux


def buscar_vertice_ubicacion(grafo, buscado):
    '''Devuelve la direccion del elemento buscado'''
    aux = grafo.inicio
    while aux is not None and aux.info.ubicacion != buscado:
        aux = aux.sig
    return aux


def buscar_arista(vertice, buscado):
    '''Devuelve la direccion del elemento buscado'''
    aux = vertice.adyacentes.inicio
    while aux is not None and aux.destino != buscado:
        aux = aux.sig
    return aux


def tamanio_grafo(grafo):
    '''Devuelve el numero de vertices en el grafo'''
    return grafo.tamanio


def grafo_vacio(grafo):
    '''Devuelve true si el grafo esta vacio'''
    return grafo.inicio is None


def adyacentes(vertice):
    '''Muestra los adyacentes del vertice'''
    aux = vertice.adyacentes.inicio
    while aux is not None:
        print(aux.destino, aux.info)
        aux = aux.sig


def es_adyacente(vertice, destino):
    '''Determina si el destino es adyacente directo'''
    resultado = False
    aux = vertice.adyacentes.inicio
    while aux is not None and not resultado:
        if aux.destino == resultado:
            resultado = True
        aux = aux.sig
    return resultado


def marcar_no_visitado(grafo):
    '''Marca todos los vertices del grafo como no visitados'''
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig


def barrido_profundidad(grafo, vertice):
    '''Barrido en profundidad del grafo'''
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if not adyacente.visitado:
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_amplitud(grafo, vertice):
    '''Barrido en amplitud del grafo'''
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while adyacentes is not None:
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_profundidad_red(grafo, vertice):
    '''Barrido en profundidad del grafo'''
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacente = buscar_vertice_red(grafo, adyacentes.destino)
                if not adyacente.visitado:
                    barrido_profundidad_red(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_amplitud_red(grafo, vertice):
    '''Barrido en amplitud del grafo'''
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while adyacentes is not None:
                    adyacente = buscar_vertice_red(grafo, adyacentes.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig


def dijkstra(grafo, origen, destino):
    '''Algoritmo de Dijkstra para hallar el camino mas corto'''
    no_visitados = Heap(tamanio_grafo(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info == origen:
            arribo_heap(no_visitados, [aux, None], 0)
        else:
            arribo_heap(no_visitados, [aux, None], inf)
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_heap(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = busqueda_heap(no_visitados, aux.destino)
            if no_visitados.vector[pos][0] > dato[0] + aux.info:
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino

def dijkstra_red(grafo, origen, destino):
    '''Dijkstra para hallar el camino mas corto'''
    no_visitados = Heap(tamanio_grafo(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info.nombre == origen:
            arribo_heap(no_visitados, [aux, None], 0)
        else:
            arribo_heap(no_visitados, [aux, None], inf)
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_heap(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = busqueda_heap_red(no_visitados, aux.destino)
            if no_visitados.vector[pos][0] > dato[0] + aux.info:
                no_visitados.vector[pos][1][1] = dato[1][0].info.nombre
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino

def dijkstra_distancia(grafo, origen, destino):
    '''Dijkstra para hallar el camino mas corto'''
    no_visitados = Heap(tamanio_grafo(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info.nombre == origen:
            arribo_heap(no_visitados, [aux, None], 0)
        else:
            arribo_heap(no_visitados, [aux, None], inf)
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_heap(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = busqueda_heap_aero(no_visitados, aux.destino)
            if no_visitados.vector[pos][0] > dato[0] + aux.info.distancia:
                no_visitados.vector[pos][1][1] = dato[1][0].info.nombre
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info.distancia)
            aux = aux.sig
    return camino


def dijkstra_duracion(grafo, origen, destino):
    '''Dijkstra para hallar el camino de menos duracion'''
    no_visitados = Heap(tamanio_grafo(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info.nombre == origen:
            arribo_heap(no_visitados, [aux, None], 0)
        else:
            arribo_heap(no_visitados, [aux, None], inf)
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_heap(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = busqueda_heap_aero(no_visitados, aux.destino)
            if no_visitados.vector[pos][0] > dato[0] + aux.info.duracion:
                no_visitados.vector[pos][1][1] = dato[1][0].info.nombre
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info.duracion)
            aux = aux.sig
    return camino


def dijkstra_costo(grafo, origen, destino):
    '''Dijkstra para hallar el camino de menor coste'''
    no_visitados = Heap(tamanio_grafo(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info.nombre == origen:
            arribo_heap(no_visitados, [aux, None], 0)
        else:
            arribo_heap(no_visitados, [aux, None], inf)
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_heap(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = busqueda_heap_aero(no_visitados, aux.destino)
            if no_visitados.vector[pos][0] > dato[0] + aux.info.costo:
                no_visitados.vector[pos][1][1] = dato[1][0].info.nombre
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info.costo)
            aux = aux.sig
    return camino



def prim(grafo):
    '''Algoritmo de Prim para hallar el árbol de expansión mínimo'''
    bosque = []
    aristas = Heap(tamanio_grafo(grafo) ** 2)
    adyac = grafo.inicio.adyacentes.inicio
    while adyac is not None:
        arribo_heap(aristas, [grafo.inicio.info, adyac.destino], adyac.info)
        adyac = adyac.sig
    while len(bosque) // 2 < tamanio_grafo(grafo) and not heap_vacio(aristas):
        dato = atencion_heap(aristas)
        if len(bosque) == 0 or ((dato[1][0] not in bosque) ^ (dato[1][1] not in bosque)):
            bosque += dato[1]
            destino = buscar_vertice(grafo, dato[1][1])
            adyac = destino.adyacentes.inicio
            while adyac is not None:
                arribo_heap(aristas, [destino.info, adyac.destino], adyac.info)
                adyac = adyac.sig
    return bosque


def prim_red(grafo):
    '''Algoritmo de Prim para hallar el árbol de expansión mínimo'''
    bosque = []
    aristas = Heap(tamanio_grafo(grafo) ** 2)
    adyac = grafo.inicio.adyacentes.inicio
    while adyac is not None:
        arribo_heap(aristas, [grafo.inicio.info.nombre, adyac.destino], adyac.info)
        adyac = adyac.sig
    while len(bosque) // 2 < tamanio_grafo(grafo) and not heap_vacio(aristas):
        dato = atencion_heap(aristas)
        if len(bosque) == 0 or ((dato[1][0] not in bosque) ^ (dato[1][1] not in bosque)):
            bosque += dato[1]
            destino = buscar_vertice_maravilla(grafo, dato[1][1])
            adyac = destino.adyacentes.inicio
            while adyac is not None:
                arribo_heap(aristas, [destino.info, adyac.destino], adyac.info)
                adyac = adyac.sig
    return bosque


def prim_arq(grafo):
    '''Algoritmo de Prim para hallar el árbol de expansión mínimo'''
    bosque = []
    aristas = Heap(tamanio_grafo(grafo) ** 2)
    adyac = buscar_vertice_maravilla(grafo, 'La ciudad de Petra')
    adyac = adyac.adyacentes.inicio
    while adyac is not None:
        arribo_heap(aristas, [grafo.inicio.info.nombre, adyac.destino], adyac.info)
        adyac = adyac.sig
    while len(bosque) // 2 < tamanio_grafo(grafo) and not heap_vacio(aristas):
        dato = atencion_heap(aristas)
        if len(bosque) == 0 or ((dato[1][0] not in bosque) ^ (dato[1][1] not in bosque)):
            bosque += dato[1]
            destino = buscar_vertice_maravilla(grafo, dato[1][1])
            adyac = destino.adyacentes.inicio
            while adyac is not None:
                arribo_heap(aristas, [destino.info, adyac.destino], adyac.info)
                adyac = adyac.sig
    return bosque

def prim_nat(grafo):
    '''Algoritmo de Prim para hallar el árbol de expansión mínimo'''
    bosque = []
    aristas = Heap(tamanio_grafo(grafo) ** 2)
    adyac = grafo.inicio.adyacentes.inicio
    while adyac is not None:
        arribo_heap(aristas, [grafo.inicio.info.nombre, adyac.destino], adyac.info)
        adyac = adyac.sig
    while len(bosque) // 2 < tamanio_grafo(grafo) and not heap_vacio(aristas):
        dato = atencion_heap(aristas)
        if len(bosque) == 0 or ((dato[1][0] not in bosque) ^ (dato[1][1] not in bosque)):
            bosque += dato[1]
            destino = buscar_vertice_maravilla(grafo, dato[1][1])
            adyac = destino.adyacentes.inicio
            while adyac is not None:
                arribo_heap(aristas, [destino.info, adyac.destino], adyac.info)
                adyac = adyac.sig
    return bosque


def kruskal(grafo):
    '''Algoritmo de Kruskal para hallar el árbol de expansión mínimo'''
    bosque = []
    aristas = Heap(tamanio_grafo(grafo) ** 2)
    aux = grafo.inicio
    while aux is not None:
        bosque.append([aux.info])
        adyac = aux.adyacentes.inicio
        while adyac is not None:
            arribo_heap(aristas, [aux.info, adyac.destino], adyac.info)
            adyac = adyac.sig
        aux = aux.sig
    while len(bosque) > 1 and not heap_vacio(aristas):
        dato = atencion_heap(aristas)
        origen = None
        for elemento in bosque:
            if dato[1][0] in elemento:
                origen = bosque.pop(bosque.index(elemento))
                break
        destino = None
        for elemento in bosque:
            if dato[1][1] in elemento:
                destino = bosque.pop(bosque.index(elemento))
                break
        if origen is not None and destino is not None:
            if len(origen) > 1 and len(destino) == 1:
                destino = [dato[1][0], dato[1][1]]
            elif len(destino) > 1 and len(origen) == 1:
                origen = [dato[1][0], dato[1][1]]
            elif len(destino) > 1 and len(origen) > 1:
                origen += [dato[1][0], dato[1][1]]
            bosque.append(origen + destino)
        else:
            bosque.append(origen)
    return bosque[0]


def existe_paso(grafo, origen, destino):
    '''Barrido en profundidad del grafo'''
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while vadyacentes is not None and not resultado:
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if adyacente.info == destino.info:
                return True
            elif not adyacente.visitado:
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado


def existe_paso_aero(grafo, origen, destino):
    '''Barrido en profundidad del grafo'''
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while vadyacentes is not None and not resultado:
            adyacente = buscar_vertice_aeropuerto(grafo, vadyacentes.destino)
            if adyacente.info == destino.info:
                return True
            elif not adyacente.visitado:
                resultado = existe_paso_aero(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado

'''
g = Grafo(False)
insertar_vertice(g, 'A')
insertar_vertice(g, 'B')
insertar_vertice(g, 'C')
insertar_vertice(g, 'F')
insertar_vertice(g, 'Z')
insertar_vertice(g, 'J')
insertar_vertice(g, 'W')
ori = buscar_vertice(g, 'A')
des = buscar_vertice(g, 'C')
insertar_arista(g, 5, ori, des)
des = buscar_vertice(g, 'B')
insertar_arista(g, 15, ori, des)
ori = buscar_vertice(g, 'C')
des = buscar_vertice(g, 'B')
insertar_arista(g, 25, ori, des)
des = buscar_vertice(g, 'F')
insertar_arista(g, 7, ori, des)
ori = buscar_vertice(g, 'J')
des = buscar_vertice(g, 'W')
insertar_arista(g, 13, ori, des)
ori = buscar_vertice(g, 'W')
des = buscar_vertice(g, 'F')
insertar_arista(g, 33, ori, des)
ori = buscar_vertice(g, 'F')
des = buscar_vertice(g, 'B')
insertar_arista(g, 10, ori, des)
des = buscar_vertice(g, 'Z')
insertar_arista(g, 19, ori, des)
print('profundidad')
ori = buscar_vertice(g, 'F')
barrido_profundidad(g, ori)
marcar_no_visitado(g)
print()
print('amplitud')
ori = buscar_vertice(g, 'F')
barrido_amplitud(g, ori)
print()
print('dijkstra')
camino_mas_corto = dijkstra(g, 'A', 'J')
fin = 'Z'
peso_total = None
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if peso_total is None and fin == dato[1][0].info:
        peso_total = dato[0]
    if fin == dato[1][0].info:
        print(dato[1][0].info)
        fin = dato[1][1]
print('peso total:', peso_total)
print()
print('prim')
bosque = prim(g)
for i in range(0,len(bosque),2):
    print(bosque[i], bosque[i+1])
print()
print('kruskal')
bosque = kruskal(g)
for i in range(0,len(bosque),2):
    print(bosque[i], bosque[i+1])
'''