from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        # Priority queue to store vertices and their key values
        key = [float('inf')] * self.V
        parent = [-1] * self.V  # Array to store constructed MST
        mst_set = [False] * self.V

        # Start from the first vertex
        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            # Pick the minimum key vertex from the set of vertices not yet included in MST
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            # Update key value and parent index of the adjacent vertices of the picked vertex
            for v, w in self.graph[u]:
                if not mst_set[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u

        # Print the constructed MST
        self.print_mst(parent)

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.weight(parent[i], i))

    def weight(self, u, v):
        for node, weight in self.graph[u]:
            if node == v:
                return weight

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim_mst()
