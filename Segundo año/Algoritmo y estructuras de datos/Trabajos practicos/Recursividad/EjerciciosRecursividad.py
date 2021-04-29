#Ejercicio 1


def fibonacci(n):
    if ( n == 1 ) or ( n == 2 ):
        return 1
    elif ( n > 2 ):
        return fibonacci( n-1 ) + fibonacci( n - 2)

numero = 8
"""
print (fibonacci(numero))
"""

#Ejercicio 2
'''
def Suma_enteros(n):
    if (n == 1):
        return 1
    elif (n > 1):
        return n + Suma_enteros(n - 1)

num = 5

print (Suma_enteros(num))
'''

#Ejercicio 3

'''
def producto(n1, n2):
    if(n2 == 1):
        return n1
    else:
        return n1 + producto(n1, n2-1)

numero1 = 2
numero2 = 2

print(producto (numero1,numero2))
'''

#Ejercicio 4

'''
def potencia (n1,n2):
    if ( n2 == 0 ):
        return 1
    elif ( n2 == 1 ):
        return n1
    elif ( n1 == 0 ):
        return 0
    else: 
        return n1 * potencia (n1, n2 - 1)

numero1 = 2
numero2 = 4

print(potencia (numero1,numero2))
'''

#Ejercicio 5

'''
palabra = "tomas"

def invertir(cadena):
    if(len(cadena) == 0):
        return cadena
    else:
        return cadena[len(cadena) - 1] + invertir(cadena[0:len(cadena)-1])

print(invertir(palabra))
'''

#Ejercicio 6

'''
def serie (n1,n2):
    if ( n2 == 1 ):
        return 1
    elif ( n2 > 1):
        return (n1 / n2) + (serie (n1, n2 - 1))

print(serie (1,5))
'''

#Ejercicio 7

'''
def binario (n):
    if (n == 0):
        return " "
    else:
        return binario (n // 2) + str (n % 2)

numero = 100

print(binario(numero))
'''

#Ejercicio 8

'''
def logaritmo(b, n):
    if ( b == n):
        return 1
    else:
        return 1 + logaritmo (b, n / b)

print(logaritmo(2,8))
'''

#Ejercicio 9
'''
def cuenta_digitos(n):
    if ( n < 10):
        return 1
    else:
        return 1 + cuenta_digitos (n / 10) 
    

print(cuenta_digitos(4548))
'''

#Ejercicio 10
'''
def invertir_numero(n, posicion=-1):
    posicion += 1
    tamanio = cuenta_digitos(n)

    if (tamanio == 1):
        return n * potencia(10, posicion)

    actual = n // potencia(10, tamanio-1)
    restante = n - actual * potencia(10, tamanio-1) 
    return actual * potencia(10, posicion) + invertir_numero(restante, posicion)
 
print(invertir_numero(2788,-1))
'''

#Ejercicio 11

'''
def mcd(n1,n2):
    if n1 > n2:
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1

    if ((mayor % menor) == 0):             
        return menor                
    else:
        return mcd(menor, mayor%menor)

print(mcd(4,8))
'''

#Ejercicio 12

'''
def mcm(n1, n2):
    return((n1*n2)//mcd(n1, n2))

print(mcd(4,8))
'''

#Ejercicio 13

'''
def sumar_digitos(n):
    if (n < 10):
        return n
    else:
        return (n % 10) + sumar_digitos(n // 10)

print(sumar_digitos(254))
'''
#Ejercicio 14

'''
def raiz_cuadrada(n, x):
    if ((x * x) == n):
        return x
    elif ((x*x) > 1):
        return x-1
    else:
        return raiz_cuadrada(n, x+1)

print(raiz_cuadrada(16,))
'''
#Ejercicio 15
'''
def progresion_geometrica(n):
    if(n == 1):
        return 2
    else:
        return -3 * progresion_geometrica(n-1)

print(progresion_geometrica())
'''
#Ejercicio 16
'''
vector = [1,2,3,4]
def atras_delante(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        atras_delante(vec[0:-1])

print(atras_delante(vector))
'''

#Ejercicio 17
'''
def recorrer_matriz(mat, i, j):
    if (i < len(mat)) and (j < len(mat[i])):
        print(mat[i][j])
        if(j == len(mat[i])-1):
            i+=1
            j=0
        recorrer_matriz(mat,i,j+1)

matriz = [[1,2,3],[4,5,6],[7,8,9]]

print(recorrer_matriz(matriz,0,0))
'''

#Ejercicio 18
'''
def sucesion(n):
    if (n==1):
        return 2
    else:
        return ((n+1) / sucesion(n-1))

print(sucesion(n))
'''

#Ejercicio 19 
'''
buscado = 5
vec = [1,2,3,4,5,6,7,8,9]

def busqueda_centinela(bus, v,i):
    if (bus == v[i]):
        print("El elemento que esta buscando se encuentra en la posicion N° ", i ," de la lista")
    else:
        i+=1
        return busqueda_centinela(bus,v,i)

print(busqueda_centinela(buscado,vec,0))
'''
#Ejercicio 20
'''
buscado = 9
vector = [1,2,3,4,5,6,7,8,9,10]

def busqueda_bin(bus,v,pri,ult):
    if (pri > ult):
        print("No se encuentra el elemento buscado")
    med = (pri + ult) // 2
    if (bus == v[med]):
        print("El elemento se encuentra en la posicion ",med)
    elif (bus > v[med]):
        return busqueda_bin(bus,v,med+1,ult)
    else:
        return busqueda_bin(bus,v,pri,med-1)

print(busqueda_bin(buscado,vector,0,len(vector)-1))
'''

#Ejercicio 21

'''
vec = [['coordenadas', 'blaster principal', False],
       ['coordenadas', 'blaster secundario', True],
       ['coordenadas', 'cañon', True],
       ['coordenadas', 'blaster principal', False]]

def contar_naves(vec):
    if(len(vec)==0):
        return 0
    else:
        if(vec[-1][2]):
            return 1 + contar_naves(vec[0:-1])
        else:
            return 0 + contar_naves(vec[0:-1])

print("Total de naves derribadas", contar_naves(vec))
'''
#Ejercicio 22

#Ejercicio 23
'''
def torre_de_hanoi(discos,torre1,torre2,torre3):
    if (discos > 0):
        torre_de_hanoi(discos-1,torre1,torre3,torre2)
        print("Se mueve disco desde torre ",torre1 ," hasta torre " ,torre3)
        torre_de_hanoi(discos-1,torre2,torre3,torre1)
    
print(torre_de_hanoi(3,1,2,3))
'''

#Ejercicio 24
'''
def sucesion_2(n):
    if(n == 1):
        return 5.25
    else:
        return sucesion_2(n-1) * 4

print(sucesion_2())
'''

#Ejercicio 25
'''
def sucesion_3(n):
    if (n == 1):
        return 3
    elif (n >= 2):
         return sucesion_3 ( n - 1 ) + 2 * n

print(sucesion_3())
'''
cont = 0
palabras = ['auto','colectivo','cama','espada','pelicula','agua','zapatos','agua','cama','cama','espada']

def ocurrencias(palabras, i, bus, cont):

    if i == len(palabras):
        return "No se encontro la palabra"
    else:
        if palabras[i] == bus:
            cont += 1
            print("La palabra se repite:", cont)
        
        else:    
            return ocurrencias(palabras, i + 1, bus, cont)


print(ocurrencias(palabras, 0, 'cama', cont))

tamanio = len(palabras)
def ContarOcurrencias (tamanio, bus, i):
{
if (Primero > tamanio-1) return 0;
else
 {
if (Vector[Primero] == Objetivo)
return(1 + ContarOcurrencias(N,Vector, Objetivo, Primero+1));
else return(ContarOcurrencias(N,Vector, Objetivo, Primero+1));


