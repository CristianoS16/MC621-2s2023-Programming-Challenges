tests_number = int(input())

while(tests_number):
    tests_number -= 1

    n, k, m = map(int, input().split())
    t = 0

    # Perform the calculation explicitly until it exceeds the limit
    while(n * k <= m):
        t += 1
        n *= k

    print(t)
