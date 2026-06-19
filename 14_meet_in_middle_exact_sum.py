from itertools import combinations

def subset_sums(arr):
    result = set()

    for r in range(len(arr) + 1):
        for comb in combinations(arr, r):
            result.add(sum(comb))

    return result

def has_exact_subset_sum(arr, exact_sum):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sums = subset_sums(left)
    right_sums = subset_sums(right)

    for value in left_sums:
        if exact_sum - value in right_sums:
            return True

    return False

test_cases = [
    ([1, 3, 9, 2, 7, 12], 15),
    ([3, 34, 4, 12, 5, 2], 15)
]

for arr, exact_sum in test_cases:
    print("Set:", arr)
    print("Exact Sum:", exact_sum)
    print("Output:", has_exact_subset_sum(arr, exact_sum))
    print()
