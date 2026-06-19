def three_line_assembly(station_times, transfer):
    lines = len(station_times)
    stations = len(station_times[0])
    dp = [[0] * stations for _ in range(lines)]

    for line in range(lines):
        dp[line][0] = station_times[line][0]

    for station in range(1, stations):
        for line in range(lines):
            best = float("inf")
            for previous_line in range(lines):
                cost = dp[previous_line][station - 1] + transfer[previous_line][line] + station_times[line][station]
                best = min(best, cost)
            dp[line][station] = best

    return min(dp[line][stations - 1] for line in range(lines)), dp

station_times = [
    [5, 9, 3],
    [6, 8, 4],
    [7, 6, 5]
]

transfer = [
    [0, 2, 3],
    [2, 0, 4],
    [3, 4, 0]
]

minimum_time, table = three_line_assembly(station_times, transfer)
print("DP Table:", table)
print("Minimum Production Time:", minimum_time)
