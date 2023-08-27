tests_number = int(input())

while(tests_number):
    tests_number -= 1

    n = int(input())
    hop_range = [int(n) for n in input().split()]
    range_dict = {}
    ones_count = 0
    flogs_path = [0] * (n + 1)

    # Dictionary blanket with number of occurrences of face range
    for current_range in hop_range:
        # Frogs with jump range 1 pass all positions, does not affect choice
        if current_range == 1:
            ones_count += 1
        else:
            if current_range in range_dict:
                range_dict[current_range] += 1
            else:
                range_dict[current_range] = 1

    for flog_range, flog_amount in range_dict.items():
        current_position = flog_range
        # Calculate all the positions that each frog will pass
        while(current_position <= n):
            flogs_path[current_position] += flog_amount
            current_position += flog_range

    print(max(flogs_path) + ones_count)
