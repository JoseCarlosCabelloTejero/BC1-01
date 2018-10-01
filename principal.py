#!/usr/bin/python3
#############################################################################
##                              Sistemas Inteligentes                      ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

from graph import *

grafo = Grafo("./Datos/data/Anchuras.graphml.xml")
idNodo="946409139"

##### Ejemplo del petodo perteneceNodo

print("Ejemplo del metodo perteneceNodo")
print("Nodo: ",idNodo," --> ",grafo.perteneceNodo(idNodo))
print("Nodo 1234567890 --> ",grafo.perteneceNodo("1234567890"),'\n')

#### Ejemplo del metodo posicionNodo
print("Ejemplo del metodo posicionNodo")
print("Altitud y longitud del nodo:",idNodo," -->",grafo.posicionNodo(idNodo))
print("Altitud y longitud del nodo que no existe -->",grafo.posicionNodo("1234567890"),'\n')
#### Ejemplo de adyacentes nodos
print("Ejemplo del metodo adyacentesNodo")
print("Nodos adyacentes del nodo ",idNodo,":")
aristas = grafo.adyacentesNodo(idNodo)
for i in aristas:
    print(i)
