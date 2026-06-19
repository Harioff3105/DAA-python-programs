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

matrix = [
    [0, 3, 8, -4],
    [INF, 0, 4, 1],
    [2, INF, 0, INF],
    [INF, 6, -5, 0]
]

print("Before:")
for row in matrix:
    print(row)

dist = floyd_warshall(matrix)

print("After:")
for row in dist:
    print(row)

print("Shortest path City 1 to City 3:", dist[0][2])
