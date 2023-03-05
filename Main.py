#! /usr/bin/env python3

from pstats import SortKey

from random import \
        uniform as _uniform,\
        randint as _randint

MAXIMO = 40
POBLACION = 10
NUMERO_OBJETOS = 20

def main ( ):
    posibles_articulos = generarListaArticulos ( )
    posibles_inventarios = generarListaInventarios (
        posibles_articulos
    )

    for inventario in posibles_inventarios:
        print ( inventario.peso_total )

class Inventario:
    def __init__ ( self ):
        self.lista_articulos = list ( )
        self.peso_total = 0

    def generarListaArticulos ( self ):
        for i in range ( NUMERO_OBJETOS ):
            self.lista_articulos .append (
                    _randint ( 0, 1 )
            )

    def calcularPesoTotal ( self, posibles_articulos ):
        for i in range ( NUMERO_OBJETOS ):
            self.peso_total +=\
                    self.lista_articulos [ i ] *\
                    posibles_articulos [ i ]

def generarListaArticulos ( ):
    lista_articulos = list ( )

    for i in range ( NUMERO_OBJETOS ):
        articulo = _uniform ( 0, 10 )
        articulo = round ( articulo, 1 )
        lista_articulos.append ( articulo )

    return lista_articulos

def generarListaInventarios ( posibles_articulos ):
    lista_inventarios = list ( )

    for i in range ( POBLACION ):
        inventario = Inventario ( )
        inventario.generarListaArticulos ( )
        inventario.calcularPesoTotal ( posibles_articulos )

        lista_inventarios.append ( inventario )

    return lista_inventarios

if __name__ == '__main__':
    main ( )
