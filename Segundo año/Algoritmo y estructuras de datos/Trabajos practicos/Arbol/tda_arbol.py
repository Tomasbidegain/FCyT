from tda_cola_dinamico import Cola, cola_vacia, arribo, atencion
from tda_archivo import  leer

class nodoArbol(object):

    def __init__(self, info, nrr=None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr


class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor

class nodoArbolGreek(object):
    
    def __init__(self, info, madre, descipcion=None):
        self.izq = None
        self.der = None
        self.info = info
        self.madre = madre
        self.descripcion = descipcion

def insertar_nodo(raiz, dato, nrr=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    return raiz

def insertar_nodo_huffman(raiz, dato, derrotado):
    if(raiz is None):
        raiz = nodoArbolHuffman(dato,derrotado)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo_huffman(raiz.izq, dato, derrotado)
        else:
            raiz.der = insertar_nodo_huffman(raiz.der, dato, derrotado)
    return raiz

def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def por_nivel(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)

def por_nivel_nario(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        hno = nodo.der
        while(hno is not None):
            print(hno.info)
            if(hno.izq is not None):
                arribo(cola, hno.izq)
            hno = hno.der

def busqueda(raiz, buscado):
    if(raiz is not None):
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)


def busqueda_nario(raiz, buscado, pos):
    if(raiz is not None):
        if(raiz.info == buscado):
            pos.append(raiz)
            return
        busqueda_nario(raiz.izq, buscado, pos)
        busqueda_nario(raiz.der, buscado, pos)


def busqueda_proximidad(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            print(raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)


def arbol_vacio(raiz):
    return raiz is None


def remplazar(raiz):
    """Determina el nodo que remplazará al que se elimina."""
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux


def eliminar_nodo(raiz, clave):
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

def contar_nodos(raiz, cont=0):
    if raiz is not None:
        cont = contar_nodos(raiz.izq, cont)
        cont += 1
        cont = contar_nodos(raiz.der, cont)
    return cont

def insertar_nodo_morse(raiz, dato):
    if raiz is None:
        raiz = nodoArbol(dato)
    else:
        if raiz.info[0] > dato[0]:
            raiz.izq = insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def insertar_nario(padre, hijo):
    if(padre.izq is None):
        #print('insertar hijo de', padre.info)
        padre.izq = hijo
    else:
        aux = padre.izq
        while(aux.der is not None):
            aux = aux.der
        #print('insertar hno de', aux.info)
        aux.der = hijo