from numpy.lib.function_base import gradient
import pandas as pd
from grafos import Grafo

list = []




dataset = pd.read_csv('datas/SocialNetwork.csv',encoding='ISO-8859-1')
#print(dataset.loc[dataset[UserId]==15624510])
#print(dataset.loc[0,"User ID"])
#print(len(dataset.index))

#Deletando as Colunas que não iram ser utilizadas
dataset.drop(['User ID', 'Gender','Purchased'], axis=1, inplace=True)
#Orderno o data set por idade
dataset = dataset.sort_values('EstimatedSalary', ascending=False)
#Excluo as repetições dos valores, deixando apenas a primeira aparição
dataset = dataset.drop_duplicates(subset='EstimatedSalary', keep='first')
#Converte cada coluna em um array
idade = dataset["Age"].to_numpy()
salario = dataset["EstimatedSalary"].to_numpy()
'''
print(idade)
print(salario)
print(len(salario))
print(salario[0])
'''
#Faz a matriz de adjacencia e calcula a distancia entre os vertices

for i in range(len(salario)):
    if salario[i] % 2 == 0: 
        #print("Chave " + str(salario[i]))
        for j in range(len(salario)):
            if abs(salario[i]-salario[j]) != 0:
                #print(salario[i])
                #print("-" + "Valor: " + str(salario[j]) + "=" + "Distancia: " + str(abs(salario[i]-salario[j])))
                list.append((salario[i],salario[j]))


#print(list)

#arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]
arestas = list
grafo = Grafo(arestas, direcionado=True)
#print(grafo.get_vertices())
print(grafo.get_arestas())
