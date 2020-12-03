#Classe Vertex: Onde é montado nossos Vertices
from typing import Coroutine


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
