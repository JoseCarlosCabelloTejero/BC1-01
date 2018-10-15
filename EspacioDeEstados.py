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
        if not (self.__grafo.perteneceNodo(estado.getNode())):
            return False
        else:
            for i in estado.getListNodes():
                if not(self.__grafo.perteneceNodo(i)):
                    return False
        return True

    def sucesores(self,estado):

        listaSucesores = []

        listaDeAdyacentes = self.__grafo.adyacentesNodo(estado.getNode())

        for ady in listaDeAdyacentes:
            nombreCalle = ady[2]
            accM = "EStoy en ",estado.getNode(),"y voy a ",ady[1],",",nombreCalle
            estadoNuevo = Estado(ady[1],estado.getListNodes().remove(ady[1]))
            coste = ady[3]

            listaSucesores.append([accM,estadoNuevo,coste])

        return listaSucesores
