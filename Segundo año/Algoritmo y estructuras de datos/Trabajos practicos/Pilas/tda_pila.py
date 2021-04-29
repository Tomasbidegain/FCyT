class Pila():
    """Crear una pila vacia"""
    def __init__(self):
        self.cima, self.datos = -1, [0] * 5


def apilar(pila, dato):
    """apile el dato en la cima"""
    pila.cima += 1
    pila.datos[pila.cima] = dato


def desapilar(pila):
    dato = pila.datos[pila.cima]
    pila.cima -= 1
    return dato


def pila_vacia(pila):
    return pila.cima == -1

def pila_llena(pila):
    return pila.cima == len(pila.datos)-1

def tamanio(pila):
    return pila.cima + 1

def cima(pila):
    return pila.datos[pila.cima]