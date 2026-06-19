from itertools import permutations

def tsp_min_path(matrix):
    n = len(matrix)
    cities = list(range(1, n))
    best_cost = float("inf")
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        cost = 0

        for i in range(len(path) - 1):
            cost += matrix[path[i]][path[i + 1]]

        if cost < best_cost:
            best_cost = cost
            best_path = path

    return best_cost, best_path

test_cases = [
    [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]],
    [[0,10,10,10],[10,0,10,10],[10,10,0,10],[10,10,10,0]],
    [[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]]
]

for matrix in test_cases:
    cost, path = tsp_min_path(matrix)
    print("Minimum Path Distance:", cost)
    print("Path:", path)
    print()
