"""
Hunter Mitchell
10/28/20
Description:
Implementing a Graph data structure in Python. Then testing different search methods
including a Depth First Search and Breadth First Search
"""



class Graph:
    'This class represents a graph'

    def __init__(self,edges):
        self.graph = edges

    def add_edge(self,a,b):
        self.graph[a] = b



if __name__=="__main__":

    graph_edges = {
        1:3, 9:2, 3:[4,5], 5:1
    }
    g1 = Graph(edges=graph_edges)

    print(g1.graph)