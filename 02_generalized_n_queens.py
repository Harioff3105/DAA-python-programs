def solve_generalized_queens(rows, cols, obstacles=None, restricted=None):
    obstacles = set(obstacles or [])
    restricted = restricted or {}
    solution = []
    used_cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == rows:
            return True

        for col in range(cols):
            if row in restricted and col not in restricted[row]:
                continue

            if (row, col) in obstacles:
                continue

            if col in used_cols or row - col in diag1 or row + col in diag2:
                continue

            solution.append(col + 1)
            used_cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if backtrack(row + 1):
                return True

            solution.pop()
            used_cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False

    if backtrack(0):
        return solution
    return None

print("8 x 10 Board:", solve_generalized_queens(8, 10))
print("5 x 5 Board with Obstacles:", solve_generalized_queens(5, 5, obstacles={(1, 1), (3, 3)}))
print("6 x 6 Board with Restricted First Queen:", solve_generalized_queens(6, 6, restricted={0: [0, 2, 4]}))
