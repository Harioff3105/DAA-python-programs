def sumCounts(nums):
    total = 0

    for i in range(len(nums)):
        distinct = set()

        for j in range(i, len(nums)):
            distinct.add(nums[j])
            count = len(distinct)
            total += count * count

    return total

nums = [1, 2, 1]
print(sumCounts(nums))

nums = [1, 1]
print(sumCounts(nums))