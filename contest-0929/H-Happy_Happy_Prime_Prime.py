# Check if a number is prime using the tips of the class
def is_prime_optimized(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


happy_numbers_set = set()
previous_numbers_set = set()

# Check if the number is happy and keeps a "cache" to facilitate future checks


def is_happy_number(number):
    if number in happy_numbers_set or number == 1:
        return True
    if number in previous_numbers_set:
        return False
    previous_numbers_set.add(number)
    aux_number = number
    digits_squared_sum = 0
    # Sums the number of the number
    while aux_number != 0:
        digits_squared_sum += (aux_number % 10)**2
        aux_number //= 10
    # Call the function recursively
    if is_happy_number(digits_squared_sum):
        happy_numbers_set.add(digits_squared_sum)
        return True
    return False


tests_number = int(input())
while(tests_number):
    tests_number -= 1

    current_case, number = map(int, input().split())

    is_prime = is_prime_optimized(number)
    if is_prime:
        previous_numbers_set = set()
        is_happy = is_happy_number(number)

    print(current_case, number, "YES" if is_prime and is_happy else "NO")
