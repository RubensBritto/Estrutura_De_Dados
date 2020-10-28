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
    while(k < 100):
        valorAleatorio = random.randint(1,100)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            pilha.push(dados[valorAleatorio])
            k+=1
        
def showStack():
    for i in range(pilha.size()):
       print(pilha.showStack(i))

def main():
    openData()
    aleatorioData()
    print(pilha.size())
    showStack()
    #print(len(dados))


if __name__ == "__main__":
    main()