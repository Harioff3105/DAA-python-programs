def uniqueElements(arr):
    unique = []

    for num in arr:
        if num not in unique:
            unique.append(num)

    return unique

arr = [3, 7, 3, 5, 2, 5, 9, 2]
print(uniqueElements(arr))

arr = [-1, 2, -1, 3, 2, -2]
print(uniqueElements(arr))

arr = [1000000, 999999, 1000000]
print(uniqueElements(arr))