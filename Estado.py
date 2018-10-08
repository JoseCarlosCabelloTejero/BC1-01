#!/usr/bin/python3
#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: BC1 - 01                       Curso: 2018 / 2019             ##
#############################################################################

import hashlib

class Estado:

    def md5(self,id,lista):
        m = hashlib.md5()
        m.update(id)
        m.update(lista)
        return m.hexdigest()

    def __init__(self):
        self.node = 4331489739
        self.listNodes =["4331489528","4331489668","4331489711","4762868815","4928063625"]
        self.id =  self.md5(self.node,self.listNodes)



    def prueba():
        print(self.id)
