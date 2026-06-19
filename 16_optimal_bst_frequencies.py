def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float("inf")
            total = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0
                value = left + right + total

                if value < cost[i][j]:
                    cost[i][j] = value
                    root[i][j] = r

    return cost, root

keys = [10, 12, 16, 21]
freq = [4, 2, 6, 3]

cost, root = optimal_bst(keys, freq)
print("OBST Cost:", cost[0][len(keys) - 1])

print("Cost Matrix:")
for row in cost:
    print(row)

print("Root Matrix:")
for row in root:
    print(row)

cost2, root2 = optimal_bst([10, 12], [34, 50])
print("Test Case 1 Cost:", cost2[0][1])

cost3, root3 = optimal_bst([10, 12, 20], [34, 8, 50])
print("Test Case 2 Cost:", cost3[0][2])
