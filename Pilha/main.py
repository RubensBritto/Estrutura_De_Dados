# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em ssv
import csv
import random
from pilha import Stack

dados = []
pilha =  Stack()

def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        for linha in leitor:
            dados.append(linha)

def aleatorioData():
    k = 0
    visitados = []
    valorAleatorio = random.randint(1,100)
    while(k < 100):
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            print(dados[valorAleatorio])
            pilha.push(dados[valorAleatorio])
            k+=1
        
'''
def showList():
    for i in range(len(dados)):
        rint(pilha.)
'''
def main():
    openData()
    aleatorioData()
    print(pilha.size())
    #showList()
    #print(len(dados))


if __name__ == "__main__":
    main()