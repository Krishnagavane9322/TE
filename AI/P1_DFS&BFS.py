class Graph:
#simple Graph class that represents a graph using an adjacency matrix
    def __init__(self, vertices):
        #An Constructor which initalize class attributes
        self.vertices = vertices
        #The outer loop iterates over rows and the inner loop iterates over columns
        self.adj_matrix = [[0 for j in range(vertices)] for i in range(vertices)]
    
    def add_edge(self, u, v):
        #when called it updates both u,v & v,u as 1 in matrix
        self.adj_matrix[u][v] =1
        self.adj_matrix[v][u] = 1
    
    def dfs(self, start):
        visited = [False for i in range(self.vertices)]
        #A matrix of visited is initilized first False values after visit True
        stack = []
        stack.append(start)
        visited[start] = True
        while stack:
            s = stack.pop()
            print(s, end=' ')
            for i in range(self.vertices):
                if self.adj_matrix[s][i] == 1 and not visited[i]:
                    #Here visited means that index node is visited
                    stack.append(i)
                    visited[i] = True
    def bfs(self, start):
        visited = [False for i in range(self.vertices)]
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            s = queue.pop(0)
            print(s, end=' ')
            for i in range(self.vertices):
                if self.adj_matrix[s][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
# Creating a graph with 5 vertices
g = Graph(5)
# Adding edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
# Testing the DFS algorithm
print("DFS traversal starting from vertex 0:")
g.dfs(0)
print()
# Testing the BFS algorithm
print("BFS traversal starting from vertex0:")
g.bfs(0)
print()