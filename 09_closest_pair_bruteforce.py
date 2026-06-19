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

points = [(1, 2), (4, 5), (7, 8), (3, 1)]
pair, min_distance = closest_pair(points)

print("Closest pair:", pair[0], "-", pair[1])
print("Minimum distance:", min_distance)
print("Time Complexity: O(n^2)")
