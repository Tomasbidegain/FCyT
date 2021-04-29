from tda_cola_dinamica import Cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
from tda_pila_dinamica import Pila, pila_vacia, desapilar, apilar, tamanio, cima
from tda_sublista import Lista, eliminar, insertar, busqueda, barrido, barrido_con_sublista, tamanio,lista_vacia, criterio

#Ejercicio 1
"""
def usar_la_fuerza(mochila, i):
    if i == len(mochila):
        return "No encontro el sable de luz"
    else:
        if mochila[i] == 'Sable de luz':
            print("El sable de luz se encuentra en la posicion:")
            return i + 1
        else:
            return usar_la_fuerza(mochila, i + 1)

mochila = ['Lentes', 'Botella de agua','Dinero', 'Linterna', 'Sable de luz', "Cuchillo"]

print(usar_la_fuerza(mochila, 0))
"""

#Ejercicio 2
"""
cola_redes = Cola()
pila_instagram = Pila()

dato = ["","",""]

archivo = open('notificaciones')
linea = archivo.readline()
while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = linea[1].title()
    linea[2] = linea[2].title()
    arribo(cola_redes, linea)
    linea = archivo.readline()

def eliminar_face():
    if dato[1] == 'Facebook':
        print('Eliminando notificacion de',dato[1],'"',dato[2],'"')
        atencion(cola_redes)
def mostrar_py():
    if 'Python'in dato[2]:
        print('Tweet que contiene la palabra"Python"')
        print(dato)

def alamacenar_instagram():
    if dato[1] == "Instagram":
        apilar(pila_instagram, dato)

for i in range(0,tamanio(cola_redes)):
    dato = en_frente(cola_redes)
    eliminar_face()
    mostrar_py()
    alamacenar_instagram()
    mover_final(cola_redes)
"""

#Ejercicio 3

pila_trajes = Pila()
pila_trajes_aux = Pila()
"""
archivo = open('trajes')
linea = archivo.readline()
while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = linea[1].title()
    linea[2] = linea[2].title()
    apilar(pila_trajes, linea)
    linea = archivo.readline()

while not pila_vacia(pila_trajes):
    x = desapilar(pila_trajes)
    if x[0] == "Mark XLIV":
        print("El traje",x[0],"fue utilizado en la pelicula",x[2])
    
    if x[1] == "Daniado":
        print("Modelo daniado:",x[0])
    if x[2] == "Avengers: End Game":
        print("Traje usado en la pelicula Avengers: End Game:",x[0])
    if x[1] != "Impecable":
        apilar(pila_trajes_aux,x)

while not pila_vacia(pila_trajes_aux):
    x = desapilar(pila_trajes_aux)
    apilar(pila_trajes, x)

print("pila modificada")
while not pila_vacia(pila_trajes):
    print(desapilar(pila_trajes))
"""

#Ejercicio 4

personajes_aux = Lista()
personajes_aux = ['Black Widow', 'Hulk','Rocket Racoonn', 'Loki']

lista_personajes = Lista()
lista_personajes_aux = Lista()
archivo = open('personajes')
linea = archivo.readline()
while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    insertar(lista_personajes, linea)
    linea = archivo.readline()
print("Lista de personajes:")
barrido(lista_personajes)

aux = lista_personajes.inicio
while (aux is not None):
    if (aux.info == "Thor"):
        print("Thor esta en la posicion",aux)

    if (aux.info) == "Scalet Witch":
        aux.info = "Scarlet Witch"
    
    aux = aux.sig

#Ejercicio 5
"La funcion O grande caracteriza la eficiencia de un algoritmo por el tiempo de ejecución o el nivel de complejidad y en cuanto a el orden de complejidad de una busqueda secuencial es de log n"