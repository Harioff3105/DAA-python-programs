def binarySearch(arr, key):
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [3, 4, 6, -9, 10, 8, 9, 30]

key = 10
result = binarySearch(arr, key)
if result != -1:
    print("Element", key, "is found at position", result)
else:
    print("Element", key, "is not found")

key = 100
result = binarySearch(arr, key)
if result != -1:
    print("Element", key, "is found at position", result)
else:
    print("Element", key, "is not found")