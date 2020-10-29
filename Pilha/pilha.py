from os import sendfile


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def percorrer(self, j, dado):
        for i in range(self.size()):
            if (str(dado.lower()) in self.items[i][j].lower()):
                return True
    def percorrer2(self, j, dado):
         for i in range(self.size()):
            if (dado.lower() in self.items[i][j].lower()):
                return self.items[i]
    
    def stackEditar(self, i, j, dados):
        self.items[i][j] = str(dados)
    
    def indiceStack(self,j,dado):
        for i in range(self.size()):
            if (dado.lower() in self.items[i][j].lower()):
                return i

    def showStack(self,i):
        return self.items[i]
    