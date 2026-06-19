def game_of_life(board):
    m = len(board)
    n = len(board[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            live_neighbors = 0

            for dx, dy in directions:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 1:
                    live_neighbors += 1

            if board[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    result[i][j] = 1
            else:
                if live_neighbors == 3:
                    result[i][j] = 1

    return result

print(game_of_life([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
print(game_of_life([[1, 1], [1, 0]]))
