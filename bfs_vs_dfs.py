"""
Hunter Mitchell
10/28/20
Description:
Implementing a Graph and Binary Search Tree data structure in Python. Then testing different search methods
including a Depth First Search and Breadth First Search
"""

from collections import defaultdict


class Graph:
    'This class represents a graph'

    def __init__(self):
        self.graph = {}

    #def add_edge(self,a,b)
    #    self.graph



class Node:
    'This class represents a node'

    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right



class BST:
    'This class represents a Binary Search Tree'

    def __init__(self,root):
        self.root = Node(root)

    def add_leaf(self,leaf): # add leaf to tree
        temp = self.root
        while (temp != None):
            if (leaf < temp.value): 
                if (temp.left == None):
                    temp.left = Node(leaf)
                    temp = None
                else:
                    temp = temp.left

            elif (leaf > temp.value):
                if (temp.right == None):
                    temp.right = Node(leaf)
                    temp = None
                else:
                    temp = temp.right
            else :
                print('same value as something in here already')
                temp = None


    def print_bst_dfs_iter(self): # print the binary search tree using depth first method iteratively

        temp = self.root
        print(temp.value)
        visited = [temp] # list of what nodes have been visited
        stack = [temp] # our stack

        while (len(stack) != 0):

            temp = stack[-1]

            if (temp.left != None and temp.left not in visited):
                temp = temp.left
                print(temp.value)
                stack.append(temp)
                visited.append(temp)
            elif (temp.right != None and temp.right not in visited):
                temp = temp.right
                print(temp.value)
                stack.append(temp)
                visited.append(temp)
            else :
                stack.pop()
            


    def print_bst_dfs_rec(self,curr): # print the binary search tree using depth first method recursively

        print(curr.value)
        if curr.left != None:
            self.print_bst_dfs_rec(curr.left)
        if curr.right != None:
            self.print_bst_dfs_rec(curr.right)

    def print_bst_bfs(self):
        temp = self.root
        queue = [temp.value]
        








if __name__ == "__main__":

    #g1 = Graph()
    #print(g1.graph)

    bst1 = BST(5)
    for i in [3,1,4,8,10]:
        bst1.add_leaf(i)



    print('Printing BST DFS Iteratively')
    bst1.print_bst_dfs_iter()
    print('Printing BST DFS Recursively')
    bst1.print_bst_dfs_rec(bst1.root)
    #print('Printing BST BFS')
    #bst1.print_bst_bfs(bst1.root)

