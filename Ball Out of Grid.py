def findPaths(m, n, N, i, j):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[i][j] = 1
    count = 0

    for step in range(N):
        temp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if dp[r][c] > 0:
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr = r + dr
                        nc = c + dc

                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            count += dp[r][c]
                        else:
                            temp[nr][nc] += dp[r][c]

        dp = temp

    return count

print(findPaths(2, 2, 2, 0, 0))
print(findPaths(1, 3, 3, 0, 1))