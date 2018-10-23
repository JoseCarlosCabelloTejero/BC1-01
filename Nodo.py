#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################


class Nodo:

    def __init__(self,padre,estado,costo,f,accion):
        #Informacion del nodo
        self.nodoPadre= padre
        #Informacion del dominio
        self.estado= estado
        self.costo= padre.getCosto() + costo
        self.accion=accion
        self.p=padre.getProfundidad() + 1
        self.f=f


## Getter del atributo costo
    def getCosto(self):
        return self.costo

## Getter del atributo profundidad
    def getProfundidad(self):
        return self.p

## Getter del atributo F
    def getF(self):
        return self.f
