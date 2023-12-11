tests_number = int(input())

while(tests_number):
    tests_number -= 1

    k = int(input())

    fib_numbers = [2, 3]
    mod_numbers = [2]

    # Calculates the sequence of Fibonacci and Fibonacci%K and for when there is repetition
    while fib_numbers[-1] % k not in mod_numbers:
        fib_numbers.append(fib_numbers[-2] + fib_numbers[-1])
        mod_numbers.append(fib_numbers[-2] % k)

    print(mod_numbers.index(fib_numbers[-1] % k)+2)
