#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################
from Nodo import Nodo

class Frontera:

    def __init__(self):
        self.listaFrontera=CreaFrontera()

###############################################################################
#   Nombre del metodo: crearFrontera
#   Fecha de creacion: 17/10/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado: Devuelve una lista que sera la frontera
#   Descripcion:   Método para crear una frontera vacia.
################################################################################

    def CreaFrontera(self):
        frontera = []
        return frontera

###############################################################################
#   Nombre del metodo: insertar
#   Fecha de creacion: 17/10/2018
#   Version: 1.0
#   Argumentos de entrada: Un nodo del arbol (de la clase Nodo)
#   Valor retornado: Void
#   Descripcion:   Este metodo insertara dentro de la frontera el nodo dado
#                  y una vez insertado ordenara la lista de los nodos de la
#                  frontera por el menor f(atributo de la clase nodo). Por tanto
#                  el nodo con menor f estara en la primera posicion de la cola.
################################################################################

    def insertar(self,nodoArbol):
        self.listaFrontera.append(nodoArbol)
        self.listaFrontera=sorted(self.listaFrontera,key=lambda Nodo: Nodo.getF())

###############################################################################
#   Nombre del metodo: elimina
#   Fecha de creacion: 17/10/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado: Devuelve el nodo que esta en la cabeza de la frontera
#   Descripcion:   Este metodo es el que se encarga de sacar el nodo de la
#                  frontera con menor f, este nodo sera siempre la cabeza de
#                  la cola, una vez lo saca, lo borra de la frontera.
################################################################################

    def elimina(self):
        return self.listaFrontera.pop(0)

###############################################################################
#   Nombre del metodo: esVacia
#   Fecha de creacion: 1710/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado: Devuelve un booleano (True) si la frontera esta vacia.
#   Descripcion:   Metodo encargado de devolver si la frontera esta o no vacia.
#                  si esta vacia devovlera True y si no devolvera False. 
################################################################################

    def esVacia(self):
        return self.listaFrontera == []
