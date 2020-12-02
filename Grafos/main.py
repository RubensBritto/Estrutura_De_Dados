from numpy.lib.function_base import gradient
import pandas as pd
from grafo import Graph

list = []
listTemp = []
graphs = Graph()


def openData():

    #Abertura CSv
    dataset = pd.read_csv('datas/SocialNetwork.csv',encoding='ISO-8859-1')

    #Deletando as Colunas que não iram ser utilizadas
    dataset.drop(['User ID', 'Gender','Purchased'], axis=1, inplace=True)
    #Orderno o data set por idade
    dataset = dataset.sort_values('EstimatedSalary', ascending=False)
    #Excluo as repetições dos valores, deixando apenas a primeira aparição
    dataset = dataset.drop_duplicates(subset='EstimatedSalary', keep='first')
    #Converte cada coluna em um array
    #idade = dataset["Age"].to_numpy()
    salario = dataset["EstimatedSalary"].to_numpy()

    #Faz a lista de adjacencia e calcula a distancia entre os vertices
    for i in range(len(salario)):
        if salario[i] % 2 == 0: 
            #print("Chave " + str(salario[i]))
            for j in range(len(salario)):
                if abs(salario[i]-salario[j]) != 0:
                    list.append((salario[i],salario[j]))
                    listTemp.append((salario[i],salario[j],abs(salario[i]-salario[j])))

def constructorGraph():
    #Transforma a lista de adjacencia em um dicionario
    aresta = dict(list)
    
    #Adicona as chaves do dicionairo com vertice do grafo
    for i in aresta.keys():
        graphs.add_vertex(i)

    #Cria as arestas (que são a ligação dos vertices) ponderadas (subtração dos salarios)
    for i,j,k in listTemp:
        graphs.add_edge(i,j,k) 

def showData():
    esc = input("Digite o que Deseja printar\n1- Caminhos do grafo\n2 - Lista de adjacencia\n")
    if esc == '1':
        #Printa os caminhos do grafo com seus respectivos pesos 
        for v in graphs:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
    if esc == '2':
        #Printa lista de adjacencia
        for v in graphs:
            print ('VERTICE [%s]= %s' %(v.get_id(), graphs.vert_dict[v.get_id()]))
            print('')



def main():
    openData()
    constructorGraph()
    #showData()
    a=input()
    b=input()
    graphs.dijkstra('16000','15000')


if __name__ == "__main__":
    main()
