def findMaximum(arr):
    if len(arr) == 0:
        return "List is empty"

    arr.sort()
    return arr[-1]

arr = []
print(findMaximum(arr))

arr = [5]
print(findMaximum(arr))

arr = [3, 3, 3, 3, 3]
print(findMaximum(arr))