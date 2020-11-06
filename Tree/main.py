
# -*- coding: utf-8 -*-
import csv
from tree import BinarySearchTree
import random

# C - Country 
# R - Region
# HR - Happiness Rank
# HS - Happiness Score
# SE - Standard Error
# E - Economy (GDP per Capita)
# FH - Family,Health (Life Expectancy)
# F - Freedom
# T - Trust (Government Corruption),
# G - Generosity,
# DR - Dystopia Residual



dadosTemp = []
dados = []
listaTemp2 = []

'''
with open('datas/2015.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, fieldnames=["C", "R", "HR", "HS", "SE", "E", "FH", "F", "T", "G", "DR"])
    csv_reader.__next__()

    for row in csv_reader:
        print(row)
        print( row["T"] + ', ' + row["P"] + ', ' + row["U"] )
'''
"""
def indexData(i,j):
    newtemp = dadosTemp
    newtemp2 = []
    newtemp2.append(j)
    newtemp3 = dadosTemp + newtemp2
    return newtemp3
"""
def openData():
    with open('datas/2015.csv', newline='') as arquivo:
        leitor=csv.reader(arquivo)
        leitor.__next__()
        i = 0
        j = 0
        listTemp  = []
        listaTemp2 = []
        for linha in leitor:
            listTemp.append(j)
            dadosTemp.append(linha)
            listaTemp2[i] = listTemp + dadosTemp
            i+=1
            j+=1

def aleatorioData():
    bst = BinarySearchTree()
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,100)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            bst.insert(valorAleatorio)
            dados.append(listaTemp2[k])
            k+=1
    #bst.inorder_traversal()
    #bst.simetric_traversal()
    #bst.view()

def main():
    openData()
    aleatorioData()
    for i in range(len(dados)):
        print(dados[i])
    
if __name__ == "__main__":
    main()
    print()
    