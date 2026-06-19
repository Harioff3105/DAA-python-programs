def champagne_tower(poured, query_row, query_glass):
    dp = [[0] * 101 for _ in range(101)]
    dp[0][0] = poured

    for row in range(100):
        for glass in range(row + 1):
            extra = (dp[row][glass] - 1) / 2

            if extra > 0:
                dp[row + 1][glass] += extra
                dp[row + 1][glass + 1] += extra

    return min(1, dp[query_row][query_glass])

print(champagne_tower(4, 2, 1))
print(champagne_tower(1, 0, 0))
print(champagne_tower(2, 1, 1))
