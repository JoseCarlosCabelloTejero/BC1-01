#!/usr/bin/python3
#############################################################################
##                              Sistemas Inteligentes                      ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################
from networkx import *

class Grafo:
    def __init__(self,path): #Constructor
        self.__graph = read_graphml(path)
        #read_graphml(path, node_type=<type 'str'>)

# Metodo que devuelve el atributo graph
    def getGraph(self):
        return self.__graph


    def perteneceNodo(self, idNodo):
        listaNodos=list(self.__graph.nodes)
        for i in listaNodos:
            if idNodo==i:
                return True
        return False


    def posicionNodo(self, idNodo):
        if  self.perteneceNodo(idNodo) == True:
            attrX=get_node_attributes(self.__graph,"x")
            attrY=get_node_attributes(self.__graph,"y")
            """get_node_attributes devuelve un diccionario con
            las propiedades de cada uno de los nodos del grafo"""
            return [attrX.get(idNodo),attrY.get(idNodo)]
        else:
            return "Error"


    def adyacentesNodo(self, idNodo):

        if self.perteneceNodo(idNodo) == True:
            aristas=edges(self.__graph,idNodo)
            return aristas
        else:
            return "Error"
