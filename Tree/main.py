
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
    newHappinessRank = ''
    try:
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
                    criarDado(lastData,escolha,rank)
                else:
                    print("Digite um indice de economia maior que: " + str(lastData))
                    newEconomy = float(input('Digite o Indice economico: '))
                    if newEconomy < float(lastData):
                        criarDado(lastData,escolha,rank)
                    else:
                        newHealth = float(input('Digite a Expectativa de Vida: '))
            
            elif escolha == 3:
                newHappinessRank = input("Digite o seu rank: ")
                if tree.searchHappinessRank(newHappinessRank) != None:
                    print("Pais Já Existe")
                    print("Inicie novamente")
                    criarDado(lastData,escolha,rank)
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
    except:
        print("Erro de tipo")
        criarDado(lastData,escolha,rank)

# editarDado - verifica se a chave do país a ser editado existe e permite mudar seus atributos
def editarDado():
    try:
        id = int(input("Digite o id que deseja editar: "))
        if tree.searchHappinessRank(id) == None:
            print("Pais Não Existe")
        else:
            print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n')
            print('3 - Indice Felicidade\n5 - Erro Padrão\n6 - Family\n')
            print('7 - Indice de liberdade\n8 - Indice de confiança\n9 - Indice de Generosidade\n10 - Distopia Residual')
            choose = int(input())
            if choose == 1:
                editCountry = str(input('Entre com o novo nome do país: '))            

                if tree.searchCountry(editCountry) != None:
                    print("Pais já existe")
                else:
                    tree.editarTree(id,editCountry,1)
                    print("editado")
                    return
           
            elif choose == 2:
                editRegion = str(input('Entre com a novo nome da região: '))
                tree.editarTree(id,editRegion,2)
                return
           
            elif choose == 3:
                editHappinessScore = float(input('Entre com o novo Indice de Felicidade: '))
                tree.editarTree(id,editHappinessScore,3)
                return
           
            elif choose == 4:
                editStandartError = float(input('Entre com o novo Erro Padrão: '))
                tree.editarTree(id,editStandartError,4)
                return

            elif choose == 5:
                editFamily = float(input('Entre com o novo indice "Family": '))
                tree.editarTree(id,editFamily,5)
                return
                
            elif choose == 6:
                editFreedom = float(input('Entre com o novo indice de liberdade: '))
                tree.editarTree(id,editFreedom,6)
                return
           
            elif choose == 7:
                editTrust = float(input('Entre com o novo indice de confiança: '))
                tree.editarTree(id,editTrust,7)
                return
                
            elif choose == 8:
                editGenerosity = float(input('Entre com o novo indice "Generosity": '))
                tree.editarTree(id,editGenerosity,8)
                return
           
            elif choose == 9:
                editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
                tree.editarTree(id,editDystopiaResidual,9)
                return
    except:
        print("Erro de Tipo, Tente Novamente")
        editarDado()

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
        tree.postorder_traversal()
        start(retorno,escolha,rank)
    if choose == 4:
        if escolha == 1:
            print("Exclusão Por ordenação de Rank")
            data = int(input("Digite o indice do pais deseja remover: "))
            if tree.searchHappinessRank(data) != None:
                tree.removeHappinessRank(data)
                print("Removido com sucesso")
                start(retorno,escolha,rank)
            else:
                print("Pais não existe")
                start(retorno,escolha,rank)


        elif escolha == 2:
            print("Exclusão Por ordenação de Economia")
            data = float(input("Digite o indice de Economia que deseja remover: "))
            if tree.searchEconomy(data) != None:
                tree.removeEconomy(data)
                print("Removido com sucesso")
                start(retorno,escolha,rank)
            else:
                print("Indice não existe")
                start(retorno,escolha,rank)

        elif escolha == 3:
            print("Exclusão Por ordenação de Expectativa de vida")
            data = float(input("Digite o indice de Expectativa de vida que deseja remover: "))
            if tree.searchHealth(data) != None:       
                tree.removeHealth(data)
                print("Removido com sucesso")
                start(retorno,escolha,rank)
            else:
                print("Indice não existe")
                start(retorno,escolha,rank)
            
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
