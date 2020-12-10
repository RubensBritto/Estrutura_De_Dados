# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em csv
import csv # módulo necessário poder se trabalhar com csv
import random # módulo para geração de números pseudo-aleatórios
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza

from fila import Queue
from pais import Pais

dados = []
fila =  Queue()
country = Pais()

# openData - abre os arquivos (csv) e faz toda manipulação para ser colocado na fila
def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        for linha in leitor:
            dados.append(linha)

# saveNewDataCsv - recebe a fila de dados com todas as alterações e manipulações e exportar para outro arquivo csv
def saveNewDataCsv(dadosFinal):
    with open('datas/2015_1.csv', 'w', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        for linha in dadosFinal:
            escrever.writerow(linha)

# aleatorioData - cria uma lista com os 100 dados aleatórios da base de dados original e 
# adciona a fila
def aleatorioData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,157)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            fila.enqueue(dados[valorAleatorio])
            k+=1

#showQueue - imprime todos os dados contidos na fila        
def showQueue():
    for i in range(fila.size()):
       print(fila.showQueue(self,i))


# removeFromQueue - cria uma lista temporaria, guarda o index do item da fila a ser removido
# passa a fila para uma lista, remove o item na lista e depois coloca essa lista sem o item de volta na fila

def removeFromQueue(indexItem):
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
def deletarDado():
    if fila.isEmpty() == False:
        country = input('Digite o pais que deseja deletar: ')
        indexQueue = fila.unqueue(0,country)
        removeFromQueue(indexQueue)
        print('Removido!')
    else:
        print('Fila ja está vazia')


# start - aqui são oferecidas aos usuários todas as opções disponíveis em um menu interativo
def start():
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Lista\n4-Deletar Item\n5-Exportar CSV\n6-Limpar Console\n0-Sair')
    esc = int(input())
    if esc == 1:
        #criarDado()
        newCountry = input('Digite o nome do pais: ')
        newHappinessRank = int(input('Digite o rank da felicidade: '))
        if (fila.percorrerQueue(0,newCountry)) != False or (fila.percorrerQueue(2,str(newHappinessRank))) != False:
            print('Inicie Novamente o cadastro por favor')
            start()
        item = country.insert(newCountry,newHappinessRank)
        fila.enqueue(item)
        start()
        
    if esc == 2:
        nameCountry = str(input("Digite o nome do pais que deseja editar: "))
        if fila.percorrerQueue(0, nameCountry) == True:
            sumario = fila.indiceQueue(0,nameCountry)
            i,j,data =country.editar(sumario)
            if j == 0:
                if fila.percorrerQueue(0,data) != True:
                    fila.queueEditar(i,j,data)
                    start()
                else:
                    print("Nome da pais ja existe na fila")
                    start()
            elif j == 2:
                if fila.percorrerQueue(2,int(data)) != True:
                    fila.queueEditar(i,j,data)
                    start()
                else:
                    print("Rankg ja existe na fila")
                    start()   
            else: 
                fila.queueEditar(i,j,data)
                print("EDIÇÃO COMPLETA")
                start()
        else:
            print("Pais não existe na fila")
            start()
        
    if esc == 3:
        showQueue()
        start()
        
    
    if esc == 4:
        deletarDado()
        start()
            
    if esc == 5:
        dadosFinal = []
        for i in range(fila.size()):
            dadosFinal.append(fila.returnLast(i))
        saveNewDataCsv(dadosFinal)
        start()
        
    if esc == 6:        
        os.system('clear')
        start()
        
    if esc == 0:
        exit()
        
    else:
        print("Operação invalida!")
        start()
def main():
    openData()
    aleatorioData()
    start()

if __name__ == "__main__":
    main()
