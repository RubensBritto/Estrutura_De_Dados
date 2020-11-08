
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
tree = BinarySearchTree()


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
        for linha in leitor:
            dadosTemp.append(linha)

def aleatorioData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1,100)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            tree.insert(valorAleatorio)
            dados.append(dadosTemp[k])
            k+=1
def main():
    openData()
    aleatorioData()
    tree.inorder_traversal()
    if tree.search(2) != None:
        print('ENCONTRADO')
    else:
        print('NÃO ENCONTRADO')
if __name__ == "__main__":
    main()
    print()
    