def graph_coloring_min_colors(n, edges):
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

    def solve(vertex, max_colors):
        if vertex == n:
            return True

        for color in range(max_colors):
            if is_safe(vertex, color):
                colors[vertex] = color

                if solve(vertex + 1, max_colors):
                    return True

                colors[vertex] = -1

        return False

    for max_colors in range(1, n + 1):
        colors[:] = [-1] * n

        if solve(0, max_colors):
            return max_colors, colors

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4

min_colors, color_assignment = graph_coloring_min_colors(n, edges)
print("Minimum number of colors:", min_colors)
print("Color assignment:", color_assignment)
print("Maximum regions you can color:", (n + 2) // 3)
