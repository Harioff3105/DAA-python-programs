def dice_throw(num_sides, num_dice, target):
    dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
    dp[0][0] = 1

    for dice in range(1, num_dice + 1):
        for total in range(1, target + 1):
            for face in range(1, num_sides + 1):
                if total - face >= 0:
                    dp[dice][total] += dp[dice - 1][total - face]

    return dp[num_dice][target]

print("Test Case 1:", dice_throw(6, 2, 7))
print("Test Case 2:", dice_throw(4, 3, 10))
