from fila import Queue
fila =  Queue()

class Pais:
    def __init__(self,name=None,region=None,happinessRank=None,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None):
        self.name = str(name)
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
        self.item = []
# criarDado - pega todas as informações necessárias para o cadastro e adiciona na fila 
# (caso não tenha um pais de mesmo nome)

    def insert(self, newCountry,newHappinessRank):
        try:
            self.item.insert(0,newCountry)
            newRegion = input('Digite o nome da regiao: ')
            self.item.append(newRegion)
            self.item.insert(2,newHappinessRank)
            newHappinessScore = float(input('Digite o score da felicidade: '))
            self.item.append(newHappinessScore)
            newStandardError = float(input('Digite o Erro Padrão: '))
            self.item.append(newStandardError)
            newEconomy = float(input('Digite a economia: '))
            self.item.append(newEconomy)
            newFamily = float(input('Digite da Família: '))
            self.item.append(newFamily)
            newHealth = float(input('Digite da Saúde: '))
            self.item.append(newHealth)
            newFreedom = float(input('Digite a Liberdade: '))
            self.item.append(newFreedom)
            newTrust = float(input('Digite a Confiança: '))
            self.item.append(newTrust)
            newGenerosity = float(input('Digite de Generosidade: '))
            self.item.append(newGenerosity)
            newDystopiaResidual = float(input('Digite a Distopia Residual: '))
            self.item.append(newDystopiaResidual)
            return(self.item)
        except:
            print("Erro de tipo")
            self.insert(newCountry,newHappinessRank)

# editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos

    def editar(self,sumario):
        
        print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
        print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
        print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
        choose = int(input())
        if choose == 1:
            editCountry = input('Entre com o novo nome do país: ')
            return (sumario,0,editCountry)
        
        elif choose == 2:
            editRegion = input('Entre com a novo nome da região: ')
            return(sumario,1,editRegion)

        elif choose == 3:
            editHappinessScore = int(input('Entre com o novo rank de Felicidade: '))
            return(sumario,2,editHappinessScore)
       
        elif choose == 4:
            editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
            return(sumario,3,editHappinessRank)
            
        elif choose == 5:
            editStandartError = float(input('Entre com o novo Erro Padrão: '))
            return(sumario,4,editStandartError)
            

        elif choose == 6:
            editEconomy = float(input('Entre com a novo valor da Economia: '))
            return(sumario,5,editEconomy)
            
        elif choose == 7:
            editFamily = float(input('Entre com o novo indice "Family": '))
            return(sumario,6,editFamily)
            

        elif choose == 8:
            editHealth = float(input('Entre com o novo indice "Health": '))
            return(sumario,7,editHealth)
            

        elif choose == 9:
            editFreedom = float(input('Entre com o novo indice de liberdade: '))
            return(sumario,8,editFreedom)
            

        elif choose == 10:
            editTrust = float(input('Entre com o novo indice de confiança: '))
            return(sumario,9,editTrust)
            

        elif choose == 11:
            editGenerosity = float(input('Entre com o novo indice "Generosity": '))
            return(sumario,10,editGenerosity)
            

        elif choose == 12:
            editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
            return(sumario,11,editDystopiaResidual)
            
