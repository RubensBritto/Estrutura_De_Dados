#from main import main 
itemTemp = []

class opLista:
    #Função criarDados() - Função que adciona um novo dado na lista (adcionando todas as informações de um novo país)
    #Usamos uma lista temporaria para ir guardando cada item necessário para completar uma linha de dados, depois
    #Retornamos esse valor para ser adcionado na lista original
    def criarNewDado(self, newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError, newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity,newDystopiaResidual):
        itemTemp.clear()
        
        self.country = newCountry
        itemTemp.append(newCountry)

        self.region = newRegion
        itemTemp.append(newRegion)

        self.happinessRank = newHappinessRank
        itemTemp.append(str(newHappinessRank))

        self.happinessScore = newHappinessScore
        itemTemp.append(str(newHappinessRank))
        
        self.standardError = newStandardError
        itemTemp.append(str(newStandardError))

        self.economy = newEconomy
        itemTemp.append(str(newEconomy))

        self.family = str(newFamily)
        itemTemp.append(str(newFamily))

        self.health = str(newHealth)
        itemTemp.append(str(newHealth))

        self.freedom = newFreedom
        itemTemp.append(str(newFreedom))
        
        self.trust = newTrust
        itemTemp.append(str(newTrust))

        self.generosity= newGenerosity
        itemTemp.append(str(newGenerosity))
        
        self.dystopiaResidual = newDystopiaResidual
        itemTemp.append(str(newDystopiaResidual))
        #Retorno da lista com todas as novas informações
        return itemTemp

    #Campo das edições de dados: as funções a seguir permite editar cada item da base de dados validas!
    #Colocamos em métodos separadas para melhorar a eficiência do retorno.
    def editarCountry(self, newCountry):
        self.country = newCountry
        return str(newCountry)
        
    def editarRegion(self, newRegion):
        self.region = newRegion
        return str(newRegion)
        
    def editarHappinessRank(self, newHappinessRank):
        self.happinessRank = newHappinessRank
        return str(newHappinessRank)
        
    def editarHappinessScore(self, newHappinessScore):
        self.happinessScore = newHappinessScore
        return str(newHappinessScore)
        
    def editarStandardError(self, newStandardError):
        self.standardError = newStandardError
        return str(newStandardError)
        
    def editarEconomy(self, newEconomy):
        self.economy = newEconomy
        return str(newEconomy)
        
    def editarFamily(self, newFamily):
        self.familyHealth = newFamily
        return str(newFamily)

    def editarHealth(self, newHealth):
        self.health = newHealth
        return str(newHealth)
        
    def editarFreedom(self, newFreedom):
        self.freedom = newFreedom
        return str(newFreedom)
        
    def editarTrust(self, newTrust):
        self.trust = newTrust
        return str(newTrust)
        
    def editarGenerosity(self,newGenerosity):
        self.generosity = newGenerosity
        return str(newGenerosity)
        
    def editarDystopiaResidual(self, newDystopiaResidual):
        self.dystopiaResidual = newDystopiaResidual
        return str(newDystopiaResidual)