def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum

test_cases = [
    [5, 7, 3, 4, 9, 12, 6, 2],
    [1, 3, 5, 7, 9, 11, 13, 15, 17],
    [22, 34, 35, 36, 43, 67, 12, 13, 15, 17]
]

for arr in test_cases:
    mn, mx = find_min_max(arr)
    print("Array:", arr)
    print("Min =", mn, "Max =", mx)
    print()
