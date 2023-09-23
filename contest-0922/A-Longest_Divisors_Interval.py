tests_number = int(input())

while(tests_number):
    tests_number -= 1
    n = int(input())
    i = 1

    # Test all divisible values from scratch
    while(n % i == 0):
        i += 1

    print(i-1)
