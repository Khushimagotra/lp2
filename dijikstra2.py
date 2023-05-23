from heapq import heappop, heappush
import sys

def dijkstra(vertices, edges):
  """
  Dijkstra's algorithm to find the minimum spanning tree of a graph.

  Args:
    vertices: A list of vertices in the graph.
    edges: A list of edges in the graph.

  Returns:
    A list of edges in the minimum spanning tree.
  """

  # Create a set of vertices that have not yet been visited.
  unvisited = set(vertices)

  # Create a dictionary to store the distance to each vertex from the source vertex.
  distance = {v: float("inf") for v in vertices}
  distance[0] = 0

  # Create a heap to store the vertices that are closest to the source vertex.
  heap = []
  heappush(heap, (0, 0))

  # While there are vertices that have not yet been visited:
  while unvisited:
    # Remove the vertex with the shortest distance from the heap.
    _, current_vertex = heappop(heap)

    # Remove the current vertex from the set of unvisited vertices.
    unvisited.remove(current_vertex)

    # For each edge that is connected to the current vertex:
    for neighbor, weight in edges[current_vertex]:
      # If the distance to the neighbor is greater than the distance to the current vertex plus the weight of the edge:
      if distance[neighbor] > distance[current_vertex] + weight:
        # Update the distance to the neighbor.
        distance[neighbor] = distance[current_vertex] + weight

        # Add the neighbor to the heap.
        heappush(heap, (distance[neighbor], neighbor))

  # Return the list of edges in the minimum spanning tree.
  return [(u, v) for u, v, w in edges if w == distance[v]]


def main():
  """
  Main function.

  This function prompts the user to enter the number of vertices and edges in a
  graph. It then uses Dijkstra's algorithm to find the minimum spanning tree of
  the graph and prints the edges in the minimum spanning tree.
  """

  num_vertices = int(input("Enter the number of vertices: "))
  num_edges = int(input("Enter the number of edges: "))

  vertices = list(range(num_vertices))
  edges = []

  for _ in range(num_edges):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

  mst = dijkstra(vertices, edges)

  print("The minimum spanning tree is:")
  for edge in mst:
    print(edge)


if __name__ == "__main__":
  main()