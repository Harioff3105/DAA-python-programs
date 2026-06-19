def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a

test_cases = [
    [5, 2, 9, 1, 5, 6],
    [10, 8, 6, 4, 2],
    [1, 2, 3, 4, 5]
]

for arr in test_cases:
    print("Input:", arr)
    print("Output:", selection_sort(arr))
    print()

print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
