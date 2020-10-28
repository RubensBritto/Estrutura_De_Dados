# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em ssv
import csv
import random
import os

from pilha import Stack

dados = []
pilha =  Stack()

def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        for linha in leitor:
            dados.append(linha)

def saveNewDataCsv(dados):
    with open('datas/2015_1.csv', 'w', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        for linha in dados:
            escrever.writerow(linha)

def aleatorioData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,100)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            pilha.push(dados[valorAleatorio])
            k+=1
        
def showStack():
    for i in range(pilha.size()):
       print(pilha.showStack(i))

def verificar(newCountry, newHappinessRank):
    for i in range(pilha.size()):
        if pilha.percorrer(0,newCountry) == True or pilha.percorrer(2,newHappinessRank) == True: 
                print('Pais ou Rankg ja existe')
                return False 
    

def criarDado():
    itemTemp = []
    newCountry = input('Digite o nome do pais: ')
    itemTemp.append(newCountry)
    newRegion = input('Digite o nome da regiao: ')
    itemTemp.append(newRegion)
    newHappinessRank = int(input('Digite o rank da felicidade: '))
    itemTemp.append(str(newHappinessRank))
    verificacao = verificar(newCountry,str(newHappinessRank))
    if verificacao == False:
        print('Inicie Novamente o cadastro por favor')
        itemTemp.clear()
        criarDado()
    else:
        newHappinessScore = float(input('Digite o score da felicidade: '))
        itemTemp.append(str(newHappinessScore))
        newStandardError = float(input('Digite o Erro Padrão: '))
        itemTemp.append(str(newStandardError))
        newEconomy = float(input('Digite a economia: '))
        itemTemp.append(str(newEconomy))
        newFamily = float(input('Digite da Família: '))
        itemTemp.append(str(newFamily))
        newHealth = float(input('Digite da Saúde: '))
        itemTemp.append(str(newHealth))
        newFreedom = float(input('Digite a Liberdade: '))
        itemTemp.append(str(newFreedom))
        newTrust = float(input('Digite a Confiança: '))
        itemTemp.append(str(newTrust))
        newGenerosity = float(input('Digite de Generosidade: '))
        itemTemp.append(str(newGenerosity))
        newDystopiaResidual = float(input('Digite a Distopia Residual: '))
        itemTemp.append(str(newDystopiaResidual))
        pilha.push(itemTemp)
def ordernar(indexPilha):
    pilha[-1] = pilha[indexPilha]
    pilha[indexPilha] = pilha[-2]
    pass    
       
def deletarDado():
    country = input('Digite o pais que deseja deletar: ')
    if pilha.percorrer(0,country) == True:
        #ARRUMAR FUNÇÃO ORDENAR (COLOCAR O ITEM QUE DESEJA EXCLUIR NA ULTIMA POSIÇÃO)
        indexPilha = pilha.index(country)
        ordernar(indexPilha)
        pilha.pop()
        print('Removido!')
        return
    else:
        print('Pais não consta na lista!')    
    
def start():
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Lista\n4-Deletar Item\n5-Exportar CSV\n6-Limpar Console\n0-Sair')
    choose = int(input())
    if choose == 1:
        criarDado()
        start()
    if choose == 2:
        #editarDado()
        start()
    if choose == 3:
        showStack()
        start()
    if choose == 4:
        deletarDado()
        start()
    if choose == 5:
        saveNewDataCsv(dados)
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
    ordernar()
    start()

if __name__ == "__main__":
    main()