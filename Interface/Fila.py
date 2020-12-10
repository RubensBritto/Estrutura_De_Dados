# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em csv
import csv # módulo necessário poder se trabalhar com csv
import random # módulo para geração de números pseudo-aleatórios
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza
from tkinter import *
from tkinter import messagebox
 
'''
Class Queue - Classe da fila para realizar as operações
_init_: inicia a fila
isEmpty : retorna se a fila está vazia ou não
enqueue : insere um novo dado na Fila
dequeue : remove o primeiro item na Fila
size : retorna o tamanho da fila
showQueue: exibe a fila
percorrerQueue: retorna se determinado elemento existe ou não
indiceQueue: retorna o indice do elemento passado na Fila
editarQueue: edita um elemento na fila (caso ele exista!)
unqueue: reordena a fila caso o elemento que se deseja tirar não estiver no inicio
returnLast: retorna o último elemento da fila
'''


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def showQueue(self,i):
        return self.items[i]

    #Procura o elemento na fila e retorna true or false
    def percorrerQueue(self, j, dado):
        if j == 0:
            for i in range(self.size()):
                if (str(dado.lower()) in self.items[i][j].lower()):
                    return True
            return False
        elif j == 2:
            for i in range(self.size()):
                if (str(dado) in str(self.items[i][j])):
                    return True
            return False
    #Retorna o indice do elemento na fila
    def indiceQueue(self,j,dado):
        for i in range(self.size()):
            if (dado.lower() in self.items[i][j].lower()):
                return i
    
    def queueEditar(self, i, j, dados):
        self.items[i][j] = str(dados)
    

    def unqueue(self, j, dado):
         for i in range(self.size()):
            if (str(dado.lower()) in self.items[i][j].lower()):
                return i
    
    def returnLast(self, i):
        return self.items[i]

fila =  Queue()

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
        self.item = []
    # criarDado - pega todas as informações necessárias para o cadastro e adiciona na fila 
    # (caso não tenha um pais de mesmo nome)

    def insert(self, newCountry,newRegion,newHappinessRank,newHappinessScore,newStandardError,newEconomy,newFamily,newHealth,newFreedom,newTrust,newGenerosity,newDystopiaResidual):
        cond1 = fila.percorrerQueue(0,newCountry)
        cond2 = (fila.percorrerQueue(2,str(newHappinessRank)))
        if ((cond1 != True) and (cond2 != True)):
            self.item.insert(0,newCountry)
            #newRegion = input('Digite o nome da regiao: ')
            self.item.append(newRegion)
            self.item.insert(2,newHappinessRank)
            #newHappinessScore = float(input('Digite o score da felicidade: '))
            self.item.append(newHappinessScore)
            #newStandardError = float(input('Digite o Erro Padrão: '))
            self.item.append(newStandardError)
            #newEconomy = float(input('Digite a economia: '))
            self.item.append(newEconomy)
            #newFamily = float(input('Digite da Família: '))
            self.item.append(newFamily)
            #newHealth = float(input('Digite da Saúde: '))
            self.item.append(newHealth)
            #newFreedom = float(input('Digite a Liberdade: '))
            self.item.append(newFreedom)
            #newTrust = float(input('Digite a Confiança: '))
            self.item.append(newTrust)
            #newGenerosity = float(input('Digite de Generosidade: '))
            self.item.append(newGenerosity)
            #newDystopiaResidual = float(input('Digite a Distopia Residual: '))
            self.item.append(newDystopiaResidual)
            fila.enqueue(self.item)
            messagebox.showinfo("Ok", "Pais Adicionado com sucesso")
            return
        #return(self.item)
        else:
            messagebox.showerror("Error","Pais ou Rank ja Existe")
            return  

    # editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos

    def editar(self,choose,nameCountry,data):
        cond1 = fila.percorrerQueue(0, nameCountry)
        #print(cond1)
        if cond1 == True:
            sumario = fila.indiceQueue(0,nameCountry) #Se o Pais existe na Fila ele pode ser alterado
            if choose == 0:
                cond2 = fila.percorrerQueue(0, data)
                #print(cond2)
                if cond2 != True:
                    fila.queueEditar(sumario,0,data)
                else:
                    messagebox.showerror("Error", "Nome do Pais ja consta na Fila")
                    return

            elif choose == 1:
                fila.queueEditar(sumario,1,data)

            elif choose == 2:
                cond3 = fila.percorrerQueue(2, data)
                if cond3 != True:
                    fila.queueEditar(sumario,2,data)
                else:
                    messagebox.showerror("Error", "Rank já existe")
                    return
            elif choose == 3:
                fila.queueEditar(sumario,3,data)

            elif choose == 4:
                fila.queueEditar(sumario,4,data)

            elif choose == 5:
                fila.queueEditar(sumario,5,data)

            elif choose == 6:
                fila.queueEditar(sumario,6,data)

            elif choose == 7:
                fila.queueEditar(sumario,7,data)

            elif choose == 8:
                fila.queueEditar(sumario,8,data)

            elif choose == 9:
                fila.queueEditar(sumario,9,data)

            elif choose == 10:
                fila.queueEditar(sumario,10,data)

            elif choose == 11:
                fila.queueEditar(sumario,11,data)
        elif cond1 != True:
            messagebox.showerror("Error", "Pais não costa na fila")
            return
        messagebox.showinfo("OK", "Alteração Realizada")
    
dados = []
country = Pais()    

class Main:
    
    def iniciar (self):
        self.openData()
        self.aleatorioData()

    # openData - abre os arquivos (csv) e faz toda manipulação para ser colocado na fila
    def openData(self):
        with open('data.csv', newline='') as arquivo:
            leitor=csv.reader(arquivo)
            leitor.__next__()
            for linha in leitor:
                dados.append(linha)

    # saveNewDataCsv - recebe a fila de dados com todas as alterações e manipulações e exportar para outro arquivo csv
    def saveNewDataCsv(self,dadosFinal):
        with open('data_1.csv', 'w', newline='') as arquivo_csv:
            escrever = csv.writer(arquivo_csv)
            for linha in dadosFinal:
                escrever.writerow(linha)

    # aleatorioData - cria uma lista com os 100 dados aleatórios da base de dados original e 
    # adciona a fila
    def aleatorioData(self):
        k = 0
        visitados = []
        while(k < 100):
            valorAleatorio = random.randint(1,157)
            if valorAleatorio not in visitados:
                visitados.append(valorAleatorio)
                fila.enqueue(dados[valorAleatorio])
                k+=1

    #showQueue - imprime todos os dados contidos na fila        
    def showQueue(self):
        root = Tk()
        show = Text(root,width=500, height=50,pady=10,padx=10)
        show.pack()
        dados = []
        for i in range(fila.size()):
            dados.append(fila.showQueue(i))
            show.insert(END,"Pais: " + str(dados[i][0] )+ "\nRegião: " + str(dados[i][1] )+ "\nRank Felicidade: " + str(dados[i][2] )+ "\nScore Felicidade: " + str(dados[i][3] )+
                "\nErro Padrão: " + str(dados[i][4] )+ "\nIndice de Economia: " + str(dados[i][5] )+ "\nIndice da Familia: " + str(dados[i][6] )+ "\nExpectativa de Vida: " + str(dados[i][7] )+
                "\nIndice de Liberdade: " + str(dados[i][8] )+ "\nIndice de Confiança: " + str(dados[i][9] )+ "\nIndice de Genorosidade: "+ str(dados[i][10])+ "\nIndice de Distopia Residual: "+
                str(dados[i][11]) + "\n\n")
            

    # removeFromQueue - cria uma lista temporaria, guarda o index do item da fila a ser removido
    # passa a fila para uma lista, remove o item na lista e depois coloca essa lista sem o item de volta na fila

    def removeFromQueue(self,indexItem):
        listaTemp = []
        newIndex = indexItem + 1    
        
        for i in range(newIndex):
            listaTemp.append(fila.returnLast(i))
        listaTemp.pop()
        
        newIndex = indexItem + 1
        
        for j in range(newIndex, fila.size()):
            listaTemp.append(fila.returnLast(j))

        for j in range(fila.size()):
            fila.dequeue()

        for i in range(1,len(listaTemp)+1,1):
            fila.enqueue(listaTemp[len(listaTemp)-i])

    #deletarDado - faz uma busca pelo país (chave) em questão e o deleta
    def deletarDado(self,country):
        if fila.isEmpty() == False:
            #country = input('Digite o pais que deseja deletar: ')
            indexQueue = fila.unqueue(0,country)
            self.removeFromQueue(indexQueue)
            messagebox.showinfo("Ok","Pais removido com Sucesso")
        else:
            messagebox.showerror("Error", "A pilha já esta fazia")

    def salvaCSV(self):
        dadosFinal = []
        for i in range(fila.size()):
            dadosFinal.append(fila.returnLast(i))
        self.saveNewDataCsv(dadosFinal)
        messagebox.showinfo("Ok", "CSV Exportado com Sucesso")

