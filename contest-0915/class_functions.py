import math


# I use ChatCPT to implemet the sieve eratosthenes show in the class
def sieve_eratosthenes(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(math.sqrt(n)) + 1):
        if is_prime[num]:
            is_prime[num*num::num] = [False] * len(range(num*num, n + 1, num))

    primes = [num for num in range(n + 1) if is_prime[num]]
    return primes


# Factorial algorithm in prime numbers
def prime_factors(n):
    primes = sieve_eratosthenes(n)
    factors = []
    pf_idx = 0
    pf = primes[pf_idx]
    while(n != 1 and pf_idx < len(primes)-1):
        while n % pf == 0:
            n //= pf
            factors.append(pf)
        pf_idx += 1
        primes[pf_idx]
    if(n != 1):
        factors.append(n)
    return factors


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lmc(a, b):
    return a * (b // gcd(a, b))

# Implementation of Euler's Totic function as shown in class


def euler_phi(n):
    primes = sieve_eratosthenes(n)
    pf_idx = 0
    pf = primes[pf_idx]
    ans = n
    while (n != 1 and pf*pf <= n):
        if(n % pf == 0):
            # n = n (1-1/p)
            ans -= ans//pf
        while(n % pf == 0):
            n //= pf
        pf_idx += 1
        pf = primes[pf_idx]
    if(n != 1):
        ans -= ans//n
    return ans
