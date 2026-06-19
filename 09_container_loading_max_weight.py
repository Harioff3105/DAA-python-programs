def max_loaded_weight(weights, max_capacity):
    weights.sort(reverse=True)
    total = 0
    for weight in weights:
        if total + weight <= max_capacity:
            total += weight
    return total

print(max_loaded_weight([10,20,30,40,50], 60))
print(max_loaded_weight([5,10,15,20,25,30], 50))
