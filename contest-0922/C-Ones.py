
while True:
    try:
        n = int(input())

        count_ones = 0
        ones_number = 1

        # Find a number formed by only 1's that is multiple of n using the class tips
        while ones_number % n != 0:
            count_ones += 1
            ones_number = (ones_number * 10 + 1) % n

        print(count_ones+1)

    except EOFError:
        break
