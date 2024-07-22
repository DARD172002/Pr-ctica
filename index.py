from node import Node
class Lista():
    def __init__(self,nombre):
        self.cantNode=1
        self.nombreInit=nombre
        self.nodeInit=Node(self.nombreInit)
    def addLista(self,nombre):
        self.nombre=nombre
        self.nodeNuevo=Node(self.nombre)
        self.nodeInit.righP(self.nodeNuevo)
        self.nodeNuevo.leftP(self.nodeInit)
        self.nodeInit=self.nodeNuevo
        self.cantNode+=1
    def printLista(self):
        self.aux=self.nodeInit
        
        for i in range(self.cantNode):
           
            print(self.aux.nombreNode())
            self.aux=self.aux.getlelfP()
               
lista=Lista("hola")
lista.addLista("Nice")
lista.addLista("very")
lista.printLista()
a=10

        
    