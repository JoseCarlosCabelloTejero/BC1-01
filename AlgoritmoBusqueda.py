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
import gpxpy
import gpxpy.gpx


archivoSolucion="solucion.txt"     			 #Fichero txt en el que se escribirá la solución.
archivo_gpx="camino.gpx"					#Archivo .gpx con la solución
archivoJSON= "problema.json"      #fichero json con información del fichero grapml
                                    		#de entrada y el estado inicial.

estrategiasBusqueda=["anchura","costo","profundidad","prof_acotada","prof_ite","voraz","a*"]
nodosGenerados = 0


###############################################################################
#   Nombre del metodo: escribirSolucion
#   Fecha de creacion: 29/10/2018
#   Version: 1.1
#   Argumentos de entrada:
#                     -solucion: Lista con la secuencia de acciones que
#                                componen la solucion al problema
#                     -n_final:  Nodo objetivo al que se ha llegado. Se utiliza
#                                para obtener el costo y profundidad de la solución.
#                     -estrategia: string que indica
#
#   Descripcion: Escribe en un fichero de texto 'solucion.txt' la solución
#               encontrada al problema definido en el fichero 'problema.json'
#               Se escribe en el fichero de salida:
#                    -Estrategia utilizada
#                    -Profundidad de la Solucion
#                    -Total de nodos generados
#                    -Costo del camino que va desde el nodo Inicial al nodo Objetivo
#                    -Secuencia de nodos que se visitan hasta llegar a la solución
#
################################################################################

def escribirSolucion(solucion,n_final,estrategia,problema):
    gpx = gpxpy.gpx.GPX()
    # Create first track in our GPX:
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)


    # Create first segment in our GPX track:
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    with open(archivoSolucion,'w') as f:
        f.write("La solucion es: \nEstrategia: {}\n".format(estrategia))
        f.write("Total de nodos generados: {}\n".format(nodosGenerados))
        f.write("Costo: {}\n".format(round(n_final.getCosto(),2)))
        f.write("Profundidad: {}\n\n\n".format(n_final.getProfundidad()+1))

        for nodo in solucion:
            nodoOSM=nodo.getEstado().getNode()
            posicionOSM=problema.getEspacioEstados().getGrafo().posicionNodo(nodoOSM)

            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(posicionOSM[1], posicionOSM[0]))
            
            f.write(nodo.getAccion())
            f.write(" F: {}".format(round(nodo.getF(),2)))
            f.write("\nEstoy en {} y tengo que visitar:{} \n\n".format(nodo.getEstado().getNode(),
                nodo.getEstado().getListNodes()))
        f.close()

    with open(archivo_gpx,'w') as f:
        f.write(gpx.to_xml())
        f.close()


###############################################################################
#   Nombre del metodo: crea_nodo
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada: Elementos necesarios para crear una instancia de Nodo.
#   Valor retornado: Nodo sucesor del Nodo Padre pasado como entrada.
#   Descripcion: Función que se utiliza dentro de 'busqueda_acotada' para crear
#                 el nodo inicial.
#
#
################################################################################

def crea_nodo(padre, estado, costo, estrategia,accion):
    nodo=Nodo.Nodo(padre,estado,costo,estrategia,accion)
    return nodo


###############################################################################
#   Nombre del metodo: crearListaNodosArbol
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada:         -Ls: Lista [accion, estadoNuevo, coste] que
#                                       representa el conjunto de acciones
#                                       disponibles para un nodo 'padre' generada
#                                       por la función sucesor
#
#                                  -padre: Nodo padre del que se van a generar nodos
#                                          sucesores.
#
#                                  -estrategia: Estrategia utilizada para generar
#                                               el árbol de búsqueda. Es necesario
#                                               para crear objetos Nodo.
#
#   Valor retornado:                -Ln: Lista de nodos descendientes de 'padre'
#
#   Descripcion: Para cada acción de la lista Ls, se generan todos los nodos
#                descendientes de 'padre', como consecuencia de aplicar dichas
#                acciones
#               Utilizamos una variable global 'nodosGenerados' para llevar una
#               cuenta de los nodos generados durante el proceso de búsqueda de
#               la solución.
#
#
################################################################################

def crearListaNodosArbol(Ls, padre, prof_Max, estrategia):
    Ln=[]
    global nodosGenerados

    if (padre.getProfundidad() < int(prof_Max)):
        for sucesor in Ls:
            accion=sucesor[0]
            estado=sucesor[1]
            coste=sucesor[2]
            nodo=crea_nodo(padre,estado,coste,estrategia,accion)
            Ln.append(nodo)

            nodosGenerados += 1
    return Ln


###############################################################################
#   Nombre del metodo: crearSolucion
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada: nodo final
#
#   Valor retornado: Lista con la secuencia de nodos que hay que recorrer para
#                    llegar desde el nodo inicial al nodo objetivo. Cada uno de
#                    estos nodos contiene la acción que hay realizar para pasar
#                    de un nodo al siguiente de tal forma que la solución será
#                    una secuencia de acciones tal y como indica su definición.
#
#   Descripcion: Se van obteniendo todos los antecesores del nodo objetivo hasta
#                 llegar al nodo inicial. Cada nodo obtenido se introduce en una
#                 pila FIFO para que, posteriormente al sacarlos de la pila e
#                 introducirlos en la lista 'solucion' que se retorna, queden
#                 ordenados desde el nodo inicial al nodo que satisface la función
#                 esObjetivo.
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

###############################################################################
#   Nombre del metodo: poda
#   Fecha de creacion: 05/11/2018
#   Version: 1.0
#   Argumentos de entrada:  -diccionarioPoda: Diccionario que contiene los Estados
#                                            del Espacio de Estados que han sido
#                                            visitados y el mínimo valor de f para
#                                            cada uno de estos estados.
#                            - Ln: Lista con el conjunto de nodos sucesores de un
#                                   determinado nodo
#   Valor retornado:        -diccionarioPoda actualizado
#                           -ListaNodosPoda. Lista con los nodos han de añadirse
#                                            a la frontera. (LN - nodosPodados)
#   Descripcion: Función que implementa la poda de nodos cuyos estados ya están
#                en otros nodos generados y tengan una f mayor. Para llevar a cabo
#                la poda utilizamos un diccionario
#                Para cada Nodo de (LN) comprobamos si ese estado ya existe en el
#                diccionario (esto es, ese estado se encuentra en otro nodo ya
#                generado)
#                De ser afirmativo, comprobamos si el valor de f en el nuevo nodo es
#                menor que el mínimo valor de f en nodos ya generados para ese
#                mismo estado. Si es así, no podaremos el nodo y actualizamos el
#                mínimo valor de f.
#                Por otro lado, si el estado del nodo no se encuentra en el
#                diccionario, significa que ese estado aún no ha sido visitado.
#                Actualizamos el diccionario para futuras podas y tampoco podamos
#                dicho nodo.
################################################################################

def poda(diccionarioPoda, Ln,estrategia):

    ListaNodosPoda = []

    for nodo in Ln:
        estadoNodo = nodo.getEstado()
        idEstado = estadoNodo.getId()
        F_estado = nodo.getF()

        if( idEstado in diccionarioPoda):
            if (estrategia in ["profundidad","prof_ite","prof_acotada"]):
                if F_estado > int(diccionarioPoda.get(idEstado)):
                    diccionarioPoda.update({idEstado:F_estado})
                    ListaNodosPoda.append(nodo)
            else:
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
#   Argumentos de entrada:      -prob: Problema creado con el archivo .json de
#                                      entrada
#                               -estrategia. Estrategia utilizada para generar
#                                            el arbol de búsqueda
#                               -prof_Max. Profundidad máxima del árbol de búsqueda,
#                                           los nodos cuya profundidad sea igual
#                                           a la profundidad máxima se consideran
#                                           nodos hoja.
#   Valor retornado:            - Lista con la secuencia de nodos que hay que
#                                recorrer para llegar desde el nodo inicial al
#                                nodo objetivo, generada por la función crearSolucion
#                               -Nodo cuyo estado verifica la función esObjetivo
#
#                               Si no se ha encontrado solución devuelve None,None
#
#   Descripcion:    Algoritmo básico de búsqueda que genera un árbol de Búsqueda
#                    a partir del estado inicial y la función sucesor.
#                    La raíz del arbol de búsqueda (n_inicial) es el nodo que
#                    corresponde al estado inicial definido por el problema ('prob')
#
#
################################################################################

def busqueda_acotada (prob, estrategia, prof_Max):

    diccionarioPoda = {}

    frontera = Frontera.Frontera()
    estado_inicial = prob.getEstadoInicial()
    n_inicial = crea_nodo (None, estado_inicial, 0, estrategia, '0.0 0 0.0')
    frontera.insertar(n_inicial)
    solucion = None

    while ((solucion == None) and (not(frontera.esVacia()))):
        n_actual=frontera.elimina()
        estadoActual = n_actual.getEstado()
        if prob.esObjetivo(estadoActual):
            solucion=True
        else:
            Ls=prob.getEspacioEstados().sucesores(estadoActual)
            Ln=crearListaNodosArbol(Ls, n_actual, prof_Max, estrategia)
            ListaNodosPoda,diccionarioPoda = poda(diccionarioPoda, Ln,estrategia)
            frontera.insertarLista(ListaNodosPoda)


    if (solucion==None):
        return None,None
    else:
        return crearSolucion(n_actual),n_actual


###############################################################################
#   Nombre del metodo: Busqueda
#   Fecha de creacion: 29/10/2018
#   Version: 1.0
#   Argumentos de entrada:      -prob: Problema
#                               -estrategia: Estrategia utiliza para generar el
#                                            Árbol de Búsqueda
#                               -Prof_Max: Profundidad maxima
#                               -inc_Prof: Un incremento para la profundidad,
#                                          necesario para una estrategia
#                                          Profundidad Iterativa.
#   Valor retornado:            -Solucion: Lista de Nodos que se visitan para ir
#                                           desde el estado inicial al nodo objetivo
#                                           En caso de no haber encontrado solución
#                                           se devuelve 'None'
#                               -n_final: ÚLtimo nodo que se ha visitado. En caso de
#                                         haber encontrado solución, será el nodo
#                                         que verifica el test esObjetivo. En caso
#                                          contrario se devuelve 'None'
#
#   Descripcion: Algoritmo básico de búsqueda necesario para implementar las
#                estrategias de anchura, costo uniforme y profundidad (simple,
#                acotada e iterativa)
#
#
#
################################################################################

def Busqueda(prob, estrategia, prof_Max, inc_Prof):

    prof_Actual = inc_Prof
    solucion = None

    while ((solucion == None) and (prof_Actual<= prof_Max)):
        global nodosGenerados
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

    Prob = Problema.Problema (archivoJSON)

    solucion,n_final=Busqueda(Prob, Estrategia, Prof_Max, Inc_Prof)

    if(solucion is not None):
        escribirSolucion(solucion,n_final,Estrategia,Prob) #Se escribe la solucion en un archivo .txt
        print("Algoritmo finalizado...")
    else:
        print("Sin solucion...")
