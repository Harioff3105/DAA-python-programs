def solve_n_queens(n):
    result = []
    board = [["." for _ in range(n)] for _ in range(n)]
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return True

        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue

            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if backtrack(row + 1):
                return True

            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False

    backtrack(0)
    return result[0] if result else []

for n in [4, 5, 8]:
    print("N =", n)
    solution = solve_n_queens(n)
    for row in solution:
        print(row)
    print()
