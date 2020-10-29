#from main import main 
itemTemp = []

class opLista:
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

        return itemTemp

        
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