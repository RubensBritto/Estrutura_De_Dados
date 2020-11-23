from tree import BinarySearchTree
tree = BinarySearchTree()

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

# Insert - pega todas as informações necessárias para o cadastro e adiciona na arvore 
# (caso não tenha um pais de mesmo nome)

    def insert(self,lastData,escolha,rank):
        try:
            newEconomy = 0
            newHealth = 0
            newHappinessRank = ''
            newRegion = ''
            #try:
            newCountry = input('Digite o nome do pais: ')
            if tree.searchCountry(newCountry) != None:
                print("Pais já existe")
            else:
                newRegion = input('Digite o nome da regiao: ')
            if escolha == 1:
                newHappinessRank = int(rank)+1
                print("O seu Rank é: " + str(newHappinessRank))
                newEconomy = float(input('Digite o Indice economico: '))
                newHealth = float(input('Digite a Expectativa de Vida: '))
            
            elif escolha == 2:
                newHappinessRank = input("Digite o seu rank: ")
                if tree.searchHappinessRank(newHappinessRank) != None:
                    print("Pais Já Existe")
                    print("Inicie novamente")
                    self.insert(lastData,escolha,rank)
                else:
                    print("Digite um indice de economia maior que: " + str(lastData))
                    newEconomy = float(input('Digite o Indice economico: '))
                    if newEconomy < float(lastData):
                        self.insert(lastData,escolha,rank)
                    else:
                        newHealth = float(input('Digite a Expectativa de Vida: '))
            
            elif escolha == 3:
                newHappinessRank = input("Digite o seu rank: ")
                if tree.searchHappinessRank(newHappinessRank) != None:
                    print("Pais Já Existe")
                    print("Inicie novamente")
                    self.insert(lastData,escolha,rank)
                print("Digite um indice de expectativa de vida maior que: " + str(lastData))
                newHealth = float(input('Digite a Expectativa de Vida: '))
                if newHealth < float(lastData):
                    self.insert(lastData,escolha,rank)
                else:
                    newEconomy = float(input('Digite o Indice economico: '))   
            #salvar o novo indice in the tree
            newHappinessScore = float(input('Digite o score da felicidade: '))
            newStandardError = float(input('Digite o Erro Padrão: '))
            newFamily = float(input('Digite da Família: '))
            newFreedom = float(input('Digite a Liberdade: '))
            newTrust = float(input('Digite a Confiança: '))
            newGenerosity = float(input('Digite de Generosidade: '))
            newDystopiaResidual = float(input('Digite a Distopia Residual: '))
            print(newCountry)
            return (newCountry,newRegion,newHappinessRank,newHappinessScore,newStandardError, newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity, newDystopiaResidual)
        except:
            print("Erro de Tipo")
            self.insert(lastData,escolha,rank)

    def editar(self,id):
        try:
            print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao')
            print('3 - Indice Felicidade\n5 - Erro Padrão\n6 - Family')
            print('7 - Indice de liberdade\n8 - Indice de confiança\n9 - Indice de Generosidade\n10 - Distopia Residual')
            choose = int(input())
            if choose == 1:
                editCountry = str(input('Entre com o novo nome do país: '))            

                if tree.searchCountry(editCountry) != None:
                    print("Pais já existe")
                else:
                    return(id,editCountry,1)
           
            elif choose == 2:
                editRegion = str(input('Entre com a novo nome da região: '))
                return(id,editRegion,2)
        
            elif choose == 3:
                editHappinessScore = float(input('Entre com o novo Indice de Felicidade: '))
                return(id,editHappinessScore,3)

           
            elif choose == 4:
                editStandartError = float(input('Entre com o novo Erro Padrão: '))
                return(id,editStandartError,4)
                
            elif choose == 5:
                editFamily = float(input('Entre com o novo indice "Family": '))
                return(id,editFamily,5)
                
            elif choose == 6:
                editFreedom = float(input('Entre com o novo indice de liberdade: '))
                return(id,editFreedom,6)
                
           
            elif choose == 7:
                editTrust = float(input('Entre com o novo indice de confiança: '))
                return(id,editTrust,7)
                
                
            elif choose == 8:
                editGenerosity = float(input('Entre com o novo indice "Generosity": '))
                return(id,editGenerosity,8)
                
           
            elif choose == 9:
                editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
                return(id,editDystopiaResidual,9)
       
        except:
            print("Erro de Tipo, Tente Novamente")
            self.editarDado(id)
