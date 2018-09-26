#!/usr/bin/python3
#############################################################################
##                              Sistemas Inteligentes                      ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

from graph import *

grafo = Grafo("./Datos/data/Anchuras.graphml.xml")

#print(list(grafo.getGraph()))
#print(len(list(grafo.getGraph())))

#print(grafo.perteneceNodo('4762868811'))


#print(grafo.posicionNodo('4762868811'))

#print(grafo.posicionNodo('4762868811'))


aristas = grafo.adyacentesNodo("946409156")

for i in aristas:
    print(i)
