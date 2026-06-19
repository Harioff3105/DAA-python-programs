import itertools

def total_value(selected_items, values):
    total = 0

    for item in selected_items:
        total += values[item]

    return total

def total_weight(selected_items, weights):
    total = 0

    for item in selected_items:
        total += weights[item]

    return total

def is_feasible(selected_items, weights, capacity):
    return total_weight(selected_items, weights) <= capacity

def knapsack(weights, values, capacity):
    n = len(weights)
    best_value = 0
    best_selection = []

    for r in range(n + 1):
        for selected_items in itertools.combinations(range(n), r):
            selected_items = list(selected_items)

            if is_feasible(selected_items, weights, capacity):
                value = total_value(selected_items, values)

                if value > best_value:
                    best_value = value
                    best_selection = selected_items

    return best_selection, best_value

test_cases = [
    ([2, 3, 1], [4, 5, 3], 4),
    ([1, 2, 3, 4], [2, 4, 6, 3], 6)
]

for i, (weights, values, capacity) in enumerate(test_cases, 1):
    selection, value = knapsack(weights, values, capacity)
    print("Test Case", i)
    print("Optimal Selection:", selection)
    print("Total Value:", value)
    print()

print("Time Complexity: O(2^n)")
