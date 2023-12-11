# Return a set with all the prime factors of a number
# I use chatGPT to optimize this function
def get_prime_factors_set(n):
    prime_factors = set()

    while n % 2 == 0:
        prime_factors.add(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            prime_factors.add(i)
            n //= i

    if(n > 2):
        prime_factors.add(n)

    return prime_factors


n = int(input())

while n != 0:
    prime_factors = get_prime_factors_set(n)
    # Uses Euler's Totic function shown in class
    result = n
    for p in prime_factors:
        result *= 1-(1/p)
    print(int(result))

    n = int(input())
