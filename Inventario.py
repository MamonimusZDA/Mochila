#! /usr/bin/env python3

from functools import total_ordering
from random import randint as _randint

NUMERO_OBJETOS = 20

@total_ordering
class Inventario:
    def __init__ ( self, posibles_articulos ):
        self.lista_articulos = list ( )
        self.peso_total = 0

        for i in range ( NUMERO_OBJETOS ):
            self.lista_articulos .append (
                    _randint ( 0, 1 )
            )

        for i in range ( NUMERO_OBJETOS ):
            self.peso_total +=\
                    self.lista_articulos [ i ] *\
                    posibles_articulos [ i ]

    def __eq__(self, other):
        return self.peso_total == other.peso_total

    def __lt__(self, other):
        return self.peso_total < other.peso_total

    def __repr__(self):
        return ( f'{ repr ( self.peso_total ) }' )
