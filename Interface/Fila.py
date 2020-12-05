# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em csv
import csv # módulo necessário poder se trabalhar com csv
import random # módulo para geração de números pseudo-aleatórios
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza

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
                if (dado in self.items[i][j]):
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

    def insert(self, newCountry,newHappinessRank):
        try:
            self.item.insert(0,newCountry)
            newRegion = input('Digite o nome da regiao: ')
            self.item.append(newRegion)
            self.item.insert(2,newHappinessRank)
            newHappinessScore = float(input('Digite o score da felicidade: '))
            self.item.append(newHappinessScore)
            newStandardError = float(input('Digite o Erro Padrão: '))
            self.item.append(newStandardError)
            newEconomy = float(input('Digite a economia: '))
            self.item.append(newEconomy)
            newFamily = float(input('Digite da Família: '))
            self.item.append(newFamily)
            newHealth = float(input('Digite da Saúde: '))
            self.item.append(newHealth)
            newFreedom = float(input('Digite a Liberdade: '))
            self.item.append(newFreedom)
            newTrust = float(input('Digite a Confiança: '))
            self.item.append(newTrust)
            newGenerosity = float(input('Digite de Generosidade: '))
            self.item.append(newGenerosity)
            newDystopiaResidual = float(input('Digite a Distopia Residual: '))
            self.item.append(newDystopiaResidual)
            return(self.item)
        except:
            print("Erro de tipo")
            self.insert(newCountry,newHappinessRank)

    # editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos

    def editar(self,sumario):
        print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
        print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
        print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
        choose = int(input())
        if choose == 1:
            editCountry = input('Entre com o novo nome do país: ')
            return (sumario,0,editCountry)
        
        elif choose == 2:
            editRegion = input('Entre com a novo nome da região: ')
            return(sumario,1,editRegion)

        elif choose == 3:
            editHappinessScore = int(input('Entre com o novo rank de Felicidade: '))
            return(sumario,2,editHappinessScore)
       
        elif choose == 4:
            editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
            return(sumario,3,editHappinessRank)
            
        elif choose == 5:
            editStandartError = float(input('Entre com o novo Erro Padrão: '))
            return(sumario,4,editStandartError)
            

        elif choose == 6:
            editEconomy = float(input('Entre com a novo valor da Economia: '))
            return(sumario,5,editEconomy)
            
        elif choose == 7:
            editFamily = float(input('Entre com o novo indice "Family": '))
            return(sumario,6,editFamily)
            

        elif choose == 8:
            editHealth = float(input('Entre com o novo indice "Health": '))
            return(sumario,7,editHealth)
            

        elif choose == 9:
            editFreedom = float(input('Entre com o novo indice de liberdade: '))
            return(sumario,8,editFreedom)
            

        elif choose == 10:
            editTrust = float(input('Entre com o novo indice de confiança: '))
            return(sumario,9,editTrust)
            

        elif choose == 11:
            editGenerosity = float(input('Entre com o novo indice "Generosity": '))
            return(sumario,10,editGenerosity)
            

        elif choose == 12:
            editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
            return(sumario,11,editDystopiaResidual)
            
dados = []
fila =  Queue()
country = Pais()

class Main:

    def __init__(self):
        self.openData()
        self.aleatorioData()
        self.start()
    
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
        for i in range(fila.size()):
            print(fila.showQueue(i))


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
    def deletarDado(self):
        if fila.isEmpty() == False:
            country = input('Digite o pais que deseja deletar: ')
            indexQueue = fila.unqueue(0,country)
            self.removeFromQueue(indexQueue)
            print('Removido!')
        else:
            print('Fila ja está vazia')


    # start - aqui são oferecidas aos usuários todas as opções disponíveis em um menu interativo
    def start(self):
        print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Lista\n4-Deletar Item\n5-Exportar CSV\n6-Limpar Console\n0-Sair')
        esc = int(input())
        if esc == 1:
            #criarDado()
            newCountry = input('Digite o nome do pais: ')
            newHappinessRank = int(input('Digite o rank da felicidade: '))
            if (fila.percorrerQueue(0,newCountry)) != False or (fila.percorrerQueue(2,str(newHappinessRank))) != False:
                print('Inicie Novamente o cadastro por favor')
                self.start()
            item = country.insert(newCountry,newHappinessRank)
            fila.enqueue(item)
            self.start()
            
        if esc == 2:
            nameCountry = str(input("Digite o nome do pais que deseja editar: "))
            if fila.percorrerQueue(0, nameCountry) == True:
                sumario = fila.indiceQueue(0,nameCountry)
                i,j,data =country.editar(sumario)
                if j == 0:
                    if fila.percorrerQueue(0,data) != True:
                        fila.queueEditar(i,j,data)
                        self.start()
                    else:
                        print("Nome da pais ja existe na fila")
                        self.start()
                elif j == 2:
                    if fila.percorrerQueue(2,int(data)) != True:
                        fila.queueEditar(i,j,data)
                        self.start()
                    else:
                        print("Rankg ja existe na fila")
                        self.start()   
                else: 
                    fila.queueEditar(i,j,data)
                    print("EDIÇÃO COMPLETA")
                    self.start()
            else:
                print("Pais não existe na fila")
                self.start()
            
        if esc == 3:
            self.showQueue()
            self.start()
            
        
        if esc == 4:
            self.deletarDado()
            self.start()
                
        if esc == 5:
            dadosFinal = []
            for i in range(fila.size()):
                dadosFinal.append(fila.returnLast(i))
            self.saveNewDataCsv(dadosFinal)
            self.start()
            
        if esc == 6:        
            os.system('clear')
            self.start()
            
        if esc == 0:
            exit()
            
        else:
            print("Operação invalida!")
            self.start()
    
