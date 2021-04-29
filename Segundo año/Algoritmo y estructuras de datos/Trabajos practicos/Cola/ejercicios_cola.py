from tda_cola_dinamico import Cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
from random import randint,choice
from tda_pila_dinamica import Pila, apilar, desapilar, tamanio, pila_vacia, cima
from math import acos, cos, sin, radians
from random import randint
from time import sleep, strftime
from datetime import datetime
from copy import copy


cola = Cola()
cola_aux = Cola()
pila = Pila()

def cargar_random(cola):
    while (tamanio(cola) < 10):
        arribo(cola, randint(1,100))

def cargar_elementos(cola):
    while(tamanio(cola) < 10):
        ele = int(input('Ingrese un elemento: '))
        arribo(cola, ele)

def barrido(cola):
    for i in range(tamanio(cola)):
        print(en_frente(cola))
        mover_final(cola)

#******************************************************************************************************************************
#======================================================Ejercicio 1=============================================================
#******************************************************************************************************************************
"""
1.Eliminar de una cola de caracteres todas las vocales que aparecen.
"""


"""
vocales = "aeiouAEIOU"
while (tamanio(cola) < 10):
    caracter = input('Ingrese una letra: ')
    arribo(cola, caracter)
print(tamanio(cola))
for i in range(tamanio(cola)):
    if (en_frente(cola) in vocales): 
        atencion(cola)
    else:
        mover_final(cola)
print("Cola sin vocales")
while (not cola_vacia(cola)):
    x = atencion(cola)
    print(x)
"""


#******************************************************************************************************************************
#======================================================Ejercicio 2=============================================================
#******************************************************************************************************************************
"""
2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.
"""

"""
while (tamanio(cola) < 5):
    x = input('Ingrese un elemento:')
    arribo(cola, x)
print('Cola normal:')
while(not cola_vacia(cola)):
    x = atencion(cola)
    print(x)
    apilar(pila, x)
while(not pila_vacia(pila)):
    x = desapilar(pila)
    arribo(cola, x)
print('Cola invertida')
while (not cola_vacia(cola)):
    print(atencion(cola))
"""


#******************************************************************************************************************************
#======================================================Ejercicio 3=============================================================
#******************************************************************************************************************************
"""
3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un
palíndromo.
"""

"""
palabra = input('Ingrese una palabra ')
palindromo = False
for i in range(len(palabra)):
    arribo(cola, palabra[i])
while(not cola_vacia(cola)):
    x = atencion(cola)
    apilar(pila, x)
for i in range(len(palabra)):
    arribo(cola, palabra[i])
while(not cola_vacia(cola) and not pila_vacia(pila)):
    c = atencion(cola)
    p = desapilar(pila)
    if (c == p):
        palindromo = True
if (palindromo):
    print('La palabra',palabra,'es palindromo.')
else:
    print('La palabra',palabra,'no es palindromo.')
"""


#******************************************************************************************************************************
#======================================================Ejercicio 4=============================================================
#******************************************************************************************************************************
"""
4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no
sean primos.
"""
"""
es_primo = False
while(tamanio(cola) < 10):
    arribo(cola, randint(1,100))
for i in range(tamanio(cola)):
    x = atencion(cola)
    print(x)
    arribo(cola, x)
for i in range(tamanio(cola)):    
    if (en_frente(cola) < 2):
        mover_final(cola)
    for i in range(2, en_frente(cola)): 
        if en_frente(cola) % i == 0:    
            atencion(cola)
        else:
            mover_final(cola) 
print('Cola sin numeros primos')
print(atencion(cola))
"""

#******************************************************************************************************************************
#======================================================Ejercicio 5=============================================================
#******************************************************************************************************************************
"""
5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.
"""

"""
while (tamanio(pila) < 5):
    apilar(pila, randint(1,20))
print('Pila normal:')
while (not pila_vacia(pila)):
    x = desapilar(pila)
    print(x)
    arribo(cola,x)
while (not cola_vacia(cola)):
    x = atencion(cola)
    apilar(pila, x)
print('Pila invertida:')
while (not pila_vacia(pila)):
    print(desapilar(pila))
"""


#******************************************************************************************************************************
#======================================================Ejercicio 6=============================================================
#******************************************************************************************************************************
"""
6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar
ninguna estructura auxiliar.
"""
""" 
cargar_random(cola)
print('Cola:')
barrido(cola)
num = int(input('Ingrese un elemento a buscar sus ocurrecias: '))
cont = 0
for i in range(tamanio(cola)):
    if (en_frente(cola) == num):
        cont += 1
    mover_final(cola)
print('La cantidad de ocurrecias del numero',num,'es de:',cont)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 7=============================================================
#******************************************************************************************************************************

"""
7. Eliminar el i-ésimo elemento después del frente de la cola.
"""

""" 
cargar_random(cola)
print('Cola original:')
barrido(cola)
elemento = int(input('Ingrese el elemento a eliminar: '))
for i in range(tamanio(cola)):
    if (en_frente(cola) == elemento):
        atencion(cola)
    else:
        mover_final(cola)
print('Cola sin el elemento',elemento,':')
barrido(cola)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 8=============================================================
#******************************************************************************************************************************
"""
8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola,
utilizando solo una cola como estructura auxiliar.
"""

"""
while (tamanio(cola) < 10):
    dato = int(input("Ingrese un número "))
    if(cola_vacia(cola)):
        arribo(cola, dato)
    elif(dato < en_frente(cola)):
        arribo(cola, dato)
        for i in range (1, tamanio(cola)):
            mover_final(cola)
    else:
        cont = 0
        while (en_frente(cola) < dato and cont < tamanio(cola)):
            mover_final(cola)
            cont += 1
        arribo(cola, dato)
        for i in range(cont, tamanio(cola)-1):
            mover_final(cola)
print('Cola ordenada: ')
barrido(cola)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 9=============================================================
#******************************************************************************************************************************
"""
9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos
hay.
"""
"""
cargar_elementos(cola)
minimo = 0
maximo = 0
neg = 0
for i in range(tamanio(cola)):
    if (en_frente(cola) < 0):
        neg += 1
    if (en_frente(cola) > maximo):
        maximo = en_frente(cola)
    if (en_frente(cola) < minimo):
        minimo = en_frente(cola)
    mover_final(cola)
print('Hay',neg,'numeros negativos en la cola.')
print('El rango esta dado entre',minimo,'y',maximo,'.')
"""

#******************************************************************************************************************************
#======================================================Ejercicio 10=============================================================
#******************************************************************************************************************************
"""
10. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y
planeta de origen. Desarrollar las funciones necesarias para resolver las siguientes
actividades:
a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
b. indicar el plantea natal de Luke Skywalker y Han Solo
c. insertar un nuevo personaje antes del maestro Yoda
d. eliminar el personaje ubicado después de Jar Jar Binks
"""
"""
cola_personajes = Cola()
archivo = open('personajes')
linea = archivo.readline()
planetas = 'Alderaan Endor Tatooine'
per = 'Luke Skywalker Han Solo'
while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = linea[1].title()
    arribo(cola_personajes, linea)
    linea = archivo.readline()
print('Personajes que pertenecen a los planetas Alderaan, Endor y Tatooine')
for i in range(tamanio(cola_personajes)):
    if (en_frente(cola_personajes)[1] in planetas):
        print(en_frente(cola_personajes)[0])
    if (en_frente(cola_personajes)[0] in per):
        print('El planeta de',en_frente(cola_personajes)[0],'es',en_frente(cola_personajes)[1])
    mover_final(cola_personajes)
personaje = ['Conde','Serenno']
for i in range(1,tamanio(cola_personajes)):
    if (en_frente(cola_personajes)[0] == 'Yoda'):
        arribo(cola_personajes, personaje)
        mover_final(cola_personajes)
    elif (en_frente(cola_personajes)[0] == 'Jar Jar Binks'):
        mover_final(cola_personajes)
        x = atencion(cola_personajes)
    else:
        mover_final(cola_personajes)
print('Cola modificada')
barrido(cola_personajes)
"""
#******************************************************************************************************************************
#======================================================Ejercicio 11=============================================================
#******************************************************************************************************************************
"""
11. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en
una nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura
auxiliar, ni métodos de ordenamiento.
"""

""" 
cola1 = Cola()
cola2 = Cola()
print('cargar cola 1')
while tamanio(cola1)<5:
    dato = int(input("ingrese un número"))
    arribo(cola1, dato)
print('cargar cola 2')
while tamanio(cola2)<7:
    dato = int(input("ingrese un número"))
    arribo(cola2, dato)
cant = tamanio(cola1)
for i in range (0, cant):
    if(en_frente(cola1)< en_frente(cola2)):
        mover_final(cola1)
    else:
        while(en_frente(cola1)>en_frente(cola2)):
            dato = atencion(cola2)
            arribo(cola1, dato)
        mover_final(cola1)
while(not cola_vacia(cola2)):
    dato = atencion(cola2)
    arribo(cola1, dato)
for i in range(0, tamanio(cola1)):
    print(mover_final(cola1))
"""

#******************************************************************************************************************************
#======================================================Ejercicio 12=============================================================
#******************************************************************************************************************************
"""
12. Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes
actividades:
a. separarla en dos colas una con dígitos y otra con el resto de los caracteres.
b. determinar cuántas letras hay en la segunda cola.
c. determinar además si existen los caracteres “?” y “#”.
"""

"""
cola_digitos = Cola()
cola_caracter = Cola()
num = '1234567890'
abc = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cont = 0
preg, nume = False, False
while (tamanio(cola) < 10):
    elemento = input('Ingrese el caracter: ')
    arribo(cola, elemento)
while (not cola_vacia(cola)):
    x = atencion(cola)
    if (x in num):
        arribo(cola_digitos, x)
    else:
        arribo(cola_caracter, x)
    if (x in abc):
        cont += 1
    if (x == '?'):
        preg = True
    if (x == '#'):
        nume = True
print('Cola digitos')
barrido(cola_digitos)
print('Cola caracteres')
barrido(cola_caracter)
print('Hay',cont,'letras en la cola de caracteres')
if preg:
    print('Existe el caracter "?" en la cola')
else:
    print('No existe el caracter "?" en la cola')
if nume:
    print('Existe el caracter "#" en la cola')
else:
    print('No existe el caracter "#" en la cola')
"""

#******************************************************************************************************************************
#======================================================Ejercicio 13=============================================================
#******************************************************************************************************************************
"""
13. Realizar un algoritmo que permita realizar las siguientes funciones:
a. cargar semáforos de una rotonda y sus respectivos tiempos de encendido en
verde –cargue al menos tres semáforos–.
b. simular el funcionamiento de los semáforos cargados (cola circular).
c. debe mostrar por pantalla el cambio de colores y el número del semáforo.
"""

#******************************************************************************************************************************
#======================================================Ejercicio 14=============================================================
#******************************************************************************************************************************
"""
14. Suponga que se escapa hacia el planeta tierra en un Caza TIE robado –huyendo de un
Destructor Estelar y necesita localizar la base rebelde más cercana– y se tiene una cola
con información de las bases rebeldes en la tierra de las cuales conoce su nombre, número
de flota aérea, coordenadas de latitud y longitud. Desarrolle un algoritmo que permita
resolver las siguientes tareas una vez que aterrice:
a. determinar cuál es la base rebelde más cercana desde su posición actual.
b. para el cálculo de la distancia deberá utilizar la fórmula de Haversine:
donde r es el radio medio de la tierra en metros (6371000), φ1 y φ2 las latitudes
de los dos puntos –por ejemplo coordenadas actual–, λ1 y λ2 las longitudes de los
dos puntos –coordenadas de la base– ambos expresadas en radianes; para
convertir de grados a radianes utilice la función math.radians(ángulo coordenada).
c. mostrar el nombre y la distancia a la que se encuentran las tres bases más
cercanas y determinar cual tiene mayor flota aérea.
d. determinar la distancia hasta la base rebelde con mayor flota aérea.
"""

"""
archivo = open('bases rebeldes')
linea = archivo.readline()
Bases_rebeldes = Cola()
latitud = float(input('Ingrese la latitud desde su punto actual: '))
longitud = float(input('Ingrese la longitud desde su punto actual: '))
punto_actual = [latitud, longitud]
base = ['',0,0,0]
base2 = ['',0,0,0]
mayor_flota = 0
while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = int(linea[1])
    linea[2] = float(linea[2])
    linea[3] = float(linea[3])
    arribo(Bases_rebeldes, linea)
    linea = archivo.readline()
for i in range(tamanio(Bases_rebeldes)):
    lat = en_frente(Bases_rebeldes)[2]
    lon = en_frente(Bases_rebeldes)[3]
    puntox = [lat, lon]
    punto_actual = (radians(punto_actual[0]), radians(punto_actual[1]))
    puntox = (radians(puntox[0]), radians(puntox[1]))
    distancia = acos(sin(punto_actual[0])*sin(puntox[0]) + cos(punto_actual[0])*cos(puntox[0])*cos(punto_actual[1] - puntox[1]))
    distancia * 6371.01
    if(i == 0):
        menor_distancia = distancia
        base = en_frente(Bases_rebeldes)
    elif(distancia < menor_distancia):
        menor_distancia = distancia
        base = en_frente(Bases_rebeldes)
    if (mayor_flota < en_frente(Bases_rebeldes)[1]):
        mayor_flota = en_frente(Bases_rebeldes)[1]
        base2 = en_frente(Bases_rebeldes)
    mover_final(Bases_rebeldes)
lati = base2[2]
longi = base2[3]
punto_x = [lati, longi]
puntox = (radians(punto_x[0]), radians(punto_x[1]))
distancia1 = acos(sin(punto_actual[0])*sin(punto_x[0]) + cos(punto_actual[0])*cos(punto_x[0])*cos(punto_actual[1] - punto_x[1]))
distancia1 * 6371.01
print('La base rebelde mas cercana es desde su punto actual es',base[0],'con latitud',base[2], 'y con longitud',base[3])
print('La base rebelde con la mayor flota es',base2[0],'con',base2[1],'flota')
print('La distancia entre el punto actual y la base con mayor flota es de',distancia1)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 15=============================================================
#******************************************************************************************************************************
"""
15. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y
resuelva la siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente
con un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este
por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión.
"""
"""
nombreyap = ''
doc = 0
cat = ''
while (tamanio(cola) < 7):
    cat = input("Ingrese su categoria (empleados, staff TI, gerente): ")
    print("Por prioridad se cargan primero todos los empleados, luego el staff TI y por ultimo gerentes")
    while (cat == "empleado" and tamanio(cola) < 7):
        nombreyap = input("Ingrese su nombre y apellido: ")
        doc = int(input("Ingrese su numero de documento (sin puntos): "))
        dato = [nombreyap, doc, cat]
        arribo(cola, dato)
        cat = input("Ingrese su categoria (empleados, staff TI, gerente): ")
        if(cat != "empleado"):
            op = print('Seguro que no quiere cargar mas empleados? S/N')
            if (op == "N"):
                cat = input("Ingrese su categoria (empleados, staff TI, gerente): ")    
    while (cat == "staff TI" and tamanio(cola) < 7):
        nombreyap = input("Ingrese su nombre y apellido: ")
        doc = int(input("Ingrese su numero de documento (sin puntos): "))
        dato = [nombreyap, doc, cat]
        arribo(cola, dato)
        cat = input("Ingrese su categoria (empleados, staff TI, gerente): ")
        if(cat != "staff TI"):
            op = print('Seguro que no quiere cargar mas staff TI? S/N')
            if (op == "N"):
                cat = input("Ingrese su categoria (empleados, staff TI, gerente): ")
            
    while (cat == "gerente" and tamanio(cola) < 7):
        nombreyap = input("Ingrese su nombre y apellido: ")
        doc = int(input("Ingrese su numero de documento (sin puntos): "))
        dato = [nombreyap, doc, cat]
        arribo(cola, dato)
        cat = input("Ingrese su categoria (empleados, staff TI, gerente): ")
        if(cat != "gerente"):
            op = print('Seguro que no quiere cargar mas gerentes? S/N')
            if (op == "N"):
                cat = input("Ingrese su categoria (empleados, staff TI, gerente): ")
print('Primer documento de la cola',en_frente(cola)[0,1])
print('Los dos primeros documentos de la cola son ')
for i in range(0, tamanio(cola)):
    if (i == 0 or i == 1):
        print(en_frente(cola)[2])
    mover_final(cola)
print('Todos los docuemento de la cola: ')
for i in range(0, tamanio(cola)):
    print(en_frente(cola)[2])
    mover_final(cola)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 16=============================================================
#******************************************************************************************************************************
"""
16. Desarrollar un algoritmo que permita cargar procesos a la cola de ejecución de un
procesador, de los cuales se conoce id del proceso y tiempo de ejecución. Resuelva las
siguientes situaciones:
a. simular la atención de los procesos de la cola transcurriendo su tiempo –utilizando
la función time.sleep (segundos) – hasta que se vacíe la cola.
b. considerar que el quantum de tiempo asignado por el procesador a cada proceso
es como máximo 4.5 segundos –si el proceso no terminó su ejecución deberá
volver a la cola con el tiempo restante para terminar su ejecución–.
c. cuando se realiza el cambio de proceso, porque finalizó su ejecución o porque se
le agotó el quantum de tiempo, se pueden ingresar nuevos procesos a la cola por
el usuario.
d. no se aplican criterios de prioridad en los procesos.
"""

"""
arribo(cola, [1, 10])
arribo(cola, [2, 3])
arribo(cola, [4, 5])
while not cola_vacia(cola):
    dato = atencion(cola)
    print('Atendiendo proceso', dato[0])
    if(dato[1]>4.5):
        dato[1] = dato[1] - 4.5
        sleep(4.5)
        arribo(cola, dato)
    else:
        sleep(dato[1])
    resp = input('Quiere cargar un nuevo proceso S/N? ')
    if(resp.upper() == 'S'):
        tiempo = float(input('Ingrese tiempo del proceso '))
        arribo(cola,[randint(1, 500), tiempo])
"""

#******************************************************************************************************************************
#======================================================Ejercicio 17=============================================================
#******************************************************************************************************************************
"""
17. Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es
una letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un
algoritmo que resuelva las siguientes situaciones:
a. cargar 1000 turnos de manera aleatoria a la cola.
b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la
letra A, C y F, y la cola_2 con el resto de los turnos (B, D y E).
c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las
letras tiene mayor cantidad.
d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de
turno sea mayor que 506.
"""
"""
cola_1 = Cola()
cola_2 = Cola()
letrascola1 = ["A","C","F"]
turno1 = 0
turno2 = 0
while (tamanio(cola) < 30):
    letra = chr(randint(65, 70))
    turno = randint(000,999)
    dato = [letra, turno]
    arribo(cola, dato)
print("Cola")
barrido(cola)
for i in range(0,tamanio(cola)):
    if (en_frente(cola)[0] in letrascola1):
        arribo(cola_1, en_frente(cola))
        turno1 += 1
    else:
        arribo(cola_2, en_frente(cola))
        turno2 += 1
    mover_final(cola)
print("Cola con mayor cantidad de turnos")
if turno1 > turno2:
    barrido(cola_1)
    print("Turnos de la cola con menor cantidad de elementos, cuyo turno es menor de 505")
    for i in range(0, tamanio(cola_2)):
        if (en_frente(cola_2)[1] < 505):
            print(en_frente(cola_2))
        mover_final(cola_2)
else:
    barrido(cola_2)
    print("Turnos de la cola con menor cantidad de elementos, cuyo turno es menor de 505")
    for i in range(0, tamanio(cola_1)):
        if (en_frente(cola_1)[1] < 505):
            print(en_frente(cola_1))
        mover_final(cola_1)
"""

#******************************************************************************************************************************
#======================================================Ejercicio 18=============================================================
#******************************************************************************************************************************
"""
18. Modificar las funciones de arribo y atención del TDA cola para adaptarlo a una cola
circular, que no necesite la función mover al final; y desarrollar un función que permita
realizar un barrido de dicha estructura respetando el principio de funcionamiento de la
cola.
"""
#******************************************************************************************************************************
#======================================================Ejercicio 19=============================================================
#******************************************************************************************************************************
"""
19. Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de
cobro), que resuelva las siguientes actividades:
a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de
vehículos son los siguientes:
i. automóviles (tarifa $47);
ii. camionetas (tarifa $59);
iii. camiones (tarifa $71);
iv. colectivos (tarifa $64).
b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
c. determinar qué cabina recaudó mayor cantidad de pesos ($).
d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.
"""

"""
vehiculos = ['auto', 'camioneta', 'camion', 'colectivo']
costo = [47, 59, 71, 64]
puesto1 = Cola()
puesto2 = Cola()
puesto3 = Cola()
cantidad1  = [0, 0, 0, 0]
cantidad2  = [0, 0, 0, 0]
cantidad3  = [0, 0, 0, 0]
total1 = 0
total2 = 0
total3 = 0
for i in range (30):
    arribo(puesto1, (choice(vehiculos)))
    arribo(puesto2, (choice(vehiculos)))
    arribo(puesto3, (choice(vehiculos)))
while (not cola_vacia(puesto1)):
    vehiculo = atencion(puesto1)
    pos = vehiculos.index(vehiculo)
    total1 += costo[pos]
    cantidad2[pos] += 1
while(not cola_vacia(puesto2)):
    vehiculo = atencion(puesto2)
    pos = vehiculos.index(vehiculo)
    total2 += costo[pos]
    cantidad3[pos] += 1
while(not cola_vacia(puesto3)):
    vehiculo = atencion(puesto3)
    pos = vehiculos.index(vehiculo)
    total3 += costo[pos]
    cantidad1[pos] += 1
if ((total1 > total2) and (total1 > total3)):
    print("La cabina que recaudo mas dinero es la cabina 1")
elif (total2 > total3):
    print("La cabina que recaudo mas dinero es la cabina 2")
else:
    print("La cabina que recaudo mas dinero es la cabina 3")
print("En la cabina 1 se atendieron",cantidad1[0],"autos,",cantidad1[1],"camionetas,",cantidad1[2],"camiones y",cantidad1[3],"colectivos.")
print("En la cabina 2 se atendieron",cantidad2[0],"autos,",cantidad2[1],"camionetas,",cantidad2[2],"camiones y",cantidad2[3],"colectivos.")
print("En la cabina 3 se atendieron",cantidad3[0],"autos,",cantidad3[1],"camionetas,",cantidad3[2],"camiones y",cantidad3[3],"colectivos.")
"""

#******************************************************************************************************************************
#======================================================Ejercicio 20=============================================================
#******************************************************************************************************************************
"""
20. Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un
aeropuerto que tiene una pista, contemplando las siguientes actividades:
a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada,
aeropuerto de origen, aeropuerto de destino y su tipo (pasajeros, negocios o
carga).
b. utilizar una cola para administrar los despegues, se deben cargan ordenados por
horario de salida. Otra para los aterrizajes, se deben agregan a medida que arriban
al aeropuerto.
c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o
despegue.
d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas
colas después de realizar una atención.
e. se debe atender siempre que se pueda a los elementos de la cola de aterrizaje –
dado que son aviones que están sobrevolando en la zona de espera–, salvo que
sea el horario de salida del primer avión de la cola de despegue, en ese caso se
deberá atender dicho despegue.
f. cada tipo de avión tiene su tiempo de uso de la pista para la maniobra de
despegue y aterrizaje –adaptados a segundo para los fines prácticos del ejercicio–:
i. pasajeros (aterrizaje = 10 segundos, despegue = 5 segundos);
ii. negocios (aterrizaje = 5 segundos, despegue = 3 segundos);
iii. carga (aterrizaje = 12 segundos, despegue = 9 segundos).
g. se debe poder cancelar vuelos de despegue y poder reprogramar un vuelo para
más tarde cuando se lo atiende para despegar (en esta caso el horario de salida
será mayor que el último de la cola).
"""

"""
tipos_aviones = ['carga', 'negocios', 'pasajeros']
tiempo_despegue = [9, 3, 5]
tiempo_aterrizaje = [12, 5, 10]
cola_despegue = Cola()
cola_aterrizaje = Cola()
arribo(cola_despegue, ['airline', 'argentina', 'chile', 'carga', '07:00', '23:00'])
arribo(cola_despegue, ['airline', 'argentina', 'india', 'pasajeros', '07:10', '23:00'])
arribo(cola_despegue, ['airline', 'argentina', 'rusia', 'negocios', '07:17', '23:00'])
arribo(cola_aterrizaje, ['airline', 'argentina', 'rusia', 'negocios', '07:00', '23:00'])
hora_actual = datetime.now()
while(not cola_vacia(cola_despegue) or not cola_vacia(cola_aterrizaje)):
    hora_despegue = copy(hora_actual)
    hora_despegue.hour = int(en_frente(cola_despegue)[4][0:2])
    hora_despegue.min =int(en_frente(cola_despegue)[4][3:])
    if(not cola_vacia(cola_aterrizaje) and hora_despegue<= hora_actual):
        avion = atencion(cola_aterrizaje)
        pos = tipos_aviones.index(avion[3])
        tiempo = tiempo_aterrizaje[pos]
        print('avion aterrizando...')
        sleep(tiempo)
    else:
        avion = atencion(cola_despegue)
        pos = tipos_aviones.index(avion[3])
        tiempo = tiempo_despegue[pos]
        print('avion despegando...')
        sleep(tiempo)
hora_actual = datetime().now()
si_no = str(input("Desea seguir ingresando vuelos?  -si/no-: "))
if (si_no == "si"):
    tip = str(input("Ingrese el tipo de vuelo.  -despegue/aterrizaje-: "))
    if (tip == "despegue"):
        i = str(input("Ingrese el nombre de la aerolínea: "))
        j = str(input("Ingrese el aeropuerto de origen: "))
        k = str(input("Ingrese el aeropuerto de destino: "))
        l = (choice(tipos_aviones))
        pos = tipos_aviones.index(l)
        m = tiempo_despegue[pos]
        n = tiempo_aterrizaje[pos]
        dato = [i,j,k,l,m,n]
        arribo(cola_despegue,dato)
        print()
    elif (tip == "aterrizaje"):
        i = str(input("Ingrese el nombre de la aerolínea: "))
        j = str(input("Ingrese el aeropuerto de origen: "))
        k = str(input("Ingrese el aeropuerto de destino: "))
        l = (choice(tipos_aviones))
        pos = tipos_aviones.index(l)
        m = tiempo_despegue[pos]
        n = tiempo_aterrizaje[pos]
        dato = [i,j,k,l,m,n]
        arribo(cola_aterrizaje,dato)
        print()
"""

#******************************************************************************************************************************
#======================================================Ejercicio 21=============================================================
#******************************************************************************************************************************
"""
21. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se
conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y
Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M},
{Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las
siguientes actividades:
a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su
nombre de superhéroes.
"""
"""
aux = False
per = ""
archivo = open('personajes_marvel')
linea = archivo.readline()
while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = linea[1].title()
    linea[2] = linea[2].title()
    arribo(cola, linea)
    linea = archivo.readline()
for i in range(0,tamanio(cola)):
    if (en_frente(cola)[1] == "Capitana Marvel"):
        print("El nombre real de la actriz que hace el papel de Capitana Marvel es", en_frente(cola)[0])
    if (en_frente(cola)[0] == "Scott Lang"):
        print("El nombre del superheroe de Scott Lang es",en_frente(cola)[1])
    if(en_frente(cola)[0] == "Carol Danvers"):
        aux = True
        per = en_frente(cola)[1]
    mover_final(cola)
print("Nombre de los personajes femeninos:")
for i in range(0,tamanio(cola)):
    if (en_frente(cola)[2] == "F"): 
        print(en_frente(cola)[1])
    mover_final(cola)
print("Nombre de los superheroes masculinos:")
for i in range(0,tamanio(cola)):
    if (en_frente(cola)[2] == "M"): 
        print(en_frente(cola)[0])
    mover_final(cola)
if aux:
    print("El personaje Carol Danvers se encuentra en la cola y el nombre de su superheroe es",per)
else:
    print("El personaje Carol Danvers no se encuentra en la cola")
"""