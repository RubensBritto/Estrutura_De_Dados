ROOT = 'root'

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
        
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
            print(node)
        if node.right:
            self.inorder_traversal(node.right)

class BinarySearchTree(BinaryTree):

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
    '''
    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return None
        if node.data == value:
            return node.data
        if value < node.data:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)
    '''
    '''
    def search(self, value):
        if  self.root == None:
            return None
        noAtual = self.root
        while noAtual.data != value:
            if value < noAtual.data:
                noAtual = noAtual.left
            else:
                noAtual = noAtual.right
            if noAtual == None:
                return None
        return noAtual
    '''

    def search(self, value, node=None):
        if node is None:
            print(node)
            return None
        else:
            if value == node.data:
                return value
            elif value < node.data:
                return self.search(value, node.left)
            else:
                return self.search(value, node.right)
    '''     
    def searchIndex(self, value, node=ROOT):
        if node == ROOT:
            node = self.root
        elif node is None:
            return node.data
        elif node.data == value:
            return False
        elif value < node.data:
            return self.search(value, node.left)
        else:
            return self.search(value, node.right)
    '''
    def searchIndex(self, value, node):
        if node is None:
            return node
        else:
            if node.data == value:
                return node.data
            elif value < node.data:
                return self.search(value, node.left)
            else:
                return self.search(value, node.right)
