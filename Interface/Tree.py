# -*- coding: utf-8 -*-
import csv
from os import remove
import random
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza

#######  CLASSE TREE #######


#ROOT - recebe a raiz da tree
ROOT = 'root'

#Classe dos nós
from os import sendfile

class Node:
    #Recebe as chaves e seta os caminhos
    def __init__(self,country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual):
        self.country = str(country)
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
        self.left = None
        self.right = None

    def __str__(self):
        print("Pais: " + self.country + " - " +"Região: " + self.region + " - " + "Rank Felicidade: " + self.happinessRank + " - " +
        "Score Felicidade: " + self.happinessScore+ " - " + "Erro Padrão: " + self.standardError + " - " +
        "Economia: " + self.economy+ " - " + "Familia: " + self.family + " - " +"Expectativa de vida: " + self.health + " - "
        " Indice de Liberdade: " + self.freedom+ " - " + " Indice de Confiança: " + self.trust + " - " +" Indice de Generosidade: " + self.genorosity+
        " Indice de Distopia Residual: " + self.dystopiaResidual)
        return str()

#Classe da árvore binária
class BinaryTree:
    #Definindo os pontos de cada caminho da árvore
    def __init__(self,country=None,region=None,happinessRank=None,happinessScore=None,standardError=None, economy=None, family =None,health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None, node=None):
        if node:
            self.root = node
        elif happinessRank:
            node = Node(country,region,happinessRank,happinessScore,standardError, economy, family,health, freedom, trust, genorosity, dystopiaResidual)
            self.root = node
        else:
            self.root = None
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
    

#Classe de árvore binária de Busca
class BinarySearchTree(BinaryTree):
    #Inserir dado - insere um novo dado na árvore
    def insert(self,country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual,escolha):
        parent = None
        x = self.root
        
        if escolha == 1:
            while(x):
                parent = x
                if int(happinessRank) < int(x.happinessRank):
                    x = x.left
                else:
                    x = x.right
            if parent is None:
                self.root = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            elif int(happinessRank) < int(parent.happinessRank):
                parent.left = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            else:
                parent.right = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
        
        elif escolha == 2:
            while(x):
                parent = x
                if float(economy) < float(x.economy):
                    x = x.left
                else:
                    x = x.right
            if parent is None:
                self.root = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            elif float(economy) < float(parent.economy):
                parent.left = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            else:
                parent.right = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
        
        elif escolha == 3:
            while(x):
                parent = x
                if float(health) < float(x.health):
                    x = x.left
                else:
                    x = x.right
            if parent is None:
                self.root = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            elif float(health) < float(parent.health):
                parent.left = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)
            else:
                parent.right = Node(country,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual)   
    
    #Busca - busca o item, atráves do index, na tree
    def searchHappinessRank(self, value):
        node = self.root
        while node is not None:
            if int(value) == int(node.happinessRank):
                return value
            elif int(value) < int(node.happinessRank):
                node = node.left
            elif int(value) > int(node.happinessRank):
                node = node.right
        return None

    #Busca - busca o item, atráves do index economy, na tree
    def searchEconomy(self, value):
        node = self.root
        while node is not None:
            if float(value) == float(node.economy):
                return value
            elif float(value) < float(node.economy):
                node = node.left
            elif float(value) > float(node.economy):
                node = node.right
        return None

    #Busca - busca o item, atráves do index health, na tree
    def searchHealth(self, value):
        node = self.root
        while node is not None:
            if float(value) == float(node.health):
                return value
            elif float(value) < float(node.health):
                node = node.left
            elif float(value) > float(node.health):
                node = node.right
        return None
    
    # Busca se o Pais existe na arvore  
    def searchCountry(self, value):
        node = self.root
        while node is not None:
            if str(value.lower()) in str(node.country.lower()):
                return value
            elif str(value.lower()) < str(node.country.lower()):
                node = node.left
            elif str(value.lower()) > str(node.country.lower()):
                node = node.right
        return None
    
    #Edita um item presente na tree
    def editarTree(self, index, dado, tipo):
        node = self.root
        while node is not None:
            if int(index) == int(node.happinessRank):
                if tipo == 1:
                    node.country = str(dado)
                    return self.insert(country=node.country,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 2:
                    node.region = str(dado)
                    return self.insert(country=None,region=node.region,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 3:
                    node.happinessScore = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=node.happinessScore,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 4:
                    node.standardError = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=node.standardError, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 5:
                    node.family = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=node.family, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 6:
                    node.freedom = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=node.freedom, trust=None, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 7:
                    node.trust = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=node.trust, genorosity=None, dystopiaResidual=None,escolha=None)
                elif tipo == 8:
                    node.genorosity = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=node.genorosity, dystopiaResidual=None,escolha=None)
                elif tipo == 9:
                    node.dystopiaResidual = str(dado)
                    return self.insert(country=None,region=None,happinessRank=index,happinessScore=None,standardError=None, economy=None, family=None, health=None, freedom=None, trust=None, genorosity=None, dystopiaResidual=node.dystopiaResidual,escolha=None)

            elif int(index) < int(node.happinessRank):
                node = node.left
            elif int(index) > int(node.happinessRank):
                node = node.right
        return None
    #saveTree : Salva a árvore numa lista para poder ser exportada para csv
    def saveTree(self,value):
        listaTemp = []
        listaFinal = []
        node = self.root
        while node is not None:
            if int(value) == int(node.happinessRank):
                listaTemp.append(str(node.country))
                listaTemp.append(str(node.region))
                listaTemp.append(str(node.happinessRank)) 
                listaTemp.append(str(node.happinessScore))
                listaTemp.append(str(node.standardError)) 
                listaTemp.append(str(node.economy))
                listaTemp.append(str(node.family))
                listaTemp.append(str(node.health))
                listaTemp.append(str(node.freedom))
                listaTemp.append(str(node.trust))
                listaTemp.append(str(node.genorosity))
                listaTemp.append(str(node.dystopiaResidual))
                listaFinal.append(listaTemp)
                return (listaFinal,int(node.happinessRank))
            elif int(value) < int(node.happinessRank):
                node = node.left
            elif int(value) > int(node.happinessRank):
                node = node.right
        return (None,None)
    
    
    def _min(self, node=ROOT):
        if node == ROOT:
            node = self.root
       #Retorna o menor elemento da subárvore que tem self como raiz.
        while node.left:
            node = node.left
        return node.data
    
    #Remove da tree a partir do Happiness Rank, já reordenando a árvore
    def removeHappinessRank(self, data,node= ROOT):
        if node == ROOT:
            node = self.root
        
        if node is None:
            return None
        
        if int(data) < int(node.happinessRank):
            node.left = self.removeHappinessRank(data,node.left)
            
        if int(data) > int(node.happinessRank):
            node.right = self.removeHappinessRank(data,node.right)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substituto = self._min(node.right)
                node.happinessRank = substituto
                node.right = self.removeHappinessRank(substituto,node.right)
        return node
    
    #Remove da tree a partir do Economy, já reordenando a árvore
    def removeEconomy(self, data,node= ROOT):
        if node == ROOT:
            node = self.root
        
        if node is None:
            return None
        
        if float(data) < float(node.economy):
            node.left = self.removeEconomy(data,node.left)
            
        if float(data) > float(node.economy):
            node.right = self.removeEconomy(data,node.right)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substituto = self._min(node.right)
                node.economy = substituto
                node.right = self.removeEconomy(substituto,node.right)
        return node

    #Remove da tree a partir do Health, já reordenando a árvore
    def removeHealth(self, data,node= ROOT):
        if node == ROOT:
            node = self.root
        
        if node is None:
            return None
        
        if float(data) < float(node.health):
            node.left = self.removeHealth(data,node.left)
            
        if float(data) > float(node.health):
            node.right = self.removeHealth(data,node.right)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substituto = self._min(node.right)
                node.health = substituto
                node.right = self.removeHealth(substituto,node.right)
        return node
    
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


country = Pais()
tree = BinarySearchTree()

dadosTemp = []
dados = []
class Main:
    def __init__(self):
        self.openData()
        retorno,escolha,rank = self.aleatorioData()
        self.start(retorno,escolha,rank)
    
    def openData(self):
        with open('data.csv', newline='') as arquivo:
            leitor=csv.reader(arquivo)
            leitor.__next__()
            for linha in leitor:
                dadosTemp.append(linha)

    # saveNewDataCsv - recebe a 3árvore de dados com todas as alterações e manipulações e exportar para outro arquivo csv
    def saveNewDataCsv(self,dadosFinal):
        with open('data_1.csv', 'w', newline='') as arquivo_csv:
            escrever = csv.writer(arquivo_csv)
            for linha in dadosFinal:
                escrever.writerow(linha)

    #Da a opção de ordenação por determinados indices na tree (Rank,Qualidade de vida,Economia)
    def ordenar(self,escolha):
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

    def aleatorioData(self):
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
        rt,rank = self.ordenar(int(escolha))
        return (rt,escolha,rank)
        

    # editarDado - verifica se a chave do país a ser editado existe e permite mudar seus atributos
    def editarDado(self):
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
            self.editarDado()

    # start - aqui são oferecidas aos usuários todas as opções disponíveis em um menu interativo
    def start(self,retorno,escolha,rank):
        print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Tree\n4-Deletar Item\n5-Exportar CSV\n6-Limpar Console\n0-Sair')
        choose = int(input())
        if choose == 1:
            if escolha == 1:
                rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual = country.insert(retorno,escolha,rank)
                tree.insert(rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual,escolha)
            elif escolha == 2:
                rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual = country.insert(retorno,escolha,rank)
                tree.insert(rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual,escolha)
            else:
                rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual = country.insert(retorno,escolha,rank)
                tree.insert(rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual,escolha)        
            self.start(retorno,escolha,rank)
        if choose == 2:
            
            id = int(input("Digite o id que deseja editar: "))
            if tree.searchHappinessRank(id) == None:
                print("Pais Não Existe")
                self.start(retorno,escolha,rank)
                
            id,data,colum = country.editar(id)
            tree.editarTree(id,data,colum)

            self.start(retorno,escolha,rank)
        if choose == 3:
            tree.postorder_traversal()
            self.start(retorno,escolha,rank)
        if choose == 4:
            if escolha == 1:
                print("Exclusão Por ordenação de Rank")
                data = int(input("Digite o indice do pais deseja remover: "))
                if tree.searchHappinessRank(data) != None:
                    tree.removeHappinessRank(data)
                    print("Removido com sucesso")
                    self.start(retorno,escolha,rank)
                else:
                    print("Pais não existe")
                    self.start(retorno,escolha,rank)


            elif escolha == 2:
                print("Exclusão Por ordenação de Economia")
                data = float(input("Digite o indice de Economia que deseja remover: "))
                if tree.searchEconomy(data) != None:
                    tree.removeEconomy(data)
                    print("Removido com sucesso")
                    self.start(retorno,escolha,rank)
                else:
                    print("Indice não existe")
                    self.start(retorno,escolha,rank)

            elif escolha == 3:
                print("Exclusão Por ordenação de Expectativa de vida")
                data = float(input("Digite o indice de Expectativa de vida que deseja remover: "))
                if tree.searchHealth(data) != None:       
                    tree.removeHealth(data)
                    print("Removido com sucesso")
                    self.start(retorno,escolha,rank)
                else:
                    print("Indice não existe")
                    self.start(retorno,escolha,rank)
                
            else:
                print("Opção Inválida")
            self.start(retorno,escolha,rank)
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
            self.saveNewDataCsv(dadosFinal)
            self.start(retorno,escolha,rank)
        if choose == 6:        
            os.system('clear')
            self.start(retorno,escolha,rank)
        if choose == 0:
            exit()
        else:
            print("Operação invalida!")
            self.start(retorno,escolha,rank)



