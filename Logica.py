#! /usr/bin/env python3

from Inventario import Inventario
from random import uniform as _uniform

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
