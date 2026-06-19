def dijkstra_matrix(graph, source):
    n = len(graph)
    dist = [float("inf")] * n
    visited = [False] * n
    dist[source] = 0
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if graph[u][v] != float("inf") and not visited[v]:
                dist[v] = min(dist[v], dist[u] + graph[u][v])
    return dist

INF = float("inf")
graph1 = [[0,10,3,INF,INF],[INF,0,1,2,INF],[INF,4,0,8,2],[INF,INF,INF,0,7],[INF,INF,INF,9,0]]
graph2 = [[0,5,INF,10],[INF,0,3,INF],[INF,INF,0,1],[INF,INF,INF,0]]
print(dijkstra_matrix(graph1, 0))
print(dijkstra_matrix(graph2, 0))
