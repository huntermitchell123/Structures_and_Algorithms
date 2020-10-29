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

    def print_graph_dfs_iter(self,root): # print the graph using depth first method iteratively
        temp = root
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


    def print_graph_dfs_recur(self,curr): # print the graph using depth first method recursively - NOT DONE

        print(self.graph[curr])
        if self.graph[curr] != None:
            for next in self.graph[curr]:
                self.print_bst_dfs_recur(next)


    def print_graph_bfs(self): # print the graph using breadth first method - NOT DONE
        pass



if __name__=="__main__":

    graph_edges = {
        1:2, 2:[3,4], 3:5, 5:1
    }
    g1 = Graph(edges=graph_edges)
    g1.add_edge(4,6)

    print(g1.graph)
    print("Printing Graph using dfs iteratively")
    g1.print_graph_dfs_iter(1)
    #print("Printing Graph using dfs recursively")
    #g1.print_graph_dfs_recur(1)



