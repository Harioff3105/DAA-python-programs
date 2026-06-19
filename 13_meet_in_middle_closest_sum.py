from itertools import combinations
from bisect import bisect_left

def subset_sums(arr):
    result = []

    for r in range(len(arr) + 1):
        for comb in combinations(arr, r):
            result.append((sum(comb), list(comb)))

    return result

def closest_subset_sum(arr, target):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sums = subset_sums(left)
    right_sums = subset_sums(right)
    right_sums.sort(key=lambda x: x[0])

    right_values = [x[0] for x in right_sums]
    best_sum = None
    best_subset = []

    for left_sum, left_subset in left_sums:
        needed = target - left_sum
        index = bisect_left(right_values, needed)

        for i in [index - 1, index]:
            if 0 <= i < len(right_sums):
                total = left_sum + right_sums[i][0]

                if best_sum is None or abs(target - total) < abs(target - best_sum):
                    best_sum = total
                    best_subset = left_subset + right_sums[i][1]

    return best_subset, best_sum

test_cases = [
    ([45, 34, 4, 12, 5, 2], 42),
    ([1, 3, 2, 7, 4, 6], 10)
]

for arr, target in test_cases:
    subset, total = closest_subset_sum(arr, target)
    print("Set:", arr)
    print("Target Sum:", target)
    print("Closest Subset:", subset)
    print("Closest Sum:", total)
    print()
