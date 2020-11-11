#ROOT - recebe a raiz da tree
#ROOT = 'root'
#Country
#Region
# Happiness Rank
# Happiness Score
# Standard Error
# Economy (GDP per Capita)
# Family 
# Health (Life Expectancy)
# Freedom
# Trust (Government Corruption)
# Generosity
# Dystopia Residual

#Classe dos nós
class Node:
    #Recebe as chaves e seta os caminhos
    def __init__(self,country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual):
        self.country = country
        self.region = region
        self.happinessRank = happinessRank
        self.happinessScore = happinessScore
        self.standardError = standardError
        self.economy = economy 
        self.family = family
        self.health = health
        self.freedom = freedom
        self.trust = trust
        self.genorosity = genorosity
        self.dystopiaResidual = dystopiaResidual
        self.left = None
        self.right = None

    def __str__(self):
        #print(self.country)
        print("Pais: " + self.country + " - " +"Região: " + self.region + " - " + "Rank Felicidade: " + self.happinessRank + " - " +
        "Score Felicidade: " + self.happinessScore+ " - " + "Erro Padrão: " + self.standardError + " - " +
        "Economia: " + self.economy+ " - " + "Familia: " + self.family + " - " +"Expectativa de vida: " + self.health+
        " Indice de Liberdade: " + self.freedom+ " - " + " Indice de Confiança: " + self.trust + " - " +" Indice de Generosidade: " + self.genorosity+
        " Indice de Distopia Residual: " + self.dystopiaResidual)
        return str()

#Classe da árvore binária
class BinaryTree:
    #Definindo os pontos de cada caminho da árvore
    def __init__(self,country=None,region=None,happinessRank=None,happinessScore=None,standardError=None, economy=None, family =None,health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None, node=None):
        if node is None:
            self.root = node
        elif happinessRank:
            node = Node(country,region,happinessRank,happinessScore,standardError, economy, family,health, freedom, trust, genorosity, dystopiaResidual)
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
    def insert(self,country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual):
        parent = None
        x = self.root
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

    #Busca - busca o item, atráves do index, na tree
    def search(self, value):
        node = self.root
        while node is not None:
            if int(value) == int(node.happinessRank):
                return value
            elif int(value) < int(node.happinessRank):
                node = node.left
            elif int(value) > int(node.happinessRank):
                node = node.right
        return None
    
    def ordernar(self, country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual):
        node = self.root
        if node is None:
            return self.insert(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
        else:
            while node is not None:
                if int(happinessRank) < int(node.happinessRank):
                    node = node.left
                elif int(happinessRank) > int(node.happinessRank):
                    node = node.right
        
    
    def searchString(self, value):
        node = self.root
        print('aquii')
        while node is not None:
            if str(value.lower()) in str(node.country.lower()):
                print('hois')
                return value
            elif str(value.lower()) < str(node.country.lower()):
                print('boi')
                node = node.left
            elif str(value.lower()) > str(node.country.lower()):
                print('vaca')
                node = node.right
        return None
    
    def editarTree(self, index, dado, tipo):
        node = self.root
        while node is not None:
            if int(index) == int(node.happinessRank):
                if tipo == 1:
                    node.country = str(dado)
                    return self.insert(country=node.country,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)
                elif tipo == 2:
                    node.region = str(dado)
                    return self.insert(country=None,region=node.region,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)
                elif tipo == 3:
                    node.happinessRank = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)
                elif tipo == 4:
                    node.happinessScore = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=node.happinessScore,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)
                elif tipo == 5:
                    node.standardError = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=node.standardError, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)
                elif tipo == 6:
                    node.economy = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=node.economy, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)               
                elif tipo == 7:
                    node.family = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=node.family, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)
                elif tipo == 8:
                    node.health = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=node.health, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)
                elif tipo == 9:
                    node.freedom = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=node.freedom, trust=None, genorosity=None, dystopiaResidual=None)
                elif tipo == 10:
                    node.trust = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=node.trust, genorosity=None, dystopiaResidual=None)
                elif tipo == 11:
                    node.genorosity = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=node.genorosity, dystopiaResidual=None)
                elif tipo == 12:
                    node.dystopiaResidual = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=node.dystopiaResidual)

            elif int(index) < int(node.happinessRank):
                node = node.left
            elif int(index) > int(node.happinessRank):
                node = node.right
        return None

    def remove(self,country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual):

        if int(happinessRank) < int(self.happinessRank):
                self.left = self.left.remove(self,country=None,region=None,happinessRank=None,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self.right is None:
                    return self.left
            if self.left is None:
                return self.right
            #ao invés de remover o nó, copiamos os valores do nó substituto
                tmp = self.right._min()
                self.key, self.value = tmp.key, tmp.value
                self.right._remove_min()
            return self
    def _min(self):
       #Retorna o menor elemento da subárvore que tem self como raiz.
        if self.left is None:
            return self
        else:
            return self.left._min()
 
    def _remove_min(self):
        
        #Remove o menor elemento da subárvore que tem self como raiz.
        
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._removeMin()
        return self