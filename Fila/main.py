# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em csv
import csv # módulo necessário poder se trabalhar com csv
import random # módulo para geração de números pseudo-aleatórios
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza

from fila import Queue

dados = []
fila =  Queue()

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
        valorAleatorio = random.randint(1,158)
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
    itemTemp = []
    newCountry = input('Digite o nome do pais: ')
    itemTemp.append(newCountry)
    newRegion = input('Digite o nome da regiao: ')
    itemTemp.append(newRegion)
    newHappinessRank = int(input('Digite o rank da felicidade: '))
    itemTemp.append(str(newHappinessRank))
    if (fila.percorrerQueue(0,newCountry)) or (fila.percorrerQueue(2,str(newHappinessRank))) != False:
        print('Inicie Novamente o cadastro por favor')
        itemTemp.clear()
        criarDado()
    else:
        newHappinessScore = float(input('Digite o score da felicidade: '))
        itemTemp.append(str(newHappinessScore))
        newStandardError = float(input('Digite o Erro Padrão: '))
        itemTemp.append(str(newStandardError))
        newEconomy = float(input('Digite a economia: '))
        itemTemp.append(str(newEconomy))
        newFamily = float(input('Digite da Família: '))
        itemTemp.append(str(newFamily))
        newHealth = float(input('Digite da Saúde: '))
        itemTemp.append(str(newHealth))
        newFreedom = float(input('Digite a Liberdade: '))
        itemTemp.append(str(newFreedom))
        newTrust = float(input('Digite a Confiança: '))
        itemTemp.append(str(newTrust))
        newGenerosity = float(input('Digite de Generosidade: '))
        itemTemp.append(str(newGenerosity))
        newDystopiaResidual = float(input('Digite a Distopia Residual: '))
        itemTemp.append(str(newDystopiaResidual))
        fila.enqueue(itemTemp)

# editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos
def editarDado():
    country = str(input("Digite o pais que deseja editar: "))
    if fila.percorrerQueue(0, country) == True:
        sumario = fila.indiceQueue(0,country)
        print(sumario)
        print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
        print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
        print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
        choose = int(input())
        if choose == 1:
            editCountry = str(input('Entre com o novo nome do país: '))
            retorno = fila.percorrerQueue(0,editCountry)
            print(retorno)
            if retorno != True:
                fila.queueEditar(sumario,0,editCountry)
                return
            else:
                print("Pais já existe")
                editarDado()
                return
            return
        elif choose == 2:
            editRegion = input('Entre com a novo nome da região: ')
            fila.queueEditar(sumario,1,editRegion)
            return

        elif choose == 3:
            editHappinessScore = int(input('Entre com o novo rank de Felicidade: '))
            retorno = fila.percorrerQueue(2,str(editHappinessScore))
            if retorno != True:
                fila.queueEditar(sumario,2,editHappinessScore)
                return
            else:
                editarDado()
                print("Rank já existe")
                return
            return
        elif choose == 4:
            editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
            fila.queueEditar(sumario,3,editHappinessRank)
            return

        elif choose == 5:
            editStandartError = float(input('Entre com o novo Erro Padrão: '))
            fila.queueEditar(sumario,4,editStandartError)
            return

        elif choose == 6:
            editEconomy = float(input('Entre com a novo valor da Economia: '))
            fila.queueEditar(sumario,5,editEconomy)
            return
        elif choose == 7:
            editFamily = float(input('Entre com o novo indice "Family": '))
            fila.queueEditar(sumario,6,editFamily)
            return

        elif choose == 8:
            editHealth = float(input('Entre com o novo indice "Health": '))
            fila.queueEditar(sumario,7,editHealth)
            return

        elif choose == 9:
            editFreedom = float(input('Entre com o novo indice de liberdade: '))
            fila.queueEditar(sumario,8,editFreedom)
            return

        elif choose == 10:
            editTrust = float(input('Entre com o novo indice de confiança: '))
            fila.queueEditar(sumario,9,editTrust)
            return
            
        elif choose == 11:
            editGenerosity = float(input('Entre com o novo indice "Generosity": '))
            fila.queueEditar(sumario,10,editGenerosity)
            return

        elif choose == 12:
            editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
            fila.queueEditar(sumario,11,editDystopiaResidual)
            return
    print('Pais Existe')

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
