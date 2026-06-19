def find_kth_positive(arr, k):
    missing_count = 0
    current = 1
    index = 0

    while True:
        if index < len(arr) and arr[index] == current:
            index += 1
        else:
            missing_count += 1
            if missing_count == k:
                return current

        current += 1

print(find_kth_positive([2, 3, 4, 7, 11], 5))
print(find_kth_positive([1, 2, 3, 4], 2))
