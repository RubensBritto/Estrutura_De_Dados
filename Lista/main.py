
# -*- coding: utf-8 -*- 
import csv
import random # módulo para geração de números pseudo-aleatórios
import pickle # Módulo para salvar e recuperar estruturas sem perda em arquivos

'''
Para salvar ou recuperar uma estrutura de um arquivo com o módulo acima, faça assim:

>>> import pickle
>>> f = open("test.pck", "w")

Para armazenar uma estrutura de dados, use o método dump e então feche o arquivo do modo usual:

>>> pickle.dump(12.3, f)
>>> pickle.dump([1,2,3], f)
>>> f.close()
'''

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
    for i in range(len(dados)):
        if newCountry.lower() in dados[i][0].lower() or str(newHappinessRank) in dados[i][2]:
            #print('Pais ou Rankg já existe')
            return False
    print('Pais ou rankg nao existe')
    return True

def deletarDado():
    country = input('Digite o pais que deseja deletar')
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            del dados[i][0]
            print('Removido')
    print('Pais não consta na lista')        

def criarDado():
    newLine = opLista()
    newCountry = input('Digite o nome do pais: ')
    #verificar se ja existe 
    newRegion = input('Digite o nome da regiao: ')
    newHappinessRank = int(input('Digite o rank da felicidade: '))
    #verificar se já existe
    verificacao = verificar(newCountry,newHappinessRank)
    if verificacao == False:
        print('Inicie Novamente o cadastro por favor')
        criarDado()
    else:
        newHappinessScore = float(input('Digite o score da felicidade: '))
        newStandardError = float(input('Digite o Erro Padrão: '))
        newEconomy = float(input('Digite a economia: '))
        newFamilyHealth = float(input('Digite a Saúde Família: '))
        newFreedom = float(input('Digite a Liberdade: '))
        newTrust = float(input('Digite a Confiança: '))
        newDystopiaResidual = float(input('Digite a Distopia Residual: '))
        retorno = newLine.criarNewDado(newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError,newEconomy, newFamilyHealth, newFreedom, newTrust, newDystopiaResidual)
        #retorno = list(retorno)
        dados.append(retorno)
        #print(type(retorno))
        #print(dados)

def editarDado():
    country = input("Digite o pais que deseja editar: ")
    #print(dados.index(country))
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            print(i)
            dadosClone = dados
            newLine = opLista()
            print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
            print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Indice Family health')
            print('8 - Indice de liberdade\n9 - Indice de confiança\n10 - Distopia Residual')
            choose = int(input())
            if choose == 1:
                editCountry = input('Entre com o novo nome do país: ')
                newLine.editarCountry(editCountry,i)
            elif choose == 2:
                editRegion = input('Entre com a novo nome da região: ')
                newLine.editarRegion(editRegion,i)
            elif choose == 3:
                editHappinessScore = float(input('Entre com o novo rank de Felicidade: '))
                newLine.editarHappinessScore(editHappinessScore,i)
            elif choose == 4:
                editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
                newLine.editarHappinessRank(editHappinessRank,i)
            elif choose == 5:
                editStandartError = float(input('Entre com o novo Erro Padrão: '))
                newLine.editarStandardError(editStandartError,i)
            elif choose == 6:
                editEconomy = float(input('Entre com a novo valor da Economia: '))
                newLine.editarEconomy(editEconomy,i)
            elif choose == 7:
                editFamilyHealth = float(input('Entre com o novo indice "Family health": '))
                newLine.editarFamilyHealth(editFamilyHealth,i)
            elif choose == 8:
                editFreedom = float(input('Entre com o novo indice de liberdade: '))
                newLine.editarFreedom(editFreedom)
            elif choose == 9:
                editTrust = float(input('Entre com o novo indice de confiança: '))
                newLine.editarTrust(editTrust)
            elif choose == 10:
                editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
                newLine.editarDystopiaResidual(editDystopiaResidual)

        #else:
        #    print('País inválido ou Operação invalida')
def showList():
    for j in range(len(dados)):    
        print(dados[j])
    
def start():
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Lista\n4-Deletar Item')
    choose = int(input())
    if choose == 1:
        criarDado()
        start()
    if choose == 2:
        editarDado()
        start()
    if choose == 3:
        showList()
        start()
    if choose == 4:
        deletarDado()
        start()
    
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