from os import sendfile

#Nesta classe nós simulamos uma pilha implementada do zero. Basicamente definimos todas as funções que uma pilha tem 
#implementada e acessamos seus métodos na main como se fosse uma função nativa da linguagem, praticamente!

"""
Temos basicamente as seguintes funções: 
- isEmpty = verifica se a pilha está vazia
- push = adiciona um elemento (seja string, int, ou até mesmo listas)
- pop = remove um elemento da pilha, no caso, por se tratar de uma pilha, o último item
- peek = retorna o último elemento da pilha, para consultas ou implementações
- size = retorna o tamanho da pilha
- percorrerStack = percorrer a lista e verifica se determinado dado está na lista
- desempilhar = desempilha a lista para que determinado elemento possa ser removido
- returnLast = retorna o último item da lista, pórem diferente da peek, este método pode ser alterado
- stackEditar = método usado para acessar e editar determinado item da pilha
- indiceStack = retorna o indice na pilha em que o dado procurado está posicionado
- showStack = imprime na tela todos os itens presentes na pilha
"""

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
    
    def percorrerStack(self, j, dado):
        for i in range(self.size()):
            if (str(dado.lower()) in self.items[i][j].lower()):
                return True

    def desempilhar(self, j, dado):
         for i in range(self.size()):
            if (dado.lower() in self.items[i][j].lower()):
                return i

    def returnLast(self, i):
        return self.items[i]
    
    def stackEditar(self, i, j, dados):
        self.items[i][j] = str(dados)
    
    def indiceStack(self,j,dado):
        for i in range(self.size()):
            if (dado.lower() in self.items[i][j].lower()):
                return i

    def showStack(self,i):
        return self.items[i]
    
    def ordenar(indexItem):
        pass