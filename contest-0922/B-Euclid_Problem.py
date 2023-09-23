# Calcula the GCD
def get_gcd(number_1, number_2):
    while(number_2 != 0):
        rest = number_1 % number_2
        number_1 = number_2
        number_2 = rest

    return number_1

# Calculates the extended euclides coefficient as seen in class


def extended_euclid(number_1, number_2):
    if number_2 == 0:
        return 1, 0, number_1
    x0, y0, d = extended_euclid(number_2, number_1 % number_2)
    y1 = x0 - (a//b) * y0
    return x0, y1, d


while True:
    try:
        a, b = map(int, input().split())

        # Ax + by = C leads to linear congruence Ax ≡ C (mod b).
        d = get_gcd(a, b)
        x1, y1, d = extended_euclid(a, b)

        print(x1, y1, d)

    except EOFError:
        break
