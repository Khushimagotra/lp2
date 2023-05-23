from collections import defaultdict

# Function to find the vertex with the minimum key value from the set of vertices not yet included in MST
def min_key(vertices, key, mst_set):
    min_key_value = float('inf')
    min_key_vertex = None

    for v in vertices:
        if key[v] < min_key_value and not mst_set[v]:
            min_key_value = key[v]
            min_key_vertex = v

    return min_key_vertex

# Function to print the MST
def print_mst(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(parent)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Function to find the MST using Prim's algorithm
def prim_mst(graph):
    num_vertices = len(graph)
    key = [float('inf')] * num_vertices  # Key values used to pick minimum weight edge in cut
    parent = [None] * num_vertices  # Array to store constructed MST
    mst_set = [False] * num_vertices  # Set to keep track of vertices included in MST

    key[0] = 0  # Start with the first vertex
    parent[0] = -1  # First node is always the root of the MST

    for _ in range(num_vertices - 1):
        u = min_key(range(num_vertices), key, mst_set)
        mst_set[u] = True

        for v in range(num_vertices):
            if graph[u][v] > 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print_mst(parent, graph)

# Main code
graph = defaultdict(dict)

num_vertices = int(input("Enter the number of vertices in the graph: "))
num_edges = int(input("Enter the number of edges in the graph: "))

print("Enter the edges and their weights in the format 'vertex1 vertex2 weight':")
for _ in range(num_edges):
    v1, v2, weight = input().split()
    graph[int(v1)][int(v2)] = int(weight)
    graph[int(v2)][int(v1)] = int(weight)

prim_mst(graph)