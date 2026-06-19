comparisons = 0

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    global comparisons
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

test_cases = [
    [12, 4, 78, 23, 45, 67, 89, 1],
    [38, 27, 43, 3, 9, 82, 10]
]

for arr in test_cases:
    comparisons = 0
    sorted_arr = merge_sort(arr)
    print("Input:", arr)
    print("Sorted Array:", sorted_arr)
    print("Comparisons:", comparisons)
    print()
