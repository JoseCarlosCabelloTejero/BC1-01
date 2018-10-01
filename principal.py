#!/usr/bin/python3
#############################################################################
##                              Sistemas Inteligentes                      ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

from graph import *

grafo = Grafo("./Datos/data/Anchuras.graphml.xml")

##### Ejemplo del petodo perteneceNodo

print("Ejemplo del metodo perteneceNodo")
print("Nodo: 4762868811 --> ",grafo.perteneceNodo("4762868811"))
print("Nodo 1234567890 --> ",grafo.perteneceNodo("1234567890"),'\n')

#### Ejemplo del metodo posicionNodo
print("Ejemplo del metodo posicionNodo")
print("Altitud y longitud del nodo: 4762868811 -->",grafo.posicionNodo("4762868811"))
print("Altitud y longitud del nodo que no existe -->",grafo.posicionNodo("1234567890"),'\n')
#### Ejemplo de adyacentes nodos
print("Ejemplo del metodo adyacentesNodo")
print("Nodos adyacentes del nodo: 4762868811")
aristas = grafo.adyacentesNodo("4762868811")
for i in aristas:
    print(i)
