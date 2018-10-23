#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import graph


class EspacioDeEstados:

    def __init__(self,fichero):
        self.__grafo=Grafo(fichero)

###############################################################################
#   Nombre del metodo: esta
#   Fecha de creacion: 09/10/2018
#   Version: 1.0
#   Argumentos de entrada: un objeto estado de la clase Estado
#   Valor retornado: Un booleano, True si el estado esta en el espacio de estados
#                    y false si el estado no esta en el espacio de estados
#   Descripcion:   Lo primero que comprobamos es que el nodo del estado forma parte
#                  del grafo, si no es asi directamente devolvemos False ya que ese
#                  estado no formara parte del espacio de estados. Si el nodo está
#                  en el grafo ahora comprobamos que la lista de nodos que le quedan
#                  por recorrer del estado pertenecen al grafo, si es asi se devolvera
#                  true, si no es asi devolveremos false.
################################################################################

    def esta(self,estado):
        if not (self.__grafo.perteneceNodo(estado.getNode())):
            return False
        else:
            for i in estado.getListNodes():
                if not(self.__grafo.perteneceNodo(i)):
                    return False
        return True

###############################################################################
#   Nombre del metodo: sucesores
#   Fecha de creacion: 09/10/2018
#   Version: 1.0
#   Argumentos de entrada: un objeto estado
#   Valor retornado: La lista de los sucesores de ese estado
#   Descripcion:   Este metodo lo que primero hara es crear una lista con todos
#                  Los adyacentes del nodo del estado dado. Se recorre esta lista
#                  de adyacentes y creando una cadena de la forma:
#                  "Estoy en +nodo_del_estado + y voy a + nodo_adyacente + nombre_calle"
#                  Ademas crearemos el estado nuevo y calcularemos el coste de llegar
#                  al nuevo estado. Esto lo metemos en una lista de la forma:
#                  [accM,estadoNuevo,coste] siendo accM la cadena que hemos creado.
################################################################################

    def sucesores(self,estado):

        listaSucesores = []

        listaDeAdyacentes = self.__grafo.adyacentesNodo(estado.getNode())

        for ady in listaDeAdyacentes:
            nombreCalle = ady[2]
            accM = "Estoy en ",estado.getNode(),"y voy a ",ady[1],",",nombreCalle
            estadoNuevo = Estado(ady[1],estado.getListNodes().remove(ady[1]))
            coste = ady[3]

            listaSucesores.append([accM,estadoNuevo,coste])

        return listaSucesores
