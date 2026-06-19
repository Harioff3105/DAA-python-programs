def minimum_time_required(jobs, k):
    jobs.sort(reverse=True)
    workers = [0] * k
    answer = sum(jobs)
    def backtrack(index):
        nonlocal answer
        if index == len(jobs):
            answer = min(answer, max(workers))
            return
        if max(workers) >= answer:
            return
        seen = set()
        for i in range(k):
            if workers[i] in seen:
                continue
            seen.add(workers[i])
            workers[i] += jobs[index]
            backtrack(index + 1)
            workers[i] -= jobs[index]
            if workers[i] == 0:
                break
    backtrack(0)
    return answer

print(minimum_time_required([3, 2, 3], 3))
print(minimum_time_required([1, 2, 4, 7, 8], 2))
