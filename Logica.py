#! /usr/bin/env python3

from Inventario import Inventario
from random import \
        uniform as _uniform,\
        randint as _randint

NUMERO_OBJETOS = 20

def generarListaArticulos ( ):
    lista_articulos = list ( )

    for i in range ( NUMERO_OBJETOS ):
        articulo = _uniform ( 0, 10 )
        articulo = round ( articulo, 1 )
        lista_articulos.append ( articulo )

    return lista_articulos

def generarListaInventarios ( numero_inventarios, posibles_articulos ):
    lista_inventarios = list ( )

    for i in range ( numero_inventarios ):
        inventario = Inventario ( )
        inventario.generarListaArticulos ( )
        inventario.calcularPesoTotal ( posibles_articulos )

        lista_inventarios.append ( inventario )

    return lista_inventarios

def generarHijos(padre_1, padre_2):
    padre_1_dividido = []
    padre_2_dividido = []

    padre_1_dividido.append ( padre_1 [ 0 : int ( NUMERO_OBJETOS / 2 ) ] )
    padre_1_dividido.append ( padre_1 [ int ( NUMERO_OBJETOS / 2 ) : NUMERO_OBJETOS ] )
    padre_2_dividido.append ( padre_2 [ 0 : int ( NUMERO_OBJETOS / 2 ) ] )
    padre_2_dividido.append ( padre_2 [ int ( NUMERO_OBJETOS / 2 ) : NUMERO_OBJETOS ] )

    partes_padres = [
            padre_1_dividido,
            padre_2_dividido
    ]

    index_1 = _randint ( 0, 1 )
    index_2 = _randint ( 0, 1 )
    index_3 = _randint ( 0, 1 )

    hijos = []

    hijos.append (
        partes_padres [ index_1 ] [ index_2 ] +\
        partes_padres [ index_1 - 1 ] [ index_3 ]
    )
    hijos.append (
        partes_padres [ index_1 - 1 ] [ index_2 - 1 ] +\
        partes_padres [ index_1 ] [ index_3 - 1 ]
    )

    return hijos
