from tda_tabla_hash import crear_tabla, agregar_ta, agregar_tc, quitar_ta, quitar_tc, buscar_tc, buscar_ta,cantidad_ta, cantidad_tc, hash_division, hash_diccionario,bernstein,barrido_ta,barrido_tc,hash_guia_division, hash_catedra_division, bernstein_contactos,hash_troopers_division, bernstein_SW, bernstein_pokemones, bernstein_palabra,hash_pokemon_division,bernstein_catedra,bernstein_troopers,desifrar,hash_cifrado
from tda_lista_lista import Lista,insertar,eliminar,tamanio,busqueda,barrido
from random import randint, choice
from math import sqrt

# ******************************************************************************************************************************#
# ====================================================== Ejercicio 1 ===========================================================#
# ******************************************************************************************************************************#
"""
1. Desarrollar un algoritmo que permita implementar una tabla hash para representar un
diccionario que permita resolver las siguientes actividades:
a. agregar una palabra y su significado al diccionario;
b. determinar si una palabra existe y mostrar su significado;
c. borrar una palabra del diccionario;
d. la tabla debe tener 28 posiciones y manejar las colisiones con lista enlazadas;
e. mejorar el rendimiento de la tabla utilizando árboles binarios de búsqueda.
"""
class Palabra(object):
    def __init__(self,palabra,significado):
        self.palabra = palabra
        self.significado = significado
    def __str__(self):
    
        return '= ' + self.palabra + ': ' + self.significado

def diccionario():
    tabla = crear_tabla(28)
    # A
    dato = Palabra('Agua', 'Sustancia líquida sin olor, color ni sabor que se encuentra en la naturaleza en estado más o menos puro formando ríos, lagos y mares')
    agregar_ta(tabla, hash_diccionario, dato, 'palabra')
    dato = Palabra('Telefono', 'Sistema de comunicación que transmite la voz y el sonido a larga distancia por medios eléctricos o electromagnéticos.')
    agregar_ta(tabla, hash_diccionario, dato, 'palabra')
    dato = Palabra('Plato', 'Recipiente de forma circular, plano, ligeramente cóncavo en el centro, que forma parte del servicio de mesa y sirve para poner en él una ración individual de alimento.')
    agregar_ta(tabla, hash_diccionario, dato, 'palabra')
    dato = Palabra('Pasto','Hierba que come el ganado en el campo.')
    agregar_ta(tabla,hash_diccionario,dato,'palabra')
    print('Diccionario:')
    barrido_ta(tabla)
    print()
    # B
    pos = buscar_ta(tabla, hash_diccionario, Palabra('Agua',''), 'palabra')
    if pos is not None:
        print('La palabra existe \n', pos.info)
    else:
        print('La palabra no fue encontrada.')
    # C
    pos = buscar_ta(tabla, hash_diccionario, Palabra('Telefono',''), 'palabra')
    if pos is not None:
        print('La palabra '+ pos.info.palabra + ' ha sido eliiminada.')
        quitar_ta(tabla, hash_diccionario, Palabra('Telefono',''), 'palabra')
    else:
        print('La palabra no fue encontrada.')
    print()
    print('Lista con las palabras: ')
    barrido_ta(tabla)
"""
 print(diccionario())
"""
# ******************************************************************************************************************************#
# ====================================================== Ejercicio 2 ===========================================================#
# ******************************************************************************************************************************#
"""
2. Desarrollar un algoritmo que implemente una tabla hash para una guía de teléfono, los
datos que se conocen son número de teléfono, apellido, nombre y dirección de la persona.
El campo clave debe ser el número de teléfono.
"""

class Guia_de_telefono(object):
    def __init__(self, numero, apellido, nombre, direccion):
        self.numero = numero
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return "== " +self.apellido + " " + self.nombre + " == " + " \n- Numero de telefono: " + str(self.numero) + "\n- Domicilio: " + self.direccion

def guia_telefonica():
    guia = crear_tabla(20)
    dato = Guia_de_telefono(3446379368, 'Bidegain', 'Tomas', 'Vicoer de rioja 445')
    agregar_ta(guia, hash_guia_division, dato, 'numero')
    dato = Guia_de_telefono(3446845469, 'Greissing', 'Antonella', 'Gervasio Mendez 572')
    agregar_ta(guia, hash_guia_division, dato, 'numero')
    dato = Guia_de_telefono(3442845121, 'Bos', 'Esteban', 'Andrade 1500')
    agregar_ta(guia, hash_guia_division, dato, 'numero')
    dato = Guia_de_telefono(3446152462, 'Rebora', 'Marta', 'Gervasio Mendez 345')
    agregar_ta(guia, hash_guia_division, dato, 'numero')
    dato = Guia_de_telefono(3442451512, 'Euler', 'Franco', 'Clavarino 1844')
    agregar_ta(guia, hash_guia_division, dato, 'numero')
    print('Guia telefonica:')
    barrido_ta(guia)
    print()
"""
print(guia_telefonica())
"""
# ******************************************************************************************************************************#
# ====================================================== Ejercicio 3 ===========================================================#
# ******************************************************************************************************************************#
"""
3. Implementar un tabla hash cerrada para guardar las cátedras de una carrera universitaria
de acuerdo a su código, que permita resolver las siguientes actividades:
a. cargar cátedras de una carrera de las cuales se conoce nombre, modalidad (anual
o cuatrimestral), cantidad de horas;
b. además se deben poder agregar los docentes vinculados con las cátedras;
c. debe ser una tabla cerrada;
d. debe poder solucionar las colisiones;
e. no podrán estar cargadas de manera correlativa de acuerdo a un número.
"""

class Catedras(object):
    def __init__(self,codigo,nombre,modalidad,cant_horas,docente):
        self.codigo = codigo
        self.nombre = nombre
        self.modalidad = modalidad
        self.cant_horas = cant_horas
        self.docente = docente
    def __str__(self):
        return '* Codigo de la catedra: ' +str(self.codigo) + '\n-Nombre de la materia: ' + self.nombre + ', La materia es ' + self.modalidad + '\n- Cant. de horas: ' + str(self.cant_horas) + '\n- Docente: ' + self.docente

def universidad():
    cated = crear_tabla(30)
    materias = ['Algorimtos y Estr. de Datos','Calculo diferncial e integral','Ingenieria de software','Algebra','Fundamentos de programacion']
    modalidad = ['Anual', 'Cuatrimestral']
    profesores = ['Lic. Bidegain', 'Prof. Martinez', 'Lic. Greissing', 'Prof. Rebora','Ing. Sosa']
    hora_anual = [80,90,100,120,140,160,190]
    hora_cua = [30,40,50,60]
    for i in range(len(materias)):
        nom = materias[i]
        mod = choice(modalidad)
        if mod =='Anual':
            horas = choice(hora_anual)
        else:
            horas = choice(hora_cua)
        catedra = Catedras((nom[0:3]+str(randint(1100, 10000))),nom, mod, horas, profesores[i])
        agregar_tc(cated, bernstein_catedra, catedra)
    print('== Catedras == ')
    barrido_tc(cated)

"""
print(universidad())
"""

# ******************************************************************************************************************************#
# ====================================================== Ejercicio 4 ===========================================================#
# ******************************************************************************************************************************#

"""
4. Desarrollar un algoritmo que implemente una tabla hash cerrada para cargar personajes
de Star Wars de los que solo se conoce su nombre, contemplando las siguientes
actividades:
a. la tabla inicialmente será de 20 posiciones;
b. deberá permitir el manejo de colisiones;
c. cuando el factor de carga de la tabla exceda el 75%, se deberá incrementar el
tamaño de la tabla al doble y hacer un rehashing de las claves cargadas.
"""

class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "-Nombre del personaje: "+ self.nombre

def personajes():
    nombres = ['Maestro Yoda','R2D2','Obi-Wan Keobi','Han Solo','Beru Lars','Leia Organa','Chewbacca','Poe Dameron','Luke Skywalker','Darth Vader']
    personajes = crear_tabla(10)
    for i in range(len(nombres)):
        dato = Personaje(nombres[i])
        agregar_tc(personajes, bernstein_SW, dato)
        porc_tabla = (cantidad_tc(personajes)*100)/len(personajes)
        if porc_tabla > 75:
            print('75% de espacio ocupado en la tabla.')
            print('Realizando un rehashing')
            tabla_aux = crear_tabla(len(personajes)*2)
            for dato in personajes:
                if dato is not None:
                    agregar_tc(tabla_aux, bernstein_SW, dato)
            print('Datos de la nueva tabla')
            barrido_tc(tabla_aux)
            porc_tabla_aux = (cantidad_tc(tabla_aux)*100)/len(tabla_aux)
            print('Porcentaje de espacio ocupado en tabla: ' + str(porc_tabla_aux))
    print()
    print('Tabla modificada')
    barrido_tc(tabla_aux)
    print('El tamaño es : ' + str(cantidad_tc(personajes)))
"""
print(personajes())
"""

# ******************************************************************************************************************************#
# ====================================================== Ejercicio 5 ===========================================================#
# ******************************************************************************************************************************#
"""
5. Desarrollar un algoritmo que implemente una tabla hash cerrada para administrar los
contactos de personas de las cuales se conoce nombre, apellido y correo electrónico,
contemplando las siguientes pautas:
a. El campo clave para generar las posiciones son el apellido y nombre.
b. Deberá contemplar una función de sondeo para resolver las colisiones.
"""

class Contacto(object):
    def __init__ (self, apellido, nombre, correo):
        self.apellido = apellido
        self.nombre = nombre
        self.correo = correo
    
    def __str__ (self):
        return '== ' + self.apellido + " " + self.nombre +" ==" "\n- Direccion de correo electronico: " + self.correo

def contactos():    
    contac = crear_tabla(20)
    dato = Contacto('Bidegain','Tomas','tomasbidegain8888@gmail.com')
    agregar_tc(contac, bernstein_contactos, dato)
    dato = Contacto('Greissing','Antonella','greissingantonella12@hotmail.com')
    agregar_tc(contac, bernstein_contactos, dato)
    dato = Contacto('Lopez','Hugo','hugo_lopezz@gmail.com')
    agregar_tc(contac, bernstein_contactos, dato)
    dato = Contacto('Fernandez', 'Gustavo', 'guti_latromba@hotmail.com')
    agregar_tc(contac, bernstein_contactos, dato)
    dato = Contacto('Rebora', 'Marta', 'reboraMarta_12@gmail.com')
    agregar_tc(contac, bernstein_contactos, dato)
    print('==== Contactos ====')
    barrido_tc(contac)
"""
print(contactos())
"""
# ******************************************************************************************************************************#
# ====================================================== Ejercicio 6 ===========================================================#
# ******************************************************************************************************************************#

"""
6. Los Stormtrooper del imperio galáctico se identifican de la siguiente manera:

Darth Vader le encarga desarrollar los algoritmos para organizar los Stormtrooper
cumpliendo con las siguientes demandas:
a. Deberá generar 2000 Stormtrooper siguiendo el formato de la imagen anterior
contemplando las siguientes legiones FL, TF, TK, CT, FN, FO y los dígitos generados
de manera aleatoria;
b. deberá cargar los Stormtrooper generados en dos tablas hash encadenadas, en la
primera se deberá agrupar de acuerdo a los tres últimos dígitos del código y en la
segunda a partir de las iniciales de la legión;
c. ahora obtenga todos los Stormtrooper terminados en 781 para asignarlos a una
misión de asalto y a los terminados en 537 para una misión de exploración;
d. ahora obtenga los Stormtrooper de la legión CT para que custodien a Darth Vader
a una misión de exploración al planeta Hoth y los de la legión TF para una misión
de exterminación a Endor.
"""

class StormTrooper():
    def __init__(self,legion,codigo):
        self.legion = legion
        self.codigo = codigo
    def __str__(self):
        return '-Legion: ' + self.legion + '  -Codigo: ' + str(self.codigo)

def stormt():
    legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
    t_legion = crear_tabla(20)
    t_codigo = crear_tabla(1000)
    # A
    for i in range(20):
        legion = choice(legiones)
        codigo = randint(10000, 99999)
        trooper = StormTrooper(legion, codigo)
        agregar_ta(t_legion, bernstein_troopers, trooper, 'legion')
        agregar_ta(t_codigo, hash_troopers_division, trooper, 'codigo')
    # B
    print('====  Troopers por legion  ====')
    barrido_ta(t_legion)
    print()
    print('==== Troopers por código  ====')
    barrido_ta(t_codigo)
    print()
    # C
    posc = hash_division(537, t_codigo)
    if t_codigo[posc]:
        print('====  Trooper para misión de exploración  ====')
        barrido_lista(t_codigo[posc])
    print()
    posc = hash_division(781, t_codigo)
    if t_codigo[posc]:
        print('====  Trooper para misión de asalto  ====')
        barrido_lista(t_codigo[posc])
    print()
    # D
    posl = bernstein('FN', t_legion)
    if t_legion[posl]:
        print('====  Legión FN  ====' )
        barrido(t_legion[posl])
    print()
    posl = bernstein('CT', t_legion)
    if t_legion[posl]:
        print('====  Legión CT  ====')
        barrido(t_legion[posl])
"""
print(stormt())
"""

# ******************************************************************************************************************************#
# ====================================================== Ejercicio 7 ===========================================================#
# ******************************************************************************************************************************#

"""
7. Escribir un algoritmo que permita utilizar una tabla hash doble para guardar los datos de
Pokémons, que contemple las siguientes actividades:
a. la primera tabla hash debe ser cerrada y la función hash debe ser sobre el tipo de
Pokémon, con lo cual se obtendrá el acceso a la segunda tabla;
b. cada segunda tabla debe ser encadenada utilizando listas enlazadas y la función
hash deberá utilizar el número del Pokémon como clave;
c. el tamaño de la primera tabla debe ser lo suficientemente grande como para que
pueda almacenar todos los distintos tipos de Pokémon, debe manejar las
colisiones con alguna función de sondeo;
d. el tamaño de cada una de las segundas tablas debe ser 15;
e. el algoritmo debe permitir cargar tipos de Pokémon en la primera tabla y crear su
respectiva segunda tabla, –en el caso de que no exista–;
f. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que
indiquen estos tipos;
g. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre,
tipo, nivel.
"""

class Pokemon():
    def __init__(self, numero, nombre, tipo, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
    def __str__(self):
        return str(self.numero) + ' | Pokemon: ' + self.nombre + ' | Tipo: ' + self.tipo + ' | Nivel: ' + str(self.nivel)
nombres = ['Bulbasaur','Charmander','Squirtle','Pelliper','Cyndaquil','Jigglypuff','Caterpie','Eevee','Pikachu', 'Spearow','Hitmonlee','Mewtwo','Articuno','Dugtrio','Primeape','Terrakion']
tipos = ['Planta','Fuego','Agua','Agua','Fuego','Normal','Bicho','Normal','Eléctrico','Volador', 'Lucha','Psiquico','Hielo','Tierra','Lucha','Roca']

def tabla_pokemon():
    tabla_c = crear_tabla(50) 
    tabla_a = crear_tabla(20) 
    for i in range(len(nombres)):
        nom = nombres[i]
        tipo = tipos[i]
        pokemon = Pokemon(randint(100, 999), nom, tipo, randint(1, 50))
        agregar_tc(tabla_c, bernstein_pokemones, pokemon)
    print()
    print('Tabla Pokemon Hash Por Tipo: ')
    barrido_tc(tabla_c)
    print('tamaño = '+ str(cantidad_tc(tabla_c)))
    for i in range(len(tabla_c)):
        if tabla_c[i] != None:
            dato = tabla_c[i]
            agregar_ta(tabla_a,hash_pokemon_division,dato,'numero')
    print()
    print('Tabla Pokemon Hash Por Numero: ')
    barrido_ta(tabla_a)
    print('tamaño = '+ str(cantidad_ta(tabla_a)))
"""
print(tabla_pokemon())
"""
# ******************************************************************************************************************************#
# ====================================================== Ejercicio 8 ===========================================================#
# ******************************************************************************************************************************#

"""
8. La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico
interviene todas la comunicaciones, por lo que la princesa Leia nos encarga el desarrollo
de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los
siguientes requerimientos:
a. cada carácter deberá ser encriptado a ocho caracteres;
b. se deberá generar dos tablas hash para encriptar y desencriptar, para los
caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.
"""
def encriptar(oracion):
    clave = ""
    for letra in oracion:
        parte1 = str(ord(letra)*37)
        parte2 = hex(ord(letra)*2)
        clave += parte1[0] + parte2[1] + parte2[3] + parte1[1] + parte1[2] + parte2[0] + parte1[3] + parte2[2]
    return clave
def desencriptar(clave):
    oracion = ""
    while len(clave) > 0:
        caracter = ""
        caracter += clave[0] + clave[3] + clave[4] + clave[6]
        clave = clave[8:]
        caracter = int(caracter)
        caracter = int(caracter/37)
        caracter = chr(caracter)
        oracion += caracter
    return oracion
def ej_8():
    tabla1: crear_tabla(10000)
    msj = input('Ingrese una palabra para encriptar: ')
    msj_encrip = encriptar(msj)
    print('====  Palabra encriptada  ====')
    print(msj_encrip)
    msj_desenc = desencriptar(msj_encrip)
    print('==== Palabra desencriptada  ====')
    print(msj_desenc)
"""
print(ej_8())
"""
# ******************************************************************************************************************************#
# ====================================================== Ejercicio 9 ===========================================================#
# ******************************************************************************************************************************#
"""
9. Desarrollar un algoritmo que permita cifrar y descifrar un mensaje carácter a carácter,
contemplando las siguientes pautas:
a. Se debe utilizar una tabla hash para guardar los valores de codificación y
decodificación respectivamente que se vayan utilizando.
b. Se deberá cifrar de la siguiente manera: primero, convertir al valor numérico
correspondiente de la tabla ASCII cada carácter y luego, cada número de dicho
valor se deberá remplazar por su valor correspondiente según los siguientes
valores: 1 – “abd”, 2 – “def”, 3 – “ghi”, 4 –“ jkl”, 5 –“mnñ”, 6 – “opq”, 7 – “rst”, 8 –
“uvw”, 9 – “xyz”, 0 – “#?&”, y se debe agregar al final el carácter %. Por ejemplo D
= 68 debería quedar de la siguiente manera “opquvw%”.
"""

def cifrar(dato):
    valor = str(ord(dato))
    valor_cirado = ["#?&","abc","def","ghi","jkl","mnñ","opq","rst","uvw","xyz"]
    cadena = ""
    for num in valor:
        numInt = int(num)
        cadena += valor_cirado[numInt]
    cadena += "%"
    return cadena
    
"""
tabla = crear_tabla(10)
tabla2 = crear_tabla(10)
a = 'Tomas'
a_cifrado = ''
for letra in a:
    valor = buscar_ta(tabla, hash_cifrado, Palabra(letra, ''), 'palabra')
    cifrado = ''
    if(valor is None):
        cifrado = cifrar(letra)
        palabra = Palabra(letra, cifrado)
        agregar_ta(tabla, hash_cifrado, palabra, 'palabra')
    else:
        cifrado = valor.info.significado
    a_cifrado += cifrado
print(a_cifrado)
lista = a_cifrado.split('%')
lista.pop()
msj = ''
for letras in lista:
    valor = buscar_ta(tabla2, bernstein_palabra, Palabra(letras, ''), 'palabra')
    decifrado = ''
    if(valor is None):
        decifrado = desifrar(letras)
        palabra = Palabra(letras, decifrado)
        agregar_ta(tabla2, bernstein_palabra, palabra, 'palabra')
    else:
        decifrado = valor.info.significado
    msj += decifrado
print(msj)
"""

# ******************************************************************************************************************************#
# ====================================================== Ejercicio 10 ===========================================================#
# ******************************************************************************************************************************#
"""
10. Nick Fury director de la agencia S.H.I.E.L.D. intenta detener a la organización Hydra y a su
líder Red Skull, los agentes de la agencia pueden interceptar los mensajes de Hydra pero
están cifrados, por tanto no pueden hacer nada con estos; afortunadamente el Capitán
América en una misión encubierta logró determinar las pautas del método de codificación.
Ahora Fury nos solicita desarrollar el algoritmo que permita decodificar los mensajes,
contemplando las siguientes pautas:
a. Las codificación se realiza de la siguiente manera:

i. primero se convierte el carácter a su valor en la tabla ASCII y se lo
multiplica por 37 para trasnformarlo en un número de cuatro dígitos;
ii. segundo se calcula un complemento en base al valor del carácter:

iii. luego a cada digito obtenido en el punto uno se lo eleva al cuadrado y se
le suma un complemento obtenido en el punto anterior y se transforma a
carácter;
iv. por último se juntan los cuatros caracteres y se le agrega al final el
carácter correspondiente al complemento.
Por ejemplo el carácter R se codifica de la siguiente manera:
R = 82, 82 * 37 = 3034, complemento = 32 + 82 – 79 = 35 = “#”
3
2
+ 35 = 44 = “,”, 02

+ 35 = 35 = “#”, 32

+ 35 = 44 = “,”, 42

+ 35 = 51 = “3”

El resultado final son estos cinco caracteres “,#,3#”;
b. deberá utilizar una tabla hash cerrada para almacenar cada una de las cadenas de
caracteres –de cinco caracteres– asociados a cada clave, una buena alternativa
para la función hash podría ser la función de Bernstein;
c. no se debe decodificar todas las cadenas de caracteres, esto debe hacerse a
medida que se necesitan y no están en la tabla;
d. ayuda al Capitán América descifrando los siguientes tres mensajes para poder
conocer cuáles serán los próximos movimientos de Hydra (los mensajes están
almacenados en archivos de texto, que deberá leerlos previamente desde cada
archivo, en el siguiente link: https://github.com/belwalter/mensajes_codificados).
"""
