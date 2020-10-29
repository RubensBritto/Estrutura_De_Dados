# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em ssv
import csv
from os import truncate
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
    return True
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

def editarDado():
    country = str(input("Digite o pais que deseja editar: "))
    for i in range(pilha.size()):
        if pilha.percorrer(0, country) == True:
            sumario = pilha.indiceStack(0,country)
            print(sumario)
            print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
            print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
            print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
            choose = int(input())
            if choose == 1:
                editCountry = str(input('Entre com o novo nome do país: '))
                retorno = verificar(editCountry,str(0.0))
                print(retorno)
                if retorno == True:
                    pilha.stackEditar(sumario,0,editCountry)
                else:
                    print("Pais já existe")
            elif choose == 2:
                editRegion = input('Entre com a novo nome da região: ')
                pilha.stackEditar(sumario,1,editRegion)
                return

            elif choose == 3:
                editHappinessScore = float(input('Entre com o novo rank de Felicidade: '))
                retorno = verificar(" ",str(editHappinessScore))
                if retorno == True:
                    pilha.stackEditar(sumario,2,editHappinessScore)
                else:
                    print("Rank já existe")
            if choose == 4:
                editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
                pilha.stackEditar(sumario,3,editHappinessRank)
                return

            elif choose == 5:
                editStandartError = float(input('Entre com o novo Erro Padrão: '))
                pilha.stackEditar(sumario,4,editStandartError)
                return

            elif choose == 6:
                editEconomy = float(input('Entre com a novo valor da Economia: '))
                pilha.stackEditar(sumario,5,editEconomy)
                return

            elif choose == 7:
                editFamily = float(input('Entre com o novo indice "Family": '))
                pilha.stackEditar(sumario,6,editFamily)
                return

            elif choose == 8:
                editHealth = float(input('Entre com o novo indice "Health": '))
                pilha.stackEditar(sumario,7,editHealth)
                return

            elif choose == 9:
                editFreedom = float(input('Entre com o novo indice de liberdade: '))
                pilha.stackEditar(sumario,8,editFreedom)
                return

            elif choose == 10:
                editTrust = float(input('Entre com o novo indice de confiança: '))
                pilha.stackEditar(sumario,9,editTrust)
                return
            
            elif choose == 11:
                editGenerosity = float(input('Entre com o novo indice "Generosity": '))
                pilha.stackEditar(sumario,10,editGenerosity)
                return

            elif choose == 12:
                editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
                pilha.stackEditar(sumario,11,editDystopiaResidual)
                return
    print('Pais não existe')
def deletarDado():
    country = input('Digite o pais que deseja deletar: ')
    if pilha.percorrer(0,country) == True:
        #ARRUMAR FUNÇÃO ORDENAR (COLOCAR O ITEM QUE DESEJA EXCLUIR NA ULTIMA POSIÇÃO)
        
        pilha.trocar(country)
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
        editarDado()
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
    #ordernar()
    print(pilha.peek())
    start()

if __name__ == "__main__":
    main()