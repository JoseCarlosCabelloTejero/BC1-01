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

def escribirSolucion(solucion,n_final,estrategia):

    with open(archivoSolucion,'w') as f:
        f.write("La solucion es: \nEstrategia: {}\n".format(estrategia))
        f.write("Total de nodos generados: {}\n".format(n_final.getIdNodo()))
        f.write("Costo: {}\nProfundidad: {}\n\n\n".format(n_final.getCosto(),n_final.getProfundidad()+1))

        for nodo in solucion:
            if(nodo.getPadre() is None):
                f.write("None 0.0 0 0.0")
            else:
                f.write(nodo.getAccion())
            f.write("\nEstoy en {} y tengo que visitar:{} \n\n".format(nodo.getEstado().getNode(),nodo.getEstado().getListNodes()))
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
        #accion = nodoArbol.getAccion()
        pila.push(nodoArbol)
        nodoArbol = nodoArbol.getPadre()

    pila.push(nodoArbol)

    solucion = []

    while not pila.isEmpty():
        solucion.append(pila.pop())

    return solucion


def poda(diccionarioPoda, Ln):

    ListaNodosPoda = []

    for nodo in Ln:
        estadoNodo = nodo.getEstado()
        idEstado = estadoNodo.getId()
        F_estado = nodo.getF()

        if( idEstado in diccionarioPoda):
            if F_estado < int(diccionarioPoda.get(idEstado)):
                diccionarioPoda.update({idEstado:F_estado})
                ListaNodosPoda.append(nodo)
        else:
            diccionarioPoda.update({idEstado:F_estado})
            ListaNodosPoda.append(nodo)

    return ListaNodosPoda,diccionarioPoda

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

    diccionarioPoda = {}

    frontera = Frontera.Frontera()
    estado_inicial = prob.getEstadoInicial()
    n_inicial = crea_nodo (None, estado_inicial, 0,0, estrategia, None)
    frontera.insertar(n_inicial)
    solucion = None

    while ((solucion == None) and (not(frontera.esVacia()))):
        n_actual=frontera.elimina()
        if n_actual.getProfundidad() >= int(prof_Max):
            break
        estadoActual = n_actual.getEstado()
        if prob.esObjetivo(estadoActual):
            solucion=True
        else:
            Ls=prob.getEspacioEstados().sucesores(n_actual.getEstado())
            Ln=crearListaNodosArbol(Ls, n_actual, prof_Max, estrategia)
            ListaNodosPoda,diccionarioPoda = poda(diccionarioPoda, Ln)
            frontera.insertarLista(ListaNodosPoda)

    if (solucion==None):
        return None,None
    else:
        return crearSolucion(n_actual),n_actual


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
        nodosGenerados=0
        solucion,n_final = busqueda_acotada (prob, estrategia, prof_Actual)
        prof_Actual = prof_Actual + inc_Prof


    return solucion,n_final


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
        exit()


    Prof_Max = int (sys.argv[1])
    Inc_Prof= int(sys.argv[2])
    Estrategia=(sys.argv[3]).lower()

    Prob = Problema.Problema ("problema.json")

    solucion,n_final=Busqueda(Prob, Estrategia, Prof_Max, Inc_Prof)

    if(solucion is not None):
        escribirSolucion(solucion,n_final,Estrategia) #Se escribe la solucion en un archivo .txt
        print("Algoritmo finalizado...")
    else:
        print("SIn solucion...")
