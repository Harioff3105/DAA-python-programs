def find_the_city(n, edges, distanceThreshold):
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    answer = -1
    min_count = float("inf")

    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and dist[i][j] <= distanceThreshold:
                count += 1

        if count <= min_count:
            min_count = count
            answer = i

    return answer

print(find_the_city(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
print(find_the_city(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
