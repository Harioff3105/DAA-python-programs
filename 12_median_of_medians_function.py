def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group) // 2] for group in groups]
    pivot = median_of_medians(medians, (len(medians) + 1) // 2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(lows):
        return median_of_medians(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))

test_cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6),
    ([23, 17, 31, 44, 55, 21, 20, 18, 19, 27], 5)
]

for arr, k in test_cases:
    print("Array:", arr)
    print("k =", k)
    print("Output:", median_of_medians(arr, k))
    print()
