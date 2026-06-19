def has_hamiltonian_cycle(edges, n):
    graph = [[False] * n for _ in range(n)]

    for u, v in edges:
        graph[u][v] = True
        graph[v][u] = True

    path = [0]
    visited = {0}

    def backtrack(vertex):
        if len(path) == n:
            return graph[path[-1]][path[0]]

        for next_vertex in range(n):
            if next_vertex not in visited and graph[vertex][next_vertex]:
                visited.add(next_vertex)
                path.append(next_vertex)

                if backtrack(next_vertex):
                    return True

                path.pop()
                visited.remove(next_vertex)

        return False

    return backtrack(0)

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4

print(has_hamiltonian_cycle(edges, n))
