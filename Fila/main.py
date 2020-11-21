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
       print(fila.showQueue(i))

# criarDado - pega todas as informações necessárias para o cadastro e adiciona na fila 
# (caso não tenha um pais de mesmo nome)


def criarDado():
    try:
        newCountry = input('Digite o nome do pais: ')
        newRegion = input('Digite o nome da regiao: ')
        newHappinessRank = int(input('Digite o rank da felicidade: '))
        if (fila.percorrerQueue(0,newCountry)) != False or (fila.percorrerQueue(2,str(newHappinessRank))) != False:
            print('Inicie Novamente o cadastro por favor')
            criarDado()
        newHappinessScore = float(input('Digite o score da felicidade: '))
        newStandardError = float(input('Digite o Erro Padrão: '))
        newEconomy = float(input('Digite a economia: '))
        newFamily = float(input('Digite da Família: '))
        newHealth = float(input('Digite da Saúde: '))
        newFreedom = float(input('Digite a Liberdade: '))
        newTrust = float(input('Digite a Confiança: '))
        newGenerosity = float(input('Digite de Generosidade: '))
        newDystopiaResidual = float(input('Digite a Distopia Residual: '))
        data = country.insert(newCountry,newRegion,newHappinessRank,newHappinessScore,newStandardError,newEconomy,newFamily,newHealth,newFreedom,newTrust,newGenerosity,newDystopiaResidual)
        fila.enqueue(data)
    except:
        print("Erro de tipo")
        criarDado()

# editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos
def editarDado():
    #try:
    country = str(input("Digite o nome do pais que deseja editar: "))
    if fila.percorrerQueue(0, country) == True:
        sumario = fila.indiceQueue(0,country)
        #print(sumario)
        print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
        print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
        print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
        choose = int(input())
        if choose == 1:
            editCountry = input('Entre com o novo nome do país: ')
            retorno = fila.percorrerQueue(0,editCountry)
            if retorno != True:
                print('meu')
                data = country.editar(editCountry,0)
                print(data)
                fila.queueEditar(sumario,0,data)
                return
            else:
                print("Pais já existe")
                editarDado()
                return
        elif choose == 2:
            editRegion = input('Entre com a novo nome da região: ')
            newdata = country.editar(editRegion,1)
            fila.queueEditar(sumario,1,newdata)
            return

        elif choose == 3:
            editHappinessScore = int(input('Entre com o novo rank de Felicidade: '))
            retorno = fila.percorrerQueue(2,int(editHappinessScore))
            if retorno != True:
                newdata = country.editar(editHappinessScore,2)
                fila.queueEditar(sumario,2,newdata)
                return
            else:
                print("Rank já existe")
                editarDado()
                return
        elif choose == 4:
            editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
            newdata = country.editar(editHappinessRank,3)
            fila.queueEditar(sumario,3,newdata)
            return
        elif choose == 5:
            editStandartError = float(input('Entre com o novo Erro Padrão: '))
            newdata = country.editar(editStandartError,4)
            fila.queueEditar(sumario,4,newdata)
            return

        elif choose == 6:
            editEconomy = float(input('Entre com a novo valor da Economia: '))
            newdata = country.editar(editEconomy,5)
            fila.queueEditar(sumario,5,newdata)
            return
        elif choose == 7:
            editFamily = float(input('Entre com o novo indice "Family": '))
            newdata = country.editar(editFamily,6)
            fila.queueEditar(sumario,6,newdata)
            return

        elif choose == 8:
            editHealth = float(input('Entre com o novo indice "Health": '))
            newdata = country.editar(editHealth,7)
            fila.queueEditar(sumario,7,newdata)
            return

        elif choose == 9:
            editFreedom = float(input('Entre com o novo indice de liberdade: '))
            newdata = country.editar(editFreedom,8)
            fila.queueEditar(sumario,8,newdata)
            return

        elif choose == 10:
            editTrust = float(input('Entre com o novo indice de confiança: '))
            newdata = country.editar(editTrust,9)
            fila.queueEditar(sumario,9,newdata)
            return
                
        elif choose == 11:
            editGenerosity = float(input('Entre com o novo indice "Generosity": '))
            newdata = country.editar(editGenerosity,10)
            fila.queueEditar(sumario,10,newdata)
            return

        elif choose == 12:
            editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
            newdata = country.editar(editDystopiaResidual,11)
            fila.queueEditar(sumario,11,newdata)
            return
   # except:
    #    print("Erro de tipo")
    #    editarDado()

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
        criarDado()
        start()
        
    if esc == 2:
        editarDado()
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
