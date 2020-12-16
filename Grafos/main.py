from numpy.core.arrayprint import printoptions
from numpy.lib.function_base import gradient
from numpy.lib.type_check import real_if_close
import pandas as pd
from grafo import Graph

list = {}
listTemp = []
graphs = Graph()


def openData():

    #Abertura CSv
    dataset = pd.read_csv('datas/SocialNetwork.csv',encoding='ISO-8859-1')

    #Deletando as Colunas que não iram ser utilizadas
    dataset.drop(['User ID', 'Gender','Purchased','Age'], axis=1, inplace=True)
    #Orderno o data set por idade
    dataset = dataset.sort_values('EstimatedSalary', ascending=False)
    #Excluo as repetições dos valores, deixando apenas a primeira aparição
    dataset = dataset.drop_duplicates(subset='EstimatedSalary', keep='first')
    #Converte cada coluna em um array
    #idade = dataset["Age"].to_numpy()
    salario = dataset["EstimatedSalary"].to_numpy()

    #Faz a lista de adjacencia e calcula a distancia entre os vertices
    for i in range(len(salario)):
        listAux = []

        #print(i)
        if salario[i] % 2 == 0:
            #print("Chave " + str(salario[i]))
            for j in range(len(salario)):
                if abs(salario[i]-salario[j]) != 0:
                    #list.update({nome:(salario[j],abs(salario[i]-salario[j]))})
                    listTemp.append((salario[i],salario[j],abs(salario[i]-salario[j])))
                    listAux.insert(0,(salario[j],abs(salario[i]-salario[j])))
        list.update({salario[i]: listAux})
        del (listAux[0])

def constructorGraph():
    #Transforma a lista de adjacencia em um dicionario
    #Cria as arestas (que são a ligação dos vertices) ponderadas (subtração dos salarios)
        #Adicona as chaves do dicionairo com vertice do grafo
    print(list.keys())
    for i in list.keys():
        graphs.add_vertex(i)

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


def search(start,end):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = list
    infinity = 999999
    track_path = []
    
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        path_options = list[min_distance_node]
        try:
            for child_node,weight in path_options:
                if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                    shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                    track_predecessor[child_node] = min_distance_node

            unseenNodes.pop(min_distance_node)
        except TypeError:
            weight, child_node = 0,0
    currentNode = end

    while currentNode != start:
        try:
            track_path.insert(0,currentNode)
            #print(currentNode)
            currentNode = track_predecessor[currentNode]
        except:
            print("caminho nao encontrado")
            break            
    track_path.insert(0,start)

    if shortest_distance[end] != infinity:
        print("Menor distancia é" + str(shortest_distance[end]))
        print("Caminho a ser seguido" + str(track_path))
def main():
    openData()
    constructorGraph()
    #showData()
    #a=input("Digite o Primeiro vertice: ")
    #b=input("Digite o Segundo vertice: ")
    #search(a,b)
    search(150000,149000)


if __name__ == "__main__":
    main()
