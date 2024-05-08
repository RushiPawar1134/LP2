class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, start_vertex):
        visited = set()
        self.DFSUtil(start_vertex, visited)

    def BFS(self, start_vertex):
        visited = set([start_vertex])
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

# Function to take graph input from the user
def user_input_graph():
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges in the format 'a b' where 'a' and 'b' are vertex names:")
    
    for _ in range(num_edges):
        u, v = input().split()
        g.add_edge(u, v)
    return g

# Main execution
graph = user_input_graph()
print("Enter the starting vertex for DFS:")
start_vertex_dfs = input()
print("Depth First Search starting from vertex " + start_vertex_dfs)
graph.DFS(start_vertex_dfs)

print("\nEnter the starting vertex for BFS:")
start_vertex_bfs = input()
print("Breadth First Search starting from vertex " + start_vertex_bfs)
graph.BFS(start_vertex_bfs)