import json
from EspacioDeEstados import EspacioDeEstados
from Estado import Estado

class Problema:


    def leerJson(self,ficheroJson):
        jsondata=open(ficheroJson).read()
        data=json.loads(jsondata) #devuelve diccionario con los campos del json

        return data


    def __init__(self,ficheroJson):
        data=leerJson(ficheroJson)
        self.__espacioEstados=EspacioDeEstados(data.get('graphlmfile'))
        self.__estadoInicial=Estado(data.get('IntSt').get('node'),
        data.get('IntSt').get('listNodes'))


    def esObjetivo(self,estado):
        return (estado.getListNodes()==[])
