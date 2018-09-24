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
        return 0

    def adyacentesNodo(self, idNodo):
        return 0
