def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        print("After partition:", arr)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

test_cases = [
    [10, 16, 8, 12, 15, 6, 3, 9, 5],
    [12, 4, 78, 23, 45, 67, 89, 1],
    [38, 27, 43, 3, 9, 82, 10]
]

for arr in test_cases:
    print("Input:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)
    print()
