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
estrategiasBusqueda=["anchura","costo","profundidad","prof_acotada","prof_ite"]
###############################################################################
#   Nombre del metodo: escribirSolucion
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado:
#   Descripcion:
#
#
################################################################################

def escribirSolucion(solucion):
    with open(archivoSolucion,'w') as f:
        for accion in solucion:
            f.write(accion + "\n")
            f.close()


###############################################################################
#   Nombre del metodo: crea_nodo
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado:
#   Descripcion:
#
#
################################################################################

def crea_nodo(padre, estado, prof, costo, estrategia,accion):
    nodo=Nodo.Nodo(padre,estado,costo,estrategia,accion)
    return nodo


###############################################################################
#   Nombre del metodo: crearListaNodosArbol
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado:
#   Descripcion:
#
#
################################################################################

def crearListaNodosArbol(Ls, padre, prof_Max, estrategia):
    Ln=[]
    for sucesor in Ls:
        accion=sucesor[0]
        estado=sucesor[1]
        coste=sucesor[2]
        nodo=Nodo.Nodo(padre, estado, coste, estrategia, accion)
        Ln.append(nodo)
    return Ln


###############################################################################
#   Nombre del metodo: crearSolucion
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado:
#   Descripcion:
#
#
################################################################################

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


###############################################################################
#   Nombre del metodo: busqueda_acotada
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado:
#   Descripcion:
#
#
################################################################################

def busqueda_acotada (prob, estrategia, prof_Max):

    frontera = Frontera.Frontera()
    estado_inicial = prob.getEstadoInicial()
    n_inicial = crea_nodo (None, estado_inicial, 0,0, estrategia, None)
    frontera.insertar(n_inicial)
    solucion = None

    while ((solucion == None) and (not(frontera.esVacia()))):
        n_actual=frontera.elimina()
        estadoActual = n_actual.getEstado()
        if prob.esObjetivo(estadoActual):
            solucion=True
        else:
            Ls=prob.getEspacioEstados().sucesores(n_actual.getEstado())
            Ln=crearListaNodosArbol(Ls, n_actual, prof_Max, estrategia)
            frontera.insertarLista(Ln)
            print(Ln,Ls)
    if (solucion==None):
        return "NO_Solucion"
    else:
        return CreaSolucion(n_actual)


###############################################################################
#   Nombre del metodo: Busqueda
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada:
#   Valor retornado:
#   Descripcion:
#
#
################################################################################

def Busqueda(prob, estrategia, prof_Max, inc_Prof):

    prof_Actual = inc_Prof
    solucion = None

    while ((solucion == None) and (prof_Actual<= prof_Max)):
        solucion = busqueda_acotada (prob, estrategia, prof_Actual)
        prof_Actual = prof_Actual + inc_Prof


    return solucion

    Prof_Max = int (sys.argv[1])
    Inc_Prof= int(sys.argv[2])
    Estrategia=(sys.argv[3]).lower()

    Prob = Problema.Problema ("problema.json")

    solucion=Busqueda(Prob, Estrategia, Prof_Max, Inc_Prof)


################################################################################
#                               MAIN                                           #
################################################################################

if __name__=="__main__":

    #Comprobacion de los argumentos de entrada
    if not len(sys.argv)==4:
        print('Uso: ./AlgoritmoBusqueda <profMaxima> <incremento> <estrategia>')
        exit()
    elif (sys.argv[3].lower()) not in estrategiasBusqueda:
        print('Error. Estrategia de búsqueda desconocida')
        print(estrategiasBusqueda)


    Prof_Max = int (sys.argv[1])
    Inc_Prof= int(sys.argv[2])
    Estrategia=(sys.argv[3]).lower()

    Prob = Problema.Problema ("problema.json")

    solucion=Busqueda(Prob, Estrategia, Prof_Max, Inc_Prof)
    #escribirSolucion(solucion) #Se escribe la solucion en un archivo .txt

    print(solucion)
