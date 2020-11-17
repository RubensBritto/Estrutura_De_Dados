
# -*- coding: utf-8 -*-
import csv
from os import remove
from tree import BinarySearchTree
import random
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza


dadosTemp = []
dados = []
tree = BinarySearchTree()
lastData1 = 0
lastData2 = 0
lastData3 = 0

def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        for linha in leitor:
            dadosTemp.append(linha)

# saveNewDataCsv - recebe a 3árvore de dados com todas as alterações e manipulações e exportar para outro arquivo csv
def saveNewDataCsv(dadosFinal):
    with open('datas/2015_1.csv', 'w', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        for linha in dadosFinal:
            escrever.writerow(linha)
#Da a opção de ordenação por determinados indices na tree (Rank,Qualidade de vida,Economia)
def ordenar(escolha):
    if escolha == 1:   
        for i in range(len(dados)):
            for j in range(len(dados)-1):
                if int(dados[j][2]) > int(dados[j+1][2]):
                    temp = dados[j]
                    dados[j] = dados[j+1]
                    dados[j+1] = temp
        for i in range(len(dados)):
            tree.insert(dados[i][0],dados[i][1],dados[i][2],dados[i][3],dados[i][4],dados[i][5],dados[i][6],dados[i][7],dados[i][8],dados[i][9],dados[i][10],dados[i][11],escolha)

        return (dados[-1][2], dados[-1][2])

    if escolha == 2:
        for i in range(len(dados)):
            for j in range(len(dados)-1):
                if float(str(dados[j][5])) > float(str(dados[j+1][5])):
                    temp = dados[j]
                    dados[j] = dados[j+1]
                    dados[j+1] = temp

        for i in range(len(dados)):
            tree.insert(dados[i][0],dados[i][1],dados[i][2],dados[i][3],dados[i][4],dados[i][5],dados[i][6],dados[i][7],dados[i][8],dados[i][9],dados[i][10],dados[i][11],escolha)
        
        return (dados[-1][5], dados[-1][2])

    if escolha == 3:
        for i in range(len(dados)):
            for j in range(len(dados)-1):
                if float(str(dados[j][7])) > float(str(dados[j+1][7])):                        
                    temp = dados[j]
                    dados[j] = dados[j+1]
                    dados[j+1] = temp

        for i in range(len(dados)):
            tree.insert(dados[i][0],dados[i][1],dados[i][2],dados[i][3],dados[i][4],dados[i][5],dados[i][6],dados[i][7],dados[i][8],dados[i][9],dados[i][10],dados[i][11],escolha)
        return (dados[-1][7], dados[-1][2])

def aleatorioData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,157)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            #Coloca o dado de forma (e com chave) aleatória na tree
            dados.append(dadosTemp[valorAleatorio])
            k+=1
    escolha = int(input("Como deseja ordenar os dados\n1-Rank\n2-Economia\n3- Expectativa de Vida "))
    rt,rank = ordenar(int(escolha))
    return (rt,escolha,rank)
    

# criarDado - pega todas as informações necessárias para o cadastro e adiciona na árbore 
# (caso não tenha um pais de mesmo nome)
def criarDado(lastData,escolha,rank):
    newEconomy = 0
    newHealth = 0
    newCountry = input('Digite o nome do pais: ')
    newRegion = input('Digite o nome da regiao: ')
    newHappinessRank = int(rank)+1
    print("O seu Rank é: " + str(newHappinessRank))
    if escolha == 1:
        newEconomy = float(input('Digite o Indice economico: '))
        newHealth = float(input('Digite a Expectativa de Vida: '))
    elif escolha == 2:
        print("Digite um indice de economia maior que: " + str(lastData))
        newEconomy = float(input('Digite o Indice economico: '))
        if newEconomy < float(lastData):
            criarDado(lastData,escolha,rank)
        else:
            newHealth = float(input('Digite a Expectativa de Vida: '))
    elif escolha == 3:
        print("Digite um indice de expectativa de vida maior que: " + str(lastData))
        newHealth = float(input('Digite a Expectativa de Vida: '))
        if newHealth < float(lastData):
            criarDado(lastData,escolha,rank)
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
    tree.insert(newCountry,newRegion,newHappinessRank,newHappinessScore,newStandardError,newEconomy,newFamily,newHealth,newFreedom,newTrust,newGenerosity,newDystopiaResidual,escolha)

# editarDado - verifica se a chave do país a ser editado existe e permite mudar seus atributos
def editarDado():
    id = int(input("Digite o id que deseja editar: "))
    if tree.search(id) == None:
        print("Pais Não Existe")
    else:
        #Recebe o index do item buscado na tree
        sumario = tree.search(id)
        print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
        print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
        print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
        choose = int(input())
        if choose == 1:
            editCountry = str(input('Entre com o novo nome do país: '))            

            if tree.searchString(editCountry) != None:
                print("Pais já existe")
            else:
                tree.editarTree(sumario,editCountry,1)
                print("editado")
                return
        elif choose == 2:
            editRegion = str(input('Entre com a novo nome da região: '))
            tree.editarTree(sumario,editRegion,2)
            return
        elif choose == 3:
            editHappinessScore = int(input('Entre com o novo rank de Felicidade: '))
            if tree.search(editHappinessScore) != None:
                print("Rank já existe")
            else:
                tree.editarTree(sumario,editHappinessScore,3)
        elif choose == 4:
            editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
            tree.editarTree(sumario,editHappinessRank,4)
            return
        elif choose == 5:
            editStandartError = float(input('Entre com o novo Erro Padrão: '))
            tree.editarTree(sumario,editStandartError,5)
            return
        elif choose == 6:
            editEconomy = float(input('Entre com a novo valor da Economia: '))
            tree.editarTree(sumario,editEconomy,6)
            return
        elif choose == 7:
            editFamily = float(input('Entre com o novo indice "Family": '))
            tree.editarTree(sumario,editFamily,7)
            return
        elif choose == 8:
            editHealth = float(input('Entre com o novo indice "Health": '))
            tree.editarTree(sumario,editHealth,8)
            return
        elif choose == 9:
            editFreedom = float(input('Entre com o novo indice de liberdade: '))
            tree.editarTree(sumario,editFreedom,9)
            return
        elif choose == 10:
            editTrust = float(input('Entre com o novo indice de confiança: '))
            tree.editarTree(sumario,editTrust,10)
            return
            
        elif choose == 11:
            editGenerosity = float(input('Entre com o novo indice "Generosity": '))
            tree.editarTree(sumario,editGenerosity,11)
            return
        elif choose == 12:
            editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
            tree.editarTree(sumario,editDystopiaResidual,12)
            return
#Verifica se o item na árvore existe e o remove
def remover(data):  
    verificar = tree.search(data)
    if verificar != None:
        verify = tree.searchIndex(data) 
        del dados[verify]


# start - aqui são oferecidas aos usuários todas as opções disponíveis em um menu interativo
def start(retorno,escolha,rank):
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Tree\n4-Deletar Item\n5-Exportar CSV\n6-Limpar Console\n0-Sair')
    choose = int(input())
    if choose == 1:
        if escolha == 1:
            criarDado(retorno,escolha,rank)
        elif escolha == 2:
            criarDado(retorno,escolha,rank)
        else:
            criarDado(retorno,escolha,rank)
        start(retorno,escolha,rank)
    if choose == 2:
        editarDado()
        start(retorno,escolha,rank)
    if choose == 3:
        #tree.inorder_traversal()
        tree.postorder_traversal()
        start(retorno,escolha,rank)
    if choose == 4:
        if escolha == 1:
            print("Exclusão Por ordenação de Rank")
            data = int(input("Digite o indice do pais deseja remover: "))
            tree.remove(data)
            print("Removido com sucesso")

        elif escolha == 2:
            print("Exclusão Por ordenação de Economia")
            data = int(input("Digite o indice que deseja remover: "))
            tree.remove(data)
            print("Removido com sucesso")

        elif escolha == 3:
            print("Exclusão Por ordenação de Expectativa de vida")
            data = int(input("Digite o indice que deseja remover: "))
            tree.remove(data)
            print("Removido com sucesso")
        else:
            print("Opção Inválida")
        start(retorno,escolha,rank)
    if choose == 5:
        dadosFinal = []
        i = 1
        data = 0
        while data != None:
            data,j= tree.saveTree(i)
            print(data)
            if data != None:
                dadosFinal.append(data)
                i = j
            i+=1
        saveNewDataCsv(dadosFinal)
        start(retorno,escolha,rank)
    if choose == 6:        
        os.system('clear')
        start(retorno,escolha,rank)
    if choose == 0:
        exit()
    else:
        print("Operação invalida!")
        start(retorno,escolha,rank)


def main():
    openData()
    retorno,escolha,rank = aleatorioData()
    start(retorno, escolha,rank)
if __name__ == "__main__":
    main()
