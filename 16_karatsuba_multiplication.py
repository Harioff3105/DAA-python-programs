def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    power = 10 ** half

    high_x = x // power
    low_x = x % power
    high_y = y // power
    low_y = y % power

    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba(low_x + high_x, low_y + high_y)
    z2 = karatsuba(high_x, high_y)

    return (z2 * (10 ** (2 * half))) + ((z1 - z2 - z0) * power) + z0

x = 1234
y = 5678

print("x =", x)
print("y =", y)
print("z =", karatsuba(x, y))
