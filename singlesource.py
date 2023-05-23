from collections import defaultdict
import heapq

# Function to find the shortest path from a source vertex to all other vertices
# Function to find the shortest path from a source vertex to all other vertices
def dijkstra(graph, source):
    # Initialize distances and visited status for all vertices
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Create a priority queue to store vertices with their distances
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if the vertex has already been visited
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors and update distances
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

    # Create a priority queue to store vertices with their distances
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if the vertex has already been visited
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors and update distances
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Main code
graph = defaultdict(dict)

num_vertices = int(input("Enter the number of vertices in the graph: "))
num_edges = int(input("Enter the number of edges in the graph: "))

print("Enter the edges and their weights in the format 'vertex1 vertex2 weight':")
for _ in range(num_edges):
    v1, v2, weight = input().split()
    graph[int(v1)][int(v2)] = int(weight)

source_vertex = int(input("Enter the source vertex: "))

shortest_distances = dijkstra(graph, source_vertex)

print("Shortest distances from the source vertex:")
for vertex, distance in shortest_distances.items():
    print(f"To vertex {vertex}: {distance}")
