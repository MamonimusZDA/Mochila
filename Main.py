#! /usr/bin/env python3

from functools import total_ordering

from random import \
        uniform as _uniform,\
        randint as _randint

MAXIMO = 40
NUMERO_OBJETOS = 20

def main ( ):
    numero_inventarios = input ( 'Ingresa el numero total de convinaciones posibles a escojer:\n>> ' )
    numero_inventarios = int ( numero_inventarios )

    porcentaje_mutacion = input ( 'Ingresa el porcentaje de mutacion:\n>> ' )
    numero_generaciones = input ( 'Numero de generaciones:\n>> ' )

    posibles_articulos = generarListaArticulos ( )

    print ( f'\nLa mochila solo soporta { MAXIMO }kg' )
    print ( f'El peso de los posibles articulos a escoger son:\n\t{ posibles_articulos }\n' )

    posibles_inventarios = generarListaInventarios (
        numero_inventarios,
        posibles_articulos
    )

    posibles_inventarios.sort ( )

    for inventario in posibles_inventarios:
        print ( '-------------' )
        print ( f'Lista de articulos:\n\t{ inventario.lista_articulos }' )
        print ( 'Peso total: %.2f' % inventario.peso_total )

@total_ordering
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

    def __eq__(self, other):
        return self.peso_total == other.peso_total

    def __lt__(self, other):
        return self.peso_total < other.peso_total

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({repr(self.lista_articulos)}, {repr(self.peso)})")

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

if __name__ == '__main__':
    main ( )
