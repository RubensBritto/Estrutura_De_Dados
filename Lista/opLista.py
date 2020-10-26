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
        choose = int(input('Em qual linha/coluna deseja editar um novo dado?'))
        if choose == 1:
            editCountry = input('Entre com o novo nome do país: ')
        elif choose == 2:
            editRegion = input('Entre com a novo nome da região: ')
        elif choose == 3:
            editHappinessRank = input('Entre com o novo Indice de Felicidade: ')
        elif choose == 4:
            editHappinessScore = input('Entre com o novo rank de Felicidade: ')
        elif choose == 5:
            editStandartError = input('Entre com o novo Erro Padrão: ')
        elif choose == 6:
            editEconomy = input('Entre com a novo valor da Economia: ')
        elif choose == 7:
            editFamilyHealth = input('Entre com o novo indice "Family health": ')
        elif choose == 8:
            editFreedom = input('Entre com o novo indice de liberdade: ')
        elif choose == 9:
            editTrust = input('Entre com o novo indice de confiança: ')
        elif choose == 10:
            editDystopiaResidual = input('Entre com a nova distopia Residual: ')
        pass