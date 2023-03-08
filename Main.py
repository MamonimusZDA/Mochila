#! /usr/bin/env python3

from Inventario import Inventario
from Logica import *
from statistics import mode

import numpy as np

MAXIMO = 40

def main ( ):
    numero_inventarios = input ( 'Ingresa el numero total de combinaciones posibles a escoger:\n>> ' )
    numero_inventarios = int ( numero_inventarios )

    porcentaje_mutacion = input ( 'Ingresa el porcentaje de mutacion:\n>> ' )
    numero_generaciones = input ( 'Numero de generaciones:\n>> ' )
    numero_generaciones = int ( numero_generaciones )
    porcentaje_mutacion = int ( porcentaje_mutacion )

    posibles_articulos = generarListaArticulos ( )

    print ( f'\nLa mochila solo soporta { MAXIMO }kg' )
    print ( f'El peso de los posibles articulos a escoger son:\n\t{ posibles_articulos }\n' )

    posibles_inventarios = []
    lista_de_pesos = []

    for j in range ( 30 ):
        posibles_inventarios = generarListaInventarios (
            numero_inventarios,
            posibles_articulos
        )

        for i in range ( numero_generaciones ):
            posibles_inventarios = generarGeneracion ( posibles_inventarios, posibles_articulos )
            posibles_inventarios = mutarGeneracion ( posibles_inventarios, porcentaje_mutacion )
            posibles_inventarios.sort ( )
            posibles_inventarios = eliminarNoAptos ( posibles_inventarios ,numero_inventarios, posibles_articulos)

        lista_de_pesos.append ( posibles_inventarios [ -1 ] )

#         for inventario in posibles_inventarios:
#             print ( '----------' )
#             print ( f'La lista de articulos es: {inventario.lista_articulos }' )
#             print ( 'Peso total: %.2f' % inventario.peso_total )

        print ( f'\n----- { j + 1 } -----' )
        print ( 'La media es: %.2f' % media ( posibles_inventarios ) )
        print ( 'La mediana es: %.2f' % mediana ( posibles_inventarios ) )
        print ( 'La moda es: %.2f' % moda ( posibles_inventarios ) )

    print ( f'\nLos mejores sujetos fueron: { lista_de_pesos }\n')

    print ( 'La media es: %.2f' % media ( lista_de_pesos ) )
    print ( 'La mediana es: %.2f' % mediana ( lista_de_pesos ) )
    print ( 'La moda es: %.2f' % moda ( lista_de_pesos ) )
    print ( 'La desviacion estandar es: %.2f' % desviacion_estandar ( lista_de_pesos ) )

def moda ( dataset ):
    lista_peso = []
    for data in dataset:
        lista_peso.append ( data.peso_total )

    return mode ( lista_peso )

def mediana ( dataset ):
    mediana = 0

    for data in dataset:
        mediana += data.peso_total

    return mediana / len(dataset)

def media ( dataset ):
    data = sorted ( dataset )
    index = len ( dataset ) // 2

    if len ( dataset ) % 2 != 0:
        return data [ index ].peso_total

    return ( data [ index - 1 ].peso_total + data [ index ].peso_total) / 2

def desviacion_estandar ( dataset ):
    lista_peso = []
    for data in dataset:
        lista_peso.append ( data.peso_total )

    return np.sqrt ( np.var ( lista_peso ) )

if __name__ == '__main__':
    main ( )
