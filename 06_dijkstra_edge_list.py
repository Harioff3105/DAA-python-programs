import heapq
from collections import defaultdict

def dijkstra_edge_list(n, edges, source, target):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [float("inf")] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        current_dist, node = heapq.heappop(heap)
        if node == target:
            return current_dist
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return -1

edges1 = [(0,1,7),(0,2,9),(0,5,14),(1,2,10),(1,3,15),(2,3,11),(2,5,2),(3,4,6),(4,5,9)]
edges2 = [(0,1,10),(0,4,3),(1,2,2),(1,4,4),(2,3,9),(3,2,7),(4,1,1),(4,2,8),(4,3,2)]
print(dijkstra_edge_list(6, edges1, 0, 4))
print(dijkstra_edge_list(5, edges2, 0, 3))
