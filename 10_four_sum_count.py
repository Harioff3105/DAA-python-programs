def four_sum_count(A, B, C, D):
    count_ab = {}

    for a in A:
        for b in B:
            total = a + b
            count_ab[total] = count_ab.get(total, 0) + 1

    count = 0

    for c in C:
        for d in D:
            count += count_ab.get(-(c + d), 0)

    return count

print(four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))
print(four_sum_count([0], [0], [0], [0]))
