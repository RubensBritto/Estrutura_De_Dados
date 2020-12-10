# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em csv
import csv # módulo necessário poder se trabalhar com csv
import random # módulo para geração de números pseudo-aleatórios
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza
from os import sendfile
from tkinter import *
from tkinter import messagebox

#Nesta classe nós simulamos uma pilha implementada do zero. Basicamente definimos todas as funções que uma pilha tem 
#implementada e acessamos seus métodos na main como se fosse uma função nativa da linguagem, praticamente!

"""
Temos basicamente as seguintes funções: 
- isEmpty = verifica se a pilha está vazia
- push = adiciona um elemento (seja string, int, ou até mesmo listas)
- pop = remove um elemento da pilha, no caso, por se tratar de uma pilha, o último item
- peek = retorna o último elemento da pilha, para consultas ou implementações
- size = retorna o tamanho da pilha
- percorrerStack = percorrer a lista e verifica se determinado dado está na lista
- desempilhar = desempilha a lista para que determinado elemento possa ser removido
- returnLast = retorna o último item da lista, pórem diferente da peek, este método pode ser alterado
- stackEditar = método usado para acessar e editar determinado item da pilha
- indiceStack = retorna o indice na pilha em que o dado procurado está posicionado
- showStack = imprime na tela todos os itens presentes na pilha
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def percorrerStack(self, j, dado):
        for i in range(self.size()):
            if (str(dado.lower()) in self.items[i][j].lower()):
                return True
        return False

    def desempilhar(self, j, dado):
         for i in range(self.size()):
            if (dado.lower() in self.items[i][j].lower()):
                return i

    def returnLast(self, i):
        return self.items[i]
    
    def stackEditar(self, i, j, dados):
        self.items[i][j] = str(dados)
    
    def indiceStack(self,j,dado):
        for i in range(self.size()):
            if (dado.lower() in self.items[i][j].lower()):
                return i

    def showStack(self,i):
        return self.items[i]
    
    def ordenar(indexItem):
        pass

dados = []
pilha =  Stack()

class Main:
    def iniciar (self):
        self.openData()
        self.aleatorioData()

    # openData - abre os arquivos (csv) e faz toda manipulação para ser colocado na pilha
    def openData(self):
        with open('data.csv', newline='') as arquivo:
            leitor=csv.reader(arquivo)
            leitor.__next__()
            for linha in leitor:
                dados.append(linha)

    # saveNewDataCsv - recebe a pilha de dados com todas as alterações e manipulações e exportar para outro arquivo csv
    def saveNewDataCsv(self,dadosFinal):
        with open('data_1.csv', 'w', newline='') as arquivo_csv:
            escrever = csv.writer(arquivo_csv)
            for linha in dadosFinal:
                escrever.writerow(linha)

    # aleatorioData - cria uma lista com os 100 dados aleatórios da base de dados original e 
    # adciona a pilha
    def aleatorioData(self):
        k = 0
        visitados = []
        while(k < 100):
            valorAleatorio = random.randint(1,157)
            if valorAleatorio not in visitados:
                visitados.append(valorAleatorio)
                pilha.push(dados[valorAleatorio])
                k+=1
        #
    #showStack - imprime todos os dados contidos na pilha        

    def showStack(self):
        root = Tk()
        show = Text(root,width=500, height=50,pady=10,padx=10)
        show.pack()
        dados = []
        for i in range(pilha.size()):
            dados.append(pilha.showStack(i))
            show.insert(END,"Pais: " + str(dados[i][0] )+ "\nRegião: " + str(dados[i][1] )+ "\nRank Felicidade: " + str(dados[i][2] )+ "\nScore Felicidade: " + str(dados[i][3] )+
                "\nErro Padrão: " + str(dados[i][4] )+ "\nIndice de Economia: " + str(dados[i][5] )+ "\nIndice da Familia: " + str(dados[i][6] )+ "\nExpectativa de Vida: " + str(dados[i][7] )+
                "\nIndice de Liberdade: " + str(dados[i][8] )+ "\nIndice de Confiança: " + str(dados[i][9] )+ "\nIndice de Genorosidade: "+ str(dados[i][10])+ "\nIndice de Distopia Residual: "+
                str(dados[i][11]) + "\n\n")
    #verificar - mostra se o país em questão já está na pilha (impendindo repetições)
    def verificar(self,esc,dado):
        for i in range(pilha.size()):
            if esc == 1:
                if str(dado.lower()) in dados[i][0].lower():
                    messagebox.showerror("Error","Pais já existe na pilha")
                    return False

            if esc == 2:
                if str(dado) in str(dados[i][2]):
                    messagebox.showerror("Error","Rank de Felicidade já existe na pilha")
                    return False
        return True

    # criarDado - pega todas as informações necessárias para o cadastro e adiciona na pilha 
    # (caso não tenha um pais de mesmo nome)
    def criarDado(self,newCountry,newRegion,newHappinessRank,newHappinessScore,newStandardError,newEconomy,newFamily,newHealth,newFreedom,newTrust,newGenerosity,newDystopiaResidual):
        itemTemp = []
        itemTemp.append(newCountry)
        itemTemp.append(newRegion)
        itemTemp.append(str(newHappinessRank))
        verify1 = self.verificar(1,newCountry)
        verify2 = self.verificar(2,str(newHappinessRank))      
        if ((verify1 != False) and (verify2 != False)):
            itemTemp.append(str(newHappinessScore))
            itemTemp.append(str(newStandardError))
            itemTemp.append(str(newEconomy))
            itemTemp.append(str(newFamily))
            itemTemp.append(str(newHealth))
            itemTemp.append(str(newFreedom))
            itemTemp.append(str(newTrust))
            itemTemp.append(str(newGenerosity))
            itemTemp.append(str(newDystopiaResidual))
            pilha.push(itemTemp)
            messagebox.showinfo("OK", "Inserção feita com Sucesso")
            return
        else:
            return

    # editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos
    def editarDado(self,choose,country, dado):
        verify  = pilha.percorrerStack(0, country)
        if  verify != True:
            messagebox.showerror("Error", "Pais não exista na Pilha")
            return
        else:
            sumario = pilha.indiceStack(0,country)
            if choose == 0:
                retorno = self.verificar(1,dado)
                if retorno == True:
                    pilha.stackEditar(sumario,0,dado)
            
            elif choose == 1:
                pilha.stackEditar(sumario,1,dado)
            
            elif choose == 2:
                retorno = self.verificar(2,str(dado))
                if retorno == True:
                    pilha.stackEditar(sumario,2,dado)
            
            elif choose == 3:
                pilha.stackEditar(sumario,3,dado)
            
            elif choose == 4:
                pilha.stackEditar(sumario,4,dado)
            
            elif choose == 5:
                pilha.stackEditar(sumario,5,dado)
            
            elif choose == 6:
                pilha.stackEditar(sumario,6,dado)
            
            elif choose == 7:
                pilha.stackEditar(sumario,7,dado)
            
            elif choose == 8:
                pilha.stackEditar(sumario,8,dado)
            
            elif choose == 9:
                pilha.stackEditar(sumario,9,dado)
            
            elif choose == 10:
                pilha.stackEditar(sumario,10,dado)

            elif choose == 11:
                pilha.stackEditar(sumario,11,dado)

        messagebox.showinfo("OK", "Edição Relizada com sucesso")

    # removeFromStack - cria uma lista temporaria, guarda o index do item da pilha a ser removido
    # passa a pilha para uma lista, remove o item na lista e depois coloca essa lista sem o item de volta na pilha

    def removeFromStack(self,indexItem):
        listaTemp = []
        newIndex = indexItem + 1

        for i in range(newIndex):
            listaTemp.append(pilha.returnLast(i))
        listaTemp.pop()

        newIndex = indexItem + 1

        for j in range(newIndex, pilha.size()):
            listaTemp.append(pilha.returnLast(j))

        for j in range(pilha.size()):
            pilha.pop()

        i = 0    
        while (i < (len(listaTemp))):
            pilha.push(listaTemp[i])
            i+=1

    #deletarDado - faz uma busca pelo país (chave) em questão e o deleta
    def deletarDado(self,country):
        if pilha.isEmpty() == False:
            indexStack = pilha.desempilhar(0,country)
            self.removeFromStack(indexStack)
            messagebox.showinfo("OK", "Pais Removido com Sucesso")
        else:
            messagebox.showerror("Error", "Pilha já esta vazia")

    # salvaCSV - Exporta o arquivo csv
    def salvaCSV(self):
        dadosFinal = []
        for i in range(pilha.size()):
            dadosFinal.append(pilha.returnLast(i))
        self.saveNewDataCsv(dadosFinal)
        messagebox.showinfo("Ok", "CSV Exportado com Sucesso")

       