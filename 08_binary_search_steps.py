def binary_search_steps(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print("Low =", low + 1, "High =", high + 1, "Mid =", mid + 1, "Value =", arr[mid])

        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

test_cases = [
    ([3, 9, 14, 19, 25, 31, 42, 47, 53], 31),
    ([13, 19, 24, 29, 35, 41, 42], 42),
    ([20, 40, 60, 80, 100, 120], 60)
]

for arr, key in test_cases:
    print("Array:", arr)
    print("Search Key:", key)
    print("Position:", binary_search_steps(arr, key))
    print()

print("Binary Search works correctly only on sorted arrays.")
print("If the array is not sorted, the result may be wrong because the algorithm discards half of the array based on order.")
