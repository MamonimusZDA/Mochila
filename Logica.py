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
        inventario = Inventario ( posibles_articulos )

        lista_inventarios.append ( inventario )

    return lista_inventarios

def generarGeneracion( lista_inventarios, posibles_articulos ):
    numero_poblacion = len ( lista_inventarios )
    for i in range ( int ( numero_poblacion / 2 ) ):
        inventario_tmp_1 = Inventario ( posibles_articulos )
        inventario_tmp_2 = Inventario ( posibles_articulos )

        inv_1 = lista_inventarios [ _randint ( 1, numero_poblacion-1 ) ]
        inv_2 = lista_inventarios [ _randint ( 1, numero_poblacion-1 ) ]

        numero_corte = _randint ( 1, NUMERO_OBJETOS - 1 )

        parte_1p1 = inv_1.lista_articulos [ 0 : numero_corte ]
        parte_2p2 = inv_2.lista_articulos [ numero_corte : NUMERO_OBJETOS ]

        parte_1p2 = inv_1.lista_articulos [ numero_corte : NUMERO_OBJETOS ]
        parte_2p1 = inv_2.lista_articulos [ 0 : numero_corte ]

        inventario_tmp_1.lista_articulos = parte_1p1 + parte_2p2
        inventario_tmp_2.lista_articulos = parte_1p2 + parte_2p1

        lista_inventarios.append ( inventario_tmp_1 )
        lista_inventarios.append ( inventario_tmp_2 )

    return lista_inventarios

def mutarGeneracion ( lista_inventarios, porcentaje_mutacion ):
    for i in range ( len ( lista_inventarios ) ):
        posibilidad = _randint ( 1, 100 )

        if posibilidad <= porcentaje_mutacion:
            index = _randint ( 0, NUMERO_OBJETOS - 1 )
            ls_tmp = lista_inventarios [ i ].lista_articulos

            if ls_tmp [ index ] == 0:
                ls_tmp [ index ] = 1
            else:
                ls_tmp [ index ] = 0

            lista_inventarios [ i ].lista_articulos = ls_tmp

    return lista_inventarios

def eliminarNoAptos ( lista_inventarios ,numero_inventarios,posibles_articulos):
    for i in range(len(lista_inventarios)):
        if(lista_inventarios[i].peso_total>40):
            lista_inventarios = lista_inventarios[0:i]
            break
    if(len(lista_inventarios)>numero_inventarios):
        lista_inventarios.sort ( reverse = True )
        lista_inventarios = lista_inventarios[0:numero_inventarios]
        lista_inventarios.sort ( )
    if(len(lista_inventarios)<numero_inventarios):
        lista_tmp=generarListaInventarios(numero_inventarios-len(lista_inventarios),posibles_articulos)
        lista_inventarios.extend(lista_tmp)
    return lista_inventarios
