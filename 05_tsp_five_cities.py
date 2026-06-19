from itertools import permutations

def tsp(cities, dist):
    start = cities[0]
    best_cost = float("inf")
    best_route = None

    for perm in permutations(cities[1:]):
        route = [start] + list(perm) + [start]
        cost = 0

        for i in range(len(route) - 1):
            cost += dist[route[i]][route[i + 1]]

        if cost < best_cost:
            best_cost = cost
            best_route = route

    return best_route, best_cost

cities = ["A", "B", "C", "D", "E"]

dist = {
    "A": {"A":0, "B":10, "C":15, "D":20, "E":25},
    "B": {"A":10, "B":0, "C":35, "D":25, "E":30},
    "C": {"A":15, "B":35, "C":0, "D":30, "E":20},
    "D": {"A":20, "B":25, "C":30, "D":0, "E":15},
    "E": {"A":25, "B":30, "C":20, "D":15, "E":0}
}

route, cost = tsp(cities, dist)
print("Shortest Route:", " -> ".join(route))
print("Total Distance:", cost)
