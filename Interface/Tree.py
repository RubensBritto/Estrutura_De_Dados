# -*- coding: utf-8 -*-
import csv
from os import remove
import random
import os
from tkinter import messagebox 
from tkinter import *

#módulo para acessar o terminal do sistema e poder fazer a limpeza

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
        ("Pais: " + self.country + " - " +"Região: " + self.region + " - " + "Rank Felicidade: " + self.happinessRank + " - " +
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
        listTemp = []
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        listTemp.append(str(node))
        print(listTemp)
    

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
        if tree.searchHappinessRank(data) == None:
            messagebox.showerror("Error", "Rank não Existe na Arvore")
            return
        
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
        if tree.searchEconomy(data) == None:
            messagebox.showerror("Error", "Rank não Existe na Arvore")
            return
        
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
        if tree.searchHealth(data) == None:
            messagebox.showerror("Error", "Rank não Existe na Arvore")
            return
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

    def insert(self,escolha,retorno,newCountry,newRegion,newHappinessRank,newHappinessScore,newStandardError, newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity, newDystopiaResidual):
        if escolha == 1:
            if int(newHappinessRank) < int(retorno):
                messagebox.showerror("Error","Digite um valor Superior a: " + retorno)
                return
        if escolha == 2:
            if float(newHappinessRank) < float(retorno):
                    messagebox.showerror("Error","Digite um valor Superior a: " + retorno)
                    return
        if escolha == 3:
            if float(newHappinessRank) < float(retorno):
                messagebox.showerror("Error","Digite um valor Superior a: " + retorno)
                return  
        verify1 = tree.searchCountry(newCountry) 
        
        if  verify1 != None:
            messagebox.showerror("Error","Pais já existe")
            return
        else:
            verify2 = tree.searchHappinessRank(newHappinessRank)
            if verify2 != None:
                messagebox.showerror("Error","Rankg já existe")
                return
            else:
                tree.insert(newCountry,newRegion,newHappinessRank,newHappinessScore,newStandardError, newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity, newDystopiaResidual,escolha)
                messagebox.showinfo("OK", "Inserção Feita com Sucesso")
            

    def editar(self,choose,id,dado):
        verify = tree.searchHappinessRank(id)
        print(verify)
        if verify == None:
            messagebox.showerror("Error","Pais Não Existe")
            return
        else:
            if choose == 1:
                #editCountry = str(input('Entre com o novo nome do país: '))            
                if tree.searchCountry(dado) != None:
                    messagebox.showerror("Error", "Pais ja existe na Arvore")
                    return
                else:
                    tree.editarTree(id,dado,1)
        
            elif choose == 2:
                #editRegion = str(input('Entre com a novo nome da região: '))
                tree.editarTree(id,dado,2)
        
            elif choose == 3:
                #editHappinessScore = float(input('Entre com o novo Indice de Felicidade: '))
                tree.editarTree(id,dado,3)
        
            elif choose == 4:
                #editStandartError = float(input('Entre com o novo Erro Padrão: '))
                tree.editarTree(id,dado,4)
                
            elif choose == 5:
                #editFamily = float(input('Entre com o novo indice "Family": '))
                tree.editarTree(id,dado,5)
                
            elif choose == 6:
                #editFreedom = float(input('Entre com o novo indice de liberdade: '))
                tree.editarTree(id,dado,6)
                
        
            elif choose == 7:
                #editTrust = float(input('Entre com o novo indice de confiança: '))
                tree.editarTree(id,dado,7)
                
                
            elif choose == 8:
                #editGenerosity = float(input('Entre com o novo indice "Generosity": '))
                tree.editarTree(id,dado,8)
                
        
            elif choose == 9:
                #editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
                tree.editarTree(id,dado,9)
        messagebox.showinfo("Ok", "Alteração Efetuada")
        return

country = Pais()
tree = BinarySearchTree()

dadosTemp = []
dados = []
class Main:
    def iniciar(self,escolha):
        #print("oi")
        self.openData()
        k = 0
        visitados = []
        while(k < 100):
            valorAleatorio = random.randint(1,157)
            if valorAleatorio not in visitados:
                visitados.append(valorAleatorio)
                #Coloca o dado de forma (e com chave) aleatória na tree
                dados.append(dadosTemp[valorAleatorio])
                k+=1
        rt,rank = self.ordenar(int(escolha))
        return (rt,escolha,rank)

    
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


    # start - aqui são oferecidas aos usuários todas as opções disponíveis em um menu interativo
    def removeHappinessRank(self,dado):
        rt = tree.removeHappinessRank(dado)
        if rt != None:
            messagebox.showinfo("OK","Remoção realizada")
            return
    
    def removeEconomy(self,dado):
        rt = tree.removeEconomy(dado)
        if rt != None:
            messagebox.showinfo("OK","Remoção realizada")
            return
    
    def removeHealth(self,dado):
        rt = tree.removeHealth(dado)
        if rt != None:
            messagebox.showinfo("OK","Remoção realizada")
            return
    def show(self):
        tree.postorder_traversal()


    def start(self,retorno,escolha,rank):
        print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Tree\n4-Deletar Item\n5-Exportar CSV\n6-Limpar Console\n0-Sair')
        choose = int(input())
        if choose == 1:
            if escolha == 1:
                rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual = country.insert(retorno,escolha,rank)
                #tree.insert(rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual,escolha)
            elif escolha == 2:
                rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual = country.insert(retorno,escolha,rank)
                #tree.insert(rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual,escolha)
            else:
                rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual = country.insert(retorno,escolha,rank)
                #tree.insert(rtCountry,region,happinessRank,happinessScore,standardError, economy, family, health, freedom, trust, genorosity, dystopiaResidual,escolha)        
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



