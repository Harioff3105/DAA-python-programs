def find_target_sum_ways(nums, target):
    count = 0

    def backtrack(index, total):
        nonlocal count

        if index == len(nums):
            if total == target:
                count += 1
            return

        backtrack(index + 1, total + nums[index])
        backtrack(index + 1, total - nums[index])

    backtrack(0, 0)
    return count

print(find_target_sum_ways([1, 1, 1, 1, 1], 3))
print(find_target_sum_ways([1], 1))
