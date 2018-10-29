#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################


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
        if estrategia = 'Anchura':
            f=self.p
        elif estrategia = "Costo":
            f=self.costo
        else:
            f=(-1)*self.p

        return f

    def __init__(self,padre,estado,costo,estrategia,accion):
        #Informacion del nodo
        self.nodoPadre= padre
        #Informacion del dominio
        self.estado= estado
        self.accion=accion

        if self.nodoPadre == None:
            self.costo=0
            self.p=0
        else:
            self.costo= padre.getCosto() + costo
            self.p=padre.getProfundidad() + 1

        self.f=self.definirEstrategia(estrategia)


## Getter del atributo costo
    def getCosto(self):
        return self.costo

## Getter del atributo profundidad
    def getProfundidad(self):
        return self.p

## Getter del atributo F
    def getF(self):
        return self.f

    def getEstado(self):
        return self.estado
