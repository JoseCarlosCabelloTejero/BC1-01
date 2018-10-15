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

    def __init__(self,node,listNodes):
        self.node = node
        self.listNodes =sorted(listNodes)
        self.id = self.md5metodo(self.node,self.listNodes)


    def getNode(self):
        return self.node

    def getListNodes(self):
        return self.listNodes
