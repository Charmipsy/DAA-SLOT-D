import numpy as np

def tsp_dp(graph):
    num_cities = len(graph)
    all_points_set = set(range(num_cities))

    # Memoization table
    memo = {}

    # Helper function to find the shortest tour from start to end, passing through the given set of points
    def dp(start, points_set):
        # If only one point left, return the distance to the end
        if len(points_set) == 1:
            return graph[start][next(iter(points_set))]

        # If this subproblem has already been solved, return the memoized value
        if (start, points_set) in memo:
            return memo[(start, points_set)]

        # Recursively find the shortest tour passing through each remaining point
        min_distance = float('inf')
        for point in points_set:
            new_set = points_set - {point}
            distance = graph[start][point] + dp(point, new_set)
            min_distance = min(min_distance, distance)

        # Memoize the result
        memo[(start, points_set)] = min_distance
        return min_distance

    # Start with city 0 and find the shortest tour
    return dp(0, all_points_set)

# Example usage:
graph = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

shortest_tour_length = tsp_dp(graph)
print("Shortest tour length:", shortest_tour_length)
