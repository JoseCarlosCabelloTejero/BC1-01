#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import hashlib

class Estado:

    def md5metodo(self,id,lista):
        n=0
        m = hashlib.md5()
        m.update(id.encode())
        for i in lista:
            m.update(lista[n].encode())
            n=n+1
        return m.hexdigest()

    def __init__(self,nodo,listaNodos):
        self.node = nodo
        self.listNodes =sorted(listaNodos)
        self.idEstado = self.md5metodo(self.node,self.listNodes)


    def node(self):
        return self.nodes

    def listNodes(self):
        return self.listNodes
        
    def idEstado(self):
        return self.idEstado
