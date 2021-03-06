
# -*- coding: utf-8 -*- 
import csv # módulo necessário poder se trabalhar com csv
import os # módulo para acessar o terminal do sistema e poder fazer a limpeza
import random # módulo para geração de números pseudo-aleatórios
from opLista import opLista


dados = []
dadosTemp = []

# openData - abre os arquivos (csv) e faz toda manipulação para ser colocado na lista
def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        for linha in leitor:
            dadosTemp.append(linha)

# aleatorioData - cria uma lista com os 100 dados aleatórios da base de dados original 
def aleatorioData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,100)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            dados.append(dadosTemp[valorAleatorio])
            k+=1

# altera_csv - recebe a lista de dados com todas as alterações e manipulações e exportar para outro arquivo csv
def altera_csv(dados):
    with open('datas/2015_1.csv', 'w', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        for linha in dados:
            escrever.writerow(linha)

#inserirDadoMatriz - adiciona na lista os arquivos que forma alterados, de forma "pontual" na linha e coluna desejada
def inserirDadoMatriz(i,j,item):
    dados[i][j] = item

#indiceItem - retorna o indice do item na lista, usando como chave o país
def indiceItem(country):
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            return i
    return

#verificar - mostra se o país em questão já está na lista (impendindo repetições)
def verificar(newCountry, newHappinessRank):
    for i in range(len(dados)):
        if newCountry.lower() in dados[i][0].lower() or str(newHappinessRank) in dados[i][2]:
            return False
    print('Pais ou ranking nao existe')
    return True

#deletarDado - faz uma busca pelo país (chave) em questão e o deleta
def deletarDado():
    country = input('Digite o pais que deseja deletar: ')
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            del dados[i]
            print('Removido!')
            return
    print('Pais não consta na lista!')        

# criarDado - pega todas as informações necessárias para o cadastro e adiciona na lista 
# (caso não tenha um pais de mesmo nome)
def criarDado():
    newLine = opLista()
    newCountry = input('Digite o nome do pais: ')
    newRegion = input('Digite o nome da regiao: ')
    newHappinessRank = int(input('Digite o rank da felicidade: '))
    verificacao = verificar(newCountry,newHappinessRank)
    if verificacao == False:
        print('Inicie Novamente o cadastro por favor')
        criarDado()
    else:
        newHappinessScore = float(input('Digite o score da felicidade: '))
        newStandardError = float(input('Digite o Erro Padrão: '))
        newEconomy = float(input('Digite a economia: '))
        newFamily = float(input('Digite da Família: '))
        newHealth = float(input('Digite da Saúde: '))
        newFreedom = float(input('Digite a Liberdade: '))
        newTrust = float(input('Digite a Confiança: '))
        newGenerosity = float(input('Digite de Generosidade: '))
        newDystopiaResidual = float(input('Digite a Distopia Residual: '))
        retorno = newLine.criarNewDado(newCountry, newRegion, newHappinessRank, newHappinessScore, newStandardError,newEconomy, newFamily, newHealth, newFreedom, newTrust, newGenerosity, newDystopiaResidual)
        dados.append(retorno)

# editarDado - verifica se o país (chave) a ser editado existe e permite mudar seus atributos
def editarDado():
    country = input("Digite o pais que deseja editar: ")
    for i in range(len(dados)):
        if country.lower() in dados[i][0].lower():
            linhaDados = indiceItem(country)
            newLine = opLista()
            print('Em qual linha/coluna deseja editar um novo dado?\n1 - Pais\n2 - Regiao\n3 - Rankg felicidade')
            print('4 - Indice Felicidade\n5 - Erro Padrão\n6 - Economia\n7 - Family\n8 - Health')
            print('9 - Indice de liberdade\n10 - Indice de confiança\n11 - Indice de Generosidade\n12 - Distopia Residual')
            choose = int(input())
            if choose == 1:
                editCountry = input('Entre com o novo nome do país: ')
                retorno = newLine.editarCountry(editCountry)
                retorno2 = verificar(editCountry,0)
                if retorno2 == True:
                    inserirDadoMatriz(linhaDados,0,retorno)
                else:
                    print("Pais já existe")
            elif choose == 2:
                editRegion = input('Entre com a novo nome da região: ')
                retorno = newLine.editarRegion(editRegion)
                inserirDadoMatriz(linhaDados,1,retorno)

            elif choose == 3:
                editHappinessScore = float(input('Entre com o novo rank de Felicidade: '))
                retorno = newLine.editarHappinessScore(editHappinessScore)
                retorno2 = verificar("",editHappinessScore)
                if retorno2 == True:
                    inserirDadoMatriz(linhaDados,2,retorno)
                else:
                    print("Rank já existe")

            elif choose == 4:
                editHappinessRank = float(input('Entre com o novo Indice de Felicidade: '))
                retorno = newLine.editarHappinessRank(editHappinessRank)
                inserirDadoMatriz(linhaDados,3,retorno)

            elif choose == 5:
                editStandartError = float(input('Entre com o novo Erro Padrão: '))
                retorno = newLine.editarStandardError(editStandartError)
                inserirDadoMatriz(linhaDados,4,retorno)

            elif choose == 6:
                editEconomy = float(input('Entre com a novo valor da Economia: '))
                retorno = newLine.editarEconomy(editEconomy)
                inserirDadoMatriz(linhaDados,5,retorno)

            elif choose == 7:
                editFamily = float(input('Entre com o novo indice "Family": '))
                retorno = newLine.editarFamily(editFamily)
                inserirDadoMatriz(linhaDados,6,retorno)

            elif choose == 8:
                editHealth = float(input('Entre com o novo indice "Health": '))
                retorno = newLine.editarHealth(editHealth)
                inserirDadoMatriz(linhaDados,7,retorno)

            elif choose == 9:
                editFreedom = float(input('Entre com o novo indice de liberdade: '))
                retorno = newLine.editarFreedom(editFreedom)
                inserirDadoMatriz(linhaDados,8,retorno)

            elif choose == 10:
                editTrust = float(input('Entre com o novo indice de confiança: '))
                retorno = newLine.editarTrust(editTrust)
                inserirDadoMatriz(linhaDados,9,retorno)

            elif choose == 11:
                editGenerosity = float(input('Entre com o novo indice "Generosity": '))
                retorno = newLine.editarGenerosity(editGenerosity)
                inserirDadoMatriz(linhaDados,10,retorno)

            elif choose == 12:
                editDystopiaResidual = float(input('Entre com a nova distopia Residual: '))
                retorno = newLine.editarDystopiaResidual(editDystopiaResidual)
                inserirDadoMatriz(linhaDados,11,retorno)

#showList - imprime todos os dados contidos na lista
def showList():
    for i in range(len(dados)):    
        print(dados[i])

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
        showList()
        start()
    if choose == 4:
        deletarDado()
        start()
    if choose == 5:
        altera_csv(dados)
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
    

