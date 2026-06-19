def champagneTower(poured, query_row, query_glass):
    dp = [[0] * 101 for _ in range(101)]
    dp[0][0] = poured

    for r in range(100):
        for c in range(r + 1):
            extra = (dp[r][c] - 1) / 2

            if extra > 0:
                dp[r + 1][c] += extra
                dp[r + 1][c + 1] += extra

    return min(1, dp[query_row][query_glass])


poured = 4
query_row = 2
query_glass = 1

print(champagneTower(poured, query_row, query_glass))