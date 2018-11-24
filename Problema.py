import json
from EspacioDeEstados import EspacioDeEstados
from Estado import Estado

class Problema:

###############################################################################
#   Nombre del metodo: leerJson
#   Fecha de creacion: 17/10/2018
#   Version: 1.0
#   Argumentos de entrada: ruta del fichero json
#   Valor retornado: devuelve un diccionario correspondiente a leer el fichero json
#   Descripcion:   Utilizamos la bilbioteca Json para leer el fichero json y
#                  convertirlo en un diccionario donde podremos acceder a todos sus
#                  datos conociendo el nombre del campo.
################################################################################

    def leerJson(self,ficheroJson):
        jsondata=open(ficheroJson).read()
        data=json.loads(jsondata) #devuelve diccionario con los campos del json

        return data


    def __init__(self,ficheroJson):
        data=self.leerJson(ficheroJson)
        self.__espacioEstados=EspacioDeEstados(data.get('graphlmfile'))

        #Definicion del EstadoInicial
        OSM_inicial=data.get('IntSt').get('node')
        listNodes_inicial=data.get('IntSt').get('listNodes')
        heuristica=self.__espacioEstados.calcularHeuristica(OSM_inicial,listNodes_inicial)
        self.__estadoInicial=Estado(OSM_inicial,listNodes_inicial,heuristica)


###############################################################################
#   Nombre del metodo: esObjetivo
#   Fecha de creacion: 17/10/2018
#   Version: 1.0
#   Argumentos de entrada: Un objeto estado de la clase Estados
#   Valor retornado: Devuelve un booleano (True) si el estado es objetivo y
#                    (False) si no lo es
#   Descripcion:   Para saber si un estado es objetivo lo que hacemos es comprobar
#                  si la lista de nodos que le quedan por recorrer es vacia o no.
#                  Si esta vacia devolvemos True ya que el nodo es obejtivo, si no
#                  lo esta devolveremos False
################################################################################


    def getEstadoInicial(self):
        return self.__estadoInicial

    def getEspacioEstados(self):
        return self.__espacioEstados

    def esObjetivo(self,estado):

        return estado.getListNodes() == []
