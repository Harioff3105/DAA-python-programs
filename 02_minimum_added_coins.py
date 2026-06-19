def minimum_added_coins(coins, target):
    coins.sort()
    reachable = 0
    added = 0
    i = 0
    while reachable < target:
        if i < len(coins) and coins[i] <= reachable + 1:
            reachable += coins[i]
            i += 1
        else:
            reachable += reachable + 1
            added += 1
    return added

print(minimum_added_coins([1, 4, 10], 19))
print(minimum_added_coins([1, 4, 10, 5, 7, 19], 19))
