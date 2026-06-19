def strassen_2x2(A, B):
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]

    e, f = B[0][0], B[0][1]
    g, h = B[1][0], B[1][1]

    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    C11 = p5 + p4 - p2 + p6
    C12 = p1 + p2
    C21 = p3 + p4
    C22 = p1 + p5 - p3 - p7

    return [[C11, C12], [C21, C22]]

A = [[1, 7], [3, 5]]
B = [[6, 8], [4, 2]]

print("Matrix A:", A)
print("Matrix B:", B)
print("Product Matrix C:", strassen_2x2(A, B))
