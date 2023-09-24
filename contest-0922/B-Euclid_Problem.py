# Calcula the GCD
def get_gcd(a, b):
    while(b != 0):
        rest = a % b
        a = b
        b = rest

    return a

# Calculates the extended euclides coefficient as seen in class


def extended_euclid(a, b):
    if b == 0:
        return 1, 0, a
    x0, y0, d = extended_euclid(b, a % b)
    return y0,  (x0 - (a//b) * y0), d


while True:
    try:
        a, b = map(int, input().split())

        # ax + by = c leads to linear congruence ax ≡ c (mod b).
        d = get_gcd(a, b)
        # Find Bézout coefficients
        x1, y1, d = extended_euclid(a, b)

        print(x1, y1, d)

    except EOFError:
        break
