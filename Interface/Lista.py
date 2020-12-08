#from main import main

# -*- coding: utf-8 -*- 
import csv # módulo necessário poder se trabalhar com csv
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza
import random # módulo para geração de números pseudo-aleatórios
from tkinter import *
from tkinter import messagebox
 

dados = []
dadosTemp = []
itemTemp = []

class Pais:
    #Função criarDados() - Função que adciona um novo dado na lista (adcionando todas as informações de um novo país)
    #Usamos uma lista temporaria para ir guardando cada item necessário para completar uma linha de dados, depois
    #Retornamos esse valor para ser adcionado na lista original
    def criarNewDado(self, newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError, newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity,newDystopiaResidual):
        itemTemp.clear()
        
        self.country = newCountry
        itemTemp.append(newCountry)

        self.region = newRegion
        itemTemp.append(newRegion)

        self.happinessRank = newHappinessRank
        itemTemp.append(str(newHappinessRank))

        self.happinessScore = newHappinessScore
        itemTemp.append(str(newHappinessRank))
        
        self.standardError = newStandardError
        itemTemp.append(str(newStandardError))

        self.economy = newEconomy
        itemTemp.append(str(newEconomy))

        self.family = str(newFamily)
        itemTemp.append(str(newFamily))

        self.health = str(newHealth)
        itemTemp.append(str(newHealth))

        self.freedom = newFreedom
        itemTemp.append(str(newFreedom))
        
        self.trust = newTrust
        itemTemp.append(str(newTrust))

        self.generosity= newGenerosity
        itemTemp.append(str(newGenerosity))
        
        self.dystopiaResidual = newDystopiaResidual
        itemTemp.append(str(newDystopiaResidual))
        #Retorno da lista com todas as novas informações
        return itemTemp

    #Campo das edições de dados: as funções a seguir permite editar cada item da base de dados validas!
    #Colocamos em métodos separadas para melhorar a eficiência do retorno.
    def editarCountry(self, newCountry):
        self.country = newCountry
        return str(newCountry)
        
    def editarRegion(self, newRegion):
        self.region = newRegion
        return str(newRegion)
        
    def editarHappinessRank(self, newHappinessRank):
        self.happinessRank = newHappinessRank
        return str(newHappinessRank)
        
    def editarHappinessScore(self, newHappinessScore):
        self.happinessScore = newHappinessScore
        return str(newHappinessScore)
        
    def editarStandardError(self, newStandardError):
        self.standardError = newStandardError
        return str(newStandardError)
        
    def editarEconomy(self, newEconomy):
        self.economy = newEconomy
        return str(newEconomy)
        
    def editarFamily(self, newFamily):
        self.familyHealth = newFamily
        return str(newFamily)

    def editarHealth(self, newHealth):
        self.health = newHealth
        return str(newHealth)
        
    def editarFreedom(self, newFreedom):
        self.freedom = newFreedom
        return str(newFreedom)
        
    def editarTrust(self, newTrust):
        self.trust = newTrust
        return str(newTrust)
        
    def editarGenerosity(self,newGenerosity):
        self.generosity = newGenerosity
        return str(newGenerosity)
        
    def editarDystopiaResidual(self, newDystopiaResidual):
        self.dystopiaResidual = newDystopiaResidual
        return str(newDystopiaResidual)



class Main:

    def __init__(self):
        self.openData()
        self.aleatorioData()
        #self.start()
        
    # openData - abre os arquivos (csv) e faz toda manipulação para ser colocado na lista
    def openData(self):
        with open('data.csv', newline='') as arquivo:
            leitor=csv.reader(arquivo)
            leitor.__next__()
            for linha in leitor:
                dadosTemp.append(linha)

    # aleatorioData - cria uma lista com os 100 dados aleatórios da base de dados original 
    def aleatorioData(self):
        k = 0
        visitados = []
        while(k < 100):
            valorAleatorio = random.randint(1,100)
            if valorAleatorio not in visitados:
                visitados.append(valorAleatorio)
                dados.append(dadosTemp[valorAleatorio])
                k+=1

    # altera_csv - recebe a lista de dados com todas as alterações e manipulações e exportar para outro arquivo csv
    def altera_csv(self,dados):
        with open('data_1.csv', 'w', newline='') as arquivo_csv:
            escrever = csv.writer(arquivo_csv)
            for linha in dados:
                escrever.writerow(linha)

    #inserirDadoMatriz - adiciona na lista os arquivos que forma alterados, de forma "pontual" na linha e coluna desejada
    def inserirDadoMatriz(self,i,j,item):
        dados[i][j] = item

    #indiceItem - retorna o indice do item na lista, usando como chave o país
    def indiceItem(self,country):
        for i in range(len(dados)):
            if country.lower() in dados[i][0].lower():
                return i
        return

    #verificar - mostra se o país em questão já está na lista (impendindo repetições)
    def verificar(self,newCountry, newHappinessRank):
        for i in range(len(dados)):
            print(i)
            if newCountry.lower() in dados[i][0].lower() or str(newHappinessRank) in dados[i][2]:
                return False
        return True
    #verificar - mostra se o país em questão já está na lista (impendindo repetições)
    
    def verificar2(self,esc,newCountry=None, newHappinessRank=None):
        for i in range(len(dados)):
            if esc == 1:
                if newCountry.lower() in dados[i][0].lower():
                    return False

            if esc == 2:
                if str(newHappinessRank) in dados[i][2]:
                    return False
        return True
    #deletarDado - faz uma busca pelo país (chave) em questão e o deleta
    def deletarDado(self,country):
        for i in range(len(dados)):
            if country.lower() in dados[i][0].lower():
                del dados[i]
                messagebox.showinfo("OK", "Pais Removido com Sucesso")
                return
        messagebox.showerror("Error", "Pais não existe")     

    # criarDado - pega todas as informações necessárias para o cadastro e adiciona na lista 
    # (caso não tenha um pais de mesmo nome)
    def criarDado(self,newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError,newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity, newDystopiaResidual):        
        
        newLine = Pais()
        country = newCountry 
        rank = newHappinessRank
        verify = self.verificar(country,rank)
        print(verify)
        if  verify == False:
            messagebox.showinfo("Erro", "Pais ou rank já existe")
            return
        else:
            retorno = newLine.criarNewDado(newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError,newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity, newDystopiaResidual)
            dados.append(retorno)
            messagebox.showinfo("Ok", "Pais criado com Sucesso")


    # editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos
    def editarDado(self,choose,country,data):
        for i in range(len(dados)):
            if str(country.lower()) in dados[i][0].lower():
                linhaDados = self.indiceItem(country)
                newLine = Pais()
                if choose == 1:
                    retorno = newLine.editarCountry(data)
                    retorno2 = self.verificar2(1,data)

                    if retorno2 == True:
                        self.inserirDadoMatriz(linhaDados,0,retorno)
                        messagebox.showinfo("Ok", "Edição Realizada")
                    else:
                        messagebox.showerror("Error", "Pais já Existe")
                elif choose == 2:
                    retorno = newLine.editarRegion(data)
                    self.inserirDadoMatriz(linhaDados,1,retorno)

                elif choose == 3:
                    retorno = newLine.editarHappinessScore(data)
                    retorno2 = self.verificar2(2,data)
                    if retorno2 == True:
                        self.inserirDadoMatriz(linhaDados,2,retorno)
                    else:
                        messagebox.showinfo("Erro", "Rank já existe")

                elif choose == 4:
                    retorno = newLine.editarHappinessRank(data)
                    self.inserirDadoMatriz(linhaDados,3,retorno)

                elif choose == 5:
                    retorno = newLine.editarStandardError(data)
                    self.inserirDadoMatriz(linhaDados,4,retorno)

                elif choose == 6:
                    retorno = newLine.editarEconomy(data)
                    self.inserirDadoMatriz(linhaDados,5,retorno)

                elif choose == 7:
                    retorno = newLine.editarFamily(data)
                    self.inserirDadoMatriz(linhaDados,6,retorno)

                elif choose == 8:
                    retorno = newLine.editarHealth(data)
                    self.inserirDadoMatriz(linhaDados,7,retorno)

                elif choose == 9:
                    retorno = newLine.editarFreedom(data)
                    self.inserirDadoMatriz(linhaDados,8,retorno)

                elif choose == 10:
                    retorno = newLine.editarTrust(data)
                    self.inserirDadoMatriz(linhaDados,9,retorno)

                elif choose == 11:
                    retorno = newLine.editarGenerosity(data)
                    self.inserirDadoMatriz(linhaDados,10,retorno)

                elif choose == 12:
                    retorno = newLine.editarDystopiaResidual(data)
                    self.inserirDadoMatriz(linhaDados,11,retorno)


    def salvaData(self):
        self.altera_csv(dados)
        messagebox.showinfo("OK", "Arquivo Criado com Sucesso")

    #showList - imprime todos os dados contidos na lista
    def showList(self):
        root = Tk()
        show = Text(root,width=500, height=50)
        show.pack()

        for i in range(len(dados)):
            show.insert(END,dados[i])

