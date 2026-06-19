def findMax(arr):
    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum

arr = [1, 2, 3, 4, 5]
print(findMax(arr))

arr = [7, 7, 7, 7, 7]
print(findMax(arr))

arr = [-10, 2, 3, -4, 5]
print(findMax(arr))