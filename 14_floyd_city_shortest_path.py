INF = float("inf")

def floyd_warshall(nodes, edges):
    index = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[index[u]][index[v]] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist, index

nodes = ["A", "B", "C", "D"]
edges = [("B", "A", 2), ("A", "C", 3), ("C", "D", 1), ("D", "A", 6), ("C", "B", 7)]
dist, index = floyd_warshall(nodes, edges)
print("Shortest path C to A:", dist[index["C"]][index["A"]])

nodes2 = ["A", "B", "C", "D", "E"]
edges2 = [("C","A",2), ("A","B",4), ("B","C",1), ("B","E",6), ("E","A",1), ("A","D",5), ("D","E",2), ("E","D",4), ("D","C",1), ("C","D",3)]
dist2, index2 = floyd_warshall(nodes2, edges2)
print("Shortest path E to C:", dist2[index2["E"]][index2["C"]])
