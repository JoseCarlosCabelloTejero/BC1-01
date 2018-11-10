#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import graph

from Estado import *

class EspacioDeEstados:

    def __init__(self,fichero):
        self.__grafo=graph.Grafo(fichero)

###############################################################################
#   Nombre del metodo: esta
#   Fecha de creacion: 09/10/2018
#   Version: 1.0
#   Argumentos de entrada: un objeto estado de la clase Estado
#   Valor retornado: Un booleano, True si el estado esta en el espacio de estados
#                    y false si el estado no esta en el espacio de estados
#   Descripcion:   Lo primero que comprobamos es que el nodo del estado forma parte
#                  del grafo, si no es asi directamente devolvemos False ya que ese
#                  estado no formara parte del espacio de estados. Si el nodo está
#                  en el grafo ahora comprobamos que la lista de nodos que le quedan
#                  por recorrer del estado pertenecen al grafo, si es asi se devolvera
#                  true, si no es asi devolveremos false.
################################################################################

    def esta(self,estado):
        if not (self.__grafo.perteneceNodo(estado.getNode())):
            return False
        else:
            for i in estado.getListNodes():
                if not(self.__grafo.perteneceNodo(i)):
                    return False
        return True

###############################################################################
#   Nombre del metodo: sucesores
#   Fecha de creacion: 7/11/2018
#   Version: 2.0
#   Argumentos de entrada: un objeto estado
#   Valor retornado: La lista de los sucesores de ese estado
#   Descripcion:  Partiendo por una lado, de una lista con todos los nodos del grafo 
#		adyacentes al estado actual, y, por otro lado, de una lsita con los nodos que faltan
#		por recorrer en el estado actual, vamos a generar una lista de sucesores
#		para dicho estado.
#		Recorremos la lista de adyacentes para generar los estados sucesores dicho
#		estado. Para cada nuevo estado sucesor, le metemos como lista de estados por visitar
#		aquellos estados adyacentes que no se encuentren la lista de nodos por 
#		recorrer del estado anterior.
#		
################################################################################

    def sucesores(self,estado):

        listaSucesores = []

        listaDeAdyacentes = self.__grafo.adyacentesNodo(estado.getNode())

        listaNodosPorRecorrer = estado.getListNodes()

        for ady in listaDeAdyacentes:
            nombreCalle = ady[2]

            listaNodosNueva = []

            for i in listaNodosPorRecorrer:
                if not i == ady[1]:
                    listaNodosNueva.append(i)

            estadoNuevo = Estado(ady[1],sorted(listaNodosNueva))
            coste = ady[3]
            accM= '{} --> {} ({}) coste: {}'.format(estado.getNode(),ady[1],nombreCalle,ady[3])
            listaSucesores.append([accM,estadoNuevo,coste])

        return listaSucesores
