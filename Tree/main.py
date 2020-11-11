
# -*- coding: utf-8 -*-
import csv
from os import remove
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

# saveNewDataCsv - recebe a 3árvore de dados com todas as alterações e manipulações e exportar para outro arquivo csv
def saveNewDataCsv(dadosFinal):
    with open('datas/2015_1.csv', 'w', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        for linha in dadosFinal:
            escrever.writerow(linha)

def ordenar(escolha):
    if escolha == 1:   
        for i in range(len(dados)):
            for j in range(len(dados)-1):
                if int(dados[j][2]) > int(dados[j+1][2]):
                    temp = dados[j]
                    dados[j] = dados[j+1]
                    dados[j+1] = temp
        
        for i in range(len(dados)):
            tree.insert(dados[i][0],dados[i][1],dados[i][2],dados[i][3],dados[i][4],dados[i][5],dados[i][6],dados[i][7],dados[i][8],dados[i][9],dados[i][10],dados[i][11])
        for i in range(len(dados)):
            print(dados[i])
    if escolha == 2:
        for i in range(len(dados)):
            for j in range(len(dados)-1):
                if float(str(dados[j][5])) > float(str(dados[j+1][5])):
                    temp = dados[j]
                    dados[j] = dados[j+1]
                    dados[j+1] = temp
        #for i in range(len(dados)):
        #    print(dados[i])
        for i in range(len(dados)):
            tree.insert(dados[i][0],dados[i][1],dados[i][2],dados[i][3],dados[i][4],dados[i][5],dados[i][6],dados[i][7],dados[i][8],dados[i][9],dados[i][10],dados[i][11])

    if escolha == 3:
        for i in range(len(dados)):
            for j in range(len(dados)-1):
                if float(str(dados[j][7])) > float(str(dados[j+1][7])):                        
                    temp = dados[j]
                    dados[j] = dados[j+1]
                    dados[j+1] = temp
        #for i in range(len(dados)):
        #    print(dados[i])
        
        for i in range(len(dados)):
            tree.insert(dados[i][0],dados[i][1],dados[i][2],dados[i][3],dados[i][4],dados[i][5],dados[i][6],dados[i][7],dados[i][8],dados[i][9],dados[i][10],dados[i][11])

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
    escolha = int(input("Como deseja ordenar os dados\n1-Rank\n2-Economia\n3- Expeectativa de Vida "))
    ordenar(int(escolha))
    

# criarDado - pega todas as informações necessárias para o cadastro e adiciona na árbore 
# (caso não tenha um pais de mesmo nome)
def criarDado():
    listTemp = []
    newCountry = input('Digite o nome do pais: ')
    listTemp.append(newCountry)
    newRegion = input('Digite o nome da regiao: ')
    listTemp.append(newRegion)
    newHappinessRank = int(input('Digite o rank da felicidade: '))
    listTemp.append(newHappinessRank)
    if tree.search(newHappinessRank) != None:
        #Verifica se a árvore tá vazia
        print('Inicie Novamente o cadastro por favor')
        listTemp.clear()
        criarDado()
    else:
        #salvar o novo indice in the tree
        newHappinessScore = float(input('Digite o score da felicidade: '))
        listTemp.append(newHappinessScore)
        newStandardError = float(input('Digite o Erro Padrão: '))
        listTemp.append(newStandardError)
        newEconomy = float(input('Digite a economia: '))
        listTemp.append(newEconomy)
        newFamily = float(input('Digite da Família: '))
        listTemp.append(newFamily)
        newHealth = float(input('Digite da Saúde: '))
        listTemp.append(newHealth)
        newFreedom = float(input('Digite a Liberdade: '))
        listTemp.append(newFreedom)
        newTrust = float(input('Digite a Confiança: '))
        listTemp.append(newTrust)
        newGenerosity = float(input('Digite de Generosidade: '))
        listTemp.append(newGenerosity)
        newDystopiaResidual = float(input('Digite a Distopia Residual: '))
        listTemp.append(newDystopiaResidual)
        tree.ordernar(listTemp[0],listTemp[1],listTemp[2],listTemp[3],listTemp[4],listTemp[5],listTemp[6],listTemp[7],listTemp[8],listTemp[9],listTemp[10],listTemp[11])

# editarDado - verifica se o país a ser editado existe e permite mudar seus atributos
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

def remover(data):  
    verificar = tree.search(data)
    if verificar != None:
        verify = tree.searchIndex(data)
        #FALTA remover da arvore 
        del dados[verify]


# start - aqui são oferecidas aos usuários todas as opções disponíveis em um menu interativo
def start():
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Tree\n4-Deletar Item\n5- Ordenar\n6-Exportar CSV\n7-Limpar Console\n0-Sair')
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
        print("Digite qual coluna deseja excluir\n1 - Pais\n2 - Rank de Felicidade\n3 - Regiao")
        esc = int(input())
        if esc == 1:
            country = str(input("Digite o pais que deseja remover: "))
            remover(country)
        elif esc == 2:
            rank = str(input("Digite o Rank que deseja remover: "))
            remover(rank)
        elif esc == 3:
            region = str(input("Digite a Região que deseja remover: "))
            remover(region)
        else:
            print("Opção Inválida")
        start()
    if choose == 5:
        esc = int(input("Digite como Deseja ordenar\n1 - Pais\n2 - Regiao \n3 - Rank\n"))
        if esc == 1:
            ordenar(esc)
        elif esc == 2:
            ordenar(esc)
        elif esc == 3:
            ordenar(esc)
        else:
            print("Opção Inválida")
        start()
    if choose == 6:
        dadosFinal = []
        for i in range(len(dados)):
            dadosFinal.append(dados(i))
        saveNewDataCsv(dadosFinal)
        start()
    if choose == 7:        
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
    print('TREE')
    tree.inorder_traversal()
    #tree.printTree()
    rtr = tree.search(90)
    if  rtr == None:
        print('NAO ENCONTRADO')
    else:
        print('ENCONTRADO')

if __name__ == "__main__":
    main()
