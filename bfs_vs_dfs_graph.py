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
        try:
            if type(self.graph[a]) == int: # if a is already connected a number
                temp_list = [self.graph[a]]
                temp_list.append(b)
                self.graph[a] = temp_list
            elif type(self.graph[a]) == list: # if a is already connected to multiple numbers
                temp_list = self.graph[a]
                temp_list.append(b)
                self.graph[a] = temp_list
        except: # if a is not connected to anything
            self.graph[a] = b


    def print_graph_dfs_iter(self,start): # print the graph using depth first method iteratively
        temp = start
        print(temp)
        stack = [temp]
        visited = [temp]
        while (len(stack) != 0):
            temp = stack[-1]
            try: 
                if (type(self.graph[temp]) == int): # if the next is one number
                    if (self.graph[temp] not in stack and self.graph[temp] not in visited):
                        stack.append(self.graph[temp])
                        print(self.graph[temp])
                        visited.append(self.graph[temp])
                    else :
                        stack.pop()
                if (type(self.graph[temp]) == list): # if the next is multiple numbers
                    for i in self.graph[temp]:
                        if (i not in stack and i not in visited):
                            stack.append(i)
                            print(i)
                            visited.append(i)
                            break
                        else :
                            stack.pop()
            except: # if there is no self.graph[temp]
                stack.pop()


    def print_graph_dfs_recur(self,curr,visited): # print the graph using depth first method recursively

        print(curr)
        visited.append(curr)

        try:
            if type(self.graph[curr]) == int: # if there is one number next
                if self.graph[curr] not in visited:
                    self.print_graph_dfs_recur(self.graph[curr],visited)

            if type(self.graph[curr]) == list: # if there are multiple numbers next
                for i in self.graph[curr]:
                    if i not in visited:
                        self.print_graph_dfs_recur(i,visited)

        except: # if there is nothing next
            pass


    def print_graph_bfs(self,start): # print the graph using breadth first method

        print(start)
        queue = [start]
        visited = [start]

        while (len(queue) != 0):
            for temp in queue[:]:

                try:
                    if type(self.graph[temp]) == int and self.graph[temp] not in visited: # if next is one number
                        print(self.graph[temp])
                        queue.append(self.graph[temp])
                        visited.append(self.graph[temp])
                    if type(self.graph[temp]) == list: # if next is multiple numbers
                        for i in self.graph[temp]:
                            if i not in visited:
                                print(i)
                                queue.append(i)
                                visited.append(i)

                except: # if there is nothing next
                    pass

                queue.pop(0)



if __name__=="__main__":

    graph_edges = {
        1:2, 2:[3,4], 3:5, 5:1
    }
    g1 = Graph(edges=graph_edges)

    g1.add_edge(4,6)

    print("Graph edges: ",g1.graph)

    print("Printing Graph using dfs iteratively")
    g1.print_graph_dfs_iter(1)
    print("Printing Graph using dfs recursively")
    g1.print_graph_dfs_recur(1,[])
    print("Printing Graph using bfs")
    g1.print_graph_bfs(1)
    



