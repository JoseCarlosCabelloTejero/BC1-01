#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import EspacioDeEstados
import Problema
import Frontera
import Nodo
import sys


def busqueda_acotada (prob, estrategia, prof_Max):

    frontera = Frontera.Frontera()
    n_inicial = crea_nodo (None, prob.getEstadoInicial, 0, estrategia, None)
    frontera.insertar(n_inicial)
    solucion = None

def crea_nodo(padre, estado, prof, costo, estrategia,accion):
    nodo=Nodo.Nodo(padre,estado,costo,estrategia,accion)
    return nodo

def Busqueda(prob, estrategia, prof_Max, inc_Prof):

    prof_Actual = inc_Prof
    solucion = None

    while ((solucion == None) and (prof_Actual<= prof_Max)):
        solucion = busqueda_acotada (prob, estrategia, prof_Actual)
        prof_Actual = prof_Actual + inc_Prof

    return solucion





if __name__= "__main__":

    #Comprobacion de los argumentos de entrada
    if not len(sys.argv)==3:
        print('Uso: ./AlgoritmoBusqueda <profMaxima> <incremento>')
        exit()

    Prof_Max = int (sys.argv[1])
    Inc_Prof= int(sys.argv[2])

    Prob = Problema.Problema ("problema.json")
