

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def showQueue(self,i):
        return self.items[i]

    #Procura o elemento na fila e retorna true or false
    def percorrerQueue(self, j, dado):
        for i in range(self.size()):
            if (str(dado.lower()) in self.items[i][j].lower()):
                return True
        return False
    #Retorna o indice do elemento na fila
    def indiceQueue(self,j,dado):
        for i in range(self.size()):
            if (dado.lower() in self.items[i][j].lower()):
                return i
    
    def queueEditar(self, i, j, dados):
        self.items[i][j] = str(dados)
    

    def unqueue(self, j, dado):
         for i in range(self.size()):
            if (str(dado.lower()) in self.items[i][j].lower()):
                return i
    
    def returnLast(self, i):
        return self.items[i]