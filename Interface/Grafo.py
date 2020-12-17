#Classe Vertex: Onde é montado nossos Vertices
from numpy.core.arrayprint import printoptions
from numpy.lib.function_base import gradient
from numpy.lib.type_check import real_if_close
import pandas as pd
from tkinter import *
from tkinter import messagebox


class Vertex:
    #__init__ = Inicialzação das arestas setando o id e o vertice adjacente
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
    #__str__ = Retorna uma string mostrando os nós e arestas
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    #add_neighbor = O nó do grafo recebe um novo vizinho de peso 0
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    #get_connections = retorna as chaves das arestas
    def get_connections(self):
        return self.adjacent.keys()  
    #get_id = retorna o id do nó
    def get_id(self):
        return self.id
    #get_weight = retorna o peso da aresta
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

#Classe Graph = classe na qual é montado nosso grafo
class Graph(dict):
    
    # __init__ = inicialização do vertice e o numero de vertices
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
    
    # __iter__ = função para iterar os valores dos vertices
    def __iter__(self):
        return iter(self.vert_dict.values())
    
    # add_vertex = se adciona um novo vertice no grafo com as ligações já existentes
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    #get_vertex = retorna (se existir) um nó do vertice
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    #add_edge = adciona uma nova aresta no grafo
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
    
    # get_vertices = retorna todos os vertices do grafo
    def get_vertices(self):
        return self.vert_dict.keys()

graphs = Graph()
list = {}
listTemp = []

class Main():
    def iniciar (self):
        self.openData()
        self.constructorGraph()

    def openData(self):

        #Abertura CSv
        dataset = pd.read_csv('SocialNetwork.csv',encoding='ISO-8859-1')

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
                        listTemp.append((salario[i],salario[j],abs(salario[i]-salario[j])))
                        listAux.insert(0,(salario[j],abs(salario[i]-salario[j])))
            list.update({salario[i]: listAux})
            del (listAux[0])

    def constructorGraph(self):
        #Transforma a lista de adjacencia em um dicionario
        #Cria as arestas (que são a ligação dos vertices) ponderadas (subtração dos salarios)    
        #Adicona as chaves do dicionairo com vertice do grafo
        
        for i in list.keys():
            graphs.add_vertex(i)

        for i,j,k in listTemp:
            graphs.add_edge(i,j,k) 

    def showData(self,esc):
        #esc = input("Digite o que Deseja printar\n1- Caminhos do grafo\n2 - Lista de adjacencia\n")
        root = Tk()
        show = Text(root,width=500, height=50,pady=10,padx=10)
        show.pack()
        #show.insert(END,"A Menor distância é: " + str(shortest_distance[end]) + "\n\n" + "Caminho a ser seguido, passa pelos Nós: " + str(track_path))
        if esc == '1':
            #Printa os caminhos do grafo com seus respectivos pesos 
            for v in graphs:
                for w in v.get_connections():
                    vid = v.get_id()
                    wid = w.get_id()
                    show.insert(END,'( %s , %s, %3d )\n\n'  % ( vid, wid, v.get_weight(w)))
            return
        if esc == '2':
            #Printa lista de adjacencia
            for v in graphs:
                show.insert (END,'VERTICE [%s]= %s\n\n' %(v.get_id(), graphs.vert_dict[v.get_id()]))
            return

    def search(self,start,end):
        if start <= end:
            messagebox.showerror("Error", "O valor do Nó incial necessitar ser maior")
            return
        
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
                messagebox.showerror("Error", "Caminho não existe")
                #print("caminho nao encontrado")
                break            
        track_path.insert(0,start)
        if shortest_distance[end] != infinity:
            root = Tk()
            show = Text(root,width=500, height=50,pady=10,padx=10)
            show.pack()
            show.insert(END,"A Menor distância é: " + str(shortest_distance[end]) + "\n\n" + "Caminho a ser seguido, passa pelos Nós: " + str(track_path))
            #print("Menor distancia é" + str(shortest_distance[end]))
            #print("Caminho a ser seguido" + str(track_path))
