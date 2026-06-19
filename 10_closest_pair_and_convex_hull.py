import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    min_distance = float("inf")
    pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])

            if d < min_distance:
                min_distance = d
                pair = (points[i], points[j])

    return pair, min_distance

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]

pair, min_distance = closest_pair(points)
print("Closest pair:", pair)
print("Minimum distance:", min_distance)

hull = convex_hull(points)
print("Convex Hull:", hull)

print("Closest Pair Time Complexity: O(n^2)")
print("Convex Hull Time Complexity: O(n log n)")
print("Collinear points are handled by keeping boundary points when cross product is 0.")
