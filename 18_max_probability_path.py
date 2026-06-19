import heapq
from collections import defaultdict

def max_probability(n, edges, succProb, start, end):
    graph = defaultdict(list)

    for (u, v), prob in zip(edges, succProb):
        graph[u].append((v, prob))
        graph[v].append((u, prob))

    probabilities = [0.0] * n
    probabilities[start] = 1.0
    heap = [(-1.0, start)]

    while heap:
        prob, node = heapq.heappop(heap)
        prob = -prob

        if node == end:
            return prob

        if prob < probabilities[node]:
            continue

        for neighbor, edge_prob in graph[node]:
            new_prob = prob * edge_prob

            if new_prob > probabilities[neighbor]:
                probabilities[neighbor] = new_prob
                heapq.heappush(heap, (-new_prob, neighbor))

    return 0.0

print(max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print(max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
