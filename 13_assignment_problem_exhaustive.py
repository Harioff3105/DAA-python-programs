import itertools

def total_cost(assignment, cost_matrix):
    total = 0

    for worker in range(len(assignment)):
        task = assignment[worker]
        total += cost_matrix[worker][task]

    return total

def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    min_cost = float("inf")
    best_assignment = None

    for assignment in itertools.permutations(range(n)):
        cost = total_cost(assignment, cost_matrix)

        if cost < min_cost:
            min_cost = cost
            best_assignment = assignment

    result = []

    for worker, task in enumerate(best_assignment):
        result.append((f"worker {worker + 1}", f"task {task + 1}"))

    return result, min_cost

test_cases = [
    [[3, 10, 7], [8, 5, 12], [4, 6, 9]],
    [[15, 9, 4], [8, 7, 18], [6, 12, 11]]
]

for i, matrix in enumerate(test_cases, 1):
    assignment, cost = assignment_problem(matrix)
    print("Test Case", i)
    print("Optimal Assignment:", assignment)
    print("Total Cost:", cost)
    print()

print("Time Complexity: O(n!)")
