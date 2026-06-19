def subsets(nums):
    nums.sort()
    result = []

    def backtrack(index, path):
        result.append(path.copy())

        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
