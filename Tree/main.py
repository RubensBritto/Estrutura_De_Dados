
# -*- coding: utf-8 -*-
import csv
from tree import BinarySearchTree
import random
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza


dadosTemp = []
dados = []
tree = BinarySearchTree()

def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        for linha in leitor:
            dadosTemp.append(linha)

# saveNewDataCsv - recebe a pilha de dados com todas as alterações e manipulações e exportar para outro arquivo csv
def saveNewDataCsv(dadosFinal):
    with open('datas/2015_1.csv', 'w', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        for linha in dadosFinal:
            escrever.writerow(linha)

def aleatorioData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,158)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            tree.insert(valorAleatorio)
            dados.append(dadosTemp[k])
            k+=1

#inserirDados - adiciona na lista os arquivos que forma alterados, de forma "pontual" na linha e coluna desejada
def inserirDados(i,j,item):
    dados[i][j] = str(item)

def indiceItem(country):
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            return i
    return None

# criarDado - pega todas as informações necessárias para o cadastro e adiciona na pilha 
# (caso não tenha um pais de mesmo nome)
def criarDado():
    itemTemp = []
    newCountry = input('Digite o nome do pais: ')
    itemTemp.append(newCountry)
    newRegion = input('Digite o nome da regiao: ')
    itemTemp.append(newRegion)
    newHappinessRank = int(input('Digite o rank da felicidade: '))
    itemTemp.append(str(newHappinessRank))
    verificacao = tree.search(newHappinessRank)
    if verificacao != None:
        print('Inicie Novamente o cadastro por favor')
        itemTemp.clear()
        criarDado()
    else:
        #salvar o novo indice in the tree
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
        dados.append(itemTemp)

# editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos
def editarDado():
    country = str(input("Digite o pais que deseja editar: "))
    sumario = indiceItem(country)
    if sumario == None:
        print("Pais Existe")
    else:
        print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
        print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
        print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
        choose = int(input())
        if choose == 1:
            editCountry = str(input('Entre com o novo nome do país: '))
            inserirDados(sumario,0,editCountry)
        elif choose == 2:
            editRegion = input('Entre com a novo nome da região: ')
            inserirDados(sumario,1,editRegion)
            return
        elif choose == 3:
            editHappinessScore = float(input('Entre com o novo rank de Felicidade: '))
            retorno = tree.search(editHappinessScore)
            if retorno != None:
                print("Rank já existe")
            else:
                tree.insert(editHappinessScore)
                inserirDados(sumario,2,editHappinessScore)
        elif choose == 4:
            editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
            inserirDados(sumario,3,editHappinessRank)
            return
        elif choose == 5:
            editStandartError = float(input('Entre com o novo Erro Padrão: '))
            inserirDados(sumario,4,editStandartError)
            return
        elif choose == 6:
            editEconomy = float(input('Entre com a novo valor da Economia: '))
            inserirDados(sumario,5,editEconomy)
            return
        elif choose == 7:
            editFamily = float(input('Entre com o novo indice "Family": '))
            inserirDados(sumario,6,editFamily)
            return
        elif choose == 8:
            editHealth = float(input('Entre com o novo indice "Health": '))
            inserirDados(sumario,7,editHealth)
            return
        elif choose == 9:
            editFreedom = float(input('Entre com o novo indice de liberdade: '))
            inserirDados(sumario,8,editFreedom)
            return
        elif choose == 10:
            editTrust = float(input('Entre com o novo indice de confiança: '))
            inserirDados(sumario,9,editTrust)
            return
            
        elif choose == 11:
            editGenerosity = float(input('Entre com o novo indice "Generosity": '))
            inserirDados(sumario,10,editGenerosity)
            return
        elif choose == 12:
            editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
            inserirDados(sumario,11,editDystopiaResidual)
            return
    
# start - aqui são oferecidas aos usuários todas as opções disponíveis em um menu interativo
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
        tree.inorder_traversal()
        start()
    if choose == 4:
        #deletarDado()
        start()
    if choose == 5:
        dadosFinal = []
        for i in range(len(dados)):
            dadosFinal.append(dados(i))
        saveNewDataCsv(dadosFinal)
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
    #tree.inorder_traversal()
    rtr = tree.search(101)
    if  rtr != None:
        print('ENCONTRADO')
    else:
        print('NÃO ENCONTRADO')
    print(rtr)

if __name__ == "__main__":
    main()
