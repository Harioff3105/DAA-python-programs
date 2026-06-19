def sum_subarray_mins(arr):
    mod = 10 ** 9 + 7
    stack = []
    total = 0

    for i in range(len(arr) + 1):
        current = arr[i] if i < len(arr) else 0

        while stack and (i == len(arr) or arr[stack[-1]] >= current):
            mid = stack.pop()
            left = mid - stack[-1] if stack else mid + 1
            right = i - mid
            total += arr[mid] * left * right

        stack.append(i)

    return total % mod

print(sum_subarray_mins([3, 1, 2, 4]))
print(sum_subarray_mins([11, 81, 94, 43, 3]))
