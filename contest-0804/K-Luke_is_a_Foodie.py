# I read part of the tip for this problem
tests_number = int(input())

while(tests_number):
    tests_number -= 1

    n, x = map(int, input().split())
    numbers = [int(n) for n in input().split()]

    # Determine v limit for each step
    min_list = [item - x for item in numbers]
    max_list = [item + x for item in numbers]

    # Set the initial limit
    min_limint = min_list[0]
    max_limit = max_list[0]
    count = 0

    for i in range(1, n):
        # For each step the current limit is reduced according to the current value
        min_limint = max(min_limint, min_list[i])
        max_limit = min(max_limit, max_list[i])
        # When the values are reversed there is no v that can attach to the
        # limit of all the previous steps plus the current, it is necessary to update
        if (min_limint > max_limit):
            count += 1
            min_limint = min_list[i]
            max_limit = max_list[i]

    print(count)
