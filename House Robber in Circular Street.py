def robLinear(nums):
    prev1 = 0
    prev2 = 0

    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current

    return prev1

def rob(nums):
    n = len(nums)

    if n == 0:
        return 0

    if n == 1:
        return nums[0]

    return max(robLinear(nums[1:]), robLinear(nums[:-1]))

nums = [2, 3, 2]
print("The maximum money you can rob without alerting the police is", rob(nums))

nums = [1, 2, 3, 1]
print("The maximum money you can rob without alerting the police is", rob(nums))