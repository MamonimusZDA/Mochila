# Programa para Maximisar el las convinaciones de pesos para una mochila de 40kg.

from pstats import SortKey
import random

#Definimos el maximo de peso de la mochila en un rango aleatorio
#MAXIMO = random.randint ( 1, 200 ) 

MAXIMO = 40

#NUM_DE_OBJETOS = random.randint ( 2, 50 ) 
NUM_DE_OBJETOS = 20

def crearobjetos ( ) :
    opciones_objetos = list ( )
    i = 0
    while ( i < NUM_DE_OBJETOS ) :
       opciones_objetos.append ( round ( random.uniform ( 0, 10 ), 1 ) )
       i += 1

    return opciones_objetos

#Iniciamos los objetos actuales en una lista con numeros aleatorios.
INVENTARIO_ACTUAL = crearobjetos ( )
class inventario ( object ) :
    def __init__ ( self ) :
        self.lista_de_objetos = list ( )
        self.Peso_inventario = 0
        for i in range ( len ( INVENTARIO_ACTUAL ) ) :
            numbin = random.randint ( 0, 1 ) 
            self.lista_de_objetos.append ( numbin ) 
        for i in range ( len ( INVENTARIO_ACTUAL ) ) :
            self.Peso_inventario = self.Peso_inventario + ( self.lista_de_objetos [ i ] * INVENTARIO_ACTUAL [ i ] )

def iniciar_inventarios ( ) :
    lista_inventarios = list ( )
    i = 0
    while ( i < POBLACION )  :
        i += 1
        new_inv = inventario ( )
        lista_inventarios.append ( new_inv ) 
    return lista_inventarios

def ordenar_inventarios ( lista ) :
       pass

def hacerhijos ( lista ) :
    Num = len ( lista )  - 1
    while i < ( len ( lista ) ) :
        i += 2
        invuno = lista [ i ]
        invdos = lista [ i * 1 ]
        corteuno = random.randint ( 1, 15 ) 
        cortedos = random.randint ( 1, 15 ) 
    return lista

def mochila ( ) :
    lista = iniciar_inventarios ( )

print ( 'Ingresa el numero total de Inventarios para tu mochila (POBLACION MI CUATE ) ')
POBLACION = int ( input ( ) )
print ( 'Ingresa el porcentaje de mutacion')
p_muta = input ( )
print ( 'Numero de generaciones')
n_generacion = input ( )
print ( 'El peso maximo de los objetos es: ', MAXIMO ) 
print ( 'Los objetos creados son: ', INVENTARIO_ACTUAL ) 
n_lista = iniciar_inventarios ( )
for i in range ( len ( n_lista ) ) :
    print ( 'Lista numero: ', i + 1, ' ', n_lista[i].lista_de_objetos,
          '\nPESO TOAL: ', n_lista[i].Peso_inventario ) 
