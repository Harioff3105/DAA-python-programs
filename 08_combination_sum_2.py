def combination_sum2(candidates, target):
    result = []
    candidates.sort()

    def backtrack(start, total, path):
        if total == target:
            result.append(path.copy())
            return

        if total > target:
            return

        previous = None

        for i in range(start, len(candidates)):
            if candidates[i] == previous:
                continue

            path.append(candidates[i])
            backtrack(i + 1, total + candidates[i], path)
            path.pop()
            previous = candidates[i]

    backtrack(0, 0, [])
    return result

print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combination_sum2([2, 5, 2, 1, 2], 5))
