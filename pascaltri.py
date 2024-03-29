INF = float('inf')

def floyd_algorithm(graph):
    num_vertices = len(graph)
    # Initialize the distance matrix with the given graph
    dist = [row[:] for row in graph]

    # Calculate shortest paths using Floyd's algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage:
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

shortest_paths = floyd_algorithm(graph)

print("Shortest paths between all pairs of vertices:")
for row in shortest_paths:
    print(row)
