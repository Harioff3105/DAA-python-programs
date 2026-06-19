def orientation(a, b, c):
    value = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])

    if value == 0:
        return 0
    elif value > 0:
        return 1
    else:
        return 2

def convex_hull(points):
    n = len(points)

    if n < 3:
        return points

    hull = []
    leftmost = 0

    for i in range(1, n):
        if points[i][0] < points[leftmost][0]:
            leftmost = i

    p = leftmost

    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == leftmost:
            break

    return hull

points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
print("Convex Hull:", convex_hull(points))
print("Time Complexity: O(nh), where h is number of hull points")
