from pstats import SortKey

from random import \
        uniform as _uniform,\
        randint as _randint

MAXIMO = 40
NUM_DE_OBJETOS = 20

def crearObjetos ( ) :
    opciones_objetos = list ( )

    for i in range ( NUM_DE_OBJETOS ) :
        opciones_objetos.append ( round ( _uniform ( 0, 10 ), 1 ) )

    return opciones_objetos

#Iniciamos los objetos actuales en una lista con numeros aleatorios.
INVENTARIO_ACTUAL = crearObjetos ( )

class Inventario ( object ) :
    def __init__ ( self ) :
        self.lista_de_objetos = list ( )
        self.Peso_inventario = 0
        for i in range ( len ( INVENTARIO_ACTUAL ) ) :
            numbin = _randint ( 0, 1 )
            self.lista_de_objetos.append ( numbin )
        for i in range ( len ( INVENTARIO_ACTUAL ) ) :
            self.Peso_inventario = self.Peso_inventario + ( self.lista_de_objetos [ i ] * INVENTARIO_ACTUAL [ i ] )

def iniciarInventarios ( ) :
    lista_inventarios = list ( )

    for i in range ( POBLACION - 1 ):
        lista_inventarios.append ( Inventario ( ) )

    return lista_inventarios

def ordenarInventarios ( lista ) :
    pass

def hacerHijos ( lista ) :
    for i in range ( 0, 2, len ( lista ) ) :
        invuno = lista [ i ]
        invdos = lista [ i * 1 ]
        corteuno = _randint ( 1, 15 )
        cortedos = _randint ( 1, 15 )

    return lista

def mochila ( ) :
    lista = iniciarInventarios ( )

POBLACION = int ( input ( 'Ingresa el numero total de articulos posibles a escojer:\n>> ' ) )

p_muta = input ( 'Ingresa el porcentaje de mutacion:\n>> ' )
n_generacion = input ( 'Numero de generaciones:\n>> ' )

print ( f'El peso maximo de los objetos es: { MAXIMO }' )
print ( f'Los objetos creados son: { INVENTARIO_ACTUAL }' )

n_lista = iniciarInventarios ( )

for i in range ( len ( n_lista ) ) :
    print ( f'Lista numero: { i + 1 } -- { n_lista [ i ].lista_de_objetos }' )
    print ( 'PESO TOTAL: %.2f' % n_lista[ i ].Peso_inventario )
