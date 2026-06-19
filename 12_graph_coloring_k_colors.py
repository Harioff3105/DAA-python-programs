def can_color_graph(n, edges, k):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [-1] * n

    def is_safe(vertex, color):
        for neighbor in graph[vertex]:
            if colors[neighbor] == color:
                return False
        return True

    def backtrack(vertex):
        if vertex == n:
            return True

        for color in range(k):
            if is_safe(vertex, color):
                colors[vertex] = color

                if backtrack(vertex + 1):
                    return True

                colors[vertex] = -1

        return False

    possible = backtrack(0)
    return possible, colors if possible else []

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
k = 3

possible, colors = can_color_graph(n, edges, k)
print("Can color graph using", k, "colors?", possible)
print("Color assignment:", colors)
print("Maximum regions you can color:", (n + 2) // 3)
