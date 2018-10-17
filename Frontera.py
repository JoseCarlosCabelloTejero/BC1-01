#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################
from Nodo import Nodo

class Frontera:

    def __init__(self):
        self.listaFrontera=CreaFrontera()

    def CreaFrontera(self):
        frontera = []
        return frontera

    def insertar(self,nodoArbol):
        self.listaFrontera.append(nodoArbol)
        self.listaFrontera=sorted(self.listaFrontera,key=lambda Nodo: Nodo.getF())

    def elimina(self):

        return self.listaFrontera.pop(0)


    def esVacia(self):
        return self.listaFrontera == []
