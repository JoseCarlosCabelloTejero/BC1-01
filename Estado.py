#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import hashlib


class Estado:

###############################################################################
#   Nombre del metodo: md5generador
#   Fecha de creacion: 08/10/2018
#   Version: 1.0
#   Argumentos de entrada: id del nodo y la lista de nodos que quedan por recorrer
#   Valor retornado: Devuelve el id del estado codificado en MD5
#   Descripcion:   Utilizamos la bilbioteca hashlib para codificar el id del nodo
#                  Y la lista de nodos que quedan por recorrer en un codigo MD5 que
#                  sera el identificador del estado.
################################################################################

    def md5generador(self,idNodo,lista):
        n=0
        m = hashlib.md5()
        m.update(idNodo.encode())
        for i in lista:
            m.update(lista[n].encode())
            n=n+1
        return m.hexdigest()



#Constructor

    def __init__(self,nodeOSM,listNodes,heuristica):
        self.__nodeOSM = nodeOSM
        self.__listNodes = sorted(listNodes)
        self.__id = self.md5generador(self.__nodeOSM,self.__listNodes)
        self.__heuristica = heuristica

## Getter del atributo node
    def getNodeOSM(self):
        return self.__nodeOSM

    def getListNodes(self):
        return self.__listNodes

    def getId(self):
        return self.__id

    def getHeuristica(self):
        return self.__heuristica
