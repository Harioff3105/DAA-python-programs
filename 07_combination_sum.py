def combination_sum(candidates, target):
    result = []
    candidates.sort()

    def backtrack(start, total, path):
        if total == target:
            result.append(path.copy())
            return

        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, total + candidates[i], path)
            path.pop()

    backtrack(0, 0, [])
    return result

print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))
