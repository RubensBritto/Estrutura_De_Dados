import csv
import random
from opLista import opLista

dados = []
dadosTemp = []


#Abrindo o arquivo csv com a função open
arq = open('datas/2015.csv', 'r')
#atribuindo os valores do arquivo à uma lista até achar um \n
dadosTemp = arq.read().split("\n")
#passando a lista para string para poder separar os elementos
dadosTemp = ','.join(dadosTemp)
#Separando os elementos quando se encontra uma vírgula
dadosTemp = dadosTemp.split(",")
#Fechando o arquivo csv para que a lista possa ser fechada 
arq.close()

def addLista(x,y):
    item = []
    j = 0
    for i in range(x,y,1):
        if j <= 11:
            j += 1
            item.append(dadosTemp[i])
    return item
def verificar(newCountry, newHappinessRank):
    '''
    country1=0
    happy1 = 0
    while couytry1 != dados[newCountry]:
        i+=1
            return dados[i]
    '''
    i=0 
    j=1 
    #print(dados)
    for i in dados[0:-1]:
    
        #print("O TIPO DE i é: ", str(type(i)))
            #print("O tipo de dados[i] é: ", str(type(dados[i])))
        
        if newCountry in dados.index(newCountry):
            print('Pais já existente')
            return False
        else:
            print("Pais Cadastrado com sucesso!")
            return True
        

def criarDado():
    newLine = opLista()
    newCountry = input('Digite o nome do pais: ')
    #verificar se ja existe 
    newRegion = input('Digite o nome da regiao: ')
    newHappinessRank = input('Digite o rank da felicidade: ')
    #verificar se já existe
    verificacao = verificar(newCountry,newHappinessRank)
    if verificacao == False:
        criarDado()
    else:
        newHappinessScore = input('Digite o score da felicidade: ')
        newStandardError = input('Digite o Erro Padrão: ')
        newEconomy = input('Digite a economia: ')
        newFamilyHealth = input('Digite a Saúde Família: ')
        newFreedom = input('Digite a Liberdade: ')
        newTrust = input('Digite a Confiança: ')
        newDystopiaResidual = input('Digite a Distopia Residual: ')
        retorno = newLine.criarNewDado(newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError,newEconomy, newFamilyHealth, newFreedom, newTrust, newDystopiaResidual)
        dados.append(retorno)
        print(dados)

def editarDado():
    pass
def showList():
    for j in len(dados):    
        print(dados[j])
    
def start():
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Lista')
    choose = int(input())
    if choose == 1:
        criarDado()
    if choose == 2:
        editarDado()
    if choose == 3:
        showList()
def main():
    k = 0
    visitados = []
    #print(dados)
    #1908
    while k < 100:
        valorAleatorio = random.randint(1,100)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            cmc = valorAleatorio * 12
            fim = cmc + 12
            dados.append(addLista(cmc,fim))
            k += 1
    '''
    print("OS VALORES ALEATORIOS")
    print(visitados)
    print("________________________________________________________________________")
    '''

    start()

if __name__ == "__main__":
    main()
    

#Aleatorio