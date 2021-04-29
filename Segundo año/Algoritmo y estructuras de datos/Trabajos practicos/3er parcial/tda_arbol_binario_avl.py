from tda_cola_dinamico import Cola, cola_vacia, arribo, atencion
from tda_archivo import leer

class nodoArbol(object):

    def __init__(self, info, campo = None, umbral=None, nrr = None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr
        self.altura = 0
        self.campo = campo
        self.umbral = umbral

    def __STR__(self, info, valor):
        self.info = info
        self.valor = valor



class nodoMarvel(object):
    
    def __init__(self, info, villano):
        self.izq = None
        self.der = None
        self.info = info
        self.villano = None
        self.altura = 0


class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor


def altura(raiz):
    """Devuelve la altura de un nodo."""
    if(raiz is None):
        return -1
    else:
        return raiz.altura


def actualizaraltura(raiz):
    """Actualiza la altura de un nodo."""
    if(raiz is not None):
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1



def insertar_nodo(raiz, dato, nrr=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz

def insertar_nodo_clima(raiz, dato, campo=None, umbral=None):
    if(raiz is None):
        raiz = nodoArbol(dato, campo, umbral)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo_clima(raiz.izq, dato, campo, umbral)
        else:
            raiz.der = insertar_nodo_clima(raiz.der, dato, campo, umbral)
    # raiz = balancear(raiz)
    # actualizaraltura(raiz)
    return raiz


def insertar_marvel(raiz, dato, villano):
    if(raiz is None):
        raiz = nodoArbol(dato, villano)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato, villano)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, villano)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz

def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

from tda_archivo import leer



def inorden_name(raiz, archivo, jedis):
    if(raiz is not None):
        inorden_name(raiz.izq, archivo, jedis)
        jedi = leer(archivo, raiz.nrr)
        jedis.append(jedi)
        inorden_name(raiz.der, archivo, jedis)


def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info, raiz.altura)
        preorden(raiz.izq)
        preorden(raiz.der)


def padre(raiz, buscado):
    if(raiz is not None):
        if((raiz.der is not None and raiz.der.info == buscado) or (raiz.izq is not None and raiz.izq.info == buscado)):
            print('el padre de buscado es', raiz.info)
            
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


def busqueda(raiz, buscado):
    if(raiz is not None):
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)

def busqueda_archivo_letra(raiz, buscado, archivo):
    if(raiz is not None):
        x = leer(archivo, raiz.nrr)
        for i in range(len(x.nombre)):
            if(x.nombre[i] == buscado):
                print('------------')
                print('Nombre:' + str(x.nombre) + '\nEspecie: ' + str(x.especie) + '\nAño de nacimiento: ' + str(x.anio) + '\nColor del sable: ' + str(x.color_sable) + '\nRanking: ' + str(x.ranking) + '\nMaestro: ' +str(x.maestro))
                print('------------')
        busqueda_archivo_letra(raiz.izq, buscado, archivo)
        busqueda_archivo_letra(raiz.der, buscado, archivo)

def busqueda_proximidad(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            print(raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)

def busqueda_proximidad_archivo_jedis(raiz, buscado, archivo):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            x = leer(archivo, raiz.nrr)
            print('------------')
            print('Nombre:' + str(x.nombre) + '\nEspecie: ' + str(x.especie) + '\nAño de nacimiento: ' + str(x.anio) + '\nColor del sable: ' + str(x.color_sable) + '\nRanking: ' + str(x.ranking) + '\nMaestro: ' +str(x.maestro))
            print('------------')
        busqueda_proximidad_archivo_jedis(raiz.izq, buscado, archivo)
        busqueda_proximidad_archivo_jedis(raiz.der, buscado, archivo)


def busqueda_proximidad_archivo_personajes(raiz, buscado, archivo):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            x = leer(archivo, raiz.nrr)
            print('------------')
            print('Nombre:' + str(x.nombre) + '\nEdad: ' + str(x.edad) + '\nAltura: ' + str(x.altura) + '\nCodigo: ' + str(x.codigo))
            print('------------')
        busqueda_proximidad_archivo_personajes(raiz.izq, buscado, archivo)
        busqueda_proximidad_archivo_personajes(raiz.der, buscado, archivo)

def busqueda_archivo_personajes(raiz, buscado, archivo):
    if(raiz is not None):
        x = leer(archivo, raiz.nrr)
        if(x.nombre == buscado):
            print('------------')
            print('Nombre:' + str(x.nombre) + '\nEdad: ' + str(x.edad) + '\nAltura: ' + str(x.altura) + '\nCodigo: ' + str(x.codigo))
            print('------------')
        busqueda_archivo_personajes(raiz.izq, buscado, archivo)
        busqueda_archivo_personajes(raiz.der, buscado, archivo)

def busqueda_archivo_personajes_pos(raiz, buscado, archivo):
    if(raiz is not None):
        x = leer(archivo, raiz.nrr)
        if(x.edad == buscado):
            print('------------')
            print('El Personaje',x.nombre ,'se encuentra en la posicion: ', raiz.nrr)
            print('------------')
        busqueda_archivo_personajes_pos(raiz.izq, buscado, archivo)
        busqueda_archivo_personajes_pos(raiz.der, buscado, archivo)

def busqueda_archivo_personajes_pos_c(raiz, buscado, archivo):
    if(raiz is not None):
        x = leer(archivo, raiz.nrr)
        if(x.codigo == buscado):
            print('------------')
            print('El Personaje',x.nombre ,'con codigo',x.codigo,'se encuentra en la posicion: ', raiz.nrr)
            print('------------')
        busqueda_archivo_personajes_pos_c(raiz.izq, buscado, archivo)
        busqueda_archivo_personajes_pos_c(raiz.der, buscado, archivo)

def busqueda_archivo_personajes_cm(raiz, buscado, archivo):
    if(raiz is not None):
        x = leer(archivo, raiz.nrr)
        if(x.altura < buscado):
            print('------------')
            print('Nombre:' + str(x.nombre) + '\nEdad: ' + str(x.edad) + '\nAltura: ' + str(x.altura) + '\nCodigo: ' + str(x.codigo))
            print('------------')
        busqueda_archivo_personajes_cm(raiz.izq, buscado, archivo)
        busqueda_archivo_personajes_cm(raiz.der, buscado, archivo)

def busqueda_proximidad_archivo_libros(raiz, buscado, archivo):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            x = leer(archivo, raiz.nrr)
            print('------------')
            print()
            print( 'Titulo:', x.titulo, '\nISBN:', x.isbn, '\nAutor / Autores: ', x.autores, '\nEditorial:', x.editorial, '\nCantidad de paginas:', x.cantidadPag)
            print()
            print('------------')
        busqueda_proximidad_archivo_libros(raiz.izq, buscado, archivo)
        busqueda_proximidad_archivo_libros(raiz.der, buscado, archivo)

def busqueda_proximidad_archivo_autor(raiz, buscado, archivo):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            x = leer(archivo, raiz.nrr)
            print('------------')
            print()
            print( 'El/Los autor/es del libro', x.titulo, 'es/son ', x.autores)
            print()
            print('------------')
        busqueda_proximidad_archivo_autor(raiz.izq, buscado, archivo)
        busqueda_proximidad_archivo_autor(raiz.der, buscado, archivo)

def busqueda_archivo(raiz, cantidad, archivo):
    if(raiz is not None):
        libro = leer(archivo, raiz.nrr)
        if(libro.cant > cantidad):
            print(libro.isbn, libro.cant, libro.titulo, libro.autores)
        busqueda_archivo(raiz.izq, cantidad, archivo)
        busqueda_archivo(raiz.der, cantidad, archivo)

def busqueda_archivo_libros(raiz, buscado, archivo):
    if(raiz is not None):
        x = leer(archivo, raiz.nrr)
        if(x.cantidadPag > buscado):
            print()
            print( 'Titulo:', x.titulo, '\nISBN:', x.isbn, '\nAutor / Autores: ', x.autores, '\nEditorial:', x.editorial, '\nCantidad de paginas:', x.cantidadPag)
            print()
            print('------------')
        busqueda_archivo_libros(raiz.izq, buscado, archivo)
        busqueda_archivo_libros(raiz.der, buscado, archivo)

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
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz, x


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


def rotar_simple(raiz, control):
    """Realiza una rotación simple de nodos a la derecha o a la izquierda."""
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizaraltura(raiz)
    actualizaraltura(aux)
    raiz = aux
    return raiz

def rotar_doble(raiz, control):
    """Realiza una rotación doble de nodos a la derecha o a la izquierda."""
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz


def balancear(raiz):
    """Determina que rotación hay que hacer para balancear el árbol."""
    if(raiz is not None):
        if(altura(raiz.izq)-altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.der)-altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz

def cortar_por_nivel(raiz, bosque):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        if(altura(nodo) == 7 ):
            bosque.append(nodo.izq)
            bosque.append(nodo.der)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)

def contar(raiz, cantidad):
    if(raiz is not None):
        contar(raiz.izq, cantidad)
        contar(raiz.der, cantidad)
        cantidad[0] += 1