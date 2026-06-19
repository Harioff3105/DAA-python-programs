def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

test_cases = [
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [5, 5, 5, 5, 5],
    [2, 3, 1, 3, 2, 1, 1, 3]
]

for arr in test_cases:
    print("Input:", arr)
    print("Output:", insertion_sort(arr))
    print()

print("Insertion Sort is stable because duplicate values keep their relative order.")
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
