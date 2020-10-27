#from main import main 
itemTemp = []

class opLista:
    '''
    def __init__(self, country, region, happinessRank, happinessScore, standardError, economy, familyHealth, freedom, trust, dystopiaResidual):
        self.country = country
        self.region = region 
        self.happinessRank =  happinessRank
        self.happinessScore = happinessScore
        self.standardError =  standardError
        self.economy =  economy
        self.familyHealth =  familyHealth
        self.freedom = freedom
        self.trust = trust
        self.dystopiaResidual = dystopiaResidual
        pass
    '''
    def criarNewDado(self, newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError, newEconomy, newFamilyHealth, newFreedom, newTrust, newDystopiaResidual):
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
        self.familyHealth = newFamilyHealth
        itemTemp.append(str(newFamilyHealth))
        self.freedom = newFreedom
        itemTemp.append(str(newFreedom))
        self.trust = newTrust
        itemTemp.append(str(newTrust))
        self.dystopiaResidual = newDystopiaResidual
        itemTemp.append(str(newDystopiaResidual))
        return itemTemp

        
    def editarCountry(self, newCountry):
        self.country = newCountry
        pass
    def editarRegion(self, newRegion):
        self.region = newRegion
        pass
    def editarHappinessRank(self, newHappinessRank):
        self.happinessRank = newHappinessRank
        pass
    def editarHappinessScore(self, newHappinessScore):
        self.happinessScore = newHappinessScore
        pass
    def editarStandardError(self, newStandardError):
        self.standardError = newStandardError
        pass
    def editarEconomy(self, newEconomy):
        self.economy = newEconomy
        pass
    def editarFamilyHealth(self, newFamilyHealth):
        self.familyHealth = newFamilyHealth
        pass
    def editarFreedom(self, newFreedom):
        self.freedom = newFreedom
        pass
    def editarTrust(self, newTrust):
        self.trust = newTrust
        pass
    def editarDystopiaResidual(self, newDystopiaResidual):
        self.dystopiaResidual = newDystopiaResidual
        pass