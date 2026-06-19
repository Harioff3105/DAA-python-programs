from functools import lru_cache

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

def cat_mouse_game(graph):
    n = len(graph)

    @lru_cache(None)
    def solve(mouse, cat, turn):
        if turn == 2 * n:
            return DRAW
        if mouse == 0:
            return MOUSE_WIN
        if mouse == cat:
            return CAT_WIN

        if turn % 2 == 0:
            result = CAT_WIN
            for nxt in graph[mouse]:
                outcome = solve(nxt, cat, turn + 1)
                if outcome == MOUSE_WIN:
                    return MOUSE_WIN
                if outcome == DRAW:
                    result = DRAW
            return result
        else:
            result = MOUSE_WIN
            for nxt in graph[cat]:
                if nxt == 0:
                    continue
                outcome = solve(mouse, nxt, turn + 1)
                if outcome == CAT_WIN:
                    return CAT_WIN
                if outcome == DRAW:
                    result = DRAW
            return result

    return solve(1, 2, 0)

print(cat_mouse_game([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))
print(cat_mouse_game([[1,3],[0],[3],[0,2]]))
