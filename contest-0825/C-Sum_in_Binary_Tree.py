tests_number = int(input())

while(tests_number):

    n = int(input())
    count = 1
    # The number to be added will always be the floor of the division by two of the previous number
    while(n > 1):
        count += n
        n = n//2

    print(count)

    tests_number -= 1
