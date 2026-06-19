def find_min_max(arr):
    return min(arr), max(arr)

test_cases = [
    [2, 4, 6, 8, 10, 12, 14, 18],
    [11, 13, 15, 17, 19, 21, 23, 35, 37],
    [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
]

for arr in test_cases:
    mn, mx = find_min_max(arr)
    print("Array:", arr)
    print("Min =", mn, "Max =", mx)
    print()
