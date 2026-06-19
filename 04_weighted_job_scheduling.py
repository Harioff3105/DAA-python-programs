from bisect import bisect_right

def job_scheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    ends = [job[1] for job in jobs]
    dp = [0] * (len(jobs) + 1)
    for i in range(1, len(jobs) + 1):
        start, end, value = jobs[i - 1]
        previous = bisect_right(ends, start, 0, i - 1)
        dp[i] = max(dp[i - 1], dp[previous] + value)
    return dp[-1]

print(job_scheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))
print(job_scheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))
