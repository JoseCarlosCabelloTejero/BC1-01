#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import Estado


class Nodo:

###############################################################################
#   Nombre del metodo: definirEstrategia
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada: Una cadena con el nomnre de la estrategia de busqueda
#   Valor retornado: El valor de la f para la estrategia dada
#   Descripcion: El metodo calcula el valor de la f dependiendo de la
#                estrategia de busqueda utilizada
################################################################################

    def definirEstrategia(self,estrategia):
        if estrategia == 'anchura':
            f=self.__p
        elif estrategia == "costo":
            f=self.__costo
        elif estrategia == 'voraz':
            f=self.__h
        elif estrategia == 'a*':
            f=self.__h + self.__costo
        else:
            f=int((-1)*self.__p)

        return f


    def __init__(self,padre,estado,costo,estrategia,accion):
        #Informacion del nodo
        self.__nodoPadre= padre

        #Informacion del dominio
        self.__estado= estado
        self.__accion=accion

        if estrategia == 'voraz' or estrategia == 'a*':
            self.__h=estado.getHeuristica()
        else:
            self.__h=None

        if self.__nodoPadre == None:
            self.__costo=0
            self.__p=0
        else:
            self.__costo= padre.getCosto() + float(costo)
            self.__p=padre.getProfundidad() + 1

        self.__f=self.definirEstrategia(estrategia)


    def getIdNodo(self):
        return self.__idNodo

## Getter del atributo costo
    def getCosto(self):
        return self.__costo

## Getter del atributo profundidad
    def getProfundidad(self):
        return self.__p

## Getter del atributo F
    def getF(self):
        return self.__f

    def getEstado(self):
        return self.__estado

    def getPadre(self):
        return self.__nodoPadre

    def getAccion(self):
        return self.__accion
