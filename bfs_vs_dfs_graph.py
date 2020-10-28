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

    def print_graph_dfs_iter(self): # print the graph using depth first method iteratively
        pass

    def print_graph_dfs_recur(self,curr): # print the graph using depth first method recursively

        print(self.graph[curr])
        if self.graph[curr] != None:
            for next in self.graph[curr]:
                self.print_bst_dfs_recur(next)


    def print_graph_bfs(self): # print the graph using breadth first method
        pass



if __name__=="__main__":

    graph_edges = {
        1:2, 2:[3,4], 3:5#, 5:1
    }
    g1 = Graph(edges=graph_edges)
    g1.add_edge(4,6)

    print(g1.graph)
    print("Printing Graph using dfs recursively")
    g1.print_graph_dfs_recur(1)



