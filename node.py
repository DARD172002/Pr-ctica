class Node():
    def __init__(self,nombre):
        self.nombre=nombre
        self.puntLEFT=None
        self.puntRight=None
    def righP(self,node):
        self.puntRight=node
    def leftP(self,node):
        self.puntLEFT=node
    def getlelfP(self):
        return self.puntLEFT
    def getRight(self):
        return self.puntRight
    def nombreNode(self):
        return self.nombre