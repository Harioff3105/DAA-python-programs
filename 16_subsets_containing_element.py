def subsets_containing_x(nums, x):
    result = []

    def backtrack(index, path):
        if index == len(nums):
            if x in path:
                result.append(path.copy())
            return

        backtrack(index + 1, path)

        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()

    backtrack(0, [])
    return result

def subsets(nums):
    result = []

    def backtrack(index, path):
        if index == len(nums):
            result.append(path.copy())
            return

        backtrack(index + 1, path)
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()

    backtrack(0, [])
    return result

print(subsets_containing_x([2, 3, 4, 5], 3))
print(subsets([1, 2, 3]))
print(subsets([0]))
