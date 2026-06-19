INF = float("inf")

def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

routers = ["A", "B", "C", "D", "E", "F"]
n = 6
matrix = [[INF] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = 0

edges = [
    (0, 1, 1), (0, 2, 5), (1, 2, 2), (1, 3, 1),
    (2, 4, 3), (3, 4, 1), (3, 5, 6), (4, 5, 2)
]

for u, v, w in edges:
    matrix[u][v] = w
    matrix[v][u] = w

before = floyd_warshall(matrix)
print("Router A to Router F before failure:", before[0][5])

matrix[1][3] = INF
matrix[3][1] = INF

after = floyd_warshall(matrix)
print("Router A to Router F after failure:", after[0][5])
