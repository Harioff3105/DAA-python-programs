def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid + 1, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

test_cases = [
    ([5, 10, 15, 20, 25, 30, 35, 40, 45], 20),
    ([10, 20, 30, 40, 50, 60], 50),
    ([21, 32, 40, 54, 65, 76, 87], 32)
]

for arr, key in test_cases:
    position, comparisons = binary_search(arr, key)
    print("Array:", arr)
    print("Search Key:", key)
    print("Position:", position)
    print("Comparisons:", comparisons)
    print()
