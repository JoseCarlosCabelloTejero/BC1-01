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



    def getCosto(self):
        return self.costo


    def getProfundidad(self):
        return self.p

    def getF(self):
        return self.f
