#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################


class Nodo:

    def __init__(self,padre,estado,costo):
        #Informacion del nodo
        self.nodoPadre= padre
        self.id=
        m

        #Informacion del dominio
        self.estado= estado
        self.costo= padre.getCosto() + costo
        self.accion=
        self.p=padre.getProfundidad() + 1
        self.f=


    def getCosto(self):
        return self.costo


    def getProfundidad(self):
        return self.p

    def getF(self):
        return self.f
