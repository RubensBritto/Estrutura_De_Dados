
#ROOT - recebe a raiz da tree
ROOT = 'root'

#Classe dos nós
from os import sendfile

class Node:
    #Recebe as chaves e seta os caminhos
    def __init__(self,country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual):
        self.country = str(country)
        self.region = str(region)
        self.happinessRank = str(happinessRank)
        self.happinessScore = str(happinessScore)
        self.standardError = str(standardError)
        self.economy = str(economy) 
        self.family = str(family)
        self.health = str(health)
        self.freedom = str(freedom)
        self.trust = str(trust)
        self.genorosity = str(genorosity)
        self.dystopiaResidual = str(dystopiaResidual)
        self.left = None
        self.right = None

    def __str__(self):
        print("Pais: " + self.country + " - " +"Região: " + self.region + " - " + "Rank Felicidade: " + self.happinessRank + " - " +
        "Score Felicidade: " + self.happinessScore+ " - " + "Erro Padrão: " + self.standardError + " - " +
        "Economia: " + self.economy+ " - " + "Familia: " + self.family + " - " +"Expectativa de vida: " + self.health + " - "
        " Indice de Liberdade: " + self.freedom+ " - " + " Indice de Confiança: " + self.trust + " - " +" Indice de Generosidade: " + self.genorosity+
        " Indice de Distopia Residual: " + self.dystopiaResidual)
        return str()

#Classe da árvore binária
class BinaryTree:
    #Definindo os pontos de cada caminho da árvore
    def __init__(self,country=None,region=None,happinessRank=None,happinessScore=None,standardError=None, economy=None, family =None,health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None, node=None):
        if node:
            self.root = node
        elif happinessRank:
            node = Node(country,region,happinessRank,happinessScore,standardError, economy, family,health, freedom, trust, genorosity, dystopiaResidual)
            self.root = node
        else:
            self.root = None
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
    

#Classe de árvore binária de Busca
class BinarySearchTree(BinaryTree):
    #Inserir dado - insere um novo dado na árvore
    def insert(self,country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual,escolha):
        parent = None
        x = self.root
        
        if escolha == 1:
            while(x):
                parent = x
                if int(happinessRank) < int(x.happinessRank):
                    x = x.left
                else:
                    x = x.right
            if parent is None:
                self.root = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            elif int(happinessRank) < int(parent.happinessRank):
                parent.left = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            else:
                parent.right = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
        
        elif escolha == 2:
            while(x):
                parent = x
                if float(economy) < float(x.economy):
                    x = x.left
                else:
                    x = x.right
            if parent is None:
                self.root = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            elif float(economy) < float(parent.economy):
                parent.left = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            else:
                parent.right = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
        
        elif escolha == 3:
            while(x):
                parent = x
                if float(health) < float(x.health):
                    x = x.left
                else:
                    x = x.right
            if parent is None:
                self.root = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            elif float(health) < float(parent.health):
                parent.left = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            else:
                parent.right = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)   
    
    #Busca - busca o item, atráves do index, na tree
    def searchHappinessRank(self, value):
        node = self.root
        while node is not None:
            if int(value) == int(node.happinessRank):
                return value
            elif int(value) < int(node.happinessRank):
                node = node.left
            elif int(value) > int(node.happinessRank):
                node = node.right
        return None

    #Busca - busca o item, atráves do index economy, na tree
    def searchEconomy(self, value):
        node = self.root
        while node is not None:
            if float(value) == float(node.economy):
                return value
            elif float(value) < float(node.economy):
                node = node.left
            elif float(value) > float(node.economy):
                node = node.right
        return None

    #Busca - busca o item, atráves do index health, na tree
    def searchHealth(self, value):
        node = self.root
        while node is not None:
            if float(value) == float(node.health):
                return value
            elif float(value) < float(node.health):
                node = node.left
            elif float(value) > float(node.health):
                node = node.right
        return None
    
    # Busca se o Pais existe na arvore  
    def searchCountry(self, value):
        node = self.root
        while node is not None:
            if str(value.lower()) in str(node.country.lower()):
                return value
            elif str(value.lower()) < str(node.country.lower()):
                node = node.left
            elif str(value.lower()) > str(node.country.lower()):
                node = node.right
        return None
    
    #Edita um item presente na tree
    def editarTree(self, index, dado, tipo):
        node = self.root
        while node is not None:
            if int(index) == int(node.happinessRank):
                if tipo == 1:
                    node.country = str(dado)
                    return self.insert(country=node.country,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 2:
                    node.region = str(dado)
                    return self.insert(country=None,region=node.region,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 3:
                    node.happinessScore = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=node.happinessScore,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 4:
                    node.standardError = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=node.standardError, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 5:
                    node.family = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=node.family, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 6:
                    node.freedom = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=node.freedom, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 7:
                    node.trust = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=node.trust, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 8:
                    node.genorosity = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=node.genorosity, dystopiaResidual=None,escolha=None)
                elif tipo == 9:
                    node.dystopiaResidual = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=node.dystopiaResidual,escolha=None)

            elif int(index) < int(node.happinessRank):
                node = node.left
            elif int(index) > int(node.happinessRank):
                node = node.right
        return None
#saveTree : Salva a árvore numa lista para poder ser exportada para csv
    def saveTree(self,value):
        listaTemp = []
        listaFinal = []
        node = self.root
        while node is not None:
            if int(value) == int(node.happinessRank):
                listaTemp.append(str(node.country))
                listaTemp.append(str(node.region))
                listaTemp.append(str(node.happinessRank)) 
                listaTemp.append(str(node.happinessScore))
                listaTemp.append(str(node.standardError)) 
                listaTemp.append(str(node.economy))
                listaTemp.append(str(node.family))
                listaTemp.append(str(node.health))
                listaTemp.append(str(node.freedom))
                listaTemp.append(str(node.trust))
                listaTemp.append(str(node.genorosity))
                listaTemp.append(str(node.dystopiaResidual))
                listaFinal.append(listaTemp)
                return (listaFinal,int(node.happinessRank))
            elif int(value) < int(node.happinessRank):
                node = node.left
            elif int(value) > int(node.happinessRank):
                node = node.right
        return (None,None)
    
    
    def _min(self, node=ROOT):
        if node == ROOT:
            node = self.root
       #Retorna o menor elemento da subárvore que tem self como raiz.
        while node.left:
            node = node.left
        return node.data
    
    #Remove da tree a partir do Happiness Rank, já reordenando a árvore
    def removeHappinessRank(self, data,node= ROOT):
        if node == ROOT:
            node = self.root
        
        if node is None:
            return None
        
        if int(data) < int(node.happinessRank):
            node.left = self.removeHappinessRank(data,node.left)
            
        if int(data) > int(node.happinessRank):
            node.right = self.removeHappinessRank(data,node.right)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substituto = self._min(node.right)
                node.happinessRank = substituto
                node.right = self.removeHappinessRank(substituto,node.right)
        return node
    
    #Remove da tree a partir do Economy, já reordenando a árvore
    def removeEconomy(self, data,node= ROOT):
        if node == ROOT:
            node = self.root
        
        if node is None:
            return None
        
        if float(data) < float(node.economy):
            node.left = self.removeEconomy(data,node.left)
            
        if float(data) > float(node.economy):
            node.right = self.removeEconomy(data,node.right)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substituto = self._min(node.right)
                node.economy = substituto
                node.right = self.removeEconomy(substituto,node.right)
        return node

    #Remove da tree a partir do Health, já reordenando a árvore
    def removeHealth(self, data,node= ROOT):
        if node == ROOT:
            node = self.root
        
        if node is None:
            return None
        
        if float(data) < float(node.health):
            node.left = self.removeHealth(data,node.left)
            
        if float(data) > float(node.health):
            node.right = self.removeHealth(data,node.right)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substituto = self._min(node.right)
                node.health = substituto
                node.right = self.removeHealth(substituto,node.right)
        return node