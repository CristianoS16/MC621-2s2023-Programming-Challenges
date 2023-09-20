import math


# Check if a number is prime using the tips of the class
def is_prime_optimized(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


n = int(input())

while n != 0:
    aux_number = 2 * n + 1
    if aux_number % 2 == 0:
        aux_number += 1

    # Search for the first prime number greater than 2*n
    while(not is_prime_optimized(aux_number)):
        aux_number += 2

    if(not is_prime_optimized(n)):
        print(f"{aux_number} ({n} is not prime)")
    else:
        print(aux_number)

    n = int(input())
