def exponentMod(x, y, n):
    if y == 0:
        return 1
    if x == 0:
        return 1

    if y % 2 == 0:
        v = exponentMod(x, y//2, n)
        v = (v*v) % n
    else:
        v = x % n
        v = (v * exponentMod(x, y-1, n) % n)

    return (v + n) % n


def extended_euclid(a, b):
    if b == 0:
        return 1, 0, a
    x0, y0, d = extended_euclid(b, a % b)
    return y0,  (x0 - (a//b) * y0), d
