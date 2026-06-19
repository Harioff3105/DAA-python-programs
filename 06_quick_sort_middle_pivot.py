def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        print("After partition:", arr)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

test_cases = [
    [19, 72, 35, 46, 58, 91, 22, 31],
    [31, 23, 35, 27, 11, 21, 15, 28],
    [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
]

for arr in test_cases:
    print("Input:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)
    print()
