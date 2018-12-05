#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import graph

from Estado import *
import math

class EspacioDeEstados:

    def __init__(self, ficheroGraphml):
        self.__grafo = graph.Grafo(ficheroGraphml)

    def getGrafo(self):
        return self.__grafo

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

    def esta(self, estado):
        if not (self.__grafo.perteneceNodo(estado.getNode())):
            return False
        else:
            for i in estado.getListNodes():
                if not(self.__grafo.perteneceNodo(i)):
                    return False
        return True

###############################################################################
#   Nombre del metodo: calcularHeuristica
#   Fecha de creacion: 12/11/2018
#   Version: 1.0
#   Argumentos de entrada: nodoOSM y lista de nodos por recorrer desde ese Nodo
#   Valor retornado: Mínima distancia desde nodoOSM hasta cualquiera de los
#                      nodos contenidos en 'listNodes'
#   Descripcion: Se calcula la distancia geógrafica desde nodoOSM hasta a cada uno
#                  de los nodos de ListNodes. De todas estas distancias se retorna
#                  la más pequeña.
################################################################################

    def calcularHeuristica(self, nodoOSM, listNodes):

        heuristicas = []

        for nodo in listNodes:
            aux = self.distance(nodoOSM,nodo)
            heuristicas.append(aux)

        if heuristicas==[]:
            heuristicas.append(0)

        return min(heuristicas)

###############################################################################
#   Nombre del metodo: distance
#   Fecha de creacion: 12/11/2018
#   Version: 1.0
#   Argumentos de entrada:Nodos OSM entre los cuales se desea calcular la distancia
#                        existente
#   Valor retornado:  Distancia geográfica entre dos nodos OSM
#   Descripcion: Retorna la
################################################################################

    def distance(self, idNode1, idNode2):

        (lng1,lat1) = self.__grafo.posicionNodo(idNode1)
        (lng2,lat2) = self.__grafo.posicionNodo(idNode2)
        earth_radious=6371009

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        d_phi = phi2 - phi1

        theta1 = math.radians(lng1)
        theta2 = math.radians(lng2)
        d_theta = theta2 - theta1

        h = math.sin(d_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_theta/2)**2
        h=min(1.0,h)

        arc = 2 * math.asin(math.sqrt(h))

        dist = arc * earth_radious;

        return dist
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

    def sucesores(self, estado):

        listaSucesores = []

        listaDeAdyacentes = self.__grafo.adyacentesNodo(estado.getNodeOSM())

        listaNodosPorRecorrer = estado.getListNodes()

        for ady in listaDeAdyacentes:
            nombreCalle = ady[2]

            listaNodosNueva = []

            for i in listaNodosPorRecorrer:
                if not i == ady[1]:
                    listaNodosNueva.append(i)

            heuristica=self.calcularHeuristica(ady[1],listaNodosNueva)

            estadoNuevo = Estado(ady[1],sorted(listaNodosNueva),heuristica)
            coste = ady[3]
            accM= '{} --> {} ({}) coste: {}'.format(estado.getNodeOSM(),ady[1],nombreCalle,round(float(ady[3]),2))
            listaSucesores.append([accM,estadoNuevo,coste])

        return listaSucesores
