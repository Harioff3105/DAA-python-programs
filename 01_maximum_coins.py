def max_coins(piles):
    piles.sort()
    total = 0
    left = 0
    right = len(piles) - 1
    while left < right:
        total += piles[right - 1]
        left += 1
        right -= 2
    return total

print(max_coins([2, 4, 1, 2, 7, 8]))
print(max_coins([2, 4, 5]))
