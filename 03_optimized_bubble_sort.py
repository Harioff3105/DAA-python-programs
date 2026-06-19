def bubble_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break

    return a

test_cases = [
    [64, 25, 12, 22, 11],
    [29, 10, 14, 37, 13],
    [3, 5, 2, 1, 4],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1]
]

for arr in test_cases:
    print("Input:", arr)
    print("Output:", bubble_sort(arr))
    print()

print("Best Case Time Complexity: O(n)")
print("Average/Worst Case Time Complexity: O(n^2)")
