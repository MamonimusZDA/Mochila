#! /usr/bin/env python3

from Inventario import Inventario
from Logica import *

MAXIMO = 40

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

if __name__ == '__main__':
    main ( )
