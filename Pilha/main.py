# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em csv
import csv # módulo necessário poder se trabalhar com csv
import random # módulo para geração de números pseudo-aleatórios
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza

from pilha import Stack

dados = []
pilha =  Stack()

# openData - abre os arquivos (csv) e faz toda manipulação para ser colocado na pilha
def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        for linha in leitor:
            dados.append(linha)

# saveNewDataCsv - recebe a pilha de dados com todas as alterações e manipulações e exportar para outro arquivo csv
def saveNewDataCsv(dadosFinal):
    with open('datas/2015_1.csv', 'w', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        for linha in dadosFinal:
            escrever.writerow(linha)

# aleatorioData - cria uma lista com os 100 dados aleatórios da base de dados original e 
# adciona a pilha
def aleatorioData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,100)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            pilha.push(dados[valorAleatorio])
            k+=1

#showStack - imprime todos os dados contidos na pilha        
def showStack():
    for i in range(pilha.size()):
       print(pilha.showStack(i))

#verificar - mostra se o país em questão já está na pilha (impendindo repetições)
def verificar(newCountry, newHappinessRank):
    for i in range(pilha.size()):
        if pilha.percorrerStack(0,newCountry) == True or pilha.percorrerStack(2,newHappinessRank) == True: 
                print('Pais ou Rankg ja existe')
                return False 
    return True

# criarDado - pega todas as informações necessárias para o cadastro e adiciona na pilha 
# (caso não tenha um pais de mesmo nome)
def criarDado():
    itemTemp = []
    newCountry = input('Digite o nome do pais: ')
    itemTemp.append(newCountry)
    newRegion = input('Digite o nome da regiao: ')
    itemTemp.append(newRegion)
    newHappinessRank = int(input('Digite o rank da felicidade: '))
    itemTemp.append(str(newHappinessRank))
    verificacao = verificar(newCountry,str(newHappinessRank))
    if verificacao == False:
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
        pilha.push(itemTemp)

# editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos
def editarDado():
    country = str(input("Digite o pais que deseja editar: "))
    for i in range(pilha.size()):
        if pilha.percorrerStack(0, country) == True:
            sumario = pilha.indiceStack(0,country)
            print(sumario)
            print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
            print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
            print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
            choose = int(input())
            if choose == 1:
                editCountry = str(input('Entre com o novo nome do país: '))
                retorno = verificar(editCountry,str(0.0))
                print(retorno)
                if retorno == True:
                    pilha.stackEditar(sumario,0,editCountry)
                else:
                    print("Pais já existe")
            elif choose == 2:
                editRegion = input('Entre com a novo nome da região: ')
                pilha.stackEditar(sumario,1,editRegion)
                return

            elif choose == 3:
                editHappinessScore = float(input('Entre com o novo rank de Felicidade: '))
                retorno = verificar(" ",str(editHappinessScore))
                if retorno == True:
                    pilha.stackEditar(sumario,2,editHappinessScore)
                else:
                    print("Rank já existe")
            if choose == 4:
                editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
                pilha.stackEditar(sumario,3,editHappinessRank)
                return

            elif choose == 5:
                editStandartError = float(input('Entre com o novo Erro Padrão: '))
                pilha.stackEditar(sumario,4,editStandartError)
                return

            elif choose == 6:
                editEconomy = float(input('Entre com a novo valor da Economia: '))
                pilha.stackEditar(sumario,5,editEconomy)
                return

            elif choose == 7:
                editFamily = float(input('Entre com o novo indice "Family": '))
                pilha.stackEditar(sumario,6,editFamily)
                return

            elif choose == 8:
                editHealth = float(input('Entre com o novo indice "Health": '))
                pilha.stackEditar(sumario,7,editHealth)
                return

            elif choose == 9:
                editFreedom = float(input('Entre com o novo indice de liberdade: '))
                pilha.stackEditar(sumario,8,editFreedom)
                return

            elif choose == 10:
                editTrust = float(input('Entre com o novo indice de confiança: '))
                pilha.stackEditar(sumario,9,editTrust)
                return
            
            elif choose == 11:
                editGenerosity = float(input('Entre com o novo indice "Generosity": '))
                pilha.stackEditar(sumario,10,editGenerosity)
                return

            elif choose == 12:
                editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
                pilha.stackEditar(sumario,11,editDystopiaResidual)
                return
    print('Pais não existe')

# removeFromStack - cria uma lista temporaria, guarda o index do item da pilha a ser removido
# passa a pilha para uma lista, remove o item na lista e depois coloca essa lista sem o item de volta na pilha

def removeFromStack(indexItem):
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
def deletarDado():
    if pilha.isEmpty() == False:
        country = input('Digite o pais que deseja deletar: ')
        indexStack = pilha.desempilhar(0,country)
        removeFromStack(indexStack)
        print('Removido!')
    else:
        print('Pilha ja está vazia')
    
# start - aqui são oferecidas aos usuários todas as opções disponíveis em um menu interativo
def start():
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Lista\n4-Deletar Item\n5-Exportar CSV\n6-Limpar Console\n0-Sair')
    choose = int(input())
    if choose == 1:
        criarDado()
        start()
    if choose == 2:
        editarDado()
        start()
    if choose == 3:
        showStack()
        start()
    if choose == 4:
        deletarDado()
        start()
    if choose == 5:
        dadosFinal = []
        for i in range(pilha.size()):
            dadosFinal.append(pilha.returnLast(i))
        saveNewDataCsv(dadosFinal)
        start()
    if choose == 6:        
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

if __name__ == "__main__":
    main()
