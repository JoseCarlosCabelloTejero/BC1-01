#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################
from networkx import *

class Grafo:
    def __init__(self,path): #Constructor
        try:
            self.__graph = read_graphml(path)
        except FileNotFoundError:
            print("Error. Archivo '{0}' no encontrado".format(path))
            exit()

# Metodo que devuelve el atributo graph
    def getGraph(self):
        return self.__graph

###############################################################################
#   Nombre del metodo: perteneceNodo
#   Fecha de creacion: 24/09/2018
#   Version: 1.0
#   Argumentos de entrada: id de un Nodo
#   Valor retornado: Valor booleano (True/False) indicando si el nodo pertenece
#                    o no al grafo.
#   Descripcion:   Utilizamos la funcion list de la biblioteca networkx para obtener
#                  una lista con el id de todos los nodos del grafo
#                  Buscamos en esta lista el nodo pasado como parametro, y se
#                  retorna True en el momento en el que se encuentra, o False
#                  si se llega al final de la lista sin haberlo encontrado
################################################################################

    def perteneceNodo(self, idNodo):
        listaNodos=list(self.__graph.nodes)
        for i in listaNodos:
            if idNodo==i:
                return True
        return False

###############################################################################
#   Nombre del metodo: posicionNodo
#   Fecha de creacion: 24/09/2018
#   Version: 1.0
#   Argumentos de entrada: id del Nodo del que se quiere conocer su posicion
#   Valor retornado: Lista con las posicion (x,y) del nodo
#   Descripcion:  Se utiliza la función get_node_attributes que devuelve un
#                 diccionario con las propiedades de cada uno de los nodos del grafo
#
#
################################################################################
    def posicionNodo(self, idNodo):
        if  self.perteneceNodo(idNodo) == True:
            attrX=get_node_attributes(self.__graph,"x")
            attrY=get_node_attributes(self.__graph,"y")

            return float(attrX.get(idNodo)),float(attrY.get(idNodo))
        else:
            return "Error"

###############################################################################
#   Nombre del metodo: adyacentesNodo
#   Fecha de creacion: 25/09/2018
#   Version: 1.0
#   Argumentos de entrada: id del Nodo del que se quieren conocer sus adyacentes
#   Valor retornado: Lista con las propiedades (nombre y longitud) de las aristas
#                  adyacentes al nodo  pasado como parámetro al metodo.
#   Descripcion:   La función edges de la biblioteca networkx devuelve una
#                  vista (EdgeView) de las aristas adyacentes al nodo pasado como
#                  parámetro. Una vez que se ha comprobado que el nodo existe,
#                  utilizamos esta función para obtener un diccionario con todos
#                  los atributos de cada una de las aristas adyacentes al nodo dado.
#                  Esto es posible porque el segundo parámetro pasado a la funcion
#                  edges esta activado (True)
#
#                  La variable local 'aristas' contiene dicha vista. Cada elemento
#                  de ella es una lista que contiene el nodo origen en la posición 0
#                  el nodo destino en la posicion 1 y un diccionario con las propiedades
#                  de dicha arista en la posicion 2.
#                  Recorremos la vista 'aristas' introduciendo en 'lista' los atributos
#                  nodo origen (i0), nodo destino (i1), nombre y longitud de la aristas
#                  (que se encuentran  en un diccionario con las propiedades de esa arista (i2)).
#
#
################################################################################
    def adyacentesNodo(self, idNodo):
        lista = []
        if self.perteneceNodo(idNodo) == True:
            aristas=self.__graph.edges(idNodo,True)
            for i in aristas:
                if i[2].get("name") == None:
                    lista.append((i[0],i[1],"Sin nombre",i[2].get("length")))
                else:
                    lista.append((i[0],i[1],i[2].get("name"),i[2].get("length")))
            return lista
        else:
            return "Error"
