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
        #newCountry = input('Digite o nome do pais')
        self.country = newCountry
        itemTemp.append(newCountry)
        #verificar se ja existe 
        #newRegion = input('Digite o nome da regiao')
        self.region = newRegion
        itemTemp.append(newRegion)
        #newHappinessRank = input('Digite o rank da felicidade')
        self.happinessRank = newHappinessRank
        itemTemp.append(newHappinessRank)
        #verificar se já existe
        #newHappinessScore = input('Digite o score da felicidade')
        self.happinessScore = newHappinessScore
        itemTemp.append(newHappinessRank) 
        #newStandardError = input('Digite o Erro Padrão')
        self.standardError = newStandardError
        itemTemp.append(newStandardError)
        #newEconomy = input('Digite a economia')
        self.economy = newEconomy
        itemTemp.append(newEconomy)
        #newFamilyHealth = input('Digite a Saúde Família')
        self.familyHealth = newFamilyHealth
        itemTemp.append(newFamilyHealth)
        #newFreedom = input('Digite a Liberdade')
        self.freedom = newFreedom
        itemTemp.append(newFreedom)
        #newTrust = input('Digite a Confiança')
        self.trust = newTrust
        itemTemp.append(newTrust)
        #newDystopiaResidual = input('Digite a Distopia Residual')
        self.dystopiaResidual = newDystopiaResidual
        itemTemp.append(newDystopiaResidual)
        return itemTemp

        
    def editarDado(self):
        choose = input('Em qual linha/coluna deseja editar um novo dado?')
        if choose == 1:
            newCountry = input('Entre com o novo país:')
            self.country = newCountry
        elif choose == 2:
            newRegion = input('Entre com a nova região')
        pass