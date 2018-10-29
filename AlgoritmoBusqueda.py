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
import stack

archivoSolucion="solucion.txt"

def escribirSolucion(solucion):
    with open(archivoSolucion,'w') as f:
        for accion in solucion:
            f.write(accion + "\n")
			f.close()

def crea_nodo(padre, estado, prof, costo, estrategia,accion):
    nodo=Nodo.Nodo(padre,estado,costo,estrategia,accion)
    return nodo

def crearListaNodosArbol(Ls, padre, prof_Max, estrategia):
    Ln=[]
    for sucesor in Ls:
        accion=sucesor[0]
        estado=sucesor[1]
        coste=sucesor[2]
        nodo=Nodo.Nodo(padre, estado, coste, estrategia, accion)
        Ln.append(nodo)
    return Ln

def crearSolucion(nodo):
    pila = stack.Stack()

    nodoArbol = nodo

    while (not nodoArbol.getPadre()==None):
        accion = nodo.getAccion()
        pila.push(accion)
        nodoArbol = nodoArbol.getPadre
    pila.push(nodoArbol)

    solucion = []

    while pila.isEmpty():
        solucion.append(pila.pop())

    return solucion

def busqueda_acotada (prob, estrategia, prof_Max):

    frontera = Frontera.Frontera()
    n_inicial = crea_nodo (None, prob.getEstadoInicial, 0, estrategia, None)
    frontera.insertar(n_inicial)
    solucion = None

    while ((solucion==None) and(not (frontera.esVacia())):
        n_actual=frontera.elimina()
        if (prob.esObjetivo(n_actual.getEstado())):
            solucion=True
        else:
            Ls=prob.getEspacioEstados().sucesores(n_actual.getEstado())
            Ln=crearListaNodosArbol(Ls, n_actual, prof_Max, estrategia)
            frontera.insertarLista(Ln)

    if (solucion==None):
        return "NO_Solucion"
    else:
        return CreaSolucion(n_actual)

def Busqueda(prob, estrategia, prof_Max, inc_Prof):

    prof_Actual = inc_Prof
    solucion = None

    while ((solucion == None) and (prof_Actual<= prof_Max)):
        solucion = busqueda_acotada (prob, estrategia, prof_Actual)
        prof_Actual = prof_Actual + inc_Prof

    escribirSolucion(solucion) #Se escribe la solucion en un archivo .txt
    return solucion



if __name__= "__main__":

    #Comprobacion de los argumentos de entrada
    if not len(sys.argv)==3:
        print('Uso: ./AlgoritmoBusqueda <profMaxima> <incremento>')
        exit()

    Prof_Max = int (sys.argv[1])
    Inc_Prof= int(sys.argv[2])

    Prob = Problema.Problema ("problema.json")
