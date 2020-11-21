'''
Class Queue - Classe da fila para realizar as operações

_init_: inicia a fila
isEmpty : retorna se a fila está vazia ou não
enqueue : insere um novo dado na Fila
dequeue : remove o primeiro item na Fila
size : retorna o tamanho da fila
showQueue: exibe a fila
percorrerQueue: retorna se determinado elemento existe ou não
indiceQueue: retorna o indice do elemento passado na Fila
editarQueue: edita um elemento na fila (caso ele exista!)
unqueue: reordena a fila caso o elemento que se deseja tirar não estiver no inicio
returnLast: retorna o último elemento da fila
'''

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
        if j == 0:
            for i in range(self.size()):
                if (str(dado.lower()) in self.items[i][j].lower()):
                    return True
            return False
        elif j == 2:
            for i in range(self.size()):
                if (dado in self.items[i][j]):
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