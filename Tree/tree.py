#ROOT - recebe a raiz da tree
#ROOT = 'root'

#Classe dos nós
class Node:
    #Recebe as chaves e seta os caminhos
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

#Classe da árvore binária
class BinaryTree:
    #Definindo os pontos de cada caminho da árvore
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    #Função recursiva de percorrer árvore    
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
            print(node)
        if node.right:
            self.inorder_traversal(node.right)
            print(node)
    

#Classe de árvore binária de Busca
class BinarySearchTree(BinaryTree):
    #Inserir dado - insere um novo dado na árvore
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    #Busca - busca o item, atráves do index, na tree
    def search(self, value):
        node = self.root
        while node is not None:
            if int(value) == int(node.data):
                return node
            elif value < node.data:
                node = node.left
            elif value > node.data:
                node = node.right
        return None
    '''
    def search(self, data):
        return self.findNode(self.root, data)

    def findNode(self, currentNode, data):
        if(currentNode is None):
            return False
        elif(int(data) == int(currentNode.data)):
            return True
        elif(data < currentNode.data):
            return self.findNode(currentNode.left, data)
        else:
            return self.findNode(currentNode.right, data)
        
    '''
    #Busca por index - retorna o nó em que estar o index do item 
    def searchIndex(self, value, node):
        if node is None:
            return node
        else:
            if int(node.data) == int(value):
                return node.data
            elif value < node.data:
                return self.search(value, node.left)
            else:
                return self.search(value, node.right)
