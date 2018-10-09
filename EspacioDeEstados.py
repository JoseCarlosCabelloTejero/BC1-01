#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import graph


class EspacioDeEstados:

    def __init__(self,fichero):
        self.__grafo=Grafo(fichero)


    def esta(self,estado):
        return self.__grafo.perteneceNodo(estado.getNode())

    def sucesores(self,estado):

        listaSucesores = []

        listaDeAdyacentes = self.__grafo.adyacentesNodo(estado.getNode())

        for ady in listaDeAdyacentes:

            accM = "EStoy en ",estado.getNode(),"y voy a ",ady[1]
            estadoNuevo = #Se crea un estado
            coste = ady[3]
            listaSucesores.apend([accM,estadoNuevo,coste])

        return listaSucesores
