def min_containers(weights, max_capacity):
    weights.sort(reverse=True)
    containers = []
    for weight in weights:
        placed = False
        for i in range(len(containers)):
            if containers[i] + weight <= max_capacity:
                containers[i] += weight
                placed = True
                break
        if not placed:
            containers.append(weight)
    return len(containers)

print(min_containers([5,10,15,20,25,30,35], 50))
print(min_containers([10,20,30,40,50,60,70,80], 100))
