# I read part of the tip for this problem
tests_number = int(input())

while(tests_number):
    tests_number -= 1

    n = int(input())
    numbers = [int(n) for n in input().split()]

    # For sequences with odd number of elements the sum is not possible
    if(n % 2 == 1):
        print(-1)
        continue

    base_idx = 0
    coord = []
    total = 0

    # Check pairs of numbers to form the partitions
    while(base_idx + 1 < n):
        # Distinct numbers grouped separately make the sum zero
        if numbers[base_idx] != numbers[base_idx+1]:
            coord += [(base_idx+1, base_idx+1), (base_idx+2, base_idx+2)]
            total += 2
        # Equal numbers grouped together make the sum zero
        else:
            coord.append((base_idx+1, base_idx + 2))
            total += 1

        base_idx += 2

    print(total)
    for l, r in coord:
        print(f"{l} {r}")
