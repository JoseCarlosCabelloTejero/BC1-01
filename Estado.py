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

    def __init__(self):
        self.node = "4331489739"
        self.listNodes =["4331489528","4331489668","4331489711","4762868815","4928063625"]
        self.id = self.md5metodo(self.node,self.listNodes)


    def getNode(self):
        return self.node

    
