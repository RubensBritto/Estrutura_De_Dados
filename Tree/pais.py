from tree import BinaryTree
fila =  Queue()

class Pais:
    def __init__(self):
        self.name = None
        self.region = None
        self.happinessRank = None
        self.happinessScore = None
        self.standardError = None
        self.economy = None
        self.family = None
        self.health = None
        self.freedom = None
        self.trust = None
        self.genorosity = None
        self.dystopiaResidual = None
        self.item = []

    def insert(self,name,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual):
        self.name = str(name)
        self.item.append(self.name)
        self.region = str(region)
        self.item.append(self.region)
        self.happinessRank = str(happinessRank)
        self.item.append(self.happinessRank)
        self.happinessScore = str(happinessScore)
        self.item.append(self.happinessScore)
        self.standardError = str(standardError)
        self.item.append(self.standardError)
        self.economy = str(economy)
        self.item.append(self.economy) 
        self.family = str(family)
        self.item.append(self.family)
        self.health = str(health)
        self.item.append(self.health)
        self.freedom = str(freedom)
        self.item.append(self.freedom)
        self.trust = str(trust)
        self.item.append(self.trust)
        self.genorosity = str(genorosity)
        self.item.append(self.genorosity)
        self.dystopiaResidual = str(dystopiaResidual)
        self.item.append(self.dystopiaResidual)
        return self.item

    def editar(self,data,escolha):
        if escolha == 0:
            self.name = str(data)
            return self.name
        elif escolha == 1:
            self.region = str(data)
            return self.region
        elif escolha == 2:
            self.happinessRank = str(data)
            return self.happinessRank
        elif escolha == 3:   
            self.happinessScore = str(data)
            return self.happinessScore
        elif escolha == 4:
            self.standardError = str(data)
            return self.standardError
        elif escolha == 5:
            self.economy = str(data)
            return self.economy
        elif escolha == 6:   
            self.family = str(data)
            return self.family
        elif escolha == 7:
            self.health = str(data)
            return self.health
        elif escolha == 8:
            self.freedom = str(data)
            return self.freedom
        elif escolha == 9:
            self.trust = str(data)
            return self.trust
        elif escolha == 10:
            self.genorosity = str(data)
            return self.genorosity
        elif escolha == 11:
            self.dystopiaResidual = str(data)
            return self.dystopiaResidual

