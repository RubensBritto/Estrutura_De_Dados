
# -*- coding: utf-8 -*- 
import csv
import os
import random # módulo para geração de números pseudo-aleatórios
from opLista import opLista


dados = []
dadosTemp = []

'''
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
'''
def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        for linha in leitor:
            dadosTemp.append(linha)

def aleatorioData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,100)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            dados.append(dadosTemp[valorAleatorio])
            k+=1

def altera_csv(dados):
    with open('datas/2015_1.csv', 'w', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        for linha in dados:
            escrever.writerow(linha)


def addLista(x,y):
    item = []
    j = 0
    for i in range(x,y,1):
        if j <= 11:
            j += 1
            item.append(dadosTemp[i])
    return item
def inserirDadoMatriz(i,j,item):
    dados[i][j] = item

def indiceItem(country):
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            return i
    return
def verificar(newCountry, newHappinessRank):
    for i in range(len(dados)):
        if newCountry.lower() in dados[i][0].lower() or str(newHappinessRank) in dados[i][2]:
            #print('Pais ou Rankg já existe')
            return False
    print('Pais ou ranking nao existe')
    return True

def deletarDado():
    country = input('Digite o pais que deseja deletar: ')
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            del dados[i][0]
            print('Removido!')
            return
    print('Pais não consta na lista!')        

def criarDado():
    newLine = opLista()
    newCountry = input('Digite o nome do pais: ')
    newRegion = input('Digite o nome da regiao: ')
    newHappinessRank = int(input('Digite o rank da felicidade: '))
    verificacao = verificar(newCountry,newHappinessRank)
    if verificacao == False:
        print('Inicie Novamente o cadastro por favor')
        criarDado()
    else:
        newHappinessScore = float(input('Digite o score da felicidade: '))
        newStandardError = float(input('Digite o Erro Padrão: '))
        newEconomy = float(input('Digite a economia: '))
        newFamily = float(input('Digite da Família: '))
        newHealth = float(input('Digite da Saúde: '))
        newFreedom = float(input('Digite a Liberdade: '))
        newTrust = float(input('Digite a Confiança: '))
        newGenerosity = float(input('Digite de Generosidade: '))
        newDystopiaResidual = float(input('Digite a Distopia Residual: '))
        retorno = newLine.criarNewDado(newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError,newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity, newDystopiaResidual)
        dados.append(retorno)


def editarDado():
    country = input("Digite o pais que deseja editar: ")
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            print(i)
            sumario = indiceItem(country)
            newLine = opLista()
            print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
            print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
            print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
            choose = int(input())
            if choose == 1:
                editCountry = input('Entre com o novo nome do país: ')
                retorno = newLine.editarCountry(editCountry)
                retorno2 = verificar(editCountry,0)
                if retorno2 == True:
                    inserirDadoMatriz(sumario,0,retorno)
                else:
                    print("Pais já existe")
            elif choose == 2:
                editRegion = input('Entre com a novo nome da região: ')
                retorno = newLine.editarRegion(editRegion)
                inserirDadoMatriz(sumario,1,retorno)

            elif choose == 3:
                editHappinessScore = float(input('Entre com o novo rank de Felicidade: '))
                retorno = newLine.editarHappinessScore(editHappinessScore)
                retorno2 = verificar("",editHappinessScore)
                if retorno2 == True:
                    inserirDadoMatriz(sumario,2,retorno)
                else:
                    print("Rank já existe")

            elif choose == 4:
                editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
                retorno = newLine.editarHappinessRank(editHappinessRank)
                inserirDadoMatriz(sumario,3,retorno)

            elif choose == 5:
                editStandartError = float(input('Entre com o novo Erro Padrão: '))
                retorno = newLine.editarStandardError(editStandartError)
                inserirDadoMatriz(sumario,4,retorno)

            elif choose == 6:
                editEconomy = float(input('Entre com a novo valor da Economia: '))
                retorno = newLine.editarEconomy(editEconomy)
                inserirDadoMatriz(sumario,5,retorno)

            elif choose == 7:
                editFamily = float(input('Entre com o novo indice "Family": '))
                retorno = newLine.editarFamily(editFamily)
                inserirDadoMatriz(sumario,6,retorno)

            elif choose == 8:
                editHealth = float(input('Entre com o novo indice "Health": '))
                retorno = newLine.editarHealth(editHealth)
                inserirDadoMatriz(sumario,7,retorno)

            elif choose == 9:
                editFreedom = float(input('Entre com o novo indice de liberdade: '))
                retorno = newLine.editarFreedom(editFreedom)
                inserirDadoMatriz(sumario,8,retorno)

            elif choose == 10:
                editTrust = float(input('Entre com o novo indice de confiança: '))
                retorno = newLine.editarTrust(editTrust)
                inserirDadoMatriz(sumario,9,retorno)

            elif choose == 11:
                editGenerosity = float(input('Entre com o novo indice "Generosity": '))
                retorno = newLine.editarGenerosity(editGenerosity)
                inserirDadoMatriz(sumario,10,retorno)

            elif choose == 12:
                editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
                retorno = newLine.editarDystopiaResidual(editDystopiaResidual)
                inserirDadoMatriz(sumario,11,retorno)

        #else:
        #    print('País inválido ou Operação invalida')
def showList():
    for j in range(len(dados)):    
        print(dados[j])
    
def start():
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Lista\n4-Deletar Item\n5-Exportar CSV\n6-Limpar Console\n0-Sair')
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
    if choose == 5:
        altera_csv(dados)
        start()
    if choose == 6:        
        os.system('clear')
        start()
    if choose == 0:
        exit()
    else:
        print("Operação invalida!")
        start()
def main():
    openData()
    aleatorioData()
    start()

if __name__ == "__main__":
    main()
    

#Aleatorio