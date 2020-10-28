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
        for i in range(len(self.items)):
            if (dado.lower() in self.items[i][j].lower()):
                return True

    def showStack(self,i):
        return self.items[i]
    