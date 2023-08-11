tests_number = int(input())

while(tests_number):
    tests_number -= 1

    n = int(input())
    numbers = [int(i) for i in input().split()]
    """
    In the best case all sub-tracks have the same amount of cars and the difference always will be zero.
    In other cases there are (n-rest) subtracks with M(mean) cars and (rest) sub-tracks with M+1 cars.
    So, the inconvenience is (n-rest)*rest, because for any (n-rest) with M cars the difference 
    will be 1 for the others (rest) sub-tracks with M+1 cars.
    """
    rest = sum(numbers) % n
    print(rest*(n-rest))
